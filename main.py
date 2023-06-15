from flight_data import FlightData
from price_sheet_data import PriceSheetData
from user_sheet import UserSheetUpdate
from datetime import datetime
from dateutil.relativedelta import relativedelta
from send_email import send_email

# flight search from date to date
from_date = datetime.now().date()
to_date = from_date + relativedelta(months=+6)

# email the lowest flight price from email to email
from_email = 'YOUR EMAIL'
password = 'YOUR PASSWORD'

# class objects related to the project
flight = FlightData()
price_sheet = PriceSheetData()
user_sheet = UserSheetUpdate()

# To fill IATA code on the sheet
for value in price_sheet.sheet_values:
    code = flight.get_code(value)
    price_sheet.update_code(code, value)

# To get the price of flight
for value in price_sheet.sheet_values:
    price = int(value['lowestPrice'])
    min_price, dates = flight.check_rate(value, from_date, to_date)
    if int(min_price) < price:
        price_sheet.update_lowest_price(min_price,value)

# Asking user first name, last name and their email address
status = True
while status:
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    email = input('What is your email?\n')
    confirm_email = input('Please retype your email to confirm.\n')
    if email == confirm_email:
        print("Welcome to the club!")

        # getting value from txt file
        try:
            with open('value.txt','r') as file:
                row = file.read()
        except FileNotFoundError:
            row = 2
            with open('value.txt', 'w') as file:
                file.write(str(row))

        # updating the value on sheet
        user_sheet.update_user_data(first_name,last_name,email,row)
        row = int(row) + 1
        with open('value.txt','w') as file:
            file.write(str(row))
    continuity = input("More users? Reply with 'yes' or 'no'\n")
    if continuity.lower() == 'yes':
        status = True
    elif continuity.lower() == 'no':
        status = False

# for sending an email to users
for value in price_sheet.sheet_values:
    price = int(value['lowestPrice'])
    try:
        min_price, dates = flight.check_rate(value, from_date, to_date)
        print(min_price, dates)
    except TypeError:
        continue
    else:
        if flight.flight_stop > 0:
            print('more stop')
    if int(min_price) < price:
        price_sheet.update_lowest_price(min_price,value)
    else:
        for user in user_sheet.sheet_values:
            to_email = user['email']
            send_email(from_email,password,to_email,user,value,dates,min_price)
