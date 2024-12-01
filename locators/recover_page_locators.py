from selenium.webdriver.common.by import By


class RecoverPageLocators:
    RECOVER_HEAD2 = By.XPATH, '//h2[text()="Восстановление пароля"]'  # Заголовок2 странички восстановления пароля
    MAIL_FIELD = By.XPATH, '//input'  # Введите емейл
    ENTER_CODE = By.XPATH, '//label[text()="Введите код из письма"]'  # Поле введите код из письма при восстановлении
    RECOVER_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # Кнопка восстановить
    SHOW_PASSWORD = By.XPATH, '//div[@class="input__icon input__icon-action"]'  # Кнопка скрыть показать пароль
    ACTIVE_PASSWORD_FIELD = By.XPATH, '//div[contains(@class, "input_status_active")]'  # Активное поле пароля
    OVERLAY = By.XPATH, '//*[contains(@class, "Modal_modal_overlay__x2ZCr")]'
