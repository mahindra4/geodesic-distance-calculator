from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim 
from geopy.distance import geodesic
window = Tk()
window.geometry('700x270')
window.title('distance calculator')
distance_label = None
prev_distance_label = None
def cal():
    global distance_label,prev_distance_label
    # Label(master = window,text = 'mahindra',font = 'helbvatica').place(x = 207,y = 175)
    geolocator = Nominatim(user_agent = 'ichigo')
    address1 = entry1.get()
    address2 = entry2.get()

    location1 = geolocator.geocode(address1)
    location2 = geolocator.geocode(address2)

    if location1 is None:
        messagebox.showerror(title = 'ERROR',message = "There is something wrong with address1 specify it correctly")
        return
    if location2 is None:
        messagebox.showerror(title = 'ERROR',message = "There is something wrong with address2 specify it correctly")
        return

    coordinates1 = (location1.latitude,location1.longitude)
    coordinates2 = (location2.latitude,location2.longitude)
    
    distance = geodesic(coordinates1,coordinates2)
    distance = str(distance)
    
    if prev_distance_label is not None:
        prev_distance_label.after(0,prev_distance_label.destroy())
    
    distance_label = Label(window,text = distance,font = 'helvatica')
    prev_distance_label = distance_label
    distance_label.place(x = 207,y = 175)

Label(window,text = 'Distance between two locations caculator',font = 'helvatica',pady = 15).grid(row = 0,column = 0,columnspan = 2)
Label(window,text = 'Enter the address 1: ',font = 'helvatica',padx = 10,pady = 12).grid(row = 1,column = 0)
entry1 = Entry(window,width = 50,font = ('helvatica',12))
entry1.grid(row = 1,column = 1)
Label(window,text = 'Enter the address 2: ',font = 'helvatica',padx = 10,pady = 12).grid(row = 2,column = 0)
entry2 = Entry(window,width = 50,font = ('helvatica',12))
entry2.grid(row = 2,column = 1)
Label(window,text = 'geodesic distance: ',font = 'helvatica',pady = 15).grid(row = 3,column = 0)
button = Button(window,text = 'caculate',font = 'helvatica',padx = 7,bg = '#c9c7c3',activebackground='#c9c7c3',command = cal)
# button.grid(row = 4,column = 0)
button.place(x = 270, y = 215)
window.mainloop()