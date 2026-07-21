# report.py

from tenant import tenants
from room import rooms
from rent import rents
from complaint import complaints
from visitor import visitors


# 1. Tenant Report
def tenant_report():

    print("\n========== TENANT REPORT ==========")
    print("Total Tenants :", len(tenants))


# 2. Room Report
def room_report():

    print("\n========== ROOM REPORT ==========")

    print("Total Rooms :", len(rooms))

    total_capacity = 0
    occupied = 0

    for room in rooms:
        total_capacity += room["capacity"]
        occupied += room["occupied"]

    print("Total Capacity :", total_capacity)
    print("Occupied Beds  :", occupied)
    print("Available Beds :", total_capacity - occupied)


# 3. Rent Report
def rent_report():

    print("\n========== RENT REPORT ==========")

    total = 0
    paid = 0
    pending = 0

    for rent in rents:

        total += rent["amount"]

        if rent["status"] == "Paid":
            paid += rent["amount"]
        else:
            pending += rent["amount"]

    print("Total Rent Amount :", total)
    print("Collected Rent    :", paid)
    print("Pending Rent      :", pending)


# 4. Complaint Report
def complaint_report():

    print("\n========== COMPLAINT REPORT ==========")

    total = len(complaints)
    resolved = 0
    pending = 0

    for complaint in complaints:

        if complaint["status"] == "Resolved":
            resolved += 1
        else:
            pending += 1

    print("Total Complaints :", total)
    print("Resolved         :", resolved)
    print("Pending          :", pending)


# 5. Visitor Report
def visitor_report():

    print("\n========== VISITOR REPORT ==========")

    total = len(visitors)
    inside = 0

    for visitor in visitors:

        if visitor["status"] == "Checked In":
            inside += 1

    print("Total Visitors   :", total)
    print("Currently Inside :", inside)


# 6. Occupancy Percentage
def occupancy_percentage():

    total_capacity = 0
    occupied = 0

    for room in rooms:

        total_capacity += room["capacity"]
        occupied += room["occupied"]

    print("\n========== OCCUPANCY ==========")

    if total_capacity == 0:
        print("No Rooms Available.")
    else:
        percentage = (occupied / total_capacity) * 100
        print("Occupancy Percentage : {:.2f}%".format(percentage))


# 7. Overall Statistics
def overall_statistics():

    print("\n========== OVERALL STATISTICS ==========")

    print("Total Tenants    :", len(tenants))
    print("Total Rooms      :", len(rooms))
    print("Total Complaints :", len(complaints))
    print("Total Visitors   :", len(visitors))


# 8. Complete PG Summary
def pg_summary():

    print("\n===================================")
    print("      SMART PG MANAGEMENT")
    print("===================================")

    print("Total Tenants      :", len(tenants))
    print("Total Rooms        :", len(rooms))
    print("Total Complaints   :", len(complaints))
    print("Total Visitors     :", len(visitors))

    total_capacity = 0
    occupied = 0

    for room in rooms:
        total_capacity += room["capacity"]
        occupied += room["occupied"]

    print("Occupied Beds      :", occupied)
    print("Available Beds     :", total_capacity - occupied)

    total_revenue = 0

    for rent in rents:

        if rent["status"] == "Paid":
            total_revenue += rent["amount"]

    print("Revenue Collected  :", total_revenue)

    print("===================================")