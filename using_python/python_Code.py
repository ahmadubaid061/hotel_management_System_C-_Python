
class Room:
    def __init__(self, room_id,room_type, price, guest):
        self.room_type=room_type
        self.room_id = room_id
        self.price = price
        self.guest = guest
        
        
        #funciton for printing room data
    def __str__(self):
        return f"Room ID: {self.room_id} | Type: {self.room_type} | Price: {self.price} | Guest: {self.guest}"
        
allRooms=[] #a list for storing all rooms data
emptyRooms=[] #list for storing empty rooms data
alotedRooms=[] # list for storing  aloted rooms data only

#function for creating and classifying rooms into 3 types
def classify_rooms():
    for i in range(0,5):
        room_id=i+1
        room_type="class_A"
        price=100000
        guest="NULL"
        room=Room(room_id,room_type,price,guest)
        allRooms.append(room)
        emptyRooms.append(room)
    for i in range(5,15):
        room_id=i+1
        room_type="class_B"
        price=50000
        guest="NULL"
        room=Room(room_id,room_type,price,guest)
        allRooms.append(room) 
        emptyRooms.append(room)
    for i in range(15,30):
        room_id=i+1
        room_type="class_C"
        price=25000
        guest="NULL"
        
        room=Room(room_id,room_type,price,guest)
        allRooms.append(room)
        emptyRooms.append(room)  

classify_rooms()

print("============= Hotel Management System ===========")
print("------we provide 3 types of rooms services-------")
print("---class_A with luxury style")
print("---class_B with 2 beds")
print("---class_C with just one bed")
print("---Total NO  of Rooms : ",30)
print("---Occupied rooms are : ",len(alotedRooms))
print("---Available rooms are: ",len(emptyRooms))

print()


while(True):
    print("Please select an option to continue: ")
    print("1. View Rooms")
    print("2. View Occupied Rooms")
    print("3. View Available Rooms")
    print("4. Alot a Room")
    print("5. Vacate a Room")
    print("0. Exit")
    option=int(input("Enter your option here: "))
    match option:
        case 1:
            for room in allRooms:
                print(room)
            print()
            continue
        case 2:
            if(not alotedRooms):
                print("No room is alotted yet")
                print()
            for room in alotedRooms:
                print(room)
            print()
            continue
        case 3:
            if(not emptyRooms):
                print("All rooms are Occupied")
            print()
            for room in emptyRooms:
                print(room)
            print()
            continue
        case 4:
            print("Enter type of Room(class_A/class_B/class_C): ")
            type_of_room=input()
            if type_of_room in ["class_A", "class_B", "class_C"]:
                found=False
                for room in emptyRooms:
                    if room.room_type == type_of_room:
                        found=True
                        print("Please Enter guest Name: ")
                        name=input().strip()
                        room.guest=name
                        alotedRooms.append(room)
                        emptyRooms.remove(room)
                        print(f"Room Alotted Successfully to {name}")
                        print()
                        print("Room details!")
                        print(room)
                        print()
                        break
                if not found:
                    print("Sorry! no room is Available in that category")
                    print()       
            else:
                print("Invalid room type!")
                print()
            continue
        case 5:
            print("please enter guest name: ")
            name=input("")
            found=False
            print("Please Enter Room ID: ")
            id=int(input(""))
            for room in alotedRooms:
                if room.guest==name and room.room_id==id:
                    found=True
                    room.guest="NULL"
                    alotedRooms.remove(room)
                    emptyRooms.append(room)
                    print("Room vacated Successfully!") 
                    break
            if not found:
                print(f"No record of {name} found!")
                print()
            continue
        case 0:
            print("exiting")
            break
        case _:
            print("Invalid choice")