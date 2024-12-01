from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure


class FeedPage(BasePage):

	@allure.step('Клик по первому заказу')
	def click_first_order(self):
		self.explicit_wait(FeedPageLocators.FIRST_ORDER_CARD)
		self.click_on_element(FeedPageLocators.FIRST_ORDER_CARD)

	@allure.step('Получаем номер заказа в карточке')
	def get_order_card_id(self):
		return self.get_text_from_element(FeedPageLocators.ORDER_CARD_ID)

	@allure.step('Проверка наличия заказа в ленте')
	def check_order_id_in_order_list(self, order_id):
		locator = FeedPageLocators.ORDER_NUMBER_IN_FEED_PAGE
		locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
		self.explicit_wait(locator_with_order_id)
		return self.check_element_is_displayed(locator_with_order_id)

	@allure.step('Получение количества заказов за все время')
	def get_all_time_orders_quantity(self):
		self.explicit_wait(FeedPageLocators.ORDERS_ALL_TIME)
		return self.get_text_from_element(FeedPageLocators.ORDERS_ALL_TIME)

	@allure.step('Получение количества заказов за сегодня')
	def get_today_orders_quantity(self):
		self.find_elements_with_wait(FeedPageLocators.ORDERS_TODAY)
		return self.get_text_from_element(FeedPageLocators.ORDERS_TODAY)


	@allure.step('Дождаться отображения заголовка Ленты заказов')
	def check_title_of_orders_list_displayed(self):
		self.explicit_wait(FeedPageLocators.ORDER_FEED_TITLE)
		return self.check_element_is_displayed(FeedPageLocators.ORDER_FEED_TITLE)

	@allure.step('Проверка отображение модального окна')
	def check_modal_window(self):
		self.find_elements_with_wait(FeedPageLocators.MODAL_WINDOW_TITLE)
		return self.check_element_is_displayed(FeedPageLocators.MODAL_WINDOW_TITLE)

	@allure.step('Получить номер заказа в "В работе"')
	def get_number_of_order_in_progress(self):
		return self.get_text_from_element(FeedPageLocators.NUM_ORDER_IN_WORK)

