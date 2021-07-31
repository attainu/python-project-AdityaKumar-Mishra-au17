import xlrd
import pandas as pd 

from Profile.PassengerProfile import pssngrProfile
from Profile.DriverProfile import driverProfile



def PassengerValidate(username,password):
    print(username, password)
    # df = pd.read_excel(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx', usecols =[username,password])
    # "F:\Python class\Registered Passenger.xlsx"
    wb = xlrd.open_workbook(r'F:\Python class\project_Cab_booking\store\Registered Passenger.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,3) == username and sheet.cell_value(i,4) == password):
            print('Login Successfully...')
            pssngrProfile.passengerprofile(username)
        # else:
        #     print('Incorrect Credentials')
            
    # print(df)



def driverValidate(username,password):
    # df = pd.read_excel(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx', usecols =[username,password])
    # print(df)

    wb = xlrd.open_workbook(r'F:\Python class\project_Cab_booking\store\Registered Driver.xlsx')
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,5) == username and sheet.cell_value(i,6) == password):
            print('Login Successfully...')
            driverProfile.drvrProfileFunc(username)
        else:
            print('Incorrect Credentials')

