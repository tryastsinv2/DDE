import argparse
import sys
import os
from extract import extract
from transform import transform
from load import load

def main():
    parser = argparse.ArgumentParser(description='ETL pipeline for data processing')
    parser.add_argument('--file-id', type=str, 
                       default='1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL',
                       help='Google Drive file ID (обязательный аргумент)')
    parser.add_argument('--max-rows', type=int, default=100,
                       help='Maximum rows to load to database (default: 100)')
    parser.add_argument('--skip-extract', action='store_true',
                       help='Skip extract phase')
    parser.add_argument('--skip-transform', action='store_true',
                       help='Skip transform phase')
    parser.add_argument('--skip-load', action='store_true',
                       help='Skip load phase')
    
    args = parser.parse_args()
    
    # Проверяем обязательный аргумент
    if not args.file_id:
        print("Ошибка: file-id является обязательным аргументом")
        parser.print_help()
        sys.exit(1)
    
    try:
        # E - Extract
        if not args.skip_extract:
            raw_df = extract(args.file_id)
        else:
            print("Пропуск этапа Extract")
            # Если пропускаем extract, пытаемся загрузить из сохраненного файла
            import pandas as pd
            raw_df = pd.read_csv("data/raw/raw_data.csv")
        
        # T - Transform
        if not args.skip_transform:
            transformed_df = transform(raw_df)
        else:
            print("Пропуск этапа Transform")
            transformed_df = raw_df
        
        # L - Load
        if not args.skip_load:
            load_success = load(transformed_df, args.max_rows)
            if load_success:
                print("ETL процесс завершен успешно!")
            else:
                print("ETL процесс завершен с ошибками при загрузке")
                sys.exit(1)
        else:
            print("Пропуск этапа Load")
            print("ETL процесс завершен (без загрузки в БД)")
            
    except Exception as e:
        print(f"Ошибка в ETL процессе: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()