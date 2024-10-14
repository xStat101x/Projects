def describe_pet(animal_type='dog', pet_name=''):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('cat', 'oli') #order matters - put it in the wrong order and it doesn't make sense.
describe_pet(pet_name='moses', animal_type='cat') #order doesn't matter
describe_pet(pet_name='snuggles')