# complaint.py

# List to store complaints
complaints = []


# 1. Register Complaint
def register_complaint():

    print("\n===== REGISTER COMPLAINT =====")

    complaint = {
        "id": input("Enter Complaint ID : "),
        "tenant": input("Enter Tenant Name : "),
        "room": input("Enter Room Number : "),
        "issue": input("Enter Complaint : "),
        "status": "Pending"
    }

    complaints.append(complaint)
    print("Complaint Registered Successfully.")


# 2. View All Complaints
def view_complaints():

    print("\n===== COMPLAINT LIST =====")

    if len(complaints) == 0:
        print("No Complaints Available.")
        return

    for complaint in complaints:
        print("----------------------------")
        print("Complaint ID :", complaint["id"])
        print("Tenant Name  :", complaint["tenant"])
        print("Room Number  :", complaint["room"])
        print("Issue        :", complaint["issue"])
        print("Status       :", complaint["status"])


# 3. Search Complaint
def search_complaint():

    cid = input("\nEnter Complaint ID : ")

    for complaint in complaints:

        if complaint["id"] == cid:

            print("\nComplaint Found")
            print("Complaint ID :", complaint["id"])
            print("Tenant Name  :", complaint["tenant"])
            print("Room Number  :", complaint["room"])
            print("Issue        :", complaint["issue"])
            print("Status       :", complaint["status"])
            return

    print("Complaint Not Found.")


# 4. Update Complaint
def update_complaint():

    cid = input("\nEnter Complaint ID : ")

    for complaint in complaints:

        if complaint["id"] == cid:

            complaint["issue"] = input("Enter New Complaint : ")

            print("Complaint Updated Successfully.")
            return

    print("Complaint Not Found.")


# 5. Resolve Complaint
def resolve_complaint():

    cid = input("\nEnter Complaint ID : ")

    for complaint in complaints:

        if complaint["id"] == cid:

            complaint["status"] = "Resolved"

            print("Complaint Resolved Successfully.")
            return

    print("Complaint Not Found.")


# 6. Pending Complaints
def pending_complaints():

    print("\n===== PENDING COMPLAINTS =====")

    found = False

    for complaint in complaints:

        if complaint["status"] == "Pending":

            found = True

            print("----------------------------")
            print("Complaint ID :", complaint["id"])
            print("Tenant Name  :", complaint["tenant"])
            print("Room Number  :", complaint["room"])
            print("Issue        :", complaint["issue"])

    if not found:
        print("No Pending Complaints.")


# 7. Complaint Count
def complaint_count():

    print("\nTotal Complaints :", len(complaints))


# 8. Complaint Summary
def complaint_summary():

    pending = 0
    resolved = 0

    for complaint in complaints:

        if complaint["status"] == "Pending":
            pending += 1
        else:
            resolved += 1

    print("\n===== COMPLAINT SUMMARY =====")
    print("Total Complaints :", len(complaints))
    print("Pending          :", pending)
    print("Resolved         :", resolved)