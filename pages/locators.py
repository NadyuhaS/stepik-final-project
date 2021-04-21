from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = ( By.CSS_SELECTOR, '#login_link' )

class LoginPageLocators():
    USERNAME = ( By.CSS_SELECTOR, '#login_form #id_login-username[required]' )
    PASSWORD = ( By.CSS_SELECTOR, '#login_form #id_login-password[required]' )
    LOGIN_FORM = ( By.CSS_SELECTOR, '#login_form' )
    REGISTER_FORM = ( By.CSS_SELECTOR, '#register_form' )
