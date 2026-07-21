# visitor.py

# List to store visitor details
visitors = []


# 1. Add Visitor
def add_visitor():

    print("\n===== ADD VISITOR =====")

    visitor = {
        "id": input("Enter Visitor ID : "),
        "name": input("Enter Visitor Name : "),
        "tenant": input("Enter Tenant Name : "),
        "room": input("Enter Room Number : "),
        "status": "Checked In"
    }

    visitors.append(visitor)
    print("Visitor Added Successfully.")


# 2. View All Visitors
def view_visitors():

    print("\n===== VISITOR LIST =====")

    if len(visitors) == 0:
        print("No Visitor Records Found.")
        return

    for visitor in visitors:
        print("----------------------------")
        print("Visitor ID  :", visitor["id"])
        print("Name        :", visitor["name"])
        print("Tenant      :", visitor["tenant"])
        print("Room Number :", visitor["room"])
        print("Status      :", visitor["status"])


# 3. Search Visitor
def search_visitor():

    vid = input("\nEnter Visitor ID : ")

    for visitor in visitors:

        if visitor["id"] == vid:

            print("\nVisitor Found")
            print("Visitor ID  :", visitor["id"])
            print("Name        :", visitor["name"])
            print("Tenant      :", visitor["tenant"])
            print("Room Number :", visitor["room"])
            print("Status      :", visitor["status"])
            return

    print("Visitor Not Found.")


# 4. Check In Visitor
def check_in():

    vid = input("\nEnter Visitor ID : ")

    for visitor in visitors:

        if visitor["id"] == vid:

            visitor["status"] = "Checked In"
            print("Visitor Checked In Successfully.")
            return

    print("Visitor Not Found.")


# 5. Check Out Visitor
def check_out():

    vid = input("\nEnter Visitor ID : ")

    for visitor in visitors:

        if visitor["id"] == vid:

            visitor["status"] = "Checked Out"
            print("Visitor Checked Out Successfully.")
            return

    print("Visitor Not Found.")


# 6. Visitors by Room
def visitors_by_room():

    room = input("\nEnter Room Number : ")

    found = False

    for visitor in visitors:

        if visitor["room"] == room:

            found = True

            print("----------------------------")
            print("Visitor ID :", visitor["id"])
            print("Name       :", visitor["name"])
            print("Tenant     :", visitor["tenant"])
            print("Status     :", visitor["status"])

    if not found:
        print("No Visitors Found.")


# 7. Current Visitors
def current_visitors():

    print("\n===== CURRENT VISITORS =====")

    found = False

    for visitor in visitors:

        if visitor["status"] == "Checked In":

            found = True

            print("----------------------------")
            print("Visitor ID :", visitor["id"])
            print("Name       :", visitor["name"])
            print("Tenant     :", visitor["tenant"])
            print("Room       :", visitor["room"])

    if not found:
        print("No Visitors Currently Inside.")


# 8. Visitor Summary
def visitor_summary():

    total = len(visitors)
    checked_in = 0
    checked_out = 0

    for visitor in visitors:

        if visitor["status"] == "Checked In":
            checked_in += 1
        else:
            checked_out += 1

    print("\n===== VISITOR SUMMARY =====")
    print("Total Visitors      :", total)
    print("Checked In Visitors :", checked_in)
    print("Checked Out         :", checked_out)