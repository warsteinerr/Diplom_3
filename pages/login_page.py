import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage



class LoginPage(BasePage):

    def click_on_recover_password(self):
        self.click_element_with_js(LoginPageLocators.RECOVER_PASSWORD)




