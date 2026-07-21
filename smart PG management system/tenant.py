# tenant.py

# List to store all tenant details
tenants = []


# 1. Add Tenant
def add_tenant():
    print("\n===== ADD TENANT =====")

    tenant = {
        "id": input("Enter Tenant ID : "),
        "name": input("Enter Name : "),
        "age": int(input("Enter Age : ")),
        "gender": input("Enter Gender (Male/Female) : "),
        "phone": input("Enter Phone Number : "),
        "room": input("Enter Room Number : ")
    }

    tenants.append(tenant)
    print("\nTenant Added Successfully.")


# 2. View All Tenants
def view_all_tenants():
    print("\n===== TENANT LIST =====")

    if len(tenants) == 0:
        print("No Tenant Records Found.")
        return

    for tenant in tenants:
        print("----------------------------")
        print("ID     :", tenant["id"])
        print("Name   :", tenant["name"])
        print("Age    :", tenant["age"])
        print("Gender :", tenant["gender"])
        print("Phone  :", tenant["phone"])
        print("Room   :", tenant["room"])


# 3. Search Tenant
def search_tenant():
    print("\n===== SEARCH TENANT =====")

    tid = input("Enter Tenant ID : ")

    for tenant in tenants:
        if tenant["id"] == tid:
            print("\nTenant Found")
            print("ID     :", tenant["id"])
            print("Name   :", tenant["name"])
            print("Age    :", tenant["age"])
            print("Gender :", tenant["gender"])
            print("Phone  :", tenant["phone"])
            print("Room   :", tenant["room"])
            return

    print("Tenant Not Found.")


# 4. Update Tenant
def update_tenant():
    print("\n===== UPDATE TENANT =====")

    tid = input("Enter Tenant ID : ")

    for tenant in tenants:
        if tenant["id"] == tid:

            tenant["name"] = input("Enter New Name : ")
            tenant["age"] = int(input("Enter New Age : "))
            tenant["gender"] = input("Enter New Gender : ")
            tenant["phone"] = input("Enter New Phone : ")
            tenant["room"] = input("Enter New Room Number : ")

            print("\nTenant Updated Successfully.")
            return

    print("Tenant Not Found.")


# 5. Remove Tenant
def remove_tenant():
    print("\n===== REMOVE TENANT =====")

    tid = input("Enter Tenant ID : ")

    for tenant in tenants:
        if tenant["id"] == tid:
            tenants.remove(tenant)
            print("\nTenant Removed Successfully.")
            return

    print("Tenant Not Found.")


# 6. Count Tenants
def count_tenants():
    print("\nTotal Tenants :", len(tenants))


# 7. Male/Female Count
def gender_count():

    male = 0
    female = 0

    for tenant in tenants:
        if tenant["gender"].lower() == "male":
            male += 1
        elif tenant["gender"].lower() == "female":
            female += 1

    print("\nMale Tenants   :", male)
    print("Female Tenants :", female)


# 8. Tenant Details by Room
def tenant_by_room():

    room = input("\nEnter Room Number : ")

    found = False

    for tenant in tenants:
        if tenant["room"] == room:
            found = True
            print("----------------------------")
            print("ID     :", tenant["id"])
            print("Name   :", tenant["name"])
            print("Age    :", tenant["age"])
            print("Gender :", tenant["gender"])
            print("Phone  :", tenant["phone"])

    if not found:
        print("No Tenant Found in this Room.")