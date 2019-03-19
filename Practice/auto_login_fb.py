from selenium import webdriver


#appea alery
url = 'https://www.facebook.com'
email = '***'
password = '***'
driver = webdriver.Chrome()

#cancel alert
url = 'https://www.facebook.com'
chrome_options =webdriver.ChromeOptions()
prefs= {"profile.default_content_setting_value.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

#driver.quit()