import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recover_page import PasswordRecoverPage


class TestRecoverPage:

    @allure.title("Проверка переход на страничку восстановления пароля")
    def test_go_to_recover_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recover_page = PasswordRecoverPage(driver)
        main_page.click_personal_account_button()
        login_page.click_on_recover_password()
        assert recover_page.check_recovery_head()

    @allure.title("Проверка работы после ввода имейла и нажатия восстановить")
    def test_enter_email(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recover_page = PasswordRecoverPage(driver)
        main_page.click_personal_account_button()
        login_page.click_on_recover_password()
        recover_page.enter_email()
        recover_page.click_recover_button()
        assert recover_page.check_enter_code_field()


    @allure.title("Проверка активности поля пароля после нажатия на иконку")
    def test_active_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recover_page = PasswordRecoverPage(driver)
        main_page.click_personal_account_button()
        login_page.click_on_recover_password()
        recover_page.enter_email()
        recover_page.click_recover_button()
        recover_page.click_show_password_icon()
        assert recover_page.check_password_field_active()





