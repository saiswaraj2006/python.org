from openpyxl import Workbook

def create_excel(filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "SampleData"
    ws.append(("name","age","city"))

    data = [
        ("Shiva", 25,"HYD"),
        ("Ravi", 30,"WGL"),
        ("", 28,"KZJ"),       # empty name
        ("Kumar", 22,"HNK"),
        ("Meena", 27,"HNK"),
        ("", 35,"SEC"),       # empty name
        ("Arjun", 29,"WGL"),
        ("Sneha", 24,"SEC"),
        ("", 31,"HYD"),       # empty name
        ("Kavya", 26,"KZJ"),
    ]

    for row in data:
        ws.append(row)

    wb.save(filename)
    print(f"Excel file '{filename}' created successfully!")

# Usage
create_excel("Book1.xlsx")
