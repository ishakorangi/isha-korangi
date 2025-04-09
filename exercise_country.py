countries = [
    
biggest_country = countries[0]
for country in countries:
    print(f"name: {country["name"]} - population: {country["population"]}")
    if country ["population"] > biggest_country ["population"]:
        biggest_country = country

print(f"the biggest country is {biggest_country ["name"]} with a population of {biggest_country["population"]:,}")
