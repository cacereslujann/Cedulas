import sqlite3

conn = sqlite3.connect('datos_alumnos.db')
cursor = conn.cursor()

cursor.execute("SELECT cedula, nombre, apellido FROM alumnos ORDER BY cedula")

""" previous_cedula = None
for cedula, nombre, apellido in cursor.fetchall():
    if previous_cedula is not None and cedula == previous_cedula + 1 and nombre == previous_nombre and apellido == previous_apellido:
        with open('cedulas_consecutivas.txt', 'a') as file:
            file.write(f"Cédula: {cedula}, Nombre: {nombre}, Apellido: {apellido}\n")
    previous_cedula = cedula
    previous_nombre = nombre
    previous_apellido = apellido"""

    

# ... (código previo)
previous_cedula = None
for cedula, nombre, apellido in cursor.fetchall():
    if previous_cedula is not None and int(cedula) == previous_cedula + 1 and nombre == previous_nombre and apellido == previous_apellido:
        with open('cedulas_consecutivas.txt', 'a') as file:
            file.write(f"Cédula: {cedula}, Nombre: {nombre}, Apellido: {apellido}\n")
    previous_cedula = int(cedula)
    previous_nombre = nombre
    previous_apellido = apellido

conn.close()

# ... (código restante)
