# Jared Baker


def show_instructions():
    # Print Instructions for the Player
    print("SPACESHIP DISASTER GAME")
    print('----------------------------------------------------------------')
    print("Your spaceship was hit by debris and has split in half! You can see the escape\n"
          "pod drifting away, but you need supplies in order to fly there safely.\n"
          "You will need to gather your spacesuit, helmet, oxygen tank, jetpack, battery pack,\n"
          "and keys from different areas of your ship. Once you have your gear,\n"
          "you will be able to exit the hull rupture in your ship and fly home.\n"
          "If you enter the unpressurized area unprepared, you will lose.")
    print('----------------------------------------------------------------')
    print("Move actions: Go North, Go South, Go East, Go West")
    print("Inventory action: Get 'Item Name'")


def show_status():
    # Function that shows inventory, location, and items in room for each turn
    print()
    print('You are in the {}.'.format(current_room))
    print('Inventory:', inventory)
    if 'Get' in rooms[current_room]:
        print('You see your', rooms[current_room]['Get'])
    print('----------------------------------------------------------------')


def player_input():
    # Function that takes in player command and executes it
    global current_room
    command = input('Enter your action:\n').strip().title()
    if 'Go' in command:
        if command in rooms[current_room]:
            current_room = rooms[current_room][command]
        else:
            print('Invalid action!')
    elif 'Get' in command:
        if ('Get' in rooms[current_room]) and (rooms[current_room]['Get'] in command):
            # Adds Item to inventory and Deletes from Rooms
            inventory.append(rooms[current_room]['Get'])
            del rooms[current_room]['Get']
        else:
            print('Invalid action!')
    else:
        print('Invalid action!')


# Dictionary of all rooms and room information
rooms = {
    'Cafeteria': {
                  'Go South': 'Hangar',
                  'Go West': 'Hallway'
                  },
    'Hangar': {
               'Get': 'Jetpack',
               'Go North': 'Cafeteria',
               'Go South': 'Armory',
               'Go East': 'Storage',
               'Go West': 'Hull Rupture'
               },
    'Armory': {
               'Get': 'Battery Pack',
               'Go North': 'Hangar',
               'Go West': 'Bridge'
               },
    'Storage': {
                'Get': 'Oxygen Tank',
                'Go West': 'Hangar'
                },
    'Quarters': {
                 'Get': 'Helmet',
                 'Go South': 'Hallway'
                 },
    'Hallway': {
                'Get': 'Spacesuit',
                'Go North': 'Quarters',
                'Go South': 'Hull Rupture',
                'Go East': 'Cafeteria'
                },
    'Bridge': {
               'Get': 'Keys',
               'Go North': 'Hull Rupture',
               'Go East': 'Armory'
               },
    'Hull Rupture': {
                     'Go North': 'Hallway',
                     'Go South': 'Bridge',
                     'Go East': 'Hangar'
                     }
}

current_room = 'Cafeteria'
inventory = []

# Main Game Loop
show_instructions()

while current_room != 'Hull Rupture':
    # Player's turn loop
    show_status()
    player_input()
else:
    # End of Game sequence
    print('----------------------------------------------------------------')
    if len(inventory) == 6:
        # Player Wins
        print('You have been sucked into space through the Hull Rupture!')
        print('You fly over to the Escape Pod, and safely fly home!')
        print()
        print('    YOU  WIN   ')
    else:
        # Player Loses
        print('You have been sucked into space through the Hull Rupture!')
        print('You don\'t have everything you need, and you are unable to survive.')
        print()
        print('    YOU  LOSE   ')
    print()
    print('Thanks for playing!')