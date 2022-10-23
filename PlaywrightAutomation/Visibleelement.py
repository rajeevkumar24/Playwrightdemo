

from time import sleep
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as playwright:
        browser =  playwright.chromium.launch(headless=False,slow_mo=2)
        

        page =  browser.new_page()
        
        page.goto("http://www.amazon.com/")
        print(page.title())

        #button:visible
        #button >> visible=true
        mylist =[]

        text = page.locator("a:visible").all_inner_texts();
        for ele in text:
            mylist.append(ele)
        
        print(mylist)

        for ele1 in text:
            print(ele1)

        
        
        imagesCount = page.locator("xpath=//img >> visible=true").count();
        print(imagesCount)
       

        browser.close()









if __name__ =='__main__':
    main()


