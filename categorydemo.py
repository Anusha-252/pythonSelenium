from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://member.daraz.com.np/user/profile#/")

categoryLocate = driver.find_element(By.XPATH, "//span[@class='lzd-site-menu-nav-category-text']")
womens_fashion = driver.find_element(By.XPATH, "//*[@id='Level_1_Category_No8']/a/span[2]")
traditional_clothing = driver.find_element(By.XPATH, "//*[@id='J_8018372580']/div/ul/ul[1]/li[2]/a/span")
saree = driver.find_element(By.XPATH, "//*[@id='J_8018372580']/div/ul/ul[1]/li[2]/ul/ul/li[1]/a/span")



# Create an ActionChains object
action_chains = ActionChains(driver)
action_chains.move_to_element(categoryLocate).move_to_element(womens_fashion).move_to_element(
    traditional_clothing).move_to_element(saree).click().perform()
driver.quit()