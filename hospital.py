patients = {}

while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")

        if pid in patients:
            print("Patient ID already exists!")
        else:
            name = input("Enter Patient Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")

            patients[pid] = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Disease": disease
            }

            print("Patient added successfully!")

    elif choice == "2":
        if len(patients) == 0:
            print("No patients found.")
        else:
            print("\nPatient Records:")
            for pid, details in patients.items():
                print("---------------------------")
                print("Patient ID :", pid)
                print("Name       :", details["Name"])
                print("Age        :", details["Age"])
                print("Gender     :", details["Gender"])
                print("Disease    :", details["Disease"])

    elif choice == "3":
        pid = input("Enter Patient ID to search: ")

        if pid in patients:
            print("\nPatient Found")
            print("Name    :", patients[pid])