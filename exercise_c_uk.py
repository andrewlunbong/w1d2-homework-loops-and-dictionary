united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea" `to`"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom)
# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append({
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
})

print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.
all_the_countries = ["Scotland", "Wales", "England", "northern_ireland"]
for x in all_the_countries:
    print(x)
# 4. Use a loop to find the total population of the UK.
united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# Adding Northern Ireland to the united_kingdom list
northern_ireland = {
  "name": "Northern Ireland",
  "population": 1811000,
  "capital": "Belfast"
}
total_population = 0
for country in united_kingdom:
    total_population += country["population"]
print("total_population") 

