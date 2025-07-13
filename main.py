
Time = int(input("What is the current time? "))
TimeUntilAlarmStarts = int(input("How many hours should the alarm wait? "))
AlarmStarts = (Time + TimeUntilAlarmStarts) % 24
print(f"The alarm will go off at {AlarmStarts} hours.")
