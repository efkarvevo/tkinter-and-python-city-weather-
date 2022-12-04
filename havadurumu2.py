import pyautogui as p
import time
import datetime as dt
import selenium
from selenium import webdriver
from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk, Image 
import os
import urllib

today = dt.datetime.today()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
pageone=Tk()
pageone.title("Weather")
pageone.geometry("925x600")
pageone.maxsize(925,600)
pageone.minsize(925,600)
def getWeather(history,city):

    history=history.split("/")
    history=history[::-1]
    print(history)
    history='-'.join(history)
   

    tokyoLink="https://www.wunderground.com/history/daily/jp/tokyo/RJTT/date/20"
    parisLink="https://www.wunderground.com/history/daily/fr/paray-vieille-poste/LFPO/date/20"
    ankaraLink="https://www.wunderground.com/history/daily/tr/çubuk/LTAC/date/20"
    romaLink="https://www.wunderground.com/history/daily/it/ciampino/LIRA/date/20"
    if city=="Tokyo":
        url=tokyoLink+history
        img = ImageTk.PhotoImage(Image.open("tokyo.jpeg"))
        panel =Label(pageone, image = img)
        panel.place(x=325,y=0)
    if city=="Paris":
        url=parisLink+history
        img = ImageTk.PhotoImage(Image.open("paris.jpeg"))
        panel =Label(pageone, image = img)
        panel.place(x=325,y=0)
    if city=="Ankara":    
        url=ankaraLink+history
        img = ImageTk.PhotoImage(Image.open("ankara.jpeg"))
        panel =Label(pageone, image = img)
        panel.place(x=325,y=0)
    if city=="Roma":
        url=romaLink+history
        img = ImageTk.PhotoImage(Image.open("roma.jpeg"))
        panel =Label(pageone, image = img)
        panel.place(x=325,y=0)
    driver.get(url)
    time.sleep(2)
    max_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[1]/td[1]")
    min_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[2]/td[1]")
    avr_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]")
    max=max_Temperature.text
    min=min_Temperature.text
    davr=avr_Temperature.text
    max=round(((float(max)-32)/1.8),2)
    min=round(((float(min)-32)/1.8),2)
    davr=round(((float(davr)-32)/1.8),2)
    
    print(url)
    history=history.replace("-", "/")
    label=Label(pageone,text="20{} on date {} in city".format(history,city),anchor = "w",font=("Arial",13))
    label.place(x=15,y=480)
    label1=Label(pageone,text="Max tempature: {}°  ".format(max),anchor = "w",font=("Arial",13))
    label1.place(x=15,y=510)
    label2=Label(pageone,text="Min tempature: {}°   ".format(min),anchor = "w",font=("Arial",13))
    label2.place(x=15,y=540)
    label3=Label(pageone,text="Average temperature: {}°    ".format(davr),anchor = "w",font=("Arial",13))
    label3.place(x=15,y=570)
    pageone.mainloop()

#listbox create
Lb1 = Listbox(pageone,font=("Arial",18,"bold"),height=6,width=10)
Lb1.insert(1, "Tokyo")
Lb1.insert(2, "Paris")
Lb1.insert(3, "Ankara")
Lb1.insert(4, "Roma")
Lb1.place(x=0,y=0)
#listbox get the selected value

#place a picture
img = ImageTk.PhotoImage(Image.open("stock.jpeg"))
panel =Label(pageone, image = img)
panel.place(x=325,y=0)

def getData():
    try:
        urllib.request.urlopen("https://www.google.com/")
        try:
            history=cal.get_date()
            for i in Lb1.curselection():
                city=Lb1.get(i)
        
            getWeather(history,city)    
        except UnboundLocalError:
            check=p.confirm("Please select a city first",buttons=["OKEY"])
    except :
        check=p.confirm("Please check your internet connection",buttons=["OKEY"])
        
#history design
mindate=dt.datetime(2000,1,1)
cal = Calendar(pageone, selectmode = 'day',maxdate=today,mindate=mindate)
cal.place(x=15,y=210)
#buton design
print(today)
btn = Button(pageone, text='Get weather',font=("Arial",14), command=getData)
btn.place(x=0,y=410)
pageone.mainloop()
driver.close()