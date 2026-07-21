# main.py

from login import login

from tenant import *
from room import *
from rent import *
from complaint import *
from visitor import *
from report import *


while True:

    print("\n========================================")
    print("      SMART PG MANAGEMENT SYSTEM")
    print("========================================")

    if login():

        while True:

            print("\n========== MAIN MENU ==========")
            print("1. Tenant Management")
            print("2. Room Management")
            print("3. Rent Management")
            print("4. Complaint Management")
            print("5. Visitor Management")
            print("6. Reports")
            print("7. Exit")

            choice = int(input("\nEnter Your Choice : "))

            # ---------------- TENANT ----------------

            if choice == 1:

                while True:

                    print("\n----- TENANT MENU -----")
                    print("1. Add Tenant")
                    print("2. View All Tenants")
                    print("3. Search Tenant")
                    print("4. Update Tenant")
                    print("5. Remove Tenant")
                    print("6. Count Tenants")
                    print("7. Gender Count")
                    print("8. Tenant By Room")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        add_tenant()

                    elif ch == 2:
                        view_all_tenants()

                    elif ch == 3:
                        search_tenant()

                    elif ch == 4:
                        update_tenant()

                    elif ch == 5:
                        remove_tenant()

                    elif ch == 6:
                        count_tenants()

                    elif ch == 7:
                        gender_count()

                    elif ch == 8:
                        tenant_by_room()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            # ---------------- ROOM ----------------

            elif choice == 2:

                while True:

                    print("\n----- ROOM MENU -----")
                    print("1. Add Room")
                    print("2. View Rooms")
                    print("3. Allocate Room")
                    print("4. Vacate Room")
                    print("5. Search Room")
                    print("6. Available Rooms")
                    print("7. Occupied Rooms")
                    print("8. Room Summary")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        add_room()

                    elif ch == 2:
                        view_rooms()

                    elif ch == 3:
                        allocate_room()

                    elif ch == 4:
                        vacate_room()

                    elif ch == 5:
                        search_room()

                    elif ch == 6:
                        available_rooms()

                    elif ch == 7:
                        occupied_rooms()

                    elif ch == 8:
                        room_summary()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            # ---------------- RENT ----------------

            elif choice == 3:

                while True:

                    print("\n----- RENT MENU -----")
                    print("1. Collect Rent")
                    print("2. View Payments")
                    print("3. Search Payment")
                    print("4. Update Payment")
                    print("5. Pending Rent")
                    print("6. Total Revenue")
                    print("7. Monthly Income")
                    print("8. Rent Summary")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        collect_rent()

                    elif ch == 2:
                        view_rents()

                    elif ch == 3:
                        search_rent()

                    elif ch == 4:
                        update_rent()

                    elif ch == 5:
                        pending_rent()

                    elif ch == 6:
                        total_revenue()

                    elif ch == 7:
                        monthly_income()

                    elif ch == 8:
                        rent_summary()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            # ---------------- COMPLAINT ----------------

            elif choice == 4:

                while True:

                    print("\n----- COMPLAINT MENU -----")
                    print("1. Register Complaint")
                    print("2. View Complaints")
                    print("3. Search Complaint")
                    print("4. Update Complaint")
                    print("5. Resolve Complaint")
                    print("6. Pending Complaints")
                    print("7. Complaint Count")
                    print("8. Complaint Summary")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        register_complaint()

                    elif ch == 2:
                        view_complaints()

                    elif ch == 3:
                        search_complaint()

                    elif ch == 4:
                        update_complaint()

                    elif ch == 5:
                        resolve_complaint()

                    elif ch == 6:
                        pending_complaints()

                    elif ch == 7:
                        complaint_count()

                    elif ch == 8:
                        complaint_summary()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            # ---------------- VISITOR ----------------

            elif choice == 5:

                while True:

                    print("\n----- VISITOR MENU -----")
                    print("1. Add Visitor")
                    print("2. View Visitors")
                    print("3. Search Visitor")
                    print("4. Check In")
                    print("5. Check Out")
                    print("6. Visitors By Room")
                    print("7. Current Visitors")
                    print("8. Visitor Summary")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        add_visitor()

                    elif ch == 2:
                        view_visitors()

                    elif ch == 3:
                        search_visitor()

                    elif ch == 4:
                        check_in()

                    elif ch == 5:
                        check_out()

                    elif ch == 6:
                        visitors_by_room()

                    elif ch == 7:
                        current_visitors()

                    elif ch == 8:
                        visitor_summary()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            # ---------------- REPORT ----------------

            elif choice == 6:

                while True:

                    print("\n----- REPORT MENU -----")
                    print("1. Tenant Report")
                    print("2. Room Report")
                    print("3. Rent Report")
                    print("4. Complaint Report")
                    print("5. Visitor Report")
                    print("6. Occupancy Percentage")
                    print("7. Overall Statistics")
                    print("8. PG Summary")
                    print("9. Back")

                    ch = int(input("Enter Choice : "))

                    if ch == 1:
                        tenant_report()

                    elif ch == 2:
                        room_report()

                    elif ch == 3:
                        rent_report()

                    elif ch == 4:
                        complaint_report()

                    elif ch == 5:
                        visitor_report()

                    elif ch == 6:
                        occupancy_percentage()

                    elif ch == 7:
                        overall_statistics()

                    elif ch == 8:
                        pg_summary()

                    elif ch == 9:
                        break

                    else:
                        print("Invalid Choice")

            elif choice == 7:
                print("\nThank You for Using Smart PG Management System.")
                exit()

            else:
                print("Invalid Choice")

    else:
        print("Login Failed.")