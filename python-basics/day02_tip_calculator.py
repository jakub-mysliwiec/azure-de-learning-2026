print("Welcome to the tip calculator!")

# ----user inputs----

bill = float(input("What was the total bill ? $")) 
tip = float(input("How much tip would you like to give? 10, 12, or more %? "))
number_of_people = int(input("How many people to split the bill? "))

# ----calculation----

bill_manipulation = 1 + (tip / 100) # To be sure that always the correct percent is calculated e.g. 100% + 5% and 100 + 50% 
final_price = bill * bill_manipulation
price_per_person = round(final_price / number_of_people,2)

# ----output----

print(f"Each person should pay: ${price_per_person:.2f}")
