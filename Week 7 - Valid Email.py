import random
valid = False
exit_chat = False
operator_names = ['Adam', 'Chloe', 'David', 'Emily', 'Grace', 'Jay', 'Liam', 'Oscar', 'Peter', 'Ryan', 'Shannon']
response = []
answered = False


def check_if_pop(domain):
    global valid
    if domain != "@pop.ac.uk":
        print("Invalid Domain")
        valid = False
    else:
        valid = True


student_email = input('Please Enter Email Address:\n')
index = int(student_email.find('@'))
student_name = student_email[:index]
student_domain = student_email[index:]
student_domain = student_domain.lower()
check_if_pop(student_domain)

if valid == True:
    current_name = random.choice(operator_names)
    print('hello ' + student_name.capitalize() + ', my name is ' + current_name)
    question = input('How can i help you today?\n')
    question = question.lower()
    while answered == False:
        random_number = random.randint(1,16)
        if random_number == 15:
            exit()
        elif ''.join(sorted(question)) == 'bdegooy':
            answered == True
            break
        else:
            if 'library' in question:
                print('Sorry, the library is closed today')
            elif 'wifi' in question:
                print('WiFi is excellent across campus')
            elif 'deadline' in question:
                print('Your deadline has been extended by two working days')
            else:
                random_number = random.randint(1,4)
                if random_number == 1:
                    question = input('Tell me more\n')
                    question = question.lower()
                    continue
                else:
                    response = ['Maybe','I am pleased to hear that']
                    print(random.choice(response))
        question = input('Anything else?\n')
        question = question.lower()

