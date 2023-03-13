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
scraped_data = []

class scrape():
    def getProducts(siteSelect):
        filename = input("Enter filename containing URLs. URLs must have column header of 'Link'")
        if siteSelect == 1: #
            print("Habico")
            username = input("Enter Habico username")
            password = input("Enter Habico password")
            habicoScrape(username, password, filename)
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

def actualScrape(filename, titleCSS, priceCSS, imageCSS):
    df = pd.read_excel(filename)
    for link in df['links']:
        driver = webdriver.Chrome()
        driver.get(link)
        try:
            title = driver.find_element(By.CSS_SELECTOR, titleCSS).text
        except NoSuchElementException:
            print("No data found for title on: ", link)
            title = "No data found"
        try:
            price = driver.find_element(By.CSS_SELECTOR, priceCSS).text
        except NoSuchElementException:
            print("No data found for price on: ", link)
            price = "No data found"
        try:
            imageLink = driver.find_element(By.CSS_SELECTOR, imageCSS).text
        except NoSuchElementException:
            print("No data found for images on: ", link)
            imageLink = "No data found"
        scraped_data.append([title, price, imageLink])
        driver.quit()
        saveData(scraped_data)

def saveData(scraped_data):
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    df = pd.DataFrame(scraped_data)
    df.to_excel(f"Scraped Product Information {current_time}.xlsx", index=False)

def habicoScrape(username, password, filename):
    driver = webdriver.Chrome()
    driver.get("https://www.habico.co.uk/sign-in")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="cookies-eu-accept"]').click()
    username_element = driver.find_element(By.ID, "username")
    password_element = driver.find_element(By.ID, "current-password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'button-text').click()
    titleCSS = "h1, .h1"
    priceCSS = ".price-module .price"
    imageCSS = ".product-media img"
    actualScrape(filename, titleCSS, priceCSS, imageCSS)

def grovesScrape(username, password, filename):
    driver = webdriver.Chrome()
    driver.get("https://www.grovesltd.co.uk/guest")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="gdpr-cookie-accept"]').click()
    username_element = driver.find_element(By.ID, "Username")
    password_element = driver.find_element(By.ID, "Password")
    username_element.send_keys(username)
    password_element.send_keys(password)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn btn-primary btn-block homepage-btn').click()
    time.sleep(1)
    titleCSS = "h4, .h4"
    priceCSS = ".product-price"
    imageCSS = "img"
    actualScrape(filename, titleCSS, priceCSS, imageCSS)
