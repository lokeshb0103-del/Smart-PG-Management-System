# rent.py

rents = []


# 1. Collect Rent
def collect_rent():

    rent = {
        "tenant": input("Enter Tenant Name : "),
        "amount": int(input("Enter Rent Amount : ")),
        "month": input("Enter Month : "),
        "status": "Paid"
    }

    rents.append(rent)
    print("Rent Collected Successfully.")


# 2. View All Rents
def view_rents():

    if len(rents) == 0:
        print("No Rent Records.")
        return

    for rent in rents:
        print("----------------------")
        print("Tenant :", rent["tenant"])
        print("Amount :", rent["amount"])
        print("Month  :", rent["month"])
        print("Status :", rent["status"])


# 3. Search Rent
def search_rent():

    name = input("Enter Tenant Name : ")

    for rent in rents:

        if rent["tenant"].lower() == name.lower():

            print("----------------------")
            print("Tenant :", rent["tenant"])
            print("Amount :", rent["amount"])
            print("Month  :", rent["month"])
            print("Status :", rent["status"])
            return

    print("Rent Record Not Found.")


# 4. Update Rent
def update_rent():

    name = input("Enter Tenant Name : ")

    for rent in rents:

        if rent["tenant"].lower() == name.lower():

            rent["amount"] = int(input("Enter New Amount : "))
            rent["month"] = input("Enter New Month : ")
            rent["status"] = input("Enter Status(Paid/Pending) : ")

            print("Rent Updated Successfully.")
            return

    print("Record Not Found.")


# 5. Pending Rent
def pending_rent():

    found = False

    for rent in rents:

        if rent["status"].lower() == "pending":

            found = True

            print("----------------------")
            print("Tenant :", rent["tenant"])
            print("Amount :", rent["amount"])

    if not found:
        print("No Pending Rent.")


# 6. Total Revenue
def total_revenue():

    total = 0

    for rent in rents:

        if rent["status"].lower() == "paid":
            total += rent["amount"]

    print("Total Revenue :", total)


# 7. Monthly Income
def monthly_income():

    month = input("Enter Month : ")

    total = 0

    for rent in rents:

        if rent["month"].lower() == month.lower():

            if rent["status"].lower() == "paid":
                total += rent["amount"]

    print("Income for", month, ":", total)


# 8. Rent Summary
def rent_summary():

    paid = 0
    pending = 0

    for rent in rents:

        if rent["status"].lower() == "paid":
            paid += 1
        else:
            pending += 1

    print("\n===== RENT SUMMARY =====")
    print("Total Records :", len(rents))
    print("Paid          :", paid)
    print("Pending       :", pending)