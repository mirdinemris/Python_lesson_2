# Оператор условия


brand = 'Volvo'        # бренд
engine_volume =  1.5      # Объем двигателя
horsepower = 152       # мощность двигателя


sunroof = False        # наличие люка

# Проверка условия IF

if horsepower < 80:
    print('No Tax')

# Проверка условия IF/else
if horsepower < 80: print('No Tax')

else: print('Tax')

# Проверка условия if/elif/elif/else

tax = 0
if horsepower < 80:
    tax = 0
elif horsepower < 100:
    tax = 10000
elif horsepower < 150:
    tax = 20000
else:
    tax = 50000
    print(tax)

# Проверка условия IF для присваивания

cool_car = 0

cool_car =1 if sunroof == 1 else 0

print(cool_car)