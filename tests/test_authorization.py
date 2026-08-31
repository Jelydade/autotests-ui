import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    login_button = chromium_page.get_by_test_id('login-page-login-button')
    wrong_email_or_password = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')

    expect(login_button).to_be_disabled()
    email_input.fill('user.name@gmail.com')
    expect(login_button).to_be_disabled()
    password_input.fill('password')
    expect(login_button).to_be_enabled()
    login_button.click()
    expect(wrong_email_or_password).to_be_visible()
    expect(wrong_email_or_password).to_have_text('Wrong email or password')
