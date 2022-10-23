

from time import sleep
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False,slow_mo=100)
        

        page =  browser.new_page()
        
        page.goto("https://books-pwakit.appspot.com")
        print(page.title())

       #Page -- DOM --> Shadow DOM -->elements
       
       #Page -- DOM --> iFrame -->Shadow DOM --> elements

        page.locator("book-app[apptitle='BOOKS'] #input").fill("Testing ")
        text = page.locator("book-app[apptitle='BOOKS'] .books-desc").text_content();
        print(text)
        

        browser.close()









if __name__ =='__main__':
    main()


