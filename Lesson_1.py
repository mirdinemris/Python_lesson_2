import requests
import json
import random

term1 = random.randrange(0, 9)
term2 = random.randrange(0, 9)
symbols = ['-', '+']
symbol = random.choice(symbols)
print("Введите капчу!")
print(term1, symbol, term2, )
c = int(input('Введите Ответ ='))
if symbol == '-':
    a = term1 - term2
    if a == c:
      print('Доступ разрешен')
    elif a is not c:
      print('Доступ отклонен')

elif symbol == '+' :
    b = term1 + term2
    if b == c:
      print('Доступ разрешен')
    elif b is not c:
      print('Доступ отклонен')
      
      url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print(data)
