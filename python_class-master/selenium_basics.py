from selenium import webdriver

opts = webdriver.ChromeOptions()

# to disable browser notifications/pop ups
opts.add_argument("--disable-notifications")

# to restrict the browser from closing automatically
opts.add_experimental_option("detach", True)

# attaching driver with extra options
driver = webdriver.Chrome(options=opts)


"""
NoSuchElementException
1. check locator expression
2. synchronization - implicit/exlicit
3. new window - 
	handles = driver.window_handles
	driver.switch_to(handle[1])
4. iframe
	frame_source = index/name_attr/id_attr/web_element
	element = driver.find_element("xpath", '//iframe[@title="Sign in with Google Button"]')
	driver.switch_to.frame(element)
	
	driver.switch_to.frame(child_frame_source)
	driver.switch_to.default_content/parent_frame
"""
