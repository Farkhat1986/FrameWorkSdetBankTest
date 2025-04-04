from faker import Faker
from data.helpers.formatters import _convert_post_code_to_name

fake = Faker()
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