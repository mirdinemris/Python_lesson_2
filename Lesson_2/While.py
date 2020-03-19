# Цикл While
# Цикл For



# Простейший While
i = 0

while i < 10:
    print(i)
    i = i + 1
    if i == 5: break

answer = None
while answer != 'Volvo':
    answer = input('Какая лучшая марка автомобиля?')
    print ('Вы абсолютно правы')

while i < 9:
        print(i)
        i = i + 1
        if i == 9:break
        if i < 3: continue

# Простейший For
for i in range(0,100,15): # range(start, stop, step)
    print(i)
    if i == 5: break

for i in range(10):
    answer = input('Какая лучшая марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы')
        break

for i in range(10):
    if i == 9: break
    if i < 3: continue
    else: print(i)
