import pytest
from playwright.sync_api import sync_playwright, Page, Playwright, expect

BASE_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course'
BROWSER_STATE_PATH = 'browser-state.json'


@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(f'{BASE_URL}/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

        registration_email_input.fill('username@gmail.com')
        registration_username_input.fill('username')
        registration_password_input.fill('password')
        registration_button.click()
        expect(dashboard_title).to_be_visible()
        context.storage_state(path=BROWSER_STATE_PATH)
        browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=BROWSER_STATE_PATH)
    page = context.new_page()
    yield page
    context.close()
    browser.close()
