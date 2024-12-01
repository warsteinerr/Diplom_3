from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure


class TestAccountPage:
	@allure.title("Проверка переход в ЛК по клику на личный кабинет ")
	def test_go_to_account_page(self, driver, create_user):
		email, password = create_user
		account_page = AccountPage(driver)
		main_page = MainPage(driver)
		main_page.click_personal_account_button()
		account_page.send_login_data(email, password)
		account_page.click_login_button()
		main_page.wait_checkout_button_visible()
		main_page.click_personal_account_link()
		assert account_page.check_exit_button()

	@allure.title("Проверка выхода из аккаунта")
	def test_account_page_exit(self, driver, create_user):
		email, password = create_user
		account_page = AccountPage(driver)
		main_page = MainPage(driver)
		main_page.click_personal_account_button()
		account_page.send_login_data(email, password)
		account_page.click_login_button()
		main_page.wait_checkout_button_visible()
		main_page.click_personal_account_link()
		account_page.check_exit_button()
		account_page.click_exit_button()
		account_page.login_button_wait()
		assert account_page.check_login_button_displayed()

	@allure.title("Проверка перехода в  историю заказов")
	def test_go_to_history_orders(self, driver, create_user):
		email, password = create_user
		account_page = AccountPage(driver)
		main_page = MainPage(driver)
		main_page.click_personal_account_button()
		account_page.send_login_data(email, password)
		account_page.click_login_button()
		main_page.wait_checkout_button_visible()
		main_page.click_personal_account_link()
		account_page.click_feed_button()
		account_page.wait_history_feed_visible()
		assert account_page.check_history_feed()