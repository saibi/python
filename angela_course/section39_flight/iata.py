import requests


class IataSearch:
    def __init__(self):
        self.endpoint = "https://www.iata.org/en/publications/directories/code-search"

    def search(self, city_name):
        response = requests.get(url=self.endpoint, params={
                                "airport.search": city_name})
        response.raise_for_status()
        return response
