from pages.base_page import BasePage
from data.config import *


class ManagerPage(BasePage):
    """Страница менеджера"""

    BTN_MENU_LIST = BTN_MENU_LIST

    def click_on_item_menu(self, item_title: str):
        """Нажимает на элемент меню с указанным заголовком"""
        btn_menu_elements = self.presence_of_all_elements_located(self.BTN_MENU_LIST)
        for i in btn_menu_elements:
            if i.text == item_title:
                i.click()
                break