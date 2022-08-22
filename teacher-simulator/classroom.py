# EX 089 : Write a script that will receive several Students names, and 2 separate grades into lists, and put those into
# a list as well. Then, display a table with all the student info, ad ask if the user wants to see any student's
# info on its own.
students = []
while True:
    student = [str(input('Student name?')), int(input('First Grade:')), int(input('Second Grade:'))]
    check = str(input('[No] To Quit, [Yes] to proceed')).strip().lower()[0]
    students.append(student[:])
    student.clear()
    if check == 'n':
        break
print('No.  Name    Average Grade')
print('-='*15)
for c in range(0, len(students)):
    print(f'{c:<3} {students[c][0]:<10} {(students[c][1] + students[c][2]) / 2:>10}')
print('-=' * 15)
search = str(input('Would you like to see a specific student`s data?')).strip().lower()[0]
if search == 'y':
    while True:
        search = int(input('Which student do you wish to pull up from the system? (Search by student number!)'))
        print(students[search])
        check2 = str(input('[No] To Quit')).strip().lower()[0]
        if check2 == 'n':
            break