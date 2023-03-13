import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import math
from decimal import Decimal, ROUND_UP
from datetime import datetime

urls = []

class scrape():
    def getProducts(siteSelect):
        if siteSelect == 1: # WORKS
            print("Habico")
            productCSS = ".grid-child .grid-item"
            linkCSS = "a"
        elif siteSelect == 2: # WORKS
            print("Groves")
            productCSS = ".page .card"
            linkCSS = "a"
        elif siteSelect == 3: # WORKS
            print("SewEssential")
            productCSS = ".products-grid .product-item .product-item-details"
            linkCSS = "a"
        elif siteSelect == 4:
            print("SewingStudio")
            details = int(input("""What type of item?
1 --- Item with a larger description (Sewing machines etc...)
2 --- Item with small description (Smaller items, cheaper)\n"""))
            if details == 1:
                productCSS = ".products-grid .product-item .product-item-details .product-item-name .product-item-link"
                linkCSS = "a"
                print(".single-product-complex")
            elif details == 2: # WORKS
                productCSS = ".single-product__title"
                linkCSS = "a"
                print("CSS = .single-product__title")
        elif siteSelect == 5: #works
            print("jShop")
            productCSS = ".thumbnail a"
        elif siteSelect == 6:
            print("Craftlines")
            productCSS = ".product .wrap"
            linkCSS = ".product .h4"
        elif siteSelect == 7:
            print("SVPSewingBrands IN PROG") ### Not functional
            productCSS = ".grid-child .grid-item"
        elif siteSelect == 8:
            print("Shopify Store")
        url = input("Enter URL with products on to scrape:\n")
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            product_elements = driver.find_elements(By.CSS_SELECTOR, productCSS)
            for product_element in product_elements:
                if 'linkCSS' in locals():
                    link = product_element.find_element(By.CSS_SELECTOR, linkCSS).get_attribute("href")
                else:
                    link = product_element.get_attribute("href")
                if link != "None":
                    print(link)
                    urls.append({"Link": link})
            driver.quit()
            saveData(urls)
        except NoSuchElementException:
            print("Invalid URL. No products are being detected.")
            driver.quit()

def saveData(urls):
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    df = pd.DataFrame(urls)
    df.to_excel(f"URLS {current_time}.xlsx", index=False)
