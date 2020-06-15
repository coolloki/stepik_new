link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_add_to_basket_exist(browser):
    browser.get(link)
    try:
        btn_add_to_basket = browser.find_element_by_class_name('btn-add-to-basket')
        btn_exist = True
    except:
        btn_exist = False

    assert btn_exist == True, 'Button "Add to basket" in not exist'
