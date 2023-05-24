Финальное задание 3 спринта

-> conftest.py - fixtures

-> helpers.py - вспомогательные функции и переменные, используемые в нескольких файлах

-> locators.py - локаторы

-> urls.py - url'ы используемых страниц проекта

-> tests:
		-> TestConstructor.py - тесты на конструктор бургеров:
			- test_constructor_page_shown_from_profile_using_profile_button - проверка перехода в конструктор из профиля по кнопке
			- test_constructor_page_shown_from_profile_using_logo - проверка перехода в конструктор из профиля по иконке
			- test_page_is_scrolled_on_fillings - проверка навигации на группу ингридиентов "Начинки"
			- test_page_is_scrolled_on_sauces - проверка навигации на группу ингридиентов "Соусы"
			- test_page_is_scrolled_on_buns - проверка навигации на группу ингридиентов "Булки"
			
		-> TestLogin.py - тесты на  проверку логина:
			- test_login_page_shown_by_login_button - доступность страницы логина через кнопку на главной странице
			- test_login_page_shown_by_profile_button - страницы логина показывается при нажатии на кнопку профиля, если логин не произведен
			- test_login_page_shown_by_login_link_from_register_form - доступность страницы из формы регистрации
			- test_login_page_shown_by_login_link_from_forgot_password_page- доступность страницы из формы восстановления пароля
			- test_successful_login - проверка того, что логин работает
		
		-> TestProfile.py - тесты личного кабинета
			- test_profile_page_shown_by_profile_button - проверка страницы профиля через кнопку на главной странице
			- test_logout_by_profile_logout_button - проверка возможности сделать logout из профиля
			
		-> TestRegistration.py - тесты на регистрацию нового пользлвателя
			- test_successful_registration - проверка на успешную регистрацию, если данные корректны
			- test_failed_registration_wrong_password - проверка появления ошибки при слишком коротком пароле
