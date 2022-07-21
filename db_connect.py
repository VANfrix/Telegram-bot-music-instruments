import psycopg2
from psycopg2 import Error
from registration_db import password_bd

try:
    connection = psycopg2.connect(user="sgveurqu",
                                 password=password_bd,
                                 host="hattie.db.elephantsql.com",
                                 port="5432",
                                 database="sgveurqu")
    cursor=connection.cursor()
    
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("select * from guitars;")
    # Получить результат
    record = cursor.fetchall()
    print("таблица", record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
    