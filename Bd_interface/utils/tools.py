from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, element):
    return WebDriverWait(driver, 10).until(lambda s: s.find_element(*element))
