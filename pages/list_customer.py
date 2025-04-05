from typing import Tuple, List
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from data.config import *


class ListCustomer(BasePage):
    """Страница со списком клиентов"""
    TABLE_DATA_ROWS_LIST = TABLE_DATA_ROWS_LIST
    FIRST_NAME_TITLE = FIRST_NAME_TITLE
    FIRST_NAMES_LIST = FIRST_NAMES_LIST
    LAST_NAMES_LIST = LAST_NAMES_LIST
    POST_CODE_LIST = POST_CODE_LIST
    DELETE_BTN_LIST = DELETE_BTN_LIST

    def sort_by_first_name(self):
        """Сортируем записи по имени."""
        column = self.element_to_be_clickable(self.FIRST_NAME_TITLE)
        column.click()
        column.click()

    def delete_customers(self):
        """Удаляем выбранных клиентов."""
        delete_records_element_list = self.get_delete_records_element_list()
        for elem in delete_records_element_list:
            elem[3].click()

    def get_all_records_elements_list(self):
        """Получаем список всех элементов записей.
        Returns:
            Список кортежей элементов записей.
        """
        count_data_row = len(self.presence_of_all_elements_located(self.TABLE_DATA_ROWS_LIST))

        all_records_elements_list = []
        for i in range(1, count_data_row + 1):
            first_name_element_locator = ("xpath", f"{self.FIRST_NAMES_LIST[1]}[{i}]")
            last_name_element_locator = ("xpath", f"{self.LAST_NAMES_LIST[1]}[{i}]")
            post_code_element_locator = ("xpath", f"{self.POST_CODE_LIST[1]}[{i}]")
            delete_btn_element_locator = ("xpath", f"{self.DELETE_BTN_LIST[1]}[{i}]")

            record = tuple(self.presence_of_element_located(i) for i in [
                first_name_element_locator,
                last_name_element_locator,
                post_code_element_locator,
                delete_btn_element_locator
            ])
            all_records_elements_list.append(record)

        return all_records_elements_list

    def get_delete_records_element_list(self):
        """Получаем список элементов записей, подлежащих удалению.
        Returns:
            Список кортежей элементов записей для удаления.
        """
        all_records_element_list = self.get_all_records_elements_list()
        if not all_records_element_list:
            return []

        lengths_names_list = [len(elem[0].text) for elem in all_records_element_list]
        comparison_value = self._value_with_min_deviation_from_avg(lengths_names_list)

        delete_records_element_list = [
            elem for elem in all_records_element_list if len(elem[0].text) == comparison_value
        ]

        return delete_records_element_list

    def get_all_data_customers(self):
        """"""
        all_records_element_list = self.get_all_records_elements_list()
        if not all_records_element_list:
            return []

        all_data_element_list = [i[:-1] for i in all_records_element_list]
        all_data_customers = [tuple(i.text for i in elem) for elem in all_data_element_list]
        return all_data_customers

    @staticmethod
    def _value_with_min_deviation_from_avg(number_list: List[int]):
        """Находим значение с минимальным отклонением от среднего. Список чисел
        Returns:
            Значение с минимальным отклонением от среднего"""
        if not number_list:
            raise ValueError("List of numbers must not be empty")

        avg_value = sum(number_list) / len(number_list)
        min_deviation_value = min(list(map(lambda x: abs(x - avg_value), number_list)))

        for number in number_list:
            if abs(number - avg_value) == min_deviation_value:
                return number