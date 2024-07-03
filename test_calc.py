from calc import Calculator


def test_simple_addition():
    calc = Calculator()
    assert calc.calculate('2+2=') == 4

def test_double_subtraction():
    calc = Calculator()
    assert calc.calculate('9-3-1=') == 5

def test_simple_multiplication():
    calc = Calculator()
    assert calc.calculate('2*5=') == 10

def test_simple_division():
    calc = Calculator()
    assert calc.calculate('15/5=') == 3

def test_simple_parenthesis():
    calc = Calculator()
    assert calc.calculate('(2*3)+5=') == 11

def test_preparser():
    calc = Calculator()
    assert calc.preparse_expression('2+2=') == [2, '+', 2]

def test_double_parenthesis_parser():
    calc = Calculator()
    assert calc.preparse_expression('(2+2)*(7-3)=') == ['(', 2, '+', 2, ')', '*', '(', 7, '-', 3, ')']

def test_nested_parenthesis_parser():
    calc = Calculator()
    assert calc.preparse_expression('((2+2)*3)-5=') == ['(', '(', 2, '+', 2, ')', '*', 3, ')', '-', 5]

def test_exp_calc():
    calc = Calculator()
    print(calc.calculate_expression([3, '-', 1, '*', 7])) ## == -4

def test_mult_div():
    calc = Calculator()
    print(calc.multiply_and_divide([3, '-', 1, '*', 7]))

def test_add_sub():
    calc = Calculator()
    print(calc.add_and_subtract([3, '-', 1, '*', 7]))

def test_full():
    calc = Calculator()
    print(calc.calculate('2,37 + 1*5,12 -7/2'))

def test_chat_gpt():
    calc = Calculator()
    assert calc.calculate("1 + 1.5") == 2.5, f'caluclated: {calc.calculate("1 + 1.5")}'
    assert calc.calculate("2.5 * 2") == 5.0
    assert calc.calculate("10 / 2.5") == 4.0
    assert calc.calculate("2 + 3.3 * 1.5") == eval("2 + 3.3 * 1.5") 
    assert calc.calculate("(1 + 2.2) * 3") == eval("(1 + 2.2) * 3")
    assert calc.calculate("10 / (2 + 3.5)") == 1.8181818181818181
    assert calc.calculate("100 - 5.5 * 10") == 45.0
    assert calc.calculate("50 + 10.0 / 2") == 55.0
    assert calc.calculate("(10 - 2.5) * (5 + 3.5)") == 63.75
    assert calc.calculate("3 * (2 + 1.5) / 3") == 3.5
    assert calc.calculate("10 - 4.4 / 2 + 1") == eval("10 - 4.4 / 2 + 1")
    assert calc.calculate("20 / 4 + 3.3 * 2") == 11.6
    assert calc.calculate("(8 / 4) + (3 * 3.5)") == 12.5
    assert calc.calculate("6 * (2 + 3.5) / 5") == 6.6
    assert calc.calculate("3 + (12.0 / 4) - 2") == 4.0
    assert calc.calculate("100 / (5 * 2.5)") == 8.0
    assert calc.calculate("8 * 2.5 - 4 / 2") == 18.0
    assert calc.calculate("50 / (5 + 5.5)") == eval("50 / (5 + 5.5)")
    assert calc.calculate("(15 / 3) + (2 * 4.5)") == 14.0
    assert calc.calculate("3 * (2 + 1.2) - 4") == eval("3 * (2 + 1.2) - 4")
    assert calc.calculate("10 + 3.3 * (8 / 4)") == 16.6
    assert calc.calculate("100 - (25.0 * 3 / 5)") == 85.0
    assert calc.calculate("(8 - 2.5) * (4 + 1.2)") == eval("(8 - 2.5) * (4 + 1.2)")
    assert calc.calculate("5 + (15 / 3) * 2.5") == 17.5
    assert calc.calculate("30 / (2 + 3.5) * 4") == 21.818181818181817

def test_exponent():
    calc = Calculator()
    print(calc.calculate('2^3^4'))


if __name__ == "__main__":
    # test_simple_addition()
    # test_double_subtraction()
    test_simple_parenthesis()
    # test_preparser()
    # test_exp_calc()
    test_full()
    test_exponent()
    test_chat_gpt()
