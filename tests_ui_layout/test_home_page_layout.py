import playwright

from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright

def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False,slowMo=500)
    context = browser.new_context()

    page = login_set_up

    assert page.is_visible(HomePage.celebrating_beauty_header)
    # Click text=playwright-practice was founded by a group of like-minded fashion devotees, dete
    assert page.is_visible(HomePage.celebrating_beauty_body)

