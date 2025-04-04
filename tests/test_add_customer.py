import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.add_customer import AddCustomer
from data.helpers.generators import Customer
from pages.list_customer import ListCustomer
from pages.manager_page import ManagerPage


@allure.feature('globalsqa.com')
@allure.title('Создание клиента (Add Customer)')
@allure.description("""
    Цель: Проверка создание клиента

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"        
    2. Ввести данные в поля "Last Name", "First Name", "Post Code",  
    3. Проверить, что появилось сообщение об успешной регистрации
    4. Принять сообщение
    5. Проверить, что клиент был добавлен
    """)
@pytest.mark.parametrize(
    'first_name, last_name, post_code',
    [(Customer.first_name, Customer.last_name, Customer.post_code)]
)
def test_create_customer(driver: WebDriver, first_name: str, last_name: str, post_code: str) -> None:
    with allure.step("Открытие страницу 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        add_customer_page = AddCustomer(driver)
        add_customer_page.open()

    with allure.step("Создание нового клиента"):
        manager_page = ManagerPage(driver)
        manager_page.click_on_item_menu("Add Customer")

        add_customer_page.enter_first_name(first_name)
        add_customer_page.enter_last_name(last_name)
        add_customer_page.enter_post_code(post_code)
        add_customer_page.click_add_customer_submit_btn()

    with allure.step("Проверка, что появилось сообщение об успешной регистрации"):
        assert add_customer_page.get_alert_message() == ("Customer added successfully "
                                                         "with customer id :"), "Клиент не создан"

    with allure.step("Принятие сообщение"):
        add_customer_page.click_alert()

    with allure.step("Проверка, что клиент добавлен"):
        manager_page.click_on_item_menu("Customers")
        list_customers_page = ListCustomer(driver)
        assert (
                   first_name,
                   last_name,
                   post_code
               ) in list_customers_page.get_all_data_customers(), (f"Клиент {first_name} {last_name} "
                                                                   f"с Post Code {post_code} "
                                                                   f"не найден в списке всех клиентов")