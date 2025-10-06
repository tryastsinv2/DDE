import requests
import pandas as pd

url = "http://universities.hipolabs.com/search?country=Kuwait"
headers = {"Content-Type": "application/json"}

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
print(df)
