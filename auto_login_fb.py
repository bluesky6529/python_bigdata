from selenium import webdriver


# 出現alert視窗
url = 'https://www.facebook.com'
email = '0922307023'
password = 'mimi28947731'
driver = webdriver.Chrome()

# 取消Alert視窗
#url = 'https://www.facebook.com'
#chrome_options =webdriver.ChromeOptions()
#prefs= {"profile.default_content_setting_value.notifications":2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver=webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

#driver.quit()