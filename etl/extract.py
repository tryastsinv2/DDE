import pandas as pd
import os
from pathlib import Path

def download_data(file_id: str = "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL") -> pd.DataFrame:
    """
    Загружает данные из Google Drive и сохраняет в raw CSV
    """
    file_url = f"https://drive.google.com/uc?id={file_id}"
    raw_data = pd.read_csv(file_url)
    return raw_data

def validate_raw_data(df: pd.DataFrame) -> bool:
    """
    Валидация сырых данных
    """
    # Проверяем, что DataFrame не пустой
    if df.empty:
        raise ValueError("Загруженные данные пусты")
    
    # Проверяем наличие обязательных колонок
    required_columns = ['Year First Published', 'Oldest Known Age (Ma)']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Отсутствует обязательная колонка: {col}")
    
    return True

def save_raw_data(df: pd.DataFrame, output_dir: str = "data/raw") -> str:
    """
    Сохраняет сырые данные в CSV
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_path = os.path.join(output_dir, "raw_data.csv")
    df.to_csv(output_path, index=False)
    return output_path

def extract(file_id: str = "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL") -> pd.DataFrame:
    """
    Основная функция extract: загружает, валидирует и сохраняет сырые данные
    """
    print("Загрузка данных...")
    df = download_data(file_id)
    
    print("Валидация данных...")
    validate_raw_data(df)
    
    print("Сохранение сырых данных...")
    output_path = save_raw_data(df)
    print(f"Сырые данные сохранены в: {output_path}")
    
    print(f"Первые 5 строк данных:")
    print(df.head())
    
    return df