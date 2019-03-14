from selenium import webdriver


#appea alery
url = 'https://www.dcard.tw/login'
email = '***'
password = '***'
driver = webdriver.Chrome()

#cancel alert
url = 'https://www.dcard.tw/login'
chrome_options =webdriver.ChromeOptions()
prefs= {"profile.default_content_setting_value.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)

driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//button[@type="submit"]').click()

#driver.quit()