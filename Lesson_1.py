import requests
import json
import random

a = random.randrange(1, 5)
b = random.randrange(1, 5)
c = random.randrange(6, 9)
while b != c:
    if a != c:
        term1 = random.randrange(0, 9)
        term2 = random.randrange(0, 9)
        symbol = random.choice(['-', '+'])
        print("\033[37m♣ Капча! ♣")
        print(term1, symbol, term2, )
        c = int(input('Введите Ответ ='))
        if symbol == '+':
                b = term1 + term2
                if b != c:
                  print('\033[31m♦ В Доступе отказано ♦')
        elif symbol == '-':
               a = term1 - term2
               if a != c:
                 print('\033[31m♦ В Доступе отказано ♦')
        continue
    else:
     break

print('\033[32m ♥ Доступ_разрешен ♥')
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print('Последние вести из страны Чукепуксов!')
print(data)

