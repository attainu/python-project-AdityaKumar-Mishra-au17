# import Validate
# import Register
# from .Validate import driverValidate
# from .Validate import PassengerValidate
# from .Register import registerDriver
# from .Register import registerPassenger
from .Validate import *
from .Register import *

def passengerSignIn(regUserTyp):
    # print("Inside PasserSign in")
    ''' passenger Login
    '''
    if(regUserTyp == '1'):
        print('Enter the credential:')
        username = input('Username:')
        password = input('Password:')
        testPrint = [username,password]
        print(testPrint)
        PassengerValidate(username,password)
    elif(regUserTyp == '2'):
        print('Enter your Details:')
        name = input('Full Name:')
        phone = input('Phone Number:')
        address = input('Address:')
        username = input('Username:')
        password = input('Password:')
        regPassenger = [name, phone, address, username, password]
        print(regPassenger)
        registerPassenger(name,phone,address,username,password)
    else:
        print('You have entered a wrong value.')

    

def driverSignIn(regUserTyp):
    ''' Driver Login
    '''
    if(regUserTyp == '1'):
        print('Enter the credential:')
        username = input('Username:')
        password = input('Password:')
        driverValidate(username,password)
    elif(regUserTyp == '2'):
        print('Enter your Details:')
        name = input('Full Name:')
        phone = input('Phone Number:')
        address = input('Address:')
        carType = input('Car Type:')
        vehicleNumber = input('vehicle Number:')
        username = input('Username:')
        password = input('Password:')
        registerDriver(name,phone,address,carType,vehicleNumber,username,password)
    else:
        print('You have entered a wrong value.')
    # print("Inside driver sign in")