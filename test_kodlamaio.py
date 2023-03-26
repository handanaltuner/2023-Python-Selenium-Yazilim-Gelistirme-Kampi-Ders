from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium webdriver.common.action_chains import ActionChains



class Test_Kodlamaio:
    def test_invalid_login(self):   
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # driver.get("https://www.kodlama.io/")
        sleep(5)
        #


        # loginBtn = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div/ul/li[3]/a")
        sleep(100)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(20)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(100)
        errorMessage=driver.find_element(By.XPATH,"//*                     ")
        testResult = errorMessage.text == "HATALO GİRİŞ"
        print(f("TEST SONUCU: {testResult}"))

testClass = Test_Kodlamaio()
testClass.test_invalid_login()
while True:
    print("")



#Action Chains
actions = ActionChains(self.Driver)
actions.send_keys_to_element(usernameInput,"standard_user")
actions.send_keys_to_element(passwordInput,"secret_sauce")
actions.perform()
#usernameInput,"standard_user"
#passwordInput,"secret_sauce"
loginBtn = self.driver.find_element(By.ID,"login-button")
loginBtn.click()





