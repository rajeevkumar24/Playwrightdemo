
from msilib.schema import LaunchCondition
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True,snapshots=True,sources=True)
        page =  context.new_page()
        
        page.goto("https://playwright.dev/python/docs/intro")
        print(page.title())
        

        plugin_text = page.query_selector('//a[text()="Pytest plugin"]')
        plugin_text.click()
        print(page.url)
        context.tracing.stop(path = "trace.zip")
        context.close()
        context1 = browser.new_context()
       
        page1 =  context1.new_page()
        
        page1.goto("https://playwright.dev/python/docs/intro")
        print(page1.title())
        

        plugin_text1 = page.query_selector('//a[text()="Pytest plugin"]')
        plugin_text1.click()
        print(page.url)
        
        context.close()
        context1.close()

        browser.close()









if __name__ =='__main__':
    main()


