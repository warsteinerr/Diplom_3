from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_TITLE = By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1'  # Заголовок "Лента заказов"
    FIRST_ORDER_CARD = By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r mb-6")][1]'
    MODAL_WINDOW_TITLE = By.XPATH, '//div[contains(@class, "Modal_orderBox")]//h2'  # Заголовок модального окна
    ORDER_CARD_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    ORDER_NUMBER_IN_FEED_PAGE = By.XPATH, './/*[text()="{order_id}"]'
    ORDERS_ALL_TIME = By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p'

    ORDERS_TODAY = By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    NUM_ORDER_IN_WORK = (By.XPATH, '//ul[contains(@class, '
                                   '"OrderFeed_orderListReady")]/li[contains(@class, '
                                   '"text_type_digits-default")]')
