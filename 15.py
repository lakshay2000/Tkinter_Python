#Building a weather app
# We will connect to the API with tkinter 
from tkinter import *
import requests
import json

root=Tk()

root.geometry("600x100")

def messages(categor):
    if categor== 'Good':
        weather_color="#0C0"
    elif categor=='Moderate':
        weather_color="#FFFF00"
    elif categor=='Unhealthy for Sensitive Groups':
        weather_color="#FF9900"
    elif categor=='Unhealthy':
        weather_color="#FF0000"
    elif categor=='Very Unhealthy':
        weather_color="#990066"
    else:
        weather_color="#660000"
    return weather_color

#Airnow API - https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=988009DA-FF7A-41EE-A559-A7E3C22DC51C

def change():
    api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get()+ "&distance=5&API_KEY=988009DA-FF7A-41EE-A559-A7E3C22DC51C")
    api=json.loads(api_request.content)
    city= api[0]['ReportingArea']
    quality = api[0]['AQI']
    category= api[0]['Category']['Name']

    # if category== 'Good':
    #     weather_color="#0C0"
    # elif category=='Moderate':
    #     weather_color="#FFFF00"
    # elif category=='Unhealthy for Sensitive Groups':
    #     weather_color="#FF9900"
    # elif category=='Unhealthy':
    #     weather_color="#FF0000"
    # elif category=='Very Unhealthy':
    #     weather_color="#990066"
    # else:
    #     weather_color="#660000"
    

    myLabel.config(text=city + " Air Quality " + str(quality) + " " + category,font=('Helvectica',20),background=messages(category))
    
    root.configure(background=messages(category))

    


#Creating ziploookup function
def ziploookup():
    # zip.get()
    # zipLabel=Label(root,text=zip.get())
    # zipLabel.grid(row= 1 , column= 0,columnspan=2)
    zip_btn.destroy()
    try:
        global api_request
        global api
        global city
        global quality
        global category
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get()+ "&distance=5&API_KEY=988009DA-FF7A-41EE-A559-A7E3C22DC51C")
        api=json.loads(api_request.content)
        city= api[0]['ReportingArea']
        quality = api[0]['AQI']
        category= api[0]['Category']['Name']

        # if category== 'Good':
        #     weather_color="#0C0"
        # elif category=='Moderate':
        #     weather_color="#FFFF00"
        # elif category=='Unhealthy for Sensitive Groups':
        #     weather_color="#FF9900"
        # elif category=='Unhealthy':
        #     weather_color="#FF0000"
        # elif category=='Very Unhealthy':
        #     weather_color="#990066"
        # else:
        #     weather_color="#660000"

        

        global myLabel
        
        root.configure(background=messages(category))
        myLabel=Label(root,text=city + " Air Quality " + str(quality) + " " + category,font=('Helvectica',20),background=messages(category))
        myLabel.grid(row= 2 , column= 0,columnspan=2)
        # myLabel.destroy()

        change_zip=Button(root,text="Change Zip-code",command=change)
        change_zip.grid(row=3,column=0)

    except Exception as e:
        api="Error"


zip = Entry(root)
zip.grid(row= 0 , column= 0,sticky=W+E+N+S)
zip_btn=Button(root,text="Lookup Zipcode",command=ziploookup)
zip_btn.grid(row= 0 , column= 1,sticky=W+E+N+S)

root.mainloop()

# 90210
# 83814
# 99201
# 98944