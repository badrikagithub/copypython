from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element("link text", "Twitter").click()
print(driver.title)

# list of all the window ids that are currently open
handles = driver.window_handles
print(handles)                  # [parent_window(Demo web shop), child_window(twitter)]

driver.switch_to.window(handles[1])

driver.find_element("xpath", '//span[text()="Settings"]').click()

driver.close()      # closes the active window

driver.switch_to.window(handles[0])
print(driver.title)


