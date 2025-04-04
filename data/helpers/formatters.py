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