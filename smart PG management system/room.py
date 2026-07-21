# room.py

# List to store room details
rooms = []


# 1. Add Room
def add_room():
    print("\n===== ADD ROOM =====")

    room = {
        "room_no": input("Enter Room Number : "),
        "capacity": int(input("Enter Room Capacity : ")),
        "occupied": 0
    }

    rooms.append(room)
    print("Room Added Successfully.")


# 2. View All Rooms
def view_rooms():

    print("\n===== ROOM DETAILS =====")

    if len(rooms) == 0:
        print("No Rooms Available.")
        return

    for room in rooms:
        print("----------------------------")
        print("Room Number :", room["room_no"])
        print("Capacity    :", room["capacity"])
        print("Occupied    :", room["occupied"])
        print("Available   :", room["capacity"] - room["occupied"])


# 3. Allocate Room
def allocate_room():

    room_no = input("\nEnter Room Number : ")

    for room in rooms:

        if room["room_no"] == room_no:

            if room["occupied"] < room["capacity"]:
                room["occupied"] += 1
                print("Room Allocated Successfully.")
            else:
                print("Room is Full.")

            return

    print("Room Not Found.")


# 4. Vacate Room
def vacate_room():

    room_no = input("\nEnter Room Number : ")

    for room in rooms:

        if room["room_no"] == room_no:

            if room["occupied"] > 0:
                room["occupied"] -= 1
                print("Room Vacated Successfully.")
            else:
                print("Room is Already Empty.")

            return

    print("Room Not Found.")


# 5. Search Room
def search_room():

    room_no = input("\nEnter Room Number : ")

    for room in rooms:

        if room["room_no"] == room_no:

            print("\nRoom Found")
            print("Room Number :", room["room_no"])
            print("Capacity    :", room["capacity"])
            print("Occupied    :", room["occupied"])
            print("Available   :", room["capacity"] - room["occupied"])
            return

    print("Room Not Found.")


# 6. View Available Rooms
def available_rooms():

    print("\n===== AVAILABLE ROOMS =====")

    found = False

    for room in rooms:

        if room["occupied"] < room["capacity"]:

            found = True

            print("----------------------------")
            print("Room :", room["room_no"])
            print("Available Beds :", room["capacity"] - room["occupied"])

    if not found:
        print("No Rooms Available.")


# 7. View Occupied Rooms
def occupied_rooms():

    print("\n===== OCCUPIED ROOMS =====")

    found = False

    for room in rooms:

        if room["occupied"] > 0:

            found = True

            print("----------------------------")
            print("Room :", room["room_no"])
            print("Occupied :", room["occupied"])

    if not found:
        print("No Occupied Rooms.")


# 8. Room Summary
def room_summary():

    total_rooms = len(rooms)
    total_capacity = 0
    total_occupied = 0

    for room in rooms:
        total_capacity += room["capacity"]
        total_occupied += room["occupied"]

    print("\n===== ROOM SUMMARY =====")
    print("Total Rooms       :", total_rooms)
    print("Total Capacity    :", total_capacity)
    print("Occupied Beds     :", total_occupied)
    print("Available Beds    :", total_capacity - total_occupied)