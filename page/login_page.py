import sys
from selenium.webdriver.common.by import By
sys.path.append('../')
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage( BasePage ):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in str(self.browser.current_url)

    def should_be_login_form( self ):
        assert self.is_element_present( *LoginPageLocators.LOGIN_FORM ), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present( *LoginPageLocators.REGISTER_FORM ), "Register form is not presented"


    def register_new_user( self , email, password ):
        input_email = self.browser.find_element( *LoginPageLocators.EMAILL_ADRESS )
        input_email.send_keys( str( email ) )
        input_password1 = self.browser.find_element( *LoginPageLocators.PASSWOR )
        input_password1.send_keys( str( password ) )
        input_password2 = self.browser.find_element( *LoginPageLocators.CONFIRM_PASSWORD )
        input_password2.send_keys( str( password ) )
        button_register = self.browser.find_element( *LoginPageLocators.REGISTER_BUTTON )
        button_register.click()
        assert self.is_element_present( *LoginPageLocators.SUCCESS_MESSAGE ), "You dont register"

