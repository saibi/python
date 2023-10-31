import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/5829f1049069e6e7c7f335cbcb39321e/flightDeals/prices"
        self.api_token = "token"
        self.header = {
            "Authorization": f"Bearer {self.api_token}"
        }
        self.data = {}
        self.fake_mode = True

    def get_data(self):
        if self.fake_mode:
            data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {
                'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}, {'city': 'Seoul', 'iataCode': '', 'lowestPrice': 100, 'id': 11}]
            return data

        response = requests.get(url=self.endpoint, headers=self.header)
        response.raise_for_status()
        data = response.json()["prices"]

        return data

    def update_iata_value(self):
        if self.fake_mode:
            return

        for row in self.data:
            if row["iataCode"] != "":
                self.update_row(row["id"], row)

    def append_row(self, new_row):
        if self.fake_mode:
            return

        data = {"price": new_row}
        response = requests.post(
            url=self.endpoint, json=data, headers=self.header)
        response.raise_for_status()
        return response.json()["price"]["id"]

    def update_row(self, row_id, new_row):
        if self.fake_mode:
            return
        data = {"price": new_row}
        response = requests.put(
            url=f"{self.endpoint}/{row_id}", json=data, headers=self.header)
        response.raise_for_status()
        return response.json()["price"]["id"]

    def delete_row(self, row_id):
        if self.fake_mode:
            return
        response = requests.delete(
            url=f"{self.endpoint}/{row_id}", headers=self.header)
        response.raise_for_status()
        return response.status_code
