#game is the variable that decides if the game is actrive
game = True
room = "Repair Room"
RR_objects_list = ['broken_chromebook_1']
C1_objects_list = ['nothing']
C2_objects_list = ['nothing']
C3_objects_list = ['nothing']
PS_objects_list = ['New Screen', 'New Keyboard', 'New Trackpad']
#game is incomplete
NS_repaired = False
NK_repaired = False
NT_repaired = False
#inventory has items
inventory_NT = False
inventory_NK = False
inventory_NS = False
#This is the inventory
inventory_list = []
#if they make a move
move = False
#This will display a basic tutorial later... (not finished)
mannual = "Welcome to your first day on the job! Your job here today is to repair the chrome book in the Repair Room. You can do this with parts and typing things such as (next/previous room), (inventory), (look around), (diagnose broke_chromebook_1), (use 'part' on broken_chromebook_1), or you can always type (quit) to quit your job. Use these commands to fix the chromebook and complete your first day. Good luck!"
print(room.title())
print("Welcome to your first day on the job.")
print("Type (pick up manual) for a tutorial.")


#Checks if the game is completed after every move
if NS_repaired == True and NK_repaired == True and NT_repaired == True:
    print("Nice first day! Congrats on fixing that chromebook and can't wait to see you toommorow!")
    game = False
#While game is started
while game:
    #always print room at the beginning
    print("\n" + room.title())
    move = False
    action = input()
    
    if inventory_NS == True and inventory_NK == True and inventory_NT == True:
            PS_objects_list.append('nothing')
    #Everything that you can type in order to progress the game
    while move == False:
        #determine what they said
        if action == 'pick up manual' and room == 'Repair Room':
            print(mannual)
            move = True
        #What Problems are there with chromebook1
        elif action == 'diagnose broke_chromebook_1' and room == 'Repair Room':
            print("Needs New Screen, New Keyboard, and New Trackpad")
            move = True
        #look at your inventory
        elif action == 'inventory':
            for inventory in inventory_list:
                print("\n" + inventory)
            move = True
        #next three commands will fix the chromebook if you have the parts and are in the room
        elif action == 'use New Screen on broken_chromebook_1' and inventory_NS == True and room == 'Repair Room':
            print("nice job!")
            inventory_list.remove('New Screen')
            move = True
            NS_repaired = True
        elif action == 'use New Keyboard on broken_chromebook_1' and inventory_NK == True and room == 'Repair Room':
            print("nice job!")
            inventory_list.remove('New Keyboard')
            move = True
            NK_repaired = True
        elif action == 'use New Trackpad on broken_chromebook_1' and inventory_NT == True and room == 'Repair Room':
            print("nice job!")
            inventory_list.remove('New Trackpad')
            move = True
            NT_repaired = True
        #puts the part in their inventory and takes it away from the room
        elif action == 'pick up New Screen' and room == 'Part Storage':
            inventory_list.append('New Screen')
            PS_objects_list.remove('New Screen')
            inventory_NS = True
            move = True
        elif action == 'pick up New Keyboard' and room == 'Part Storage':
            inventory_list.append('New Keyboard')
            PS_objects_list.remove('New Keyboard')
            inventory_NK = True
            move = True
        elif action == 'pick up New Trackpad' and room == 'Part Storage':
            inventory_list.append('New Trackpad')
            PS_objects_list.remove('New Trackpad')
            inventory_NT = True
            move = True
        #What objects are in the room
        elif action == 'look around':
            if room == "Repair Room":
                for objects_RR in RR_objects_list:
                    print(objects_RR)
                    move = True
            elif room == "Classroom 1":
                for objects_C1 in C1_objects_list:
                    print(objects_C1)
                    move = True
            elif room == "Classroom 2":
                for objects_C2 in C2_objects_list:
                    print(objects_C2)
                    move = True
            elif room == "Classroom 3":
                for objects_C3 in C3_objects_list:
                    print(objects_C3)
                    move = True
            elif room == "Part Storage":
                for objects_PS in PS_objects_list:
                    print(objects_PS)
                    move = True
            else:
                print("error code 3")
                move = True
        #Ending the game
        elif action == 'quit':
            print("You are Fired!")
            game = False
        #Moving to next room    
        elif action == 'next room':
            if room == 'Repair Room':
                room = "Classroom 1"
                move = True
            elif room == 'Classroom 1':
                room = "Classroom 2"
                move = True
            elif room == 'Classroom 2':
                room = "Classroom 3"
                move = True
            elif room == 'Classroom 3':
                room = "Part Storage"
                move = True
            elif room == 'Part Storage':
                print("This is the end of the line!!")
                move = True
            else:
                print("Fail Code1")
                move = True
        #Moving to previous room
        elif action == 'previous room':
            if room == 'Part Storage':
                room = "Classroom 3"
                move = True
            elif room == 'Classroom 3':
                room = "Classroom 2"
                move = True
            elif room == 'Classroom 2':
                room = "Classroom 1"
                move = True
            elif room == 'Classroom 1':
                room = "Repair Room"
                move = True
            elif room == 'Repair Room':
                print("This is the end of the line!!")
                move = True
            else:
                print("Fail Code2")
                move = True
        else:
            print("Thats not a command I reconize.")
            move = True
        
