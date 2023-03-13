import urlgrab
import urlscraper

print("""
 ██████   ██████      ███████  ██████ ██████   █████  ██████  ███████ ██████
██    ██ ██           ██      ██      ██   ██ ██   ██ ██   ██ ██      ██   ██
██    ██ ██   ███     ███████ ██      ██████  ███████ ██████  █████   ██████
██    ██ ██    ██          ██ ██      ██   ██ ██   ██ ██      ██      ██   ██
 ██████   ██████      ███████  ██████ ██   ██ ██   ██ ██      ███████ ██   ██

""")

print("""
Please select what you wish to achieve:
1 --- Scrape a set of URLS from a supported website
2 --- Get a list of URLs saved to a spreadsheet from a collection page
""")
while True:
    user_input = int(input("Please enter number: "))
    if user_input == 1:
        print("""
        Please select what website (currently supported):
        1 --- Habico
        2 --- Groves
        3 --- SewEssential
        4 --- SewingStudio
        5 --- jShop
        6 --- Craftlines
        7 --- SVPSewingBrands
        8 --- Any Shopify store
        """)
        siteSelect = int(input("Please enter number: "))
        urlscraper.scrape.getProducts(siteSelect)
        break

    elif user_input == 2:
        print("""
        Please select what website (currently supported):
        1 --- Habico
        2 --- Groves
        3 --- SewEssential
        4 --- SewingStudio
        5 --- jShop
        6 --- Craftlines
        7 --- SVPSewingBrands
        8 --- Any Shopify store
        """)
        siteSelect = int(input("Please enter number: "))
        urlgrab.scrape.getProducts(siteSelect)
        break

    else:
        print("Not a valid option.")
