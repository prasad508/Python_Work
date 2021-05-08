#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from Xlib.ext.randr import select_input
from selenium.webdriver.support.select import Select
#from duplicity.asyncscheduler import thread


# create a new Chrome session
driver = webdriver.Chrome("C:/Users/Prasad.keluskar/Downloads/chromedriver_win32/chromedriver")
#driver.implicitly_wait(30)

# Navigate to the application home page
driver.get("https://portal.abmgg.org/test-server/#/Login")
#driver.maximize_window()

# get the search textbox
Username = driver.find_element_by_name("UserName")
Password = driver.find_element_by_name("Password")
Username.clear()
Password.clear()

# enter search keyword and submit
Username.send_keys("admin.abmgg")
Password.send_keys("Abcd123!")
Password.submit()
time.sleep(4)

driver.find_element_by_xpath("//*[@src='assets/images/login/ADMIN.png']//..").click()
time.sleep(4)
driver.find_element_by_xpath("//a[@href='#User_Management']//..").click()
time.sleep(4)
driver.find_element_by_xpath("//span[text()='New User Registration ']//..").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='RoleUid0']//..").click()
time.sleep(4)

element = driver.find_element_by_id('RoleUid0')
dp=Select(element)
dp.select_by_visible_text('Trainee')

print(len(dp.options))

