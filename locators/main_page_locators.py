from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]'  # Кнопка личный кабинет на главной
    CHECKOUT_BUTTON = By.XPATH, '//button[ text()="Оформить заказ" ]'  # Кнопка оформить заказ
    PERSONAL_ACCOUNT_LINK = By.XPATH, '//p[contains(text(),"Личный Кабинет")]'
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[contains(text(),"Конструктор")]'
    BUTTON_CLOSE_MODAL_WINDOW = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button[contains(@class, "close")]'
    CONSTRUCTOR_BASKET = By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]'
    COUNTER_OF_INGREDIENT = By.XPATH, '//p[@class="text text_type_digits-medium mr-3"]'
    MODAL_WINDOW_AFTER_CREATE_ORDER = By.XPATH, ('//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                                 '(@class, "Modal_modal__container")]')
    FEED_BUTTON = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    MAKE_BURGER_TITLE = By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]'
    DETAILS_OF_INGREDIENT = By.XPATH, '//p[contains(text(),"Калории,ккал")]'
    INGREDIENT_FROM_CONSTRUCTOR = By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]'
    CLOSE_MOD_WINDOW_AFTER_CREATE_ORDER = By.XPATH, '//button[@type="button"]'
    NINES_IN_MOD_WIN_AFTER_CREATE_ORDER = By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2'


