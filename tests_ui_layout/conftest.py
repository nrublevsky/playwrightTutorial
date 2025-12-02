import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def basic_set_up(playwright: Playwright):
    #setup browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #setup page
    page = context.new_page()

    #open url
    page.goto("https://bandcamp.com")

    #send page out
    yield page

    #teardown after test
    page.close()

@pytest.fixture
def direct_set_up(playwright: Playwright):
    #setup browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #setup page
    page = context.new_page()

    #open url
    page.goto("https://boneash.bandcamp.com/")

    #send page out
    yield page

    #teardown after test
    page.close()


@pytest.fixture
def accept_cookies(basic_set_up) -> None:
    page = basic_set_up
    page.get_by_role("button", name="Accept all").click()