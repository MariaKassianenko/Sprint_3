from selenium.webdriver.common.by import By


class RegPageStellarBurgers:
    name_input = [By.XPATH, '//label[text()="Имя"]/following-sibling::input']  # Поле ввода имени
    email_input = [By.XPATH, '//label[text()="Email"]/following-sibling::input']  # Поле для ввода Email
    password_input = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']  # Поле для ввода пароля
    register_button = [By.XPATH, '//button[text()="Зарегистрироваться"]']  # Кнопка Зарегистрироваться
    reg_wrong_password_message = [By.XPATH,
                                  '//p[text()="Некорректный пароль"]']  # Сообщение о некорр. пароле при регистрации
    enter_link = [By.XPATH, '//a[text()="Войти"]']  # Кнопка Войти


class AuthPageStellarBurgers:
    email_input_auth = [By.XPATH, '//input[@name="name"]']  # Поле ввода email на странице Авторизации
    password_input = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']  # Поле для ввода пароля
    enter_button = [By.XPATH, '//button[text()="Войти"]']  # Кнопка Войти
    registration_link = [By.XPATH,
                         '//a[text()="Зарегистрироваться"]']  # ссылка Зарегистрироваться на странице авторизации
    password_recovery_link = [By.XPATH,
                              '//a[text()="Восстановить пароль"]']  # ссылка Зарегистрироваться на странице авторизации


class PwdRecoveryPageStellarBurgers:
    enter_link = [By.XPATH, '//a[text()="Войти"]']  # Кнопка Войти


class MainPageStellarBurgers:
    user_profile_button = [By.XPATH, '//p[text()="Личный Кабинет"]']  # Кнопка перехода в профайл Личный кабинет
    name_field = [By.XPATH, '//input[@name="Name"]']  # Поле Имя
    cancel_button = [By.XPATH, '//button[text()="Отмена"]']  # Кнопка Отмена
    exit_button = [By.XPATH, '//button[text()="Выход"]']  # Кнопка Выход
    enter_my_account_button = [By.XPATH, '//button[text()="Войти в аккаунт"]']  # Кнопка Войти в аккаунт
    constructor_button = [By.XPATH, '//a[p[text()="Конструктор"]]']  # Кнопка Конструктор
    main_icon = [By.XPATH, '//div[contains(@class, "logo")]']  # Логотип Стеллар Бургерс в хэдере


def ingredients_locator(ingredient: str):
    return [By.XPATH, f'//h2[text()="{ingredient}"]']


def current_ingredient_locator(ingredient: str):
    return [By.XPATH, f'//div[span[text()="{ingredient}"]]']
