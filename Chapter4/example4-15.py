home_goals = int(input("count home goals : "))
print(f'home_goals >> {home_goals}')

guest_goals = int(input("count guest goals : "))
print(f'guest_goals >> {guest_goals}')

if home_goals > guest_goals :
    print("winner is Home goals ")
elif home_goals < guest_goals :
    print('winner is Guest goals')
else :
    print("always")