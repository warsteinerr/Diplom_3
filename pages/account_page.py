from pages.base_page import BasePage
import allure
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    @allure.step('Вводим почти и пароль')
    def send_login_data(self, email, password):
        self.send_keys_to_element(AccountPageLocators.EMAIL_INPUT_FIELD, email)
        self.send_keys_to_element(AccountPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Нажимаем кнопку войти')
    def click_login_button(self):
        self.click_element_with_js(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка кнопки выход')
    def check_exit_button(self):
        self.explicit_wait(AccountPageLocators.EXIT_BUTTON)
        return self.check_element_is_displayed(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Клик по кнопке выйти"')
    def click_exit_button(self):
        self.click_element_with_js(AccountPageLocators.EXIT_BUTTON)

    @allure.step('Ожидание кнопки войти"')
    def login_button_wait(self):
        return self.explicit_wait(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Жмем по кнопке Лента заказов"')
    def click_feed_button(self):
        self.find_elements_with_wait(AccountPageLocators.FEED_BUTTON)
        self.click_element_with_js(AccountPageLocators.FEED_BUTTON)

    @allure.step('Проверка наличия кнопки войти')
    def check_login_button_displayed(self):
        return self.check_element_is_displayed(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Ожидание кнопки войти"')
    def login_button_wait(self):
        return self.explicit_wait(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка отображения выполненных заказов')
    def check_history_feed(self):
        return self.check_element_is_displayed(AccountPageLocators.HISTORY_FEED_TODAY)

    @allure.step('Ожидание отображения заказов')
    def wait_history_feed_visible(self):
        self.explicit_wait(AccountPageLocators.HISTORY_FEED_TODAY)


