import pytest
from pom.bandcamp_elements import Bandcamp
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.basic
def test_navigate_to_page_by_search(basic_set_up, accept_cookies) -> None:
    #load page
    page = basic_set_up
    expect(page.get_by_role("button", name="Accept all")).to_be_visible()

    #accept cookies
    accept = accept_cookies
    expect(page.get_by_role("searchbox", name="Search for artist, album or")).to_be_visible(timeout=5000)

    #search for Boneash
    page.get_by_role("searchbox", name="Search for artist, album or").fill(Bandcamp.boneash_query, timeout=5000)
    expect(page.get_by_role("link", name="BONEASH Artist")).to_be_visible()

    #open Boneash from search results
    page.get_by_role("link", name="BONEASH Artist").click(timeout=50000)
    expect(page.locator("#band-name-location").get_by_text("BONEASH")).to_be_visible()

    assert page.locator("#band-name-location").get_by_text("BONEASH").is_visible()

@pytest.mark.basic
def test_navigate_by_direct_link(direct_set_up, accept_cookies) -> None:
    page = direct_set_up
    assert page.locator("#band-name-location").get_by_text("BONEASH").is_visible()