

from time import sleep
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False,slow_mo=2)
        

        page =  browser.new_page()
        
        page.goto("http://www.londonfreelance.org/courses/frames/index.html")
        print(page.title())

        #iframe

        iframe = page.frame_locator("frame[name='main']").locator("h2").text_content()
        print(iframe)
       

        browser.close()









if __name__ =='__main__':
    main()


