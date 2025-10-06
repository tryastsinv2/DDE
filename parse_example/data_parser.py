from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://acmp.ru/index.asp?main=alltasks"

page = requests.get(url)
page.encoding = "cp1251"

soup = BeautifulSoup(page.text, "html.parser")
allTasksTitle = soup.find_all("h1")
allTasksRestrictions = soup.find_all("i")

json = []

for i in range(len(allTasksTitle)):
    title = allTasksTitle[i].text.replace("Задача №" + str(i + 1), "")
    time = allTasksRestrictions[i].text.split(" Память:")[0].replace("(Время: ", "")
    memory_tmp = (
        allTasksRestrictions[i]
        .text.split(" Сложность:")[0]
        .replace("Память: ", "")
        .replace("(Время: ", "")
        .replace("сек. ", "")
        .split(" ")
    )
    memory_tmp.pop(0)
    memory = " ".join(memory_tmp)
    difficult = allTasksRestrictions[i].text[::-1].split(" ")[0].replace(")", "")[::-1]

    json.append(
        {
            "title": title,
            "time": time,
            "memory": memory,
            "difficult": difficult,
        }
    )

df = pd.DataFrame(json)
print(df)
