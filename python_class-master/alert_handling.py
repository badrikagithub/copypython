"""
1. simple alert
2. confirmation alert
3. prompt alert

"""
import time

from selenium import webdriver
driver = webdriver.Chrome()

# simple alerts

driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

# driver.find_element("xpath", '//button[@class="btn btn-danger"]').click()
#
# alert_obj = driver.switch_to.alert
# print(alert_obj.text)
# # alert_obj.accept()      # clicking on ok
# alert_obj.dismiss()

# print(alert_obj.text)       # NoAlertPresentException

##################################################################################
# confirmation alert

# driver.find_element("xpath", '//a[text()="Alert with OK & Cancel "]').click()
# time.sleep(1)
# driver.find_element("xpath", '//button[@class="btn btn-primary"]').click()
#
# alert_obj = driver.switch_to.alert

# alert_obj.dismiss()
# alert_obj.accept()

################################################################################
#
# driver.find_element("xpath", '//a[text()="Alert with Textbox "]').click()
# time.sleep(1)
#
# driver.find_element("xpath", '//button[@class="btn btn-info"]').click()
#
# alert_obj = driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.send_keys("abc")
# time.sleep(1)
# alert_obj.accept()

####################################################################################