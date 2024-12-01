import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по кнопке войти в аккаунт')
    def click_personal_account_button(self):
        self.click_element_with_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке конструктора')
    def click_constructor_button(self):
        self.click_element_with_js(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликь по кнопке лента заказов')
    def click_feed_button(self):
        self.find_elements_with_wait(MainPageLocators.FEED_BUTTON)
        self.click_element_with_js(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик по ингредиенту ')
    def click_ingredient(self):
        self.find_elements_with_wait(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)
        self.click_element_with_js(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)

    @allure.step('Клик по крестику "')
    def close_modal_window(self):
        self.explicit_wait(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW)
        self.click_element_with_js(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW)

    @allure.step('Кликнуть по кнопке оформить заказ')
    def click_checkout_button(self):
        self.click_element_with_js(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Перетаскивание ингредиента ')
    def drag_and_drop_ingredient(self):
        from_element = self.explicit_wait(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)
        to_element = self.explicit_wait(MainPageLocators.CONSTRUCTOR_BASKET)
        self.drag_and_drop_element(from_element, to_element)

    @allure.step('Клик по кнопке личный кабинет')
    def click_personal_account_link(self):
        self.click_element_with_js(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Проверка видимости кнопки оформить заказ')
    def wait_checkout_button_visible(self):
        self.explicit_wait(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Проверка отображение соберите бургер')
    def check_title_make_burger(self):
        return self.click_on_element(MainPageLocators.MAKE_BURGER_TITLE)

    @allure.step('Проверка окна детали ингредиента')
    def check_details_modal_window(self):
        self.explicit_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
        return self.check_element_is_displayed(MainPageLocators.DETAILS_OF_INGREDIENT)


    @allure.step('Проверка закрытия окна детали ингредиента')
    def check_details_modal_window_closed(self):
        self.explicit_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
        return not self.check_element_is_displayed(MainPageLocators.DETAILS_OF_INGREDIENT)

    @allure.step('Получаем счетчик ъингредиентов')
    def get_counter_of_ingredients_in_basket(self):
        return self.get_text_from_element(MainPageLocators.COUNTER_OF_INGREDIENT)

    @allure.step('Проверка отображения окна о создании заказа')
    def check_window_after_create_displayed(self):
        self.explicit_wait(MainPageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)
        return self.check_element_is_displayed(MainPageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        close_button = self.explicit_wait(MainPageLocators.CLOSE_MOD_WINDOW_AFTER_CREATE_ORDER)
        self.click_element_with_js(close_button)

    @allure.step('Получение номера заказа после создания')
    def get_number_in_modal_window_after_create_order(self):
        self.wait_for_text_to_be_changed(MainPageLocators.NINES_IN_MOD_WIN_AFTER_CREATE_ORDER, '9999')
        return self.get_text_from_element(MainPageLocators.NINES_IN_MOD_WIN_AFTER_CREATE_ORDER)

