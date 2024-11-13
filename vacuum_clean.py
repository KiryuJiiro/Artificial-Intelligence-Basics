import numpy as np

rooms = np.array(['A','B'])
states = np.array(['clean','dirty'])

def choose_room():
    room = np.random.choice(rooms)
    return room

def choose_state():
    state = np.random.choice(states)
    return state

room_state = {}
for x in rooms:
    room_state[x] = choose_state()
    
current_room = choose_room()
    
for i in range(len(rooms)): ## here range generates sequence from 0 to upto value less than the rooms ko length
    if room_state[current_room] == 'clean':
        print(f'your room {current_room} is clean ')
        print('No operation')
    else:
        print(f'your room {current_room} is dirty')
        print('cleaning')
        room_state[current_room] = 'clean'
    other_room = set(rooms) - {current_room}
    other_room = list(other_room)
    current_room = other_room[0]
         
    
    
    
    
