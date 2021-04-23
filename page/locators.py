from selenium.webdriver.common.by import By

class BasketLocators():
    ADD_TO_BASKET_BUTTON = ( By.CSS_SELECTOR, 'button.btn-add-to-basket' )
    NAME_BOOK = ( By.CSS_SELECTOR, '.product_main h1' )
    MESSAGE_SUCCESS_ADD_TO_BASKET = ( By.CSS_SELECTOR, '.alert-success .alertinner strong')
    BASKET_LINK = ( By.CSS_SELECTOR, '.basket-mini a.btn-default' )
    BASKETS_BOOK = ( By.CSS_SELECTOR, '.basket-title' )

class BasePageLocators():
    LOGIN_LINK = ( By.CSS_SELECTOR, '#login_link' )
    LOGIN_LINK_INVALID = ( By.CSS_SELECTOR, '#login_link_inc' )
    USER_ICON = ( By.CSS_SELECTOR, '.icon-user' )

class LoginPageLocators():
    USERNAME = ( By.CSS_SELECTOR, '#login_form #id_login-username[required]' )
    PASSWORD = ( By.CSS_SELECTOR, '#login_form #id_login-password[required]' )
    LOGIN_FORM = ( By.CSS_SELECTOR, '#login_form' )
    REGISTER_FORM = ( By.CSS_SELECTOR, '#register_form' )
    EMAILL_ADRESS = ( By.CSS_SELECTOR, '#register_form input[type="email"]' )
    PASSWOR = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]' )
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form button[name="registration_submit"]' )
    SUCCESS_MESSAGE = ( By.CSS_SELECTOR, "#messages .alert-success")

class MainPageLocators():
    LOGIN_LINK = ( By.CSS_SELECTOR, '#login_link' )