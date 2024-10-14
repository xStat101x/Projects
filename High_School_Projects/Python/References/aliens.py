alien_0 = {'color': 'green', 'points': 5}
alien_0 = {'color': 'yellow', 'points': 10}
alien_0 = {'color': 'red', 'points': 15}

aliens = ['alien_0', 'alien_1', 'alien_2']

for alien in aliens:
    print(alien)

#make an empty list for storing aliens
alien = []
#Make 30 green aliens.
for aliend_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Show the first 5 aliends:
for aliend in aliens[:5]:
    print(alien)
print("...")
#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

#Need to change the color if they 'level up'? (changing the first 3)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color' == 'yellow']: #What if they are already yellow.\
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
for aliend in aliens[:5]:
    print(alien)
print("The first three green aliens increased to yellow.")