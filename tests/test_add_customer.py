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
    1. Открыть страницу менеджера
    2. Перейти на страницу добавления клиента
    3. Заполнить данные клиента
    4. Нажать кнопку добавления клиента
    5. Проверить сообщение об успешном создании
    6. Принять сообщение
    7. Проверить наличие клиента в списке
    """)
def test_create_customer(driver: WebDriver) -> None:
    # Генерируем тестовые данные
    customer_data = {
        'first_name': Customer.first_name,
        'last_name': Customer.last_name,
        'post_code': Customer.post_code
    }

    with allure.step("Открытие страницы менеджера"):
        manager_page = ManagerPage(driver)
        manager_page.open()

    with allure.step("Переход на страницу добавления клиента"):
        manager_page.click_on_item_menu("Add Customer")
        add_customer_page = AddCustomer(driver)

    with allure.step(f"Заполнение данных клиента: {customer_data}"):
        add_customer_page.enter_first_name(customer_data['first_name'])
        add_customer_page.enter_last_name(customer_data['last_name'])
        add_customer_page.enter_post_code(customer_data['post_code'])
        add_customer_page.click_add_customer_submit_btn()

    with allure.step("Проверка сообщения о создании клиента"):
        expected_prefix = "Customer added successfully with customer id :"
        actual_message = add_customer_page.get_alert_message()

        assert actual_message.startswith(expected_prefix), \
            f"Alert message should start with '{expected_prefix}', got '{actual_message}'"

        customer_id = actual_message[len(expected_prefix):].strip()
        allure.attach(f"Created customer ID: {customer_id}", name="Customer ID")

    with allure.step("Подтверждение алерта"):
        add_customer_page.click_alert()

    with allure.step("Проверка наличия клиента в списке"):
        manager_page.click_on_item_menu("Customers")
        list_customers_page = ListCustomer(driver)
        customers_data = list_customers_page.get_all_data_customers()

        customer_tuple = (
            customer_data['first_name'],
            customer_data['last_name'],
            customer_data['post_code']
        )

        assert customer_tuple in customers_data, (
            f"Customer {customer_data['first_name']} {customer_data['last_name']} "
            f"with Post Code {customer_data['post_code']} not found in customers list"
        )