import requests


class PriceSheetData():
    def __init__(self):
        self.sheet_end_point = "SHEET END POINT"
        sheet_request = requests.get(url=self.sheet_end_point)
        self.sheet_values = sheet_request.json()['prices']

    def update_code(self, code,value):
        sheet_code_end_point = f"{self.sheet_end_point}" + \
                               f"{value['id']}"
        body = {
            "price": {
                "iataCode": f"{code}"
            }
        }
        sheet_code_insert = requests.put(url=sheet_code_end_point, json=body)
        print(sheet_code_insert.text)

    def update_lowest_price(self,min_price,value):
        sheet_code_end_point = f"{self.sheet_end_point}" + \
                               f"{value['id']}"
        body = {
            "price": {
                "lowestPrice": f"{min_price}"
            }
        }
        sheet_code_insert = requests.put(url=sheet_code_end_point, json=body)
        print(sheet_code_insert.text)
