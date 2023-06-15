import requests


class UserSheetUpdate:
    def __init__(self):
        self.sheet_end_point = "https://api.sheety.co/2bea3b6e38a205af5c0eb28d21f5ad45/flightDetails/users"
        request_data = requests.get(url=self.sheet_end_point)
        self.sheet_values = request_data.json()['users']

    def update_user_data(self,first_name,last_name,email,row):
        sheet_put_end_point = f"https://api.sheety.co/2bea3b6e38a205af5c0eb28d21f5ad45/flightDetails/users/{row}"
        body = {
            'user': {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
                }
        }
        request_post = requests.put(url=sheet_put_end_point,json=body)
        print(request_post.text)
