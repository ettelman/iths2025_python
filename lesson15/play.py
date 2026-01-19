from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", headless=True)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://ettelman.github.io")
    print(page.title())
    html = page.content()
    print(html)
    text = page.text_cotent("h1")
    href = page.get_attribute("a", "href")
    browser.close()

