from openpyxl import Workbook

def create_excel(filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "SampleData"

    data = [
        ("Shiva", 25),
        ("Ravi", 30),
        ("", 28),       # empty name
        ("Kumar", 22),
        ("Meena", 27),
        ("", 35),       # empty name
        ("Arjun", 29),
        ("Sneha", 24),
        ("", 31),       # empty name
        ("Kavya", 26),
    ]

    for row in data:
        ws.append(row)

    wb.save(filename)
    print(f"Excel file '{filename}' created successfully!")

# Usage
create_excel("Book1.xlsx")
