import pandas as pd

def validate_raw_data(df: pd.DataFrame) -> bool:
    """
    Валидация сырых данных
    """
    if df.empty:
        raise ValueError("Загруженные данные пусты")
    
    required_columns = ['Year First Published', 'Oldest Known Age (Ma)']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Отсутствует обязательная колонка: {col}")
    
    return True

def validate_transformed_data(df: pd.DataFrame) -> bool:
    """
    Валидация трансформированных данных
    """
    if df.empty:
        raise ValueError("Трансформированные данные пусты")
    
    if 'Year First Published' in df.columns:
        if not pd.api.types.is_integer_dtype(df['Year First Published']):
            raise ValueError("Колонка 'Year First Published' должна быть целочисленной")
    
    if 'Oldest Known Age (Ma)' in df.columns:
        if not pd.api.types.is_float_dtype(df['Oldest Known Age (Ma)']):
            raise ValueError("Колонка 'Oldest Known Age (Ma)' должна быть числовой")
    
    return True

def validate_load_parameters(df: pd.DataFrame, max_rows: int = 100) -> bool:
    """
    Валидация параметров для загрузки
    """
    if max_rows <= 0:
        raise ValueError("max_rows должен быть положительным числом")
    
    if df.empty:
        raise ValueError("DataFrame для загрузки пуст")
    
    return True