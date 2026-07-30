from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

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
    context.storage_state(path='storage-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='storage-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    courses_empty_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
    courses_empty_text = page.get_by_test_id('courses-list-empty-view-description-text')

    expect(courses_title).to_be_visible
    expect(courses_title).to_have_text('Courses')
    expect(courses_empty_list_title).to_be_visible
    expect(courses_empty_list_title).to_have_text('There is no results')
    expect(courses_empty_icon).to_be_visible
    expect(courses_empty_text).to_be_visible
    expect(courses_empty_text).to_have_text('Results from the load test pipeline will be displayed here')
