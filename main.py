
# Day of the week calculator
# Day 0 = Sunday, Day 1 = Monday, ..., Day 6 = Saturday

starting_day = int(input("Enter the starting day number (0-6, where 0=Sunday, 6=Saturday): "))
stay_length = int(input("Enter the length of your stay in nights: "))

# Calculate the return day using modulo 7 for days of the week
return_day = (starting_day + stay_length) % 7

# Day names for reference
day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(f"You will return on day {return_day} ({day_names[return_day]}).")
