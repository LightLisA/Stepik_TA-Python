from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocator


class LoginPage(BasePage):
    def click_login_button(self):
        self.click_to_button(*LoginPageLocators.LOGIN_BUTTON)

    def enter_login_parameters(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys("Test_Stepik@test.com")
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys("Test_Stepik2020")

    def should_be_login_page(self):
        # print("LoginPage --- should_be_login_url")
        self.should_be_login_url()
        # print("LoginPage --- should_be_login_form")
        self.should_be_login_form()
        # print("LoginPage --- should_be_register_form")
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # print("LOGIN_PAGE --- should_be_login_url - assert")
        # print(f'LOGIN_PAGE --- self - {self},'
        #      f'url - {self.url}, '
        #      f'current_url --- {self.browser.current_url}')
        assert "login" in self.browser.current_url, "Login URL is not presented"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # print("LOGIN_PAGE --- should_be_login_form - assert")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is not presented"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # print("LOGIN_PAGE --- should_be_register_form - assert")
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login REGISTER is not presented"
        # assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*RegisterPageLocator.REGISTER_EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*RegisterPageLocator.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*RegisterPageLocator.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.click_to_button(*RegisterPageLocator.REGISTER_BUTTON)

