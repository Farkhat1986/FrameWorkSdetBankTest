from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.config import WAIT_TIMEOUT
from data.config import PAGE_URL


class BasePage:
    """Базовый класс для всех страниц"""
    PAGE_URL = PAGE_URL

    def __init__(self, driver: WebDriver):
        """Инициализируем экземпляр страницы. Экземпляр WebDriver для управления браузером"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    # Основные методы взаимодействия с элементами
    def open(self):
        """Открывает страницу."""
        self.driver.get(self.PAGE_URL)

    def click_element(self, locator: tuple[str, str]):
        """Кликает по элементу после ожидания его кликабельности. Кортеж (стратегия, значение) для поиска элемента"""
        self.element_to_be_clickable(locator).click()

    def send_keys_to_element(self, locator: tuple[str, str], text: str):
        """Вводит текст в элемент после ожидания его кликабельности. Кортеж (стратегия, значение) для поиска элемента
           text: Текст для ввода
        """
        element = self.element_to_be_clickable(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator: tuple[str, str]):
        """Получает текст элемента после ожидания его видимости. Кортеж (стратегия, значение) для поиска элемента
           Возвращает Текст элемента
        """
        return self.presence_of_element_located(locator).text

    def is_element_present(self, locator: tuple[str, str]):
        """Проверяет наличие элемента на странице. Кортеж (стратегия, значение) для поиска элемента
        Returns:
            True если элемент присутствует, иначе False
        """
        try:
            self.presence_of_element_located(locator)
            return True
        except:
            return False

    # Методы ожидания элементов
    def element_to_be_clickable(self, locator: tuple[str, str]):
        """Ожидает, что элемент станет кликабельным. Кортеж (стратегия, значение) для поиска элемента
        Returns:
            Найденный WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def presence_of_element_located(self, locator: tuple[str, str]):
        """Ожидает присутствие элемента в DOM. Кортеж (стратегия, значение) для поиска элемента
        Returns:
            Найденный WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator: tuple[str, str]):
        """Ожидает присутствие всех элементов в DOM. Кортеж (стратегия, значение) для поиска элементов
        Returns:
            Список найденных WebElement
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # Методы для работы с алертами
    def alert_is_present(self):
        """Проверяет наличие алерта.
        Returns:
            Экземпляр Alert если алерт присутствует, иначе False
        """
        return self.wait.until(EC.alert_is_present())

    def get_alert_text(self):
        """Получает текст из алерта.
        Returns:
            Текст алерта
        """
        self.alert_is_present()
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        """Принимает алерт (нажимает OK)."""
        self.alert_is_present()
        self.driver.switch_to.alert.accept()