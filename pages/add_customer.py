from pages.base_page import BasePage


class AddCustomer(BasePage):
    """Страница добавления клиента."""
    FIRST_NAME_FIELD = ("xpath", "//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//button[@type='submit']")

    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя в поле First Name.

        Args:
            first_name: Имя клиента
        """
        self.send_keys_to_element(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию в поле Last Name.

        Args:
            last_name: Фамилия клиента
        """
        self.send_keys_to_element(self.LAST_NAME_FIELD, last_name)

    def enter_post_code(self, post_code: str) -> None:
        """Вводит почтовый индекс в поле Post Code.

        Args:
            post_code: Почтовый индекс
        """
        self.send_keys_to_element(self.POST_CODE_FIELD, post_code)

    def click_add_customer_submit_btn(self) -> None:
        """Нажимает кнопку добавления клиента."""
        self.click_element(self.ADD_CUSTOMER_SUBMIT_BTN)

    def get_alert_message(self) -> str:
        """Получает текст сообщения из алерта.

        Returns:
            Текст сообщения алерта
        """
        return self.get_alert_text()

    def click_alert(self) -> None:
        """Принимает алерт."""
        self.accept_alert()