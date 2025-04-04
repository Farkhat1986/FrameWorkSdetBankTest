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
    Цель: Проверка создания клиента

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    2. Ввести данные в поля "First Name", "Last Name", "Post Code"
    3. Нажать кнопку добавления клиента
    4. Проверить, что появилось сообщение об успешной регистрации
    5. Принять сообщение
    6. Проверить, что клиент был добавлен в список
    """)
def test_create_customer(driver: WebDriver) -> None:
    # Генерируем тестовые данные
    first_name = Customer.first_name
    last_name = Customer.last_name
    post_code = Customer.post_code

    with allure.step("Открытие страницы менеджера"):
        manager_page = ManagerPage(driver)
        manager_page.open()

    with allure.step("Переход на страницу добавления клиента"):
        manager_page.click_on_item_menu("Add Customer")
        add_customer_page = AddCustomer(driver)

    with allure.step(f"Заполнение данных клиента: {first_name}, {last_name}, {post_code}"):
        add_customer_page.enter_first_name(first_name)
        add_customer_page.enter_last_name(last_name)
        add_customer_page.enter_post_code(post_code)
        add_customer_page.click_add_customer_submit_btn()

    with allure.step("Проверка сообщения об успешном создании клиента"):
        alert_message = add_customer_page.get_alert_message()
        expected_message = "Customer added successfully with customer id :"
        assert alert_message == expected_message, \
            f"Ожидалось сообщение '{expected_message}', получено '{alert_message}'"

    with allure.step("Подтверждение алерта"):
        add_customer_page.click_alert()

    with allure.step("Проверка наличия клиента в списке"):
        manager_page.click_on_item_menu("Customers")
        list_customers_page = ListCustomer(driver)
        customers_data = list_customers_page.get_all_data_customers()

        assert (first_name, last_name, post_code) in customers_data, \
            (f"Клиент {first_name} {last_name} с Post Code {post_code} "
             "не найден в списке клиентов")