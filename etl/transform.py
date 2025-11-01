import pandas as pd
import os
from pathlib import Path

def validate_transformed_data(df: pd.DataFrame) -> bool:
    """
    Валидация трансформированных данных
    """
    # Проверяем типы данных
    if 'Year First Published' in df.columns:
        if not pd.api.types.is_integer_dtype(df['Year First Published']):
            raise ValueError("Колонка 'Year First Published' должна быть целочисленной")
    
    if 'Oldest Known Age (Ma)' in df.columns:
        if not pd.api.types.is_float_dtype(df['Oldest Known Age (Ma)']):
            raise ValueError("Колонка 'Oldest Known Age (Ma)' должна быть числовой")
    
    return True

def save_processed_data(df: pd.DataFrame, output_dir: str = "data/processed") -> str:
    """
    Сохраняет обработанные данные в parquet
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir, "processed_data.parquet")
    df.to_parquet(output_path, index=False)
    return output_path

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Основная функция transform: преобразует типы данных и сохраняет результат
    """
    print("Трансформация данных...")
    
    # Создаем копию чтобы не изменять оригинальные данные
    transformed_data = df.copy()
    
    # Приведение типов
    if 'Year First Published' in transformed_data.columns:
        transformed_data["Year First Published"] = transformed_data["Year First Published"].astype(int)
    
    if 'Oldest Known Age (Ma)' in transformed_data.columns:
        transformed_data["Oldest Known Age (Ma)"] = transformed_data["Oldest Known Age (Ma)"].astype(float)
    
    print("Валидация трансформированных данных...")
    validate_transformed_data(transformed_data)
    
    print("Сохранение обработанных данных...")
    output_path = save_processed_data(transformed_data)
    print(f"Обработанные данные сохранены в: {output_path}")
    
    return transformed_data