import sqlite3
import psycopg2
import pandas as pd
import os

def get_db_credentials(sqlite_db_path: str = "creds.db") -> tuple:
    """
    Получает credentials для PostgreSQL из SQLite базы
    """
    try:
        sqlite_connection = sqlite3.connect(sqlite_db_path)
        cursor = sqlite_connection.cursor()
        sqlite_select_query = """SELECT * from access"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        host, port, user, password = records[0]
        dbname = "homeworks"
        cursor.close()
        return host, port, user, password, dbname
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        raise
    finally:
        if 'sqlite_connection' in locals():
            sqlite_connection.close()

def create_table_schema(df: pd.DataFrame, table_name: str = "public.tryastsin") -> str:
    """
    Создает SQL схему на основе DataFrame
    """
    df_keys = list(map(lambda s: s.replace(" ", "_"), list(df.columns.values)))
    
    create_table_query = f"""CREATE TABLE IF NOT EXISTS {table_name} ("""
    for i in range(len(df_keys)):
        create_table_query += df_keys[i] + " "
        if df_keys[i] == "Year_First_Published":
            create_table_query += "integer"
        elif df_keys[i] == "Oldest_Known_Age_(Ma)":
            create_table_query += "real"
        else:
            create_table_query += "text"

        if i + 1 == len(df_keys):
            create_table_query += ")"
        else:
            create_table_query += ", "
    
    return create_table_query

def validate_load_parameters(df: pd.DataFrame, max_rows: int = 100) -> bool:
    """
    Валидация параметров для загрузки
    """
    if max_rows <= 0:
        raise ValueError("max_rows должен быть положительным числом")
    
    if df.empty:
        raise ValueError("DataFrame для загрузки пуст")
    
    return True

def load_to_postgresql(df: pd.DataFrame, max_rows: int = 100) -> bool:
    """
    Загружает данные в PostgreSQL (максимум max_rows строк)
    """
    print(f"Загрузка данных в PostgreSQL (максимум {max_rows} строк)...")
    
    validate_load_parameters(df, max_rows)
    
    try:
        host, port, user, password, dbname = get_db_credentials()
        
        postgresql_connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        cursor = postgresql_connection.cursor()
        
        # Подготовка названий колонок
        df_keys = list(map(lambda s: s.replace(" ", "_"), list(df.columns.values)))
        table_name = "public.tryastsin"
        
        # Удаляем и создаем таблицу заново
        postgresql_query_drop_table = f"""DROP TABLE IF EXISTS {table_name}"""
        cursor.execute(postgresql_query_drop_table)
        
        postgresql_query_create_table = create_table_schema(df, table_name)
        cursor.execute(postgresql_query_create_table)
        
        # Вставляем данные (максимум max_rows строк)
        rows_loaded = 0
        for index, row in df.iterrows():
            if rows_loaded >= max_rows:
                break
                
            # Подготавливаем значения для вставки
            values = []
            for value in row:
                if pd.isna(value):
                    values.append("NULL")
                elif isinstance(value, str):
                    values.append(f"'{value.replace("'", "''")}'")
                else:
                    values.append(str(value))
            
            postgresql_query_insert = f"""INSERT INTO {table_name} VALUES ({', '.join(values)})"""
            cursor.execute(postgresql_query_insert)
            rows_loaded += 1
        
        postgresql_connection.commit()
        print(f"Успешно загружено {rows_loaded} строк в PostgreSQL")
        return True
        
    except psycopg2.Error as error:
        print("Ошибка при работе с PostgreSQL", error)
        return False
    finally:
        if 'postgresql_connection' in locals():
            cursor.close()
            postgresql_connection.close()

def load(df: pd.DataFrame, max_rows: int = 100) -> bool:
    """
    Основная функция load: загружает данные в БД
    """
    success = load_to_postgresql(df, max_rows)
    return success