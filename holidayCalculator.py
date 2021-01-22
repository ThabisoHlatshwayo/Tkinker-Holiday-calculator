#Imports
import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk,Image
from hotelPrices.provincialPrices import *
from hotelPrices.internationaPrices import *
from travellingPrices.domesticTravelling import airport
from travellingPrices.internationalTravelling import internationalAirport
from calculations import calculations

#Creating an instance
win = tk.Tk()
#Creating a screen resolution
win.geometry("950x650")
#Title
win.title("Thabiso's Airport Holiday Calculator")

buttons_frame = ttk.LabelFrame(win)
buttons_frame.grid(column=0, row=0)
#Travelling Dosmestic or Internation
ttk.Label(buttons_frame, text="Travelling").grid(column=0, row=0)
travel = tk.StringVar()
chooseTravel = ttk.Combobox(buttons_frame, width=25, textvariable=travel)
chooseTravel['values'] = ("", "Domestic", "International")
chooseTravel.grid(column=0, row=1)

#Province
ttk.Label(buttons_frame, text="Final Destinition").grid(column=2, row=0)
pro = tk.StringVar()
province = ttk.Combobox(buttons_frame, width=25, textvariable=pro)
province['values'] = ("", "Gauteng", "Limpopo", "Mpumalanga", "Free State", "North West",
"Northern Cape", "Kwa-Zulu Natal", "Western Cape", "Eastern Cape", "", "USA", "Brazil", "England",
"Spain", "Portugal", "France", "Germany", "Italy", "Russia", "China", "United Emerates")
province.grid(column=2, row=1)

ttk.Label(buttons_frame, text="Initial Province").grid(column=1, row=0)
initPro = tk.StringVar()
initialProvince = ttk.Combobox(buttons_frame, width=25, textvariable=initPro)
initialProvince['values'] = ("", "Gauteng", "Limpopo", "Mpumalanga", "Free State", "North West",
"Northern Cape", "Kwa-Zulu Natal", "Western Cape", "Eastern Cape", )
initialProvince.grid(column=1, row=1)

#city
ttk.Label(buttons_frame, text="City Name").grid(column=0, row=2)
city = tk.StringVar()
distCity = ttk.Combobox(buttons_frame, width=25, textvariable=city)
distCity['values'] = ("", "Johannesburg", "Pretoria", "Polokwane", "Turf Loop", "Nelspruit", 
"Bloemfantein", "Rusternburg", "Mahikeng", "Upington", "Durban", "Cape town", "East London", 
"Port Elizabeth", "", "New York", "Los Angelas", "Rio De Jenerio", "Sau Paulo", "London", 
"Manchester", "Barcelona", "Madrid", "Benfica", "Porto", "Paris", "Monaco", "Berlin", "Munich", 
"Milan", "Rome", "Moskow", "Wu hang", "Dubai")
distCity.grid(column=0, row=3)

ttk.Label(buttons_frame, text="Hotel Name").grid(column=1, row=2)
hot = tk.StringVar()
chooseHotel = ttk.Combobox(buttons_frame, width=25, textvariable=hot)
chooseHotel['values'] = ("", "Southern Sun(JHB)", "Morning Side(JHB)", "TsogoSun(JHB)", 
"La Viska Hotel(PLK)","Green Grass(PLK)", "Sunnyside(PTA)", "GovConversional(PTA)", "Menlyn(PTA)", 
"Northern Garden(TL)", "Grand Intrance(TL)","Waterfall City(NEL)", "Mbombela Hotel(NEL)", 
"Gods Window Hotel(NEL)", "Mangaung Hotel(BLM)", "Electric Hotel(BLM)",
"Klerksdorp View(MAK)", "Krugerdorp(MAK)", "Sun City(RTB)", "Lapeng Hotel(RTB)", 
"Southern Garden(UPT)","Kimberly View(UPT)", "Protea Hotel(DBN)", "Southern Sun(DBN)", 
"Beach Front(DBN)", "London View(EL)", "Sky London Blue(EL)",
"Greenpoint View(CPT)", "Table Mountain(CPT)", "South Sun(CPT)", "Lake Hotel(PTE)", 
"Port 72 Hotel(PTE)","", "China 88(WH)", "EAI 87(DB)", "New Orleans(NY)", "Brown View(NY)", 
"Casablanca Hotel(LA)", "Ostrigde Hotel(LA)", "Santos View(RDJ)", "Rio General Hotel(RDJ)", 
"22 Sky bet(SP)", "Santos View(SP)", "Chelsea City Hotel(LON)", "Tottenham Hotel(LON)", 
"Man United TLD(MAN)", "Man City TLC(MAN)", "Barcelona View(BAR)", "Espanyol Hotel(BAR)",
"Madrid View(MAD)", "Atlentico(MAD)", "Braga View(BEN)", "Porto View(POR)", 
"Paris Saint German(PAR)","Monaco View(MON", "Belin View(BER)", "Bayern 72(BER)", "Inter Milan(MIL)",
"AC Milan(MIL","Rome View(ROM)", "Moskow 72(MOS)")
chooseHotel.grid(column=1, row=3)

ttk.Label(buttons_frame, text="Type of Room").grid(column=0, row=4)
ro = tk.StringVar()
enterRooms = ttk.Combobox(buttons_frame, width=25, textvariable=ro)
enterRooms['values'] = ("", "Family Room", "Double Bed", "Twin Bed")
enterRooms.grid(column=0, row=5)

ttk.Label(buttons_frame, text="Number of Nights").grid(column=1, row=4)
night = tk.IntVar()
chooseNights = ttk.Combobox(buttons_frame, width=25, textvariable=night)
chooseNights['values'] = (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20)
chooseNights.grid(column=1, row=5)

ttk.Label(buttons_frame, text="Extra rooms").grid(column=2, row=2)
extra = tk.IntVar()
extraR = ttk.Combobox(buttons_frame, width=22, textvariable=extra)
extraR['values'] = (0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20)
extraR.grid(column=2, row=3)

ttk.Label(buttons_frame, text="People Travelling").grid(column=2, row=4)
people = tk.IntVar()
peopleTravel = ttk.Combobox(buttons_frame, width=25, textvariable=people)
peopleTravel['values'] = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
peopleTravel.grid(column=2, row=5)

def book():
    global domInt, choPro, city, hotel, rooms, nights, extraRooms, numberOfPeople, init
    domInt = str(chooseTravel.get())
    choPro = str(province.get())
    city = str(distCity.get())
    hotel = str(chooseHotel.get())
    rooms = str(enterRooms.get())
    nights = int(chooseNights.get())
    extraRooms = int(extraR.get())
    numberOfPeople = int(peopleTravel.get())
    init = str(initialProvince.get())

    if domInt == "Domestic":
        frame = ttk.LabelFrame(buttons_frame, text=str(init) + "->" + str(choPro))
        frame.grid(column=2, row=8)
        o = ttk.Label(frame, text='South African Airways' + 
        '\nYou booked: ' + str(numberOfPeople) + ' Tickets' +
        '\nTravelling from ' + str(init) + ' to ' + str(choPro) +
        '\nEach ticket costs: R' + str(airport(init, choPro, 1)) +
        '\nTotal Price: R' + str(airport(init, choPro, numberOfPeople)))
        o.grid(column=2, row=9, sticky=tk.W)
        if choPro == "Limpopo":
            if city == "Polokwane":
                if hotel == "La Viska Hotel(PLK)":
                    cost = round(LaViskaHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(LaViskaHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Green Grass(PLK)":
                    cost = round(GreenGrass(rooms,nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(GreenGrass(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Turf Loop":
                if hotel == "Northern Garden(TL)":
                    cost = round(northGarden(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(northGarden(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Grand Intrance(TL)":
                    cost = round(grandIntrance(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(grandIntrance(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Gauteng":
            if city == "Johannesburg":
                if hotel == "Southern Sun(JHB)":
                    cost = round(southernSun(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(southernSun(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Morning Side(JHB)":
                    cost = round(morningSide(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(morningSide(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "TsogoSun(JHB)":
                    cost = round(tsogoSun(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(tsogoSun(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Pretoria":
                if hotel == "Sunnyside(PTA)":
                    cost = round(sunnyside(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(sunnyside(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "GovConversional(PTA)":
                    cost = round(govConversional(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(govConversional(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Menlyn(PTA)":
                    cost = round(menlyn(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(menlyn(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Mpumalanga":
            if city == "Nelspruit":
                if hotel == "Waterfall City(NEL)":
                    cost = round(WaterfallCity(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(WaterfallCity(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Mbombela Hotel(NEL)":
                    cost = round(mbombelaHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(mbombelaHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Gods Window Hotel(NEL)":
                    cost = round(godsWindowView(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(godsWindowView(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Free State":
            if city == "Bloemfantein":
                if hotel == "Mangaung Hotel(BLM)":
                    cost = round(mangaungHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(mangaungHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Electric Hotel(BLM)":
                    cost = round(electricHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(electricHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "North West":
            if city == "Rusternburg":
                if hotel == "Sun City(RTB)":
                    cost = round(sunSity(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(sunSity(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Lapeng Hotel(RTB)":
                    cost = round(lapengHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(lapengHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Mahikeng":
                if hotel == "Klerksdorp View(MAK)":
                    cost = round(klerksdorp(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(klerksdorp(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Krugerdorp(MAK)":
                    cost = round(krugerdorp(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(krugerdorp(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Kwa-Zulu Natal":
            if city == "Durban":
                if hotel == "Protea Hotel(DBN)":
                    cost = round(proteaHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(proteaHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Southern Sun(DBN)":
                    cost = round(southernSunDBN(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(southernSunDBN(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Beach Front(DBN)":
                    cost = round(beachFront(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(beachFront(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Eastern Cape":
            if city == "East London":
                if hotel == "London View(EL)":
                    cost = round(londoView(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(londoView(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Sky London Blue(EL)":
                    cost = round(skyLondonBlue(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(skyLondonBlue(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Port Elizabeth":
                if hotel == "Lake Hotel(PTE)":
                    cost = round(lakeHotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(lakeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Port 72 Hotel(PTE)":
                    cost = round(port72Hotel(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(port72Hotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Northern Cape":
            if city == "Upington":
                if hotel == "Southern Garden(UPT)":
                    cost = round(southernGarden(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(southernGarden(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Kimberly View(UPT)":
                    cost = round(kimberlyView(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(kimberlyView(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Western Cape":
            if city == "Cape town":
                if hotel == "Greenpoint View(CPT)":
                    cost = round(greenpointView(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(greenpointView(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Table Mountain(CPT)":
                    cost = round(tableMountain(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(tableMountain(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price*: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "South Sun(CPT)":
                    cost = round(southernSunCPT(rooms, nights, extraRooms),2)
                    frame = ttk.LabelFrame(buttons_frame, text=str(hotel.upper()))
                    frame.grid(column=1, row=8)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(southernSunCPT(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
    elif domInt == "International":
        frame = ttk.LabelFrame(buttons_frame, text=str(init) + "->" + str(city))
        frame.grid(column=2, row=8)
        o = ttk.Label(frame, text='South African Airways' + 
        '\nTrip to : ' + str(choPro) +
        '\nYou booked: ' + str(numberOfPeople) + ' Tickets' +
        '\nFrom ' + str(init) + ' to ' + str(city) +
        '\nEach ticket costs: R' + str(internationalAirport(init, choPro, 1)) +
        '\nTotal Price: R' + str(internationalAirport(init, choPro, numberOfPeople)))
        o.grid(column=2, row=9, sticky=tk.W)
        if choPro == "USA":
            if city == "New York":
                if hotel == "New Orleans(NY)":
                    cost = round(newOrleansHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(newOrleansHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Brown View(NY)":
                    cost = round(brownView(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(brownView(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Los Angelas":
                if hotel == "Casablanca Hotel(LA)":
                    cost = round(casablancaHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(casablancaHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Ostrigde Hotel(LA)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Brazil":
            if city == "Rio De Jenerio":
                if hotel == "Santos View(RDJ)":
                    cost = round(santosView(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Rio General Hotel(RDJ)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Sau Paulo":
                if hotel == "22 Sky bet(SP)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Santos View(SP)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "England":
            if city == "London":
                if hotel == "Chelsea City Hotel(LON)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Tottenham Hotel(LON)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Manchester":
                if hotel == "Man United TLD(MAN)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Man City TLC(MAN)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Spain":
            if city == "Barcelona":
                if hotel == "Barcelona View(BAR)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Espanyol Hotel(BAR)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Madrid":
                if hotel == "Madrid View(MAD)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "Atlentico(MAD)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Portugal":
            if city == "Benfica":
                if hotel == "Braga View(BEN)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Porto":
                if hotel == "Porto View(POR)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "France":
            if city == "Paris":
                if hotel == "Paris Saint German(PAR)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Monaco":
                if hotel == "Monaco View(MON":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Germany":
            if city == "Berlin":
                if hotel == "Belin View(BER)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Munich":
                if hotel == "Bayern 72(BER)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Italy":
            if city == "Milan":
                if hotel == "Inter Milan(MIL)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
                elif hotel == "AC Milan(MIL":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
            elif city == "Rome":
                if hotel == "Rome View(ROM)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "Russia":
            if city == "Moskow":
                if hotel == "Moskow 72(MOS)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "China":
            if city == "Wu hang":
                if hotel == "China 88(WH)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)
        elif choPro == "United Emerates":
            if city == "Dubai":
                if hotel == "EAI 87(DB)":
                    cost = round(ostrigdeHotel(rooms, nights, extraRooms),2)
                    x = ttk.Label(frame, text='Booking at: '+ str(hotel) + 
                    '\nNight per room: R' + str(ostrigdeHotel(rooms,1,0)) + 
                    '\nNumber of People: ' + str(numberOfPeople) +
                    '\nNumber of rooms: ' + str(extraRooms) +
                    '\nNumber of Nights: ' + str(nights) + 
                    '\nType of Room: ' + str(rooms) +
                    '\nTotal Price: R' + str(cost))
                    x.grid(column=1, row=9, sticky=tk.W)

action = ttk.Button(buttons_frame, text='Book', command=lambda:[book()])
action.grid(column=1, row=9)

win.mainloop()