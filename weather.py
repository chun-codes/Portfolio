from tkinter import *
import requests
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

API_KEY = "YourAPIKey" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_city():
    while True:
        city = textfield.get()
        if city.lower()=="exit":
            break
        return city

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise ValueError("City Not Found :(")
    return data

def display_data(data):
    city = data["name"]
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    t.config(text=f"{temp}°C")
    c.config(text=f"{city}")
    w.config(text=f"{wind}m/s")
    h.config(text=f"{humidity}%")
    d.config(text=description)
    p.config(text=f"{pressure} hPa")
    
def main():
    display_data(get_weather(get_city()))


root=Tk()
root.title("Weather App")
root.geometry("3000x4000")
root.resizable(False,False)
root.configure(bg="#8DC9D8")

box=PhotoImage(file="box.png")
boxs=Label(image=box,bg="#76BED0",width=1100)
boxs.pack(padx=8,pady=8)

Search_image=PhotoImage(file="search.png")
Search_image = Search_image.zoom(2, 2)  
myimage=Label(image=Search_image,bg="#85C5D6",borderwidth=0)
myimage.place(x=60,y=60)

textfield=tk.Entry(root,justify="center",width=20,font=("Arial Rounded MT Bold",10,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=120,y=100)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=main)
myimage_icon.place(x=870,y=109)

#logo
canvas = Canvas(root, width=700, height=700, bg="#8DC9D8", highlightthickness=0)
canvas.place(x=180, y=500)

canvas.create_oval(20, 20, 700, 700, fill="#48A8C1")

logo=PhotoImage(file="python.png")
logos=Label(image=logo,bg="#48A8C1")
logos.place(x=345,y=665)

box=PhotoImage(file="box.png")
box=box.zoom(2,2)
boxs=Label(image=box,bg="#76BED0",width=1100)
boxs.place(x=10,y=1300)


label1 = Label(root, text="WIND:", font=("Helvetica", 10, 'bold'), fg="white", bg="#76BED0")
label1.place(x=25, y=1400)

label2 = Label(root, text="HUMIDITY:", font=("Helvetica", 10, 'bold'), fg="white", bg="#76BED0")
label2.place(x=25, y=1600)

label3 = Label(root, text="DESCRIPTION:", font=("Helvetica", 10, 'bold'), fg="white", bg="#76BED0")
label3.place(x=25, y=1800)

label4 = Label(root, text="PRESSURE:", font=("Helvetica",10, 'bold'), fg="white", bg="#76BED0")
label4.place(x=25, y=2000)

t = Label(font=("arial", 30, "bold"), fg="white", bg= "#76BED0")
t.place(x=250, y=250)

c = Label(font=("arial", 15, "bold"), bg="#35879C")
c.place(x=540, y=1100,anchor="center")

w = Label(text="...", font=("arial", 9, "bold"), bg="#76BED0")
w.place(x=400, y=1400)

h = Label(text="...", font=("arial", 9, "bold"), bg="#76BED0")
h.place(x=400, y=1600)

d = Label(text="...", font=("arial", 9, "bold"), bg="#76BED0")
d.place(x=600, y=1800) 

p = Label(text="...", font=("arial", 9, "bold"), bg="#76BED0")
p.place(x=400, y=2000)


root.mainloop()