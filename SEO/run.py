from base64 import encode
import pandas as pd
import os
print(os.listdir('.'))

website_category = pd.read_excel('Categories.xlsx')
categories = list(pd.read_excel('Categories.xlsx').name)
row = []
rows = []
city = "Алматы"

for category in categories:
    title = f"{category} купить в магазине Декатлон Казахстан"
    description = f"Купить {category} в {city} ✓ 0% рассрочка на 4 месяца ✓ Доставка по всему Казахстану"
    # h1 = f""
    footer_text = f"""Часто задаваемые вопросы o категории {category}:\n
                    1. Где купить {category}?\n
                    Приобрести спортивыне товары {category} вы можете на сайте decathlon.kz\n
                    2. Как заказать дешевые спортивные товары {category}?\n
                    Заказать спортивые товары вы можете на сайте decathlon.kz после регистрации\n
                    3. Есть ли гарантия на спортивные товары?\n
                    На спортивные товары, купленные на нашем сайте или в магазине, распространяется гарантия 2 года на текстиль, аксессуары и обувь, 5 лет на палатки, спальные мешки, 10 лет на рюкзаки и пожизненная гарантия на раму, вилку и руль.\n
                    4. Как заказать {category} с доставкой?\n
                    {category} с доставкой по всему Казахстану (Алматы, Нур-султан, Шымкент, Караганда, итд.) вы можете на сайте decathlon.kz\n
                    5. Какие спортивные товары можно купить на decathlon.kz\n
                    На нашем сайте вы можете купить {category} для детей и {category} для взрослых\n
    """

    row.append(website_category[website_category.name == category].link.values[0])
    row.append(category)
    row.append(title)
    row.append(description)
    row.append(footer_text)
    rows.append(row)
    row = []
    
df = pd.DataFrame(rows, columns=["link", "category", "title", "description", "Footer text"])
df.to_excel('results.xlsx')

