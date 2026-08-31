import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    )

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    courses_empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    courses_empty_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    courses_empty_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')

    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')
    expect(courses_empty_list_title).to_be_visible()
    expect(courses_empty_list_title).to_have_text('There is no results')
    expect(courses_empty_icon).to_be_visible()
    expect(courses_empty_text).to_be_visible()
    expect(courses_empty_text).to_have_text(
        'Results from the load test pipeline will be displayed here'
    )
