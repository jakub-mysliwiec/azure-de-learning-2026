# Clean readable code vs one line perl approach

print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What was your dog's name?\n")
print(f"Your band name could be : {city} {pet}")

# Below lines maybe look smarter but needed more debug :)

print(f"It is Band Name Generator project!")
print( city := input("Enter City Name: "))
print(pet_name := input("Enter Pet Name: "))
print(f"Band name is: {city} {pet_name}")
