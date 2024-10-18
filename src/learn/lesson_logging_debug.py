from logging import getLogger, basicConfig, DEBUG, ERROR, FileHandler, StreamHandler
from random import randint

logger = getLogger()
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
file_handler = FileHandler("data.log", mode="w")
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler, console])

logger.info('����������� ����������� ��������� �������')


def check_value_by_zero(value: str, value_name: str, func_name: str):
    while True:
        print(f'���� �������� ������� �����������, ������� "����"')
        value = input(f'��� ������� �������� �� ������ ����\n{value_name}: ')
        logger.debug(f'� ������� check_value_is_number ������ �������� {value} � {value_name}')

        if value == '':
            print('�� ������ �� �����. ����� ������ ���� ������ �����. ��������� ����')
            continue
        elif value == '����':
            print(f'{func_name} ��������� ���� ������')
            return '����'
        try:
            float(value)
        except Exception:
            print('�� ����� �� �����. ��������� ����')
            continue
        else:
            if float(value) == 0:
                print('�� ����� 0. ��� ���� ������� �������� ���� ������������. ��������� ����')
                continue
            else:
                return value


def check_value_is_number(value: str, value_name: str, func_name: str):
    while True:
        print(f'���� �������� ������� �����������, ������� "����"')
        value = input(f'��� ������� �������� �� ������ ����\n{value_name}: ')
        logger.debug(f'� ������� check_value_is_number ������ �������� {value} � {value_name}')

        if value == '':
            print('�� ������ �� �����. ����� ������ ���� ������ �����. ��������� ����')
            continue
        elif value == '����':
            print(f'{func_name} ��������� ���� ������')
            return '����'
        try:
            float(value)
            return value
        except Exception:
            print('�� ����� �� �����. ��������� ����')
            continue


print('������ �������� ����������� ������� ����������� ���������.')
print('��� ����� ��� ax^2 + bx + c = 0, ��� a, b, c ��� ���������, � x ����� ���������.')
print('������� ��������� ���������, ��� a �� ����� 0, � ����������� ����� ����� ���������, ���� ��� ����.')


def quadratic_equation():

    a = ''
    a = check_value_by_zero(a, 'a', '����������� �������� ���������������')

    if a == '����':
        return

    a = int(a)

    b = ''
    b = check_value_is_number(b, 'b', '����������� �������� ���������������')
    b = int(b)

    if b == '����':
        return

    c = ''
    c = check_value_is_number(c, 'c', '����������� �������� ���������������')
    c = int(c)

    if c == '����':
        return

    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f'� ������� ����������� ��������� ����� ��� �����, � ������ x1 = {x1}, x2 = {x2}')
    elif d == 0:
        x = -b / (2 * a)
        print(f'� ������� ����������� ��������� ����� ���� ������, � ������ x = {x}')
    else:
        print('� ������� ����������� a, b � c ��������� �� ����� ������. ���������� � ������� ����������.')
        quadratic_equation()


quadratic_equation()


logger.info('����������� ����������� ��������� ����������')
print()
print('----------------------------------------------------------------')
print()
logger.info('��������� ������� ����������� ���������� ����� � ���������')

print('����� ������ �������� ��������� ���������� ����� � �������� ���� ��������� �����.')
print('������� ��� �����, ������ ������� ����� ������������� ��������� �����.')


def random_number_from_range():

    d1 = ''
    d1 = check_value_is_number(d1, 'd1', '������� ������ ���������� ����� � ���������')
    d1 = int(d1)

    if d1 == '����':
        return

    d2 = ''
    d2 = check_value_is_number(d2, 'd2', '������� ������ ���������� ����� � ���������')
    d2 = int(d2)

    if d2 == '����':
        return

    result = 0

    try:
        result = randint(int(d1), int(d2))
        logger.debug("result is %s", result)
    except Exception as e:
        logger.error("exception is %s", Exception)
        print(e)
        res = input('���� ������ ������� �����������, ������� "exit" ��� "����������": ')
        if res == 'exit':
            return print('������� ������ ���������� ����� � ��������� ��������� ���� ������')
        elif res == '����������':
            random_number_from_range()
    else:
        print(f'��������� ����� � ��������� �� {d1} �� {d2} ����� {result}')


random_number_from_range()
logger.info('��������� ���������� ���������� ����� � ���������')
print()
print('----------------------------------------------------------------')
print()
logger.info('��������� ���������� �������� ��������������� �� ������ �����')

print('��������� � ���������� �������� ��������������� �� ������ �����.')
print('������� ������ ����� ����� ������, �� ������� ����� ��������� ������� ��������������.')


def arithmetic_mean():

    s = input('������� (����� ������) ������ �����, �� ������� ������ ��������� ������� ��������������: ')
    logger.debug("s is %s", s)
    lst = s.split()
    logger.debug("lst is %s", lst)

    for i in range(len(lst)):
        try:
            check_value_is_number(lst[i], lst[i], '������� ���������� �������� ��������������� �� ������ �����')
            logger.debug("lst[i] is %s", lst[i])
            logger.debug("i is %s", i)
            lst[i] = int(lst[i])
            continue
        except ValueError:
            print(f'{i+1} �� ����� ������� ������ �� �����, ������� "����������" � ��������� ���� ������ �����, ')
            stop = input('���� ������� "����" ��� ������ �� ���������: ')
            if stop == '����':
                return print('�� ���������� ���������� �������� ��������������� �� ������ �����.')
            else:
                arithmetic_mean()

    result = sum(lst) / len(lst)
    print(result)


arithmetic_mean()
logger.info('��������� ���������� �������� ��������������� �� ������ �����')