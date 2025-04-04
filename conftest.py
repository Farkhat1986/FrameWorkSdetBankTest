import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для инициализации WebDrivers.

    Returns:
        WebDriver: Экземпляр WebDriver для управления браузером.
    """
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
