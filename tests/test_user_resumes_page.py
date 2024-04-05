import time

import pytest

from pages.user_resume import *
from pages.main_page import Autorization_customers
from pages.users import *
from pages.locators import *
import time


@pytest.mark.parametrize('username, password', [(test_user_customers_with_resumes, test_password_user_with_resumes)])
def test_1(browser, username, password):
    test_1 = UserResumes(browser, user_resume_url)
    test_1.open()
    '''Авторизация'''
    # test_1.top_button_login().click()

    # Ожидаем открытия окна авторизации
    # test_1.wait_text_in_element(button_login_accept, "Войти")

    # Авторизуемся методом из main_pages
    authorization_1 = Autorization_customers(browser)
    authorization_1.login_with_resumes(username, password)

    test_1.wait_visibility_of_element_located(create_resume_btn)

    test_1.script_scroll(test_1.create_resume_btn())



    test_1.resume_more_options_kebab().click()

    time.sleep(3)