def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_assignments = []
    for index, name in enumerate(names, start=1):
        message = f"Hello, {name}! You'll be assigned to room {index}!"
        room_assignments.append(message)
    return room_assignments

def printer(names):
    # Assuming 'batch_badge_creator' generates a list of badge messages.
    badges = batch_badge_creator(names)
    # Assuming 'assign_rooms' generates a list of room assignment messages.
    room_assignments = assign_rooms(names)
    
    # Print each badge message.
    for badge in badges:
        print(badge)
    
    # Print each room assignment message.
    for assignment in room_assignments:
        print(assignment)
