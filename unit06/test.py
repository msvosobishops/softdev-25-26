contacts = {
    "jswift": {
        "first_name": "Jane", 
        "last_name": "Swift",
        "address": {
            "city": "San Francisco",
            "street": "25th Street",
            "house_number": 11
        }
    },
    "pjohnson": {
        "first_name": "Patrick", 
        "last_name": "Johnson",
        "address": {
            "city": "Miami",
            "street": "5th Street",
            "house_number": 501
        }
    },
    "mmarkson": {
        "first_name": "Mark", 
        "last_name": "Markson",
        "address": {
            "city": "Anchorage",
            "street": "Main Street",
            "house_number": 1440
        }
    }
}



travelers = {
    "Maya": {
        "age": 16,
        "visited_countries": ["Mexico", "Nicaragua", "Portugal"],
        "favorite_activity": "Surfing"
    },
    "Jordan": {
        "age": 17,
        "visited_countries": ["Japan", "Italy", "Canada"],
        "favorite_activity": "Hiking"
    },
    "Alex": {
        "age": 15,
        "visited_countries": ["Thailand", "Spain", "Costa Rica"],
        "favorite_activity": "Photography"
    }
}


cities = []
for value in contacts.values():

    cities.append(value["address"]["city"])

print(cities)
