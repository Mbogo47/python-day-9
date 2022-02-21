travel_log = [
    {"country": "France",
     "total_visits": 12,
     "cities_visited": ["Paris", "Lille", "Dijon"],
     },
    {"country": "Germany",
     "total_visits": 5,
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     },
]
print(travel_log)


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# add_new_country("Russia",2,["Moscow","Saint Petersburg"])

add_new_country("Russia", "2", ["Moscow", "Saint Petersburg"])
print(travel_log)
