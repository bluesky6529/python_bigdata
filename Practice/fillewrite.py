content='''Hello Python
中文字測試
welcome
'''

f=open('file1.txt','w',encoding='UTF-8')
f.write(content)
f.close()