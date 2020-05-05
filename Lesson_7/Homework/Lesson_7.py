'''
LIGHT:

1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).

2) Создать doc шаблон, где будут использованы данные параметры.

3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).

4) Создать csv файл с данными о машине.

5) Создать json файл с данными о машине.

PRO:

LIGHT +

6) Замерить время генерации отчета (время выполнения пункта 3). В каждый файл пунктов 4 и 5 добавить параметр: время, затраченное на генерацию отчета.
'''

# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
buh = [['Mark', 'Model', 'Fuel consumption', 'Price'], ['UAZ', 'Buhanka', '15,5 l/100 km', '9899,98 USD']]
with open('buhanka.txt', 'w') as f:
    f.writelines(str(buh))
# 2) Создать doc шаблон, где будут использованы данные параметры.
# 3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(Brand, Auto, Benz, Cena, a,b,c,d): # возвращает словарь аргуменов
    return {
        'Mar': Brand,
        'Mod': Auto,
        'Fu': Benz,
        'Pr': Cena,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    }


def from_template(Brand, Auto, Benz, Cena, a,b,c,d, template, signature):
    template = DocxTemplate(template)
    context = get_context(Brand, Auto, Benz, Cena, a,b,c,d, )  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    bu = InlineImage(template, signature, img_size)

    context['bu'] = bu  # adds the InlineImage object to the context
    template.render(context)

    template.save(Brand + '_' + str(datetime.datetime.now().date()) + '_template.docx')


def generate_report(Brand, Auto, Benz, Cena, a,b,c,d):
    template = 'template.docx'
    signature = 'bu.png'
    document = from_template(Brand, Auto, Benz, Cena, a,b,c,d, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report(buh[0][0],buh[0][1],buh[0][2],buh[0][3],buh[1][0],buh[1][1],buh[1][2],buh[1][3])

# 4) Создать csv файл с данными о машине.
import csv
with open('buhanka.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(buh)

# 5) Создать json файл с данными о машине.

import json

json_buh = json.dumps(buh)
print(type(json_buh), json_buh)

# 6) Замерить время генерации отчета (время выполнения пункта 3). В каждый файл пунктов 4 и 5 добавить параметр: время, затраченное на генерацию отчета.

import timeit

test_example_3 = '''
buh = [['Mark', 'Model', 'Fuel consumption', 'Price'], ['UAZ', 'Buhanka', '15,5 l/100 km', '9899,98 USD']]
import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(Brand, Auto, Benz, Cena, a,b,c,d): # возвращает словарь аргуменов
    return {
        'Mar': Brand,
        'Mod': Auto,
        'Fu': Benz,
        'Pr': Cena,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
    }


def from_template(Brand, Auto, Benz, Cena, a,b,c,d, template, signature):
    template = DocxTemplate(template)
    context = get_context(Brand, Auto, Benz, Cena, a,b,c,d, )  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    bu = InlineImage(template, signature, img_size)

    context['bu'] = bu  # adds the InlineImage object to the context
    template.render(context)

    template.save(Brand + '_' + str(datetime.datetime.now().date()) + '_template.docx')


def generate_report(Brand, Auto, Benz, Cena, a,b,c,d):
    template = 'template.docx'
    signature = 'bu.png'
    document = from_template(Brand, Auto, Benz, Cena, a,b,c,d, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report(buh[0][0],buh[0][1],buh[0][2],buh[0][3],buh[1][0],buh[1][1],buh[1][2],buh[1][3])
'''
elapsed_time = timeit.timeit(test_example_3, number=100)/100
print(elapsed_time)
new_inf = [['Время затраченное на генерацию отчета: '], [elapsed_time]]
print(new_inf)

with open('buhanka.txt', 'a') as f:
    f.writelines(str(new_inf))

with open('buhanka.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')  #
        writer.writerows(new_inf)


