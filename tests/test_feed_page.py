from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.account_page import AccountPage
import allure


class TestFeedPage:
    @allure.step('Проверка открытия всплывающего окна при клике на заказ')
    def test_opening_modal_window(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_feed_button()
        feed_page.click_first_order()
        assert feed_page.check_modal_window()

    @allure.title('Проверка отображения заказов пользователя в ленте заказов')
    def test_new_order_from_history_displayed(self, driver, create_user):
        email, password = create_user
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page.send_login_data(email, password)
        account_page.click_login_button()
        main_page.wait_checkout_button_visible()
        main_page.drag_and_drop_ingredient()
        main_page.click_checkout_button()
        main_page.close_order_window()
        main_page.click_personal_account_link()
        account_page.check_exit_button()
        account_page.click_feed_button()
        order_id = feed_page.get_order_card_id()
        main_page.click_feed_button()
        assert feed_page.check_order_id_in_order_list(order_id)

    @allure.title('Проверка увеличения счетчика заказов за все вермя')
    def test_counter_orders_all_time(self, driver, create_user):
        email, password = create_user
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_feed_button()
        orders_quantity_1 = feed_page.get_all_time_orders_quantity()
        main_page.click_constructor_button()
        main_page.click_personal_account_button()
        account_page.send_login_data(email, password)
        account_page.click_login_button()
        main_page.wait_checkout_button_visible()
        main_page.drag_and_drop_ingredient()
        main_page.click_checkout_button()
        main_page.close_order_window()
        main_page.click_personal_account_link()
        account_page.check_exit_button()
        account_page.click_feed_button()
        orders_quantity_2 = feed_page.get_all_time_orders_quantity()
        assert orders_quantity_2 > orders_quantity_1

    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    def test_counter_orders_today(self, driver, create_user):
        email, password = create_user
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_feed_button()
        orders_quantity_1 = feed_page.get_today_orders_quantity()
        main_page.click_constructor_button()
        main_page.click_personal_account_button()
        account_page.send_login_data(email, password)
        account_page.click_login_button()
        main_page.wait_checkout_button_visible()
        main_page.drag_and_drop_ingredient()
        main_page.click_checkout_button()
        main_page.close_order_window()
        main_page.click_personal_account_link()
        account_page.check_exit_button()
        account_page.click_feed_button()
        orders_quantity_2 = feed_page.get_today_orders_quantity()
        assert int(orders_quantity_2) > int(orders_quantity_1)

    @allure.title('Проверка появления нового заказа в работе')
    def test_order_in_progress_displayed(self, driver, create_user):
        email, password = create_user
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        account_page.send_login_data(email, password)
        account_page.click_login_button()
        main_page.wait_checkout_button_visible()
        main_page.drag_and_drop_ingredient()
        main_page.click_checkout_button()
        new_order_id = main_page.get_number_in_modal_window_after_create_order()
        main_page.close_order_window()
        main_page.click_feed_button()
        assert feed_page.get_number_of_order_in_progress() == f'0{new_order_id}'
