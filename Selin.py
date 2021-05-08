# Selenium
import  os
from selenium import webdriver
from time import sleep

chromedriver = "C:/Users/Prasad.keluskar/Downloads/chromedriver_win32/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


# Navigate to the application home page
driver.get("https://portal.abmgg.org/test-server/#/Login")
driver.maximize_window()

# get the search textbox
Username = driver.find_element_by_name("UserName")
Password = driver.find_element_by_name("Password")
Username.clear()
Password.clear()

# enter search keyword and submit
Username.send_keys("admin.abmgg")
Password.send_keys("Abcd123!")
Password.submit()
#driver.implicitly_wait(100)
sleep(3)
driver.find_element_by_xpath("//*[@src='assets/images/login/ADMIN.png']//..").click()


# close the browser window
#driver.quit()
