import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()
action_obj = ActionChains(driver)

##################################################################################
# move_to_element

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
#
# element = driver.find_element("xpath", '(//a[contains(text(), "Computers")])[1]')
#
#
# action_obj.move_to_element(element).perform()

##################################################################################
# double_click, context_click

# path = r"C:\Users\Vidyashree M C\python_class\html_files\actions.html"
# driver.get(path)
# driver.maximize_window()
#
# first_text_field = driver.find_element("id", "clickField")
# second_text_field = driver.find_element("id", "doubleClickField")
#
# action_obj.click(first_text_field).perform()
# time.sleep(1)
# action_obj.click(second_text_field).perform()
# time.sleep(1)
#
# action_obj.double_click(first_text_field).perform()
# time.sleep(1)
# action_obj.double_click(second_text_field).perform()
# time.sleep(1)
#
# action_obj.context_click(first_text_field).perform()
# time.sleep(1)
# action_obj.context_click(second_text_field).perform()

# #####################################################################################
# # drag and drop
#
# driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
# driver.maximize_window()
#
# source = driver.find_element("id", "draggable")
# target = driver.find_element("class name", "ui-widget-header.ui-droppable")
#
# action_obj.drag_and_drop(source, target).perform()

###########################################################################################
# keyboard simulations

time.sleep(1)
action_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
action_obj.send_keys(Keys.PAGE_UP).perform()

# ctrl + A
action_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()










