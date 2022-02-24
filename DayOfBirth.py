Year = input('Input Year Of Birth: ')
Month = int(input('Input Month Of Birth (Number): '))
Day = int(input('Input Day Of Birth: '))
Century = Year[:2] + Year[4:]
Year = Year[:0] + Year[2:]
if Month > 2:
    Month -= 2
else:
    Month += 10

Week = (Day+(2.6*Month-0.2)-2*Century+Year+(Year/4)+(Century/4))%7

print(Week)
