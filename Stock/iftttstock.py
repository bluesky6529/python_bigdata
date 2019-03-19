import twstock
import time
import requests

counterLine = 0
counterError = 0

print('開始執行')
while True:
    realdata = twstock.realtime.get('2317')
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']
        if float(realprice) >= 70:
            print('鴻海目前股價:'+realprice)
            counterLine = counterLine+1
            url_ifttt ='https://maker.ifttt.com/trigger/stockLINE/with/key/v3DxbkYGIo8JhSrdMo9CS?value1=' + realprice
            resl = requests.get(url_ifttt)
            print('第'+str(counterLine)+'次發送LINE回傳訊息:'+resl.text)
        if counterLine >= 3:
            print('程式結束')
            break
        for i in range(300):
            time.sleep(300)
    else:
        print('twstock讀取錯誤，錯誤原因:'+realdata['rtmessage'])
        counterError = counterError+1
        if counterError >= 3:
            print('程式結束')
            break
        for i in range(300):
            time.sleep(300)
