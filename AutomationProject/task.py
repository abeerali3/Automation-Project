
#
path = 'C:\\Users\\aiman\\OneDrive\\Desktop\\Automation\\Employees.csv'  # Changed file path and format


with open(path, 'r') as file:
    file_data = file.readlines()  # Renamed 'lines' to 'file_data'


replacements = {
    "Leverling,Janet": "Almahdi,Abeer",
    "Buchanan,Steven": "Vosko,Yuri",
    "Suyama,Michael": "Alokby,Khaled"
}

for index, line in enumerate(file_data):
    for old_name, new_name in replacements.items():
        file_data[index] = line.replace(old_name, new_name) 


with open('updated_employee.csv', 'w') as new_file:
    new_file.writelines(file_data)  


print("Modified Employees Records:")
for line in file_data:
    print(line.strip()) 
