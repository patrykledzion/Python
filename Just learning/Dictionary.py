student = {
    458798: {
        "name": "Jan",
        "lastname": "Kowalski",
        "PESEL": "00270658742"
    },
    478569: {
        "name": "Jan",
        "lastname": "Nowak",
        "PESEL": "99071547985"
    },
    452136: {
        "name": "Piotr",
        "lastname": "Cichy",
        "PESEL": "98022236547"
    }
}

print("Insert student ID: ")
id = int(input())

try:
    print(student[id]["name"])
    print(student[id]["lastname"])
    print(student[id]["PESEL"])
except:
    print(f"No student with given ID")
