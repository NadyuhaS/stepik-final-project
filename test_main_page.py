from .page.main_page import MainPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage

def test_guest_can_go_to_login_page( browser ):
    link = "http://selenium1py.pythonanywhere.com/"
    #browser.get( link )
    #login_link = browser.find_element_by_css_selector( '#login_link' )
    #login_link.click()
    page = MainPage( browser, link )
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link( browser ) :
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage( browser, link )
    page.open()
    page.should_be_login_link()

def test_forms( browser ) :
    link = "http://selenium1py.pythonanywhere.com/" ###don't know
    page = MainPage( browser, link )
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page =  BasketPage(browser, link)
    page.open()
    page.should_be_login_link()

