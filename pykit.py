import pywhatkit as kit
import time
import openpyxl as excel

lst = []
file = excel.load_workbook("./conct_msg.xlsx")
sheet = file.active
firstCol = sheet['A']
secondCol = sheet['B']
x=10
y=49
for cell in range(len(firstCol)):
    contact = str(firstCol[cell].value)
    message = str(secondCol[cell].value)
    kit.sendwhatmsg(contact,message,x,y)
    time.sleep(20)
    y+=2

