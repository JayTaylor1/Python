class_size = input("Enter the number of students in the class:  ")
error = False

if not class_size.isdigit():
    print('Class Type ERROR')
    exit()
elif int(class_size) <= 0 :
    print('Class Size ERROR')
    exit()

lab_size = input("Enter the number of PCs in the lab:   ")
if not lab_size.isdigit():
    print('Lab Type ERROR')
    exit()
elif int(lab_size) <= 0 :
    print('Lab Size ERROR')
    exit()

number_of_labs = int(class_size) // int(lab_size)
if not int(class_size) % int(lab_size) == 0:
    number_of_labs = number_of_labs + 1
if number_of_labs == 1:
    print('You need 1 lab for all the students')
else:
    print('You need ' + str(number_of_labs) + ' labs for all the students')
pass
