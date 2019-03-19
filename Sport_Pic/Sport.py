import time
import os
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup

# 設定google chrome & 視窗最大化
driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://running.biji.co/index.php?q=album&act=photo_list&cid=6920&type=special&subtitle=2019%20SKECHERS%20LADY%E2%80%99S%20RUN-%E7%B7%A8%E8%BC%AF%E7%B2%BE%E9%81%B8'

# 開啟瀏覽器
driver.get(url)

# 隱性等待一秒
driver.implicitly_wait(1)

print("圖片下載中，請稍等..")
for i in range(1, 101):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
title = soup.select('.album-title')[0].text.strip()
all_imgs = soup.find_all('img', {"class": "photo_img photo-img"})

images_dir = title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

n = 0
for img in all_imgs:
    src = img.get('src')
    if src != None and('.jpg' in src):
        full_path = src
        filename = full_path.split('/')[-1]
        print(full_path)

        try:
            image = urlopen(full_path)
            with open(os.path.join(images_dir, filename), 'wb') as f:
                f.write(image.read())
            n += 1
            if n >= 10:
                break

        except:
            print("{} 無法讀取!".format(filename))

print("共下載", n, "張圖片")
driver.quit()
