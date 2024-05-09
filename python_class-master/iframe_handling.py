import time

from selenium import webdriver
driver = webdriver.Chrome()


path = r"C:\Users\Vidyashree M C\python_class\html_files\iframe.html"
driver.get(path)
driver.implicitly_wait(10)
driver.maximize_window()

# # frame references - index
# driver.switch_to.frame(0)

# # id
# driver.switch_to.frame("FR1")

# # name
# driver.switch_to.frame("frame1")

# frame webelement
frame_element = driver.find_element("id", "FR1")
driver.switch_to.frame(frame_element)

driver.find_element("id", "small-searchterms").send_keys("books")


# switching back to parent frame
# driver.switch_to.parent_frame()

driver.switch_to.default_content()

driver.find_element("link text", "Google").click()

time.sleep(2)

"""
parent
	- frame1
	- frame2
		-frame a
		- frame b
		- frame c
			- frame 1.1

"""

"""
1. login to redbus
2. capture the prices and names of the first 4 kids t-shirts from myntra
	and sort it based on the prices
	and capture original price
3. print all the prices of shares in demo.html
4. send different text to all the text fields in Multiple Elements with same 
	"name" property
5. select all the check boxes in descending order
"""
