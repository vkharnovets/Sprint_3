from selenium.webdriver.common.by import By

class Locators:
    # Registration form
    reg_form_name_input = By.XPATH, './/label[text()=\'Имя\']/following-sibling::input' #Окно для ввода имени
    reg_form_email_input = By.XPATH, './/label[text()=\'Email\']/following-sibling::input' #Окно для ввода email
    reg_form_password_input = By.XPATH, './/input[@type=\'password\' and @name=\'Пароль\']' #Окно для ввода пароля
    reg_form_confirm_button = By.XPATH, './/button[text()=\'Зарегистрироваться\']' #Кнопка отсылки данных
    reg_form_wrong_password_label = By.XPATH, './/p[text()=\'Некорректный пароль\']' #Текст ошибки о пароле, не соответствующем правилам
    reg_form_login_link = By.XPATH, './/a[text()=\'Войти\']' #Ссылка на страницу логина

    # Login form
    login_form_email_input = By.XPATH, './/label[text()=\'Email\']/following-sibling::input' #Окно для ввода email
    login_form_password_input = By.XPATH, './/input[@type=\'password\' and @name=\'Пароль\']' #Окно для ввода пароля
    login_form_login_button = By.XPATH, './/button[text()=\'Войти\']' #Кнопка отсылки данных

    # Main page
    main_page_login_button = By.XPATH, './/button[text()=\'Войти в аккаунт\']' #Кнопка перехода на страницу логина
    main_page_profile_button = By.XPATH, './/p[text()=\'Личный Кабинет\']' #Кнопка перехода в профиль
    main_page_create_order_button = By.XPATH, './/button[text()=\'Оформить заказ\']' #Кнопка оформления заказа

    main_page_buns_control = By.XPATH, './/span[text()=\'Булки\']/parent::div' #Ссылка для навигации на группу ингридиентов "Булки"
    main_page_sauces_control = By.XPATH, './/span[text()=\'Соусы\']/parent::div' #Ссылка для навигации на группу ингридиентов "Соусы"
    main_page_fillings_control = By.XPATH, './/span[text()=\'Начинки\']/parent::div' #Ссылка для навигации на группу ингридиентов "Начинки"

    main_page_buns_label = By.XPATH, './/h2[text()=\'Булки\']' #Заголовок группы ингридиентов "Булки"
    main_page_sauces_label = By.XPATH, './/h2[text()=\'Соусы\']' #Заголовок группы ингридиентов "Соусы"
    main_page_fillings_label = By.XPATH, './/h2[text()=\'Начинки\']' #Заголовок группы ингридиентов "Начинки"

    # Profile page
    profile_page_constructor_button = By.XPATH, './/p[text()=\'Конструктор\']' #Кнопка перехода в конструктор
    profile_page_logout_button = By.XPATH, './/button[text()=\'Выход\']' #Кнопка для осуществления logout
    profile_page_main_logo = By.XPATH, './/div[@class=\'AppHeader_header__logo__2D0X2\']' #Логотип с бургером (используется для перехода на главную страницу)

    # Forgot password page
    forgot_password_page_login_link = By.XPATH, './/a[text()=\'Войти\']' #Ссылка для перехода на страницу логина
