n = 0
team = []
num = 0
star = 0

i = input('Number Of Players: ')
n = n + int(i)
for x in range(n):
    player = []
    num += 1
    p=input('Points: ')
    f=input('Fouls: ')
    sum = int(p)*5 - int(f)*3
    if sum <= 40:
        star = 0
    else:
        star = star + sum
    player.append(num)
    player.append(p)
    player.append(f)
    player.append(sum)
    team.append(player)

print(*team, sep='\n')

gold = n * 40
print(gold)
print(star)
if star > gold:
    print('Gold Team')
else:
    print('Not A Gold Team')
