from pandas import DataFrame
import pandas as pd 
from openpyxl import load_workbook
import os


def registerPassenger(name,phone,address,username,password):
    regPassenger = [name, phone, address, username, password]
    # regPassenger = {
    #     'Name': name,
    #     'Phone': phone,
    #     'Address': address,
    #     'Username': username,
    #     'Password': password
    # }
    # df = DataFrame(regPassenger, columns = ['Name', 'Phone', 'Address', 'Username', 'Password'])
    df = DataFrame([regPassenger], columns = ['Name', 'Phone', 'Address', 'Username', 'Password'])
    # print(df)
    if(os.path.isfile(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx')):
        existingData = pd.read_excel(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx')
        allData = [existingData,df]
        appnd_df = pd.concat(allData)
        appnd_df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx',index = False, header=True)
    else:
        df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx',index = False, header=True)
    # writer.book = load_workbook(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx')
    # writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx',index = False, header=True)
    # writer.close()
    


def registerDriver(name,phone,address,carType,vehicleNumber, username,password):
    regDriver = [name, phone, address, carType, vehicleNumber, username, password]
    # regDriver ={
    #     'Name': name,
    #     'Phone': phone,
    #     'Address': address,
    #     'car Type': carType,
    #     'Vehicle Number': vehicleNumber,
    #     'Username': username,
    #     'Password': password 
    # }
    # df = DataFrame(regDriver, columns = ['Name', 'Phone', 'Address', 'Car Type', 'Vehicle Number', 'Username', 'Password' ])
    df = DataFrame([regDriver], columns = ['Name', 'Phone', 'Address', 'Car Type', 'Vehicle Number', 'Username', 'Password' ])
    if(os.path.isfile(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx')):
        existingData = pd.read_excel(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx')
        allData = [existingData,df]
        appnd_df = pd.concat(allData)
        appnd_df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx',index = False, header=True)
    else:
        df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx',index = False, header=True)
    # df.to_excel(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx',index = False, header=True)
