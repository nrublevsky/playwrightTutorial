import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=240)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3001/auto/insurance?affid=test&form=8001&user_id=072581fe-2b13-47e1-929b-d160e5e525a8")
    page.get_by_placeholder("Zip Code").click()
    page.get_by_placeholder("Zip Code").press("ControlOrMeta+a")
    page.get_by_placeholder("Zip Code").fill("33193")
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="CONTINUE").click()
    page1 = page1_info.value
    page1.goto("http://localhost:3001/auto/insurance?affid=test&form=8001&user_id=072581fe-2b13-47e1-929b-d160e5e525a8")
    page.goto("http://localhost:3001/auto/lb")
    page1.get_by_role("button", name="2024").click()
    page1.get_by_role("button", name="Ford").click()
    page1.get_by_role("button", name="bronco sport").click()
    page1.get_by_role("button", name="big bend").click()
    page1.get_by_role("button", name="No").click()
    page1.get_by_role("button", name="Allstate").click()
    page1.get_by_role("button", name="Rent").click()
    page1.get_by_role("button", name="Yes").click()
    page1.get_by_role("button", name="Female").click()
    page1.get_by_role("button", name="Continue →").click()
    page1.get_by_role("button", name="No").click()
    page1.locator("#dob_month_select").select_option("07")
    page1.locator("#dob_day_select").select_option("10")
    page1.locator("#dob_year_select").select_option("1998")
    page1.get_by_role("button", name="Continue →").click()
    page1.get_by_role("button", name="Good: 650 -").click()
    page1.get_by_role("textbox", name="First Name").click()
    page1.get_by_role("textbox", name="First Name").fill("eherh")
    page1.get_by_role("textbox", name="Last Name").click()
    page1.get_by_role("textbox", name="Last Name").fill("qerhqerh")
    page1.get_by_role("button", name="Continue →").click()
    page1.wait_for_timeout(100000)
    # page1.get_by_role("button", name="No").click()
    page1.get_by_role("textbox", name="Email").click()
    page1.get_by_role("textbox", name="Email").fill("wegf@ergwer.com")
    page1.get_by_role("button", name="Continue →").click()
    page1.get_by_role("textbox", name="Street Address").click()
    page1.get_by_role("textbox", name="Street Address").fill("1 efef sese")
    page1.get_by_role("button", name="Continue →").click()
    page1.get_by_role("button", name="No").click()
    page1.get_by_role("textbox", name="Phone Number").click()
    page1.get_by_role("textbox", name="Phone Number").fill("(666) 136-6642")
    page1.get_by_role("button", name="Get Your Free Quote →").click()
    page1.locator("div").filter(has_text=re.compile(r"^Access Your Quote$")).nth(1).click()
    expect(page1.locator("div").filter(has_text=re.compile(r"^Access Your Quote$")).nth(1)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
