from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", headless=True)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("http://localhost:4000")
    text = page.text_content("p")
    print(text)

    page.fill('input[name="username"]', "test")
    page.fill('input[name="password"]', "test")
    page.click("button[type=submit]")

    text = page.text_content("p")
    print(text)
    # page.wait_for_selector(".dashboard")
    # page.wait_for_load_state("networkidle")

    elements = page.query_selector_all('h3')

    for element in elements:
        print(element.text_content())

    browser.close()