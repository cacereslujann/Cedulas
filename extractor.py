import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Crear una conexión a la base de datos SQLite (o conectar a una existente)
conn = sqlite3.connect('datos_alumnos.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS alumnos (
        cedula TEXT,
        nombre TEXT,
        apellido TEXT,
        fechanac_dia TEXT,
        fechanac_mes TEXT,
        fechanac_anho TEXT
    )
''')


chromedriver_path = '/home/lujan/Desktop/Proyectos/Cedulas/env/chromedriver.exe'

# Configurar opciones del navegador Chrome
chrome_options = webdriver.ChromeOptions()
# Si deseas abrir el navegador en modo headless (sin ventana), descomenta la siguiente línea
# chrome_options.add_argument('--headless')

# Inicializar el navegador Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL de la página que deseas abrir
url = 'https://identidad.mtess.gov.py/alumno/register.php'

# Abrir la página en el navegador
driver.get(url)

for cedula in range(4029476, 5000000):
    # Localizar el elemento de entrada por su id
    campo_cedula = driver.find_element(By.ID, "value_cedula_1")
    campo_cedula.clear()

    # Enviar datos al campo de entrada
    campo_cedula.send_keys(str(cedula))  

    time.sleep(3)

    # Localizar el elemento de entrada por su id
    campo_nombre = driver.find_element(By.ID,"readonly_value_nombre_1")

    # Obtener el atributo 'value' del elemento
    valor_nombre = campo_nombre.get_attribute('value')

    # Imprimir el valor obtenido
    print("Valor del campo nombre:", valor_nombre)



    # Localizar el elemento de entrada por su id
    campo_apellido = driver.find_element(By.ID,"readonly_value_apellido_1")

    # Obtener el atributo 'value' del elemento
    valor_apellido = campo_apellido.get_attribute('value')

    # Imprimir el valor obtenido
    print("Valor del campo apellido:", valor_apellido)  



    # Localizar el elemento de entrada por su id
    campo_fechanac = driver.find_element(By.ID,"dayvalue_fechanac_1")

    # Obtener el atributo 'value' del elemento
    valor_fechanac= campo_fechanac.get_attribute('value')

    # Imprimir el valor obtenido
    print("Valor del campo fechanac:", valor_fechanac)




    # Localizar el elemento de entrada por su id
    campo_mes = driver.find_element(By.ID,"monthvalue_fechanac_1")

    # Obtener el atributo 'value' del elemento
    valor_mes= campo_mes.get_attribute('value')

    # Imprimir el valor obtenido
    print("Valor del campo fechanac:", valor_mes)




    # Localizar el elemento de entrada por su id
    campo_anho = driver.find_element(By.ID,"yearvalue_fechanac_1")

    # Obtener el atributo 'value' del elemento
    valor_anho= campo_anho.get_attribute('value')

    # Imprimir el valor obtenido
    print("Valor del campo fechanac:", valor_anho)




    # aca se guardan los datos en la base de datos

    # Insertar los datos en la tabla
    cursor.execute('''
        INSERT INTO alumnos (cedula, nombre, apellido, fechanac_dia, fechanac_mes, fechanac_anho)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (cedula, valor_nombre, valor_apellido, valor_fechanac, valor_mes, valor_anho))


    # Guardar los cambios y cerrar la conexión
    conn.commit()

    time.sleep(1)
conn.close()

# Mantener el navegador abierto por un tiempo para que puedas ver la página
input("Presiona Enter para cerrar el navegador...")

# Cerrar el navegador
driver.quit()

