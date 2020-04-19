car ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for features in car.keys():
  print("Key: " + features + " Values: " + str( car[features]))

print("-"*20)

a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
for key, value in a_dict.items():
    print("Key: " + key + " Value: " + str(value))

print("-"*20)