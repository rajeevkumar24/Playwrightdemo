

from time import sleep
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False,slow_mo=2)
        context = browser.new_context()

        page =  context.new_page()
        
        page.goto("https://www.orangehrm.com/")
        print(page.title())

        #single elements

        contactsales = page.locator("text=BOOK A FREE DEMO")
        contactsales.hover()

        contactsales.click()
        sleep(2)

        print(page.title())

        selectCountry = page.locator("select#Form_submitForm_Country option")
        print(selectCountry.count())
        # find elements
        print(selectCountry.all_text_contents())
       

       # plugin_text = page.query_selector('//a[text()="Pytest plugin"]')
       # plugin_text.click()

        for i in range(0,selectCountry.count()):
            ele =selectCountry.nth(i).all_text_contents()
            print(ele)
        

         
       

        browser.close()









if __name__ =='__main__':
    main()


