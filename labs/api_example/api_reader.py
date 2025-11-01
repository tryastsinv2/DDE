import requests
import pandas as pd

url = "http://universities.hipolabs.com/search?country=Kuwait"
headers = {"Content-Type": "application/json"}

response = requests.get(url)
if response.status_code == 200:
    try:
        data = response.json()
        df = pd.DataFrame(data)
        df.dropna()
        print(df.head(5))
        df.to_csv("api_reader_result.csv")
    except requests.RequestException:
        print("Ошибка при обработке запроса")
else:
    print("API не доступно")
