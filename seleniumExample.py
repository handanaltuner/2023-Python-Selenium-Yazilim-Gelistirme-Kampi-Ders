from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)

# while True:   
#     continue

input = driver.find_element(By.NAME,"q")

input.send_keys()
searchButton =driver.find_element(By.NAME, "btnK")
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şuanda {len(listOfCourses)} adet kurs var.")
#sleep(10)

#1. yontem while True:
#    pass

#2.yontem
#input()

#test otomasyonu


#driver = webdriver.Chrome("")

#HTML LOCATORS