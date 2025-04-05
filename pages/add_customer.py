from pages.base_page import BasePage
from data.config import *
import allure


class AddCustomer(BasePage):
    """Страница добавления клиента."""
    FIRST_NAME_FIELD = FIRST_NAME_FIELD
    LAST_NAME_FIELD = LAST_NAME_FIELD
    POST_CODE_FIELD = POST_CODE_FIELD
    ADD_CUSTOMER_SUBMIT_BTN = ADD_CUSTOMER_SUBMIT_BTN

    @allure.step("Ввести имя '{first_name}' в поле First Name")
    def enter_first_name(self, first_name: str):
        """Вводит имя в поле First Name"""
        self.send_keys_to_element(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Ввести фамилию '{last_name}' в поле Last Name")
    def enter_last_name(self, last_name: str):
        """Вводит фамилию в поле Last Name"""
        self.send_keys_to_element(self.LAST_NAME_FIELD, last_name)

    @allure.step("Ввести почтовый индекс '{post_code}' в поле Post Code")
    def enter_post_code(self, post_code: str):
        """Вводит почтовый индекс в поле Post Code"""
        self.send_keys_to_element(self.POST_CODE_FIELD, post_code)

    @allure.step("Нажать кнопку добавления клиента")
    def click_add_customer_submit_btn(self):
        """Нажимает кнопку добавления клиента."""
        self.click_element(self.ADD_CUSTOMER_SUBMIT_BTN)

    @allure.step("Получить текст сообщения из алерта")
    def get_alert_message(self):
        """Получает текст сообщения из алерта.
        Returns:
            Текст сообщения алерта
        """
        return self.get_alert_text()

    @allure.step("Принять алерт")
    def click_alert(self):
        """Принимает алерт."""
        self.accept_alert()