import requests
import json


#This program is based on the ThingSpeak API


def writeData():    #To upload data to ThingSpeak using inputs
    
    temp = round(float(input("\nEnter current Temperature in Kelvin\n")), 2)
    hum = round(float(input("\nEnter current Humidity in percentage\n")), 2)
    light = round(float(input("\nEnter the current Light Level in lux\n")), 2)

    URL = f'https://api.thingspeak.com/update?api_key=8LP9GDBSV1E7FWZW&field1={temp}&field2={hum}&field3={light}'

    requests.request("GET", URL)

    return "Done"

def readData():    #To retrieve data from ThingSpeak
    
    choice = int(input("\nEnter - \n1 to view all Temperature readings \n2 to view all Humidity readings \n3 to view all Light Level readings \n4 to view all readings\n"))    #To get what type of data the user wants to view
    
    if choice == 4:    #To view all the values
        Flag = True    #While loop flag
        
        while Flag:
            intChoice = input("\nEnter - \n'all' to retrieve all the data entries \nor the number of entries to retrieve\n")
            
            if intChoice == "all":
                URL = 'https://api.thingspeak.com/channels/1560819/feeds.json?api_key=L7PGHY5F9UO1Y7B5'
                break

            elif intChoice.isdigit():
                URL = f'https://api.thingspeak.com/channels/1560819/feeds.json?api_key=L7PGHY5F9UO1Y7B5&results={intChoice}'
                break

            else:
                print("\nInvalid input, please try again.\n")
        
        data = requests.request("GET", URL)    #Retrieves data using HTTP GET in JSON format
        json_data = json.loads(data.text)      #Converts JSON format to a Python library
        print(json_data)
        feeds = json_data['feeds']             #To assign the 'feeds' container to the feeds variable
        '''
        print("\n|  ENTRY NO.  | TEMPERATURE (K) |  HUMIDITY (%) | LIGHT LEVEL (lx) |")
        for i in feeds:
            e_id = i['entry_id']
            t = i['field1']
            h = i['field2']
            l = i['field2']
            print("|", str(e_id), " "*(10-len(str(e_id))), "|", str(t), " "*(14-len(str(t))), "|", str(h), " "*(12-len(str(h))), "|", str(l), " "*(15-len(str(l))), "|")'''
        
    else:              #To view any particular value
        Flag = True    #While loop flag
        
        while Flag:
            intChoice = input("\nEnter - \n'all' to retrieve all the data entries \nor the number of entries to retrieve\n")
            
            if intChoice == "all":
                URL = 'https://api.thingspeak.com/channels/1560819/feeds.json?api_key=L7PGHY5F9UO1Y7B5'
                break

            elif intChoice.isdigit():
                URL = f'https://api.thingspeak.com/channels/1560819/feeds.json?api_key=L7PGHY5F9UO1Y7B5&results={intChoice}'
                break

            else:
                print("\nInvalid input, please try again.\n")

        data = requests.request("GET", URL)    #Retrieves data using HTTP GET in JSON format
        json_data = json.loads(data.text)      #Converts JSON format to a Python library
        feeds = json_data['feeds']             #To assign the 'feeds' container to the feeds variable
        
        print("\n|  ENTRY NO.  | DATA (K/%/lx) |")
        for i in feeds:
            e_id = i['entry_id']
            f_data = i[f'field{choice}']
            print("|", str(e_id), " "*(10-len(str(e_id))), "|", str(f_data), " "*(12-len(str(f_data))), "|")

    return "Done"


#Main loop
if __name__ == '__main__':
    
    Flag = True
    while Flag:
        choice = input("\nEnter - \n1 to send data to ThingSpeak \n2 to get data from ThingSpeak\n")
        if choice == "1":
            writeData()

        elif choice == "2":
            readData()
        
        else:
            print("\nInvalid input, please try again.\n")
            continue

        choiceFinal = input("\nWould you want to carry out another action? Y/N\n").upper()
        if choiceFinal == "Y":
            continue

        else:
            print("\nThank you for using our program.\n")
            break
