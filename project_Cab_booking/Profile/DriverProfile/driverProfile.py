import xlrd
def drvrProfileFunc(username):
    wb = xlrd.open_workbook(r"F:\Python class\project_Cab_booking\store\AvailabilityDetails.xlsx")
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0,0)
    for i in range(sheet.nrows):
        if(sheet.cell_value(i,3) == username):
            print(i,sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6))
