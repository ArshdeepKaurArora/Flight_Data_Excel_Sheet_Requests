import smtplib


def send_email(from_email, password, to_email, user, value, dates, min_price):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        if len(dates) > 1:
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=f"Subject: Lowest Flight Price\n\n"
                    f"Dear {user['firstName']} {user['lastName']},\n"
                    f"Now you can travel to {value['city']}-{value['iataCode']}!."
                    f"The flight price is reduced to ${min_price} from {dates[0]} to {dates[-1]}.\n"
                    f"Enjoy your trip."
            )
        elif len(dates) == 1:
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_email,
                msg=f"Subject: Lowest Flight Price\n\n"
                    f"Dear {user['firstName']} {user['lastName']},\n"
                    f"Now you can travel to {value['city']}-{value['iataCode']}!."
                    f"The flight price is reduced to ${min_price} on {dates[0]}.\n"
                    f"Enjoy your trip."
            )

