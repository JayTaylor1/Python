username = input("Username:       ")
student_ID = input("Student ID:     ")
first_password_input = input("Please enter the new password:   ")
second_password_input = input("Please re-enter the password:    ")

invalid_strings = [student_ID, username, 'huddersfield', 'justinbieber', 'cheese', 'canalside']

if first_password_input == second_password_input:
    new_password = first_password_input

    if 6 <= len(new_password) <= 12:
        if any(substring in new_password for substring in invalid_strings):
            print("Password to obvious")
        else:
            print("Password Changed")
    else:
        print("New Password must have between 6 and 12 characters")
else:
    print("Passwords do not match")
