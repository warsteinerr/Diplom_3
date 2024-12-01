from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def explicit_wait(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element

    def click_element_with_js(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def find_elements_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator))


    def click_on_element(self, locator):
        element = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(element).click().perform()

    def wait_overlay(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(locator)
        )

    def send_keys_to_element(self, locator, key):
        self.explicit_wait(locator).send_keys(key)

    def get_text_from_element(self, locator):
        return self.explicit_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.explicit_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_element_is_displayed(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def get_link(self, link):
        self.driver.get(link)

    def url_to_be_visible(self, link):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(link)
        )

    def wait_for_new_tab_and_switch(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def drag_and_drop_element(self, from_element, to_element):
        ActionChains(self.driver).drag_and_drop(from_element, to_element).pause(8).perform()



    def wait_for_text_to_be_changed(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(
                                                        EC.text_to_be_present_in_element(locator, value))

    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

