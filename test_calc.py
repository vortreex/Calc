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

def test_simple_parenthesis_parser():
    calc = Calculator()
    assert calc.preparse_expression('(2+2)*2=') == ['(', 2, '+', 2, ')', '*', 2]

def test_simple_parenthesis_parser1():
    calc = Calculator()
    calc.parenthesis_parser(['(', 2, '+', 2, ')', '*', 2])

def test_double_parenthesis_parser():
    calc = Calculator()
    assert calc.preparse_expression('(2+2)*(7-3)=') == ['(', 2, '+', 2, ')', '*', '(', 7, '-', 3, ')']

def test_nested_parenthesis_parser():
    calc = Calculator()
    assert calc.preparse_expression('((2+2)*3)-5=') == ['(', '(', 2, '+', 2, ')', '*', 3, ')', '-', 5]

def test_nested_parenthesis_parser1():
    calc = Calculator()
    print(calc.parenthesis_parser(['(', '(', 2, '+', 2, ')', '*', 3, ')', '-', 5]))

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


if __name__ == "__main__":
    # test_simple_addition()
    # test_double_subtraction()
    # test_simple_parenthesis()
    # test_preparser()
    # test_simple_parenthesis_parser1()
    # test_double_parenthesis_parser()
    # test_nested_parenthesis_parser1()
    # test_exp_calc()
    test_full()
