countries = [
    { "name": "Nepal", "population":66700},
    { "name": "India", "population":5555789},
    { "name": "Bhutan", "population":45688977},
    { "name": "France", "population":5600988},
    { "name": "USA", "population":56678800},
]
biggest_country = countries[0]
for country in countries:
    print(f"name: {country["name"]} - population: {country["population"]}")
    if country ["population"] > biggest_country ["population"]:
        biggest_country = country

print(f"the biggest country is {biggest_country ["name"]} with a population of {biggest_country["population"]:,}")
