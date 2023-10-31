#!/bin/bash

ACCESS_TOKEN="token here"

curl 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=PAR&maxPrice=200' \
    -H 'Authorization: Bearer $ACCESS_TOKEN'

curl -X POST -H "Authorization: Bearer $ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    https://test.api.amadeus.com/v1/shopping/availability/flight-availabilities \
    -d '{
    "originDestinations": [
        {
            "id": "1",
            "originLocationCode": "ICN",
            "destinationLocationCode": "GUM",
            "departureDateTime": {
                "date": "2023-11-01"
            }
        }
    ],
    "travelers": [
        {
            "id": "1",
            "travelerType": "ADULT"
        }
    ],
    "sources": [
        "GDS"
    ]
}'
