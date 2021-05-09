from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
#print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn') #get all forms that have get-input and everything that it's a button(btn)
print(user_button2)
user_message.clear()
user_message.send_keys('I am ok')

show_message_button.click()

output_text = chrome_browser.find_element_by_id('display')
assert 'I am ok' in output_text.text

chrome_browser.close()
chrome_browser.close()