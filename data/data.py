from dataclasses import dataclass
from faker import Faker

fake = Faker()


def _convert_post_code_to_name(post_code_digits: str) -> str:
    """Преобразует последовательность цифр Post Code в соответствующее имя.

    Args:
        post_code_digits (str): Последовательность цифр Post code.

    Returns:
        str: Соответствующее имя.
    """
    post_code_numbers_list = [int(post_code_digits[x:x + 2]) for x in range(0, 10, 2)]

    code_list = [i % 26 + 97 for i in post_code_numbers_list]
    chars_list = [chr(i) for i in code_list]
    name = ''.join(chars_list).capitalize()

    return name


@dataclass
class Customer:
    """ Представляет собой клиента.

    Attributes:
        post_code (str): Post Code клиента.
        first_name (str): Преобразованное имя клиента.
        last_name (str): Фамилия клиента.
    """
    post_code: str = fake.numerify('##########')
    first_name: str = _convert_post_code_to_name(post_code)
    last_name: str = fake.last_name()