import allure
from locators.recover_page_locators import RecoverPageLocators
from pages.base_page import BasePage
from helper import *


class PasswordRecoverPage(BasePage):

    @allure.step('Проверяем есть ли заголовок Восстановить пароль на странице')
    def check_recovery_head(self):
        return self.explicit_wait(RecoverPageLocators.RECOVER_HEAD2)

    @allure.step('Передаем емейл')
    def enter_email(self):
        email = create_random_user()['email']
        self.send_keys_to_element(RecoverPageLocators.MAIL_FIELD, email)

    @allure.step('Нажимаем кнопку восстановить')
    def click_recover_button(self):
        self.find_elements_with_wait(RecoverPageLocators.RECOVER_BUTTON)
        self.click_on_element(RecoverPageLocators.RECOVER_BUTTON)

    @allure.step('Проверяем что есть поле введите код из письма')
    def check_enter_code_field(self):
        return self.explicit_wait(RecoverPageLocators.ENTER_CODE)

    @allure.step('Клик по иконке показать/скрыть пароль')
    def click_show_password_icon(self):
        self.find_elements_with_wait(RecoverPageLocators.SHOW_PASSWORD)
        self.click_element_with_js(RecoverPageLocators.SHOW_PASSWORD)

    @allure.step('Проверяес что поле ввода пароля активно')
    def check_password_field_active(self):
        return self.explicit_wait(RecoverPageLocators.ACTIVE_PASSWORD_FIELD)

    @allure.step('Ожидаем пока пропадет оверлей')
    def wait_icon_overlay(self):
        self.wait_overlay(RecoverPageLocators.OVERLAY)




