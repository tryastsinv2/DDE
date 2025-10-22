import sqlite3
import psycopg2
import pandas

try:
    sqlite_connection = sqlite3.connect("creds.db")  # добавлен в .gitignore
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from access"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    host, port, user, password = records[0]
    dbname = "homeworks"
    cursor.close()

    try:
        postgresql_connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        cursor = postgresql_connection.cursor()
        postgresql_query_create_table = (
            """CREATE TABLE IF NOT EXISTS public.tryastsin"""
        )

        df = pandas.read_csv("notebooks/prepared_dataset.csv")
        df_keys = list(map(lambda s: s.replace(" ", "_"), list(df.columns.values)))
        postgresql_query_drop_table = """DROP TABLE IF EXISTS public.tryastsin"""
        postgresql_query_create_table = (
            """CREATE TABLE IF NOT EXISTS public.tryastsin ("""
        )
        for i in range(len(df_keys)):
            postgresql_query_create_table += df_keys[i] + " "
            if df_keys[i] == "Year First Published":
                postgresql_query_create_table += "integer"
            elif df_keys[i] == "Oldest Known Age (Ma)":
                postgresql_query_create_table += "real"
            else:
                postgresql_query_create_table += "text"

            if i + 1 == len(df_keys):
                postgresql_query_create_table += ")"
            else:
                postgresql_query_create_table += ", "

        cursor.execute(postgresql_query_drop_table)
        cursor.execute(postgresql_query_create_table)
        for index, row in df.iterrows():
            if index >= 100:
                break
            postgresql_query_insert = (
                # """INSERT INTO public.tryastsin ("""
                # + ", ".join(df_keys)
                # + ") VALUES ("
                """INSERT INTO public.tryastsin VALUES ("""
                + ", ".join(
                    list(
                        map(
                            lambda x: (
                                "'" + x.replace("'", "") + "'"
                                if type(x) is str
                                else str(x)
                            ),
                            list(row),
                        )
                    )
                )
                + ")"
            )
            cursor.execute(postgresql_query_insert)

        # Проверка
        # postgresql_select_query = """SELECT * from public.tryastsin"""
        # cursor.execute(postgresql_select_query)
        # records = cursor.fetchall()
        # print(records)
    except psycopg2.Error as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if postgresql_connection:
            postgresql_connection.close()
            print("Соединение с PostgreSQL закрыто")
except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
