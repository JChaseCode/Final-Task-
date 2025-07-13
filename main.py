
Time = int(input("What is the current time? "))
TimeUntilAlarmStarts = int(input("How many hours should the alarm wait? "))
AlarmStarts = (AlarmStarts + TimeUntilAlarmStarts) % 24
print(f"The alarm will go off at {Time} hours.")
