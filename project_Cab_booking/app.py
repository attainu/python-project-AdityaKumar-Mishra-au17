from SignIn import UserSignIn

def main():
    print('\t \t Cab Booking System \n \t \t =========================')
    print("Are you a Passenger or Cab Driver? \n 1. Passenger \n 2. Cab Driver")
    userType = input("Select your option:")
    
    print("1. Registered User \n 2. New User")
    regUserTyp = input("Select your Option: ")

    if(userType == '1'):
        UserSignIn.passengerSignIn(regUserTyp)
    if(userType == '2'):
        UserSignIn.driverSignIn(regUserTyp)
    
    # signIn()

if __name__ == "__main__":
    main()
