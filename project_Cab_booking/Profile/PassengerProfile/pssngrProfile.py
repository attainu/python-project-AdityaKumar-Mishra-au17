import xlrd

def passengerprofile(username):
    print('Welcome {}',username)
    pickpoint = ''
    print('Choose Travel location: \n')
    print('No.   Pick up     Drop \n ====   =========       ============')
    wb = xlrd.open_workbook(r"F:\Python class\project_Cab_booking\store\Location.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        print(i,sheet.cell_value(i,0), sheet.cell_value(i,1))
        # if(sheet.cell_value(i,0) == username and sheet.cell_value(i,4) == password):
        #     print('Login Successfully...')
    locNumber = int(input("Choose any one Location:"))
    for i in range(sheet.nrows):
        if(i == locNumber):
            pickpoint = sheet.cell_value(i,0)
    
    print('Choose Cab:')

    wb = xlrd.open_workbook(r"F:\Python class\project_Cab_booking\store\AvailabilityDetails.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        # print(sheet.cell_value(i,5),pickpoint)
        if(sheet.cell_value(i,5) == pickpoint and sheet.cell_value(i,6) == 'Yes'):
            print(i,sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4))
    choosedCab = int(input('Choose Cab Number:'))
    print('Booking Successful...')

    # print('Choose your Drop Destination:')
    # for i in range(sheet.nrows):
    #     pickLoc = sheet.cell_value(locNumber,0)
    #     if(sheet.cell_value(i,0) == pickLoc ):
    #         print('{}. {}',i,sheet.cell_value(i,1))
    #     # print('{}. {}',i,sheet.cell_value(i,0))
    # droplocNumber = int(input("Choose Drop Location:"))