import pandas as pd

FILE_ID = "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL"  # ID файла на Google Drive
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)  # читаем файл

print(raw_data.head(10))  # выводим на экран первые 10 строк для проверки

cols_names = list(raw_data.columns.values)  # получаем список названий всех столбцов
raw_data[cols_names] = raw_data[cols_names].astype(
    str
)  # сначала преобразую все стоблцы к строке для удобства
raw_data["Year First Published"] = raw_data["Year First Published"].astype(
    int
)  # год публикации - целое число
raw_data["Oldest Known Age (Ma)"] = raw_data["Oldest Known Age (Ma)"].astype(
    float
)  # возраст - плавающее число

raw_data.to_csv("updated_data.csv")  # сохраняем в подходящий формат
