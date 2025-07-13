
# Get current time from user
current_time = int(input("What is the current time (in hours, 0-23)? "))

# Get alarm delay from user
alarm_delay = int(input("How many hours should the alarm wait? "))

# Calculate the alarm time using modular arithmetic
# Since we're working with a 24-hour clock, we use modulo 24
alarm_time = (current_time + alarm_delay) % 24

# Output the result
print(f"The alarm will go off at {alarm_time} hours.")
