from Lesson_4.Lesson_4 import f

# Тест проверяет длинну списка на выходе
def test_1_f():
    List_Names = ('Амати', 'Страдивари', 'Гварнери', 'Да Сало', 'Бергонци', 'Да Сало', 'Тесторе')
    N = 100
    test_list = f(List_Names, N)
    assert len(test_list) == N

# Тест проверяет разность списков на выходе функции
def test_2_f():
    List_Names = ('Амати', 'Страдивари', 'Гварнери', 'Да Сало', 'Бергонци', 'Да Сало', 'Тесторе')
    N = 100
    list_for_test = f(List_Names, N)
    for i in range(1,11):
        test_list = f(List_Names, N)
        assert test_list != list_for_test
