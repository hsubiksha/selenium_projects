import pytest
import yaml
import os
from pages.register_page import RegisterPage
yaml_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test_data.yaml'))

@pytest.mark.parametrize("user_data", yaml.safe_load(open(yaml_file_path)).values())
def test_registration(driver, user_data):
    register_page = RegisterPage(driver)
    register_page.open_page("https://thetestingworld.com/testings/")

    # Fill registration form
    register_page.fill_username(user_data['username'])
    register_page.fill_email(user_data['email'])
    register_page.fill_password(user_data['password'])
    register_page.fill_confirm_password(user_data['password'])
    register_page.fill_date(user_data['date'])
    register_page.fill_phone(user_data['phone'])
    register_page.fill_address(user_data['address'])
    register_page.select_address_type()
    register_page.select_gender()
    register_page.accept_terms()
    register_page.submit_form()

    if "invalid_email" in user_data['email']:
        error_message = register_page.get_error_message()
        assert "Invalid email" in error_message
