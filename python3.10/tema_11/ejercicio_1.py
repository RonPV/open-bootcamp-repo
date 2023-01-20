import sqlite3
from random import randint

def search_user(id=randint(1,8)):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM Alumnos WHERE id={id}'
    rows = cursor.execute(query)
    data = rows.fetchone()
    for row in rows:
        print(f'ID       = {row[0]}')
        print(f'NOMBRE   = {row[1]}')
        print(f'APELLIDO = {row[2]}')
    if data == None:
        print(f'Alumno no encontrado')
    cursor.close()
    conn.close()

def create_user(users_list):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    for user in users_list:
        query = f'INSERT OR IGNORE INTO Alumnos(id, nombre, apellido) VALUES(?,?,?)'
        cursor.execute(query,user)
    conn.commit()
    print('usuarios añadidos a la base de datos')

    cursor.close()
    conn.close

def main():
    users_list = [(1,'Pepe','Botellas'),
    (2,'Pedro','Picapiedras'),
    (3,'Juan','Perez'),
    (4,'Mario','Bross'),
    (5,'Paolo','Guerrero'),
    (6,'Jefferson','Farfan'),
    (7,'Claudio','Pizarro'),
    (8,'Pablo','Marmol')]

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL);''')
    
    create_user(users_list)
    search_user(input('ID del alumno: '))

    cursor.close()
    conn.close()
    

if __name__ == '__main__':
    main()