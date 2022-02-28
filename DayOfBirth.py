Year = input('Input Year Of Birth: ')
Month = int(input('Input Month Of Birth (Number): '))
Day = int(input('Input Day Of Birth: '))
Century = Year[:2] + Year[4:]
Year = Year[:0] + Year[2:]
Year = int(Year)
Century = int(Century)
type(Year)
if Month > 2:
    Month -= 2
else:
    Month += 10

Week = (Day+(2.6*Month-0.2)-2*Century+Year+(Year/4)+(Century/4))%7

if Week >= 6:
    Week = 'Saturday'

elif Week >= 5:
    Week = 'Friday'

elif Week >= 4:
    Week = 'Thursday'

elif Week >= 3:
    Week = 'Wednesday'

elif Week >= 2:
    Week = 'Tuesday'

elif Week >= 1:
    Week = 'Monday'

else:
    Week = 'Sunday'

print(Week)
