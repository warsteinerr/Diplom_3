import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.account_page import AccountPage


class TestMainPage:
    @allure.title("Переход на конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        main_page.click_constructor_button()
        assert main_page.check_title_make_burger

    @allure.title("Проверка перехода ленту заказов")
    def test_go_to_feed_orders(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button()
        assert feed_page.check_title_of_orders_list_displayed()

    @allure.title("Проверка появления окна с деталями")
    def test_show_modal_window_details_after_click_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_details_modal_window()

    @allure.title('Проверка закрытия окна по крестику')
    def test_close_modal_window_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal_window()
        assert main_page.check_details_modal_window_closed() is False

    @allure.title('При изменений в счетчике ингредиента')
    def test_increase_counter_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        assert main_page.get_counter_of_ingredients_in_basket() != 0

    @allure.title('Проверка оформеления заказа залогиненным юзером')
    def test_make_order_autorised(self, driver, create_user):
        email, password = create_user
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page.send_login_data(email, password)
        account_page.click_login_button()
        main_page.wait_checkout_button_visible()
        main_page.drag_and_drop_ingredient()
        main_page.click_checkout_button()
        assert main_page.check_window_after_create_displayed()
