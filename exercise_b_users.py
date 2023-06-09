users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt")
twitter_handle = users["Jonathan"]["twitter"]
print(twitter_handle)
# 2. Get Erik's hometown
erik_hometown= users["Erik"]["home_town"]
print(erik_hometown)
# 3. Get the list of Erik's lottery numbers
Erik_lottery_numbers = users["Erik"]["lottery_numbers"]
print(Erik_lottery_numbers)
# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
# or users["Avril"]["pets"][0]["species"]
print(avril_pet_species)
# 5. Get the smallest of Erik's lottery numbers
smallest_number = min(Erik_lottery_numbers)
print(smallest_number)
# 6. Return an list of Avril's lottery numbers that are even
Avril_lottery_numbers = users["Avril"]["lottery_numbers"]
even_numbers = [num for num in Avril_lottery_numbers if num % 2 == 0]
print(even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
Erik_lottery_numbers.append(7)
print(Erik_lottery_numbers)
# 8. Change Erik's hometown to Edinburgh
Erik = users
Erik["home_town"] = "Edinburgh"
print(Erik["home_town"])
# 9. Add a pet dog to Erik called "fluffy"

# 10. Add another person to the users dictionary
users["Andrew"] = {
    "twitter": "twitter name",
    "lottery_numbers": [11,21,28,36,48],
    "home_town": "Edinburgh",
    "pets": [
      {
        "name": "Disel",
        "species": "dog"
      }
    ]
}
