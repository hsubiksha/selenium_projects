from selenium.webdriver.common.by import By

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def fill_username(self, username):
        self.driver.find_element(By.NAME, 'fld_username').send_keys(username)

    def fill_email(self, email):
        self.driver.find_element(By.NAME, 'fld_email').send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password)

    def fill_confirm_password(self, password):
        self.driver.find_element(By.NAME, 'fld_cpassword').send_keys(password)

    def fill_date(self, date):
        self.driver.find_element(By.ID, 'datepicker').send_keys(date)

    def fill_phone(self, phone):
        self.driver.find_element(By.NAME, 'phone').send_keys(phone)

    def fill_address(self, address):
        self.driver.find_element(By.NAME, 'address').send_keys(address)

    def select_address_type(self):
        self.driver.find_element(By.XPATH, '//input[@value="home"]').click()

    def select_gender(self):
        self.driver.find_element(By.XPATH, '//select[@name="sex"]/option[3]').click()

    def accept_terms(self):
        self.driver.find_element(By.NAME, 'terms').click()

    def submit_form(self):
        self.driver.find_element(By.XPATH, '//input[@type="submit" and @value="Sign up"]').click()

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, '//span[@id="email_error"]').text
