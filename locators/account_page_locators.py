from selenium.webdriver.common.by import By


class AccountPageLocators:
    LOGIN_BUTTON = By.XPATH, '//button[ text()="Войти" ]'  # кнопка войти на странице login
    EMAIL_INPUT_FIELD = By.XPATH, '//input[@name="name"]'
    PASSWORD_INPUT_FIELD = By.XPATH, '//input[@name="Пароль"]'
    EXIT_BUTTON = By.XPATH, '//button[contains(text(), "Выход")]'  # кнопка Выход из ЛК
    FEED_BUTTON = By.XPATH, '//p[contains(text(),"Лента Заказов")]'
    HISTORY_FEED_TODAY = By.XPATH, '// p[contains(text(), "Выполнено за сегодня:")]'
    ACCOUNT_OVERLAY = By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"
