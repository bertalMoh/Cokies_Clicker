from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path=r"C:\Users\medyo\Desktop\Chrome_Driver\chromedriver.exe"
URL="https://en.wikipedia.org/wiki/Main_Page"
driver=webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=chrome_options)
driver.get(url=URL)
Number_of_articles=(driver.find_element(By.ID, "articlecount")).find_element(By.TAG_NAME, "a")
# print(Number_of_articles.text)
# Number_of_articles.click()
all_portals=driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()
seach=driver.find_element(By.NAME,"search")
seach.send_keys("python")
seach.send_keys(Keys.ENTER)
