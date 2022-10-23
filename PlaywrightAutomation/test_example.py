from playwright.sync_api import Page

def test_example_is_working(page:Page):
  
    page.goto("https://playwright.dev/python/docs/intro")
    print(page.title())
    plugin_text = page.query_selector('//a[text()="Pytest plugin"]')
    plugin_text.click()
    
    