from .page.basket_page import BasketPage
from .page.login_page import LoginPage
import pytest
import time
from random import randint

email = str( time.time() ) + str( randint( 0, 100 ) ) + "@fakemail.org"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail ),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_basket( browser, link ):
    print( link + '\n')
    page = BasketPage( browser, link )
    page.open()
    page.add_to_basket()
    page.switch_to_alert()
    page.should_be_success_message()
    page.is_equal_names_book()

@pytest.mark.need_review
def test_guest_can_add_to_basket( browser ):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage( browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()
    page.is_equal_names_book()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket( browser ) :
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link1)
    page.open()
    page.add_to_basket()
    #page.switch_to_alert()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message( browser ) :
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage( browser, link1 )
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket( browser ) :
    link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link1)
    page.open()
    page.add_to_basket()
    #page.switch_to_alert()
    page.sould_not_see_success_message()

def test_guest_should_see_login_link_on_product_page( browser ):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page( browser ) :
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                                  "http://selenium1py.pythonanywhere.com/en-gb/catalogue/" ] )
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page( browser, link ) :
    page = BasketPage( browser, link )
    page.open()
    page.go_to_basket()
    page.is_empty_basket()
    page.is_message_empty_basket()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage() :
    @pytest.fixture( scope="function", autouse=True )
    def setup( self, browser ):
        self.browser = browser
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
        page = LoginPage( self.browser, self.link )
        page.open()
        page.go_to_login_page()
        page.should_be_register_form()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user( email, '1q@3e4r5t6y' )



    def test_user_cant_see_success_message( self ) :
        link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage( self.browser, link1)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()


    def test_user_can_add_product_to_basket( self ) :
        link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage( self.browser, link )
        page.open()
        page.should_be_authorized_user()
        page.add_to_basket()
        page.should_be_success_message()
        page.is_equal_names_book()