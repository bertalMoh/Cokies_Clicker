from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#Here You need to entrer your chrome  driver path
chrome_driver_path=r"C:\Users\medyo\Desktop\Chrome_Driver\chromedriver.exe"
################################################### 
URL="http://orteil.dashnet.org/experiments/cookie/" 
driver=webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options)
driver.get(url=URL)
Cockie=driver.find_element(By.ID,"cookie")
continued=True
Elements=driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in Elements]
# Elements_text=[price.text for price in Elements]
Elements_Prices=[_.get_attribute("id") for _ in Elements]
print(Elements_Prices)
timeout=time.time()+5
five_minutes=time.time()+60*5
while continued==True :
    Cockie.click()
    # every 5 seconde
    if time.time()>timeout :
        all_items=driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_items:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID,to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_minutes:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break