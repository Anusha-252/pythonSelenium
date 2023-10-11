import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.daraz.com.np/")

health_beauty = driver.find_element(By.XPATH, '//span[text()="Health & Beauty"]')
beauty_tools = driver.find_element(By.XPATH, "//span[contains(text(), 'Beauty Tools')]")
cutting = driver.find_element(By.XPATH, "//span[contains(text(),'Curling Irons & Wands')]")

# Create an ActionChains object
action_chains = ActionChains(driver)
action_chains.move_to_element(health_beauty).move_to_element(beauty_tools).move_to_element(cutting).click().perform()
print(" Welcome to Product List Page")

# Choosing Product from List
# my_product = driver.find_element(By.XPATH, "//a[@data-spm-anchor-id='a2a0e.searchlistcategory.list.10']")
my_product=driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div/div")
my_product.click()

# Add to cart

addtocartBtn = driver.find_element(By.XPATH, "//*[@id='module_add_to_cart']/div/button[2]/span/span")
addtocartBtn.click()
time.sleep(10)

driver.quit()
