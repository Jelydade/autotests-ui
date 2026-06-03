from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    
    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    login_button = page.get_by_test_id('login-page-login-button')
    wrong_email_or_password = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    expect(login_button).to_be_disabled()
    email_input.fill('user.name@gmail.com')
    expect(login_button).to_be_disabled()
    password_input.fill('password')
    expect(login_button).to_be_enabled()
    login_button.click()
    expect(wrong_email_or_password).to_be_visible()
    expect(wrong_email_or_password).to_have_text('Wrong email or password')
    page.wait_for_timeout(2000)
