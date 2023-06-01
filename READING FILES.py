#reading from an externasl file
#r =  read
#w = write
#a = append
#r+ = read and write
employeeFile = open('employees.txt', 'r')
for employee in employeeFile.readlines():
    print(employee)
print(emSployeeFile.readable())
print(employeeFile.writable())
print(employeeFile.read())
print(employeeFile.readline())
print(employeeFile.readlines())
employeeFile.close()

# WRITING AND APPENDING TO FILES