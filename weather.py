from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from geopy.exc import GeocoderInsufficientPrivileges, GeocoderTimedOut, GeocoderServiceError, GeocoderQuotaExceeded

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        try:
            city = textfield.get()

        # Initialize the geolocator with a user agent
            geolocator = Nominatim(user_agent="weatherApp_v1")
        
        # Attempt to geocode the location with a timeout of 10 seconds
            location = geolocator.geocode(city, timeout=10)
        
            if location:
            # Initialize the TimezoneFinder object
                obj = TimezoneFinder()
            # Retrieve the timezone using the longitude and latitude of the location
                res = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            
                if res:
                    print(res)
                #t.config(text=res, fg="green")
                else:
                    print("Timezone not found")
                #t.config(text="Timezone not found", fg="red")
            else:
                    print("Location not found")
                #t.config(text="Location not found", fg="red")
        except GeocoderQuotaExceeded:
            print("Error: Geocoding quota exceeded.")
        # t.config(text="Quota exceeded", fg="red")
        except GeocoderInsufficientPrivileges:
            print("Error: Insufficient privileges to access geocoding service.")
        #t.config(text="Insufficient privileges", fg="red")
        except GeocoderTimedOut:
            print("Error: Geocoding request timed out.")
        #t.config(text="Request timed out", fg="red")
        except GeocoderServiceError:
            print("Error: Geocoding service error.")
        #t.config(text="Service error", fg="red")
        except Exception as e:
            print(f"Error: {e}")
        #t.config(text=f"Error: {e}", fg="red")
        home=pytz.timezone(res)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=82bc69992c4dda620a7560d5f0aaa6ad"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")
#searchbox
Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#Logo
Logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image=PhotoImage(file="Copy of box.png")
Frame_myimage=Label(image=Frame_image)
Frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#TIME
name=Label(root,font=("arial",15,'bold'))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)
#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,'bold'),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
p.place(x=670,y=430)
root.mainloop()





