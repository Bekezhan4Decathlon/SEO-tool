from base64 import encode
import pandas as pd 

website_category = pd.read_excel('Categories.xlsx')
categories = list(pd.read_excel('Categories.xlsx').name)
row = []
rows = []

for category in categories[:10]:
    footer_text = f"Часто задаваемые вопросы о каталоге {category}"
    title = f"This title of {category}"
    description = f"This description of {category}"

    row.append(category)
    row.append(title)
    row.append(description)
    row.append(website_category[website_category.name == category].link.values[0])
    row.append(footer_text)
    rows.append(row)
    footer_text = ""
    row = []

df = pd.DataFrame(rows, columns=["Категория", "title", "description", "link", "Footer text"])
df.to_csv("results.csv", index=False, encoding="windows-1251")

