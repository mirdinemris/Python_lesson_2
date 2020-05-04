from Lesson_5.Divisor_master import check_simple, divider_list, big_simple_div, multi_canon, big_divider
print(check_simple(-251))

# Тесты для функции проверяющей число на простоту
def test_1_check_simple():
    assert check_simple(100) == (False, None)

def test_2_check_simple():
    assert check_simple(547) == (True, None)

def test_3_check_simple():
    assert check_simple('547') == (True, None)

def test_4_check_simple():
    assert check_simple(0) == (False, None)

def test_5_check_simple():
    assert check_simple(-251) == (True, None)

# Тесты для функции находящей делители числа
def test_1_divider_list():
    assert  divider_list(999) == ([1, 3, 9, 27, 37, 111, 333, 999], None)

def test_2_divider_list():
    assert divider_list(1000) == ([1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000], None)

def test_3_divider_list():
    assert divider_list(1) == ([1], None)

def test_4_divider_list():
    assert divider_list(674) == ([1, 2,  337,  674], None)

def test_5_divider_list():
    assert divider_list(379) == ([1,  379], None)

# Тесты для функции, находящей самый большой простой делитель числа.
def test_1_big_simple_div():
    assert big_simple_div(379) == (379, None)

def test_2_big_simple_div():
    assert big_simple_div(1000) == (5, None)

def test_3_big_simple_div():
    assert big_simple_div(358) == (179, None)

def test_4_big_simple_div():
    assert big_simple_div(-562) == (281, None)

def test_5_big_simple_div():
    assert big_simple_div(1) == (1, None)


# Тесты для функции канонического разложения на множители.
# Исправил ошибку вывода результата. Обнуление листа: multiplies = [] необходимо внутри функции
# Иначе при неоднократном итерировании функции, результат выглядит как сумма результатов, прим: FAILED Tests_for_Divisor_master.py::test_1_multi_canon - AssertionError: assert ('3 * 277 * 2...7 * 5³', None) == ('2³ * 5³', None)
def test_1_multi_canon():
    assert multi_canon(1000) == ('2³ * 5³', None)

def test_2_multi_canon():
    assert multi_canon(834) == ('2 * 3 * 139', None)

def test_3_multi_canon():
    assert multi_canon(594) == ('2 * 3³ * 11', None)

def test_4_multi_canon():
    assert multi_canon(444) == ('2² * 3 * 37', None)

def test_5_multi_canon():
    assert multi_canon(221) == ('13 * 17', None)

# Тест для функции с самым большим множителем
def test_big_divider():
    assert big_divider(222) == (222, None)
    # Здесь была ошибка вызванная тем что в Return функции указан лишь оператор print который отбражается в результате теста как None