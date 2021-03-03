introductory_msg = "This is the program that can help you find your carbon footprint. Let's get started, shall we!! YES or NO"

def get_started():
    print(introductory_msg)
    validation = input().upper()
    if validation == "YES":
        validate = True
        print("Super! Let's get started. This application will record your activities for a 'day'.")
    else:
        validate = False
        print("That's alright! It was good interacting with you. Tschüss!!")
    return validate

flag = get_started()
def question_set():
    question_1 = "How do you rate yourdelf?"
    print(question_1)
    response = input()

