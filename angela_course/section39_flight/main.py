# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from iata import IataSearch

data_manager = DataManager()

sheet_data = data_manager.get_data()
print(sheet_data)

flight_search = FlightSearch()

iata_search = IataSearch()

# response = iata_search.search("Paris")
# print(response.text)


# update sheet with iata code
# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#         data_manager.update_row(row["id"], row)
