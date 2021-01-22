from hotelPrices.provincialPrices import *
from hotelPrices.internationaPrices import *
from travellingPrices.domesticTravelling import airport
from travellingPrices.internationalTravelling import *

def calculations(travelAround, finalpro, hotelChosen, typeOfRoom, numberOfNights, numberOfRooms, initialPro, number):
    if travelAround == "Domestic":
        if finalpro == "Limpopo":
            if hotelChosen == "La Viska Hotel(PLK)":
                netCalculations = round(LaViskaHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Green Grass(PLK)":
                netCalculations = round(GreenGrass(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Northern Garden(TL)":
                netCalculations = round(northGarden(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Grand Intrance(PL)":
                netCalculations = round(grandIntrance(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            
            return netCalculations

        elif finalpro == "Gauteng":
            if hotelChosen == "Southern Sun(JHB)":
                netCalculations = round(southernSun(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Morning Side(JHB":
                netCalculations = round(morningSide(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "TsogoSun(JHB)":
                netCalculations = round(tsogoSun(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Sunnyside(PTA)":
                netCalculations = round(sunnyside(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "GovConversional(PTA)":
                netCalculations = round(govConversional(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Menlyn(PTA)":
                netCalculations = round(sunnyside(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

        elif finalpro == "Mpumalanga":
            if hotelChosen == "Waterfall City(NEL)":
                netCalculations = round(WaterfallCity(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Mbombela Hotel(NEL)":
                netCalculations = round(mbombelaHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "God's Window Hotel(NEL)":
                netCalculations = round(godsWindowView(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

        elif finalpro == "Bloemfantein":
            if hotelChosen == "Mangaung Hotel(BLM)":
                netCalculations = round(mangaungHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Electric Hotel(BLM)":
                netCalculations = round(electricHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

        elif finalpro == "North West":
            if hotelChosen == "Sun City(RTB)":
                netCalculations = round(sunSity(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Lapeng Hotel(RTB)":
                netCalculations = round(lapengHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Klerksdorp View(MAK)":
                netCalculations = round(klerksdorp(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Krugerdorp(MAK)":
                netCalculations = round(krugerdorp(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

        elif finalpro == "Kwa-Zulu Natal":
            if hotelChosen == "Protea Hotel(DBN)":
                netCalculations = round(proteaHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Southern Sun(DBN)":
                netCalculations = round(southernSunDBN(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Beach Front(DBN)":
                netCalculations = round(beachFront(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

        elif finalpro == "Northern Cape":
            if hotelChosen == "Southern Garden(UPT)":
                netCalculations = round(southernGarden(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            elif hotelChosen == "Kimberly View(UPT)":
                netCalculations = round(kimberlyView(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

            return netCalculations

    elif finalpro == "Western Cape":
        if hotelChosen == "Greenpoint View(CPT)":
            netCalculations = round(greenpointView(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
        elif hotelChosen == "Table Mountain(CPT)":
            netCalculations = round(tableMountain(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
        elif hotelChosen == "South Sun(CPT)":
            netCalculations = round(southernSunCPT(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)

        return netCalculations

    elif finalpro == "Eastern Cape":
        if hotelChosen == "London View(EL)":
            netCalculations = round(londoView(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
        elif hotelChosen == "Sky London Blue(EL)":
            netCalculations = round(skyLondonBlue(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
        elif hotelChosen == "Lake Hotel(PTE)":
            netCalculations = round(lakeHotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
        elif hotelChosen == "Port 72 Hotel(PTE)":
            netCalculations = round(port72Hotel(typeOfRoom, numberOfNights, numberOfRooms) + airport(initialPro, finalpro, number),2)
            
        return netCalculations    


