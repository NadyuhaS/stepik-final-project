import math
from .base_page import BasePage
from .locators import BasketLocators
from selenium.webdriver.common.by import By

class BasketPage( BasePage ):
    def add_to_basket( self ) :
        button = self.browser.find_element( *BasketLocators.ADD_TO_BASKET_BUTTON )
        button.click()

    def switch_to_alert( self ) :
        alert = self.browser.switch_to.alert
        x = int( alert.text.split( " " )[2] )
        alert.send_keys( str( math.log( abs( 12 * math.sin( x ) ) ) ) )
        alert.accept()
        try :
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print( f" nu tip takoe {alert_text}" )
            alert.accept()
        except :
            print( f"No second alert presented " )


    def should_be_success_message( self ) :
        assert self.is_element_present( *BasketLocators.MESSAGE_SUCCESS_ADD_TO_BASKET ), f"No such element on page"

    def is_equal_names_book( self ) :
        name_book = self.browser.find_element( *BasketLocators.NAME_BOOK ).text
        name_in_message = self.browser.find_element( *BasketLocators.MESSAGE_SUCCESS_ADD_TO_BASKET ).text
        assert  name_book == name_in_message, f"Names not equal "

    def should_not_be_success_message( self ) :
        assert self.is_not_element_present( *BasketLocators.MESSAGE_SUCCESS_ADD_TO_BASKET ), "It has^ but should not"

    def should_not_see_success_message( self ):
        assert self.is_disappear( *BasketLocators.MESSAGE_SUCCESS_ADD_TO_BASKET ), "It has ^ but should not"

    def is_empty_basket( self ) :
        assert self.is_not_element_present( *BasketLocators.BASKETS_BOOK ), "Basket must be empty"

    def is_message_empty_basket( self ) :
        assert self.browser.find_element( By.CSS_SELECTOR, '.content #content_inner p' ).text != '', "Must have message"