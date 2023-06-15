import requests


class FlightData:
    def __init__(self):
        self.flight_search_end_point = "https://api.tequila.kiwi.com/v2/search"
        self.code_search_end_point = "https://api.tequila.kiwi.com/locations/query"
        self.AffilID = "YOUR AFFILIATED ID"
        self.API_key = "YOUR API KEY"
        self.departure_city = 'London'
        self.header = {
            "apikey": self.API_key
        }
        self.flight_stop = 0

    def departure_code(self):
        code_parameters = {
            'term': self.departure_city,
            'locale': 'en-US',
            'location_types': 'airport',
            'limit': "10",
            'active_only': "true",
        }
        search_code = requests.get(url=self.code_search_end_point, params=code_parameters, headers=self.header)
        search_code_data = search_code.json()['locations']
        code = search_code_data[0]["code"]
        return code

    def get_code(self,value):
        code_parameters = {
            'term': value['city'],
            'locale': 'en-US',
            'location_types': 'airport',
            'limit': "10",
            'active_only': "true",
        }
        search_code = requests.get(url=self.code_search_end_point, params=code_parameters, headers=self.header)
        search_code_data = search_code.json()['locations']
        code = search_code_data[0]["code"]
        return code

    def check_rate(self,price,from_date,to_date,stop=0):
        departure_code = self.departure_code()
        parameters = {
            "fly_from": departure_code,
            "fly_to": price['iataCode'],
            "dateFrom": from_date,
            "dateTo": to_date,
            "max_stopovers": stop,
        }
        search_flight = requests.get(url=self.flight_search_end_point,params=parameters,headers=self.header)
        search_flight_data = search_flight.json()['data']
        price_collection = []
        dates = []
        for flights in search_flight_data:
            price_collection.append(flights['price'])
            if min(price_collection) == flights['price']:
                dates.append(flights['local_departure'].split("T")[0])
        try:
            return min(price_collection), sorted(dates)
        except ValueError:
            self.check_rate(price, from_date, to_date, stop=1)
            self.flight_stop += 1

