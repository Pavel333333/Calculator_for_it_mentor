def check_digit_exception(value: str):
    if not value.isdigit():
        raise ValueError("throws Exception // �.�. ����� ������ ���� ������ ����� � ������ �����")
    elif int(value) > 10 or int(value) < 1:
        raise ValueError("throws Exception // �.�. ����������� �������� � ������� �� 1 �� 10")


operators = '+-*/'


def check_operator_exception(value: str):
    if value not in operators:
        raise ValueError("throws Exception // �.�. ������ �������������� �������� �� ������������� �������"
                         " - ��� �������� � ���� �������� (+, -, /, *)")


def check_words_quantity_exception(value: list):
    if len(value) < 3:
        raise ValueError("throws Exception // �.�. ������ �� �������� �������������� ���������")
    elif len(value) > 3:
        raise ValueError("throws Exception // �.�. ������ �������������� �������� �� ������������� �������"
                         " - ��� �������� � ���� �������� (+, -, /, *)")


def main(task: str):
    task = input('������� �������������� ��������� ��� �������: ').split()

    try:
        check_words_quantity_exception(task)
    except ValueError as e:
        return print(e)

    try:
        check_digit_exception(task[0])
        check_digit_exception(task[2])
    except ValueError as e:
        return print(e)

    try:
        check_operator_exception(task[1])
    except ValueError as e:
        return print(e)

    first_element = int(task[0])
    operator = task[1]
    second_element = int(task[2])

    match operator:
        case '+':
            return print(first_element + second_element)
        case '-':
            return print(first_element - second_element)
        case '*':
            return print(first_element * second_element)
        case '/':
            return print(int(first_element / second_element))


main(task='')