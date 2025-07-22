
Time = int(input("What is the time at the moment in hours?: "))
TimeDelay = int(input("How many hours should the alarm wait?: "))

# Calculate when the alarm will go off using modulo 24 for 24-hour format
AlarmTime = (Time + TimeDelay) % 24

print(f"The alarm will go off at {AlarmTime} hours.")
