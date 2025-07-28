import time
import sys
from PIL import Image

def quiz():
    Easy_Mode_Points = 50
    Winstreak = 0

    
    questions = [
        ("Question 1: What is the national dish of Canada?: ", ["poutine"]),
        ("Question 2: What is the national dish of Mexico?: ", ["taco", "tacos"]),
        ("Question 3: What is the national dish of Italy?: ", ["pizza"]),
        ("Question 4: What is the national dish of Japan?: ", ["sushi"]),
        ("Question 5: What is the national dish of South Korea?: ", ["kimchi"]),
        ("Question 6: What is the national dish of the United States?: ", ["hamburger", "hamburgers", "burger", "burgers"]),
        ("Question 7: What is the national dish of the United Kingdom?: ", ["fish and chips"]),
        ("Question 8: What is the national dish of Vietnam?: ", ["pho"]),
        ("Question 9: What is the national dish of Lebanon?: ", ["hummus", "hummis", "hummus dip", "hummis dip"]),
        ("Question 10: What is the national dish of Jamaica?: ", ["jerk chicken"])
    ] 

    def win(Easy_Mode_Points):
        print()
        print("That is correct!")
        time.sleep(0.5)
        print()
        if Winstreak >= 3:
            print("You have just gained 10 points because of your win streak🔥!")
            Easy_Mode_Points = Easy_Mode_Points + 10
        else:
            print("You have just gained 5 points!")
            Easy_Mode_Points = Easy_Mode_Points + 5
        print()
        print("You have", Easy_Mode_Points, "points!")
        print()
        return Easy_Mode_Points

    def loss():
        print("Game Over! You have no points left!")
        img = Image.open("gameover.png")
        img.show
        time.sleep(0.5)
        print()
        retry = input("Do you want to try again? (Yes or No): ").lower()
        if retry == "yes":
            quiz()
        else:
            print()
            print("Thanks for playing!")
            sys.exit()

    def update_points(Easy_Mode_Points):
        Easy_Mode_Points = Easy_Mode_Points - 10
        print()
        print("Incorrect!")
        print()
        print("You have", Easy_Mode_Points, "points left!")
        print()
        return Easy_Mode_Points

   
    while True:
        User_Country = input("Where are you from? (Country): ").strip()
        if User_Country == "":
            print("You haven't entered anything! Please try again.")
        else:
            break

    if User_Country.lower() == "canada":
        print()
        print("I am from Canada too!")
    else:
        print()
        print("That is a beautiful country!")

    if User_Country != "":
        time.sleep(2)
        print()
        print("Welcome to the Culture Quiz!")
        img = Image.open("Culture Qui.png")
        img.show
        time.sleep(2)
        print()
        print("The objective of this game is to survive till the end of the quiz you start with 50 points. Each correct answer to a given question adds 5 points to your score and each incorrect answer deducts 10 from your score. If you answer 3 questions correctly in a row, you will activate a win bonus streak where you get double the points (10) per question you get right until you get one wrong.".strip())

    if User_Country != "":
        print()
        Begin_Prompt = input("Press anything to continue!: ")
        if Begin_Prompt != "":
            print("")
            print("Let's begin!")
    else: 
        time.sleep(10)
        print("You haven't entered anything!")

    print()
    time.sleep(0.5)
    print("There are 10 questions, you get 5 points for each correct answer and you lose 10 points for each incorrect answer.")
    time.sleep(1.2)
    print()
    print("Good Luck!")
    print()
    print()
    print("Good Luck!")
    print()

    
    for i in range(len(questions)):
        question_text, correct_answers = questions[i]
        question_num = i + 1

        
        if question_num == 1:
            Q1_Answer = input(question_text)
            if Q1_Answer.lower() == "poutine":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
            elif Q1_Answer == "":
                print("No it is not a trick question, Canada does have a national dish!")
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

            time.sleep(0.5)         
            Ready_Or_Not = input("Are you ready for the next question? Press anything to continue: ")
            print()
            if Ready_Or_Not.strip() != "":
                time.sleep(1.5)
            else: 
                print("Quiz will automatically resume in 10 seconds!")
                time.sleep(10)
                print()

        elif question_num == 2:
            Q2_Answer = input(question_text)
            if Q2_Answer.strip().lower() in ["taco", "tacos"]:
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 3:
            print()
            Q3_Answer = input(question_text)
            if Q3_Answer.lower() == "pizza":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak == 3:
                    print("You have a win streak of 3! You will get double points for this question!")
                    print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 4:
            Q4_Answer = input(question_text)
            if Q4_Answer.lower() == "sushi":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else: 
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 5:
            Q5_Answer = input(question_text)
            if Q5_Answer.lower() == "kimchi":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

            print("You are halfway through the quiz! You got this!")
            print()
            time.sleep(0.5)
            Feedback = input("Is this mode difficult or easy? Enter to skip Feedback.:  ")
            if Feedback.lower() == "difficult":
                print("I will try to make it easier. ")
            elif Feedback.lower() == "easy":
                print("I will try to make it more challenging!")
            elif Feedback == "":
                print("You have skipped Feedback")
            else:
                print("Thanks for the feedback!")

        elif question_num == 6:
            print()
            Q6_Answer = input(question_text)
            if Q6_Answer.strip().lower() in ["hamburger", "hamburgers", "burger", "burgers"]:
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else: 
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 7:
            Q7_Answer = input(question_text)
            if Q7_Answer.lower() == "fish and chips":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 8:
            time.sleep(0.7)
            print()
            Q8_Answer = input(question_text)
            if Q8_Answer.lower() == "pho":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 9:
            time.sleep(0.7)
            print()
            Q9_Answer = input(question_text)
            print()
            print("This is one of the hardest questions on the quiz!")

            User_Hint = input("Would you like a hint? (Yes or No): ")
            if User_Hint == "Yes":
                print("The national dish of Lebanon is a very famous dip!")
            elif User_Hint == "No":
                print("Brave, you decided that you don't need a hint!")

            if Q9_Answer.strip().lower() in ["hummus", "hummis", "hummus dip", "hummis dip"]:
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                    if Winstreak == 3:
                        print("You have a win streak of 3! You will get double points for this question!")
                        print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

        elif question_num == 10:
            print()
            print("This is the last question! You got this!")
            Q10_Answer = input(question_text)
            if Q10_Answer.lower() == "jerk chicken":
                Easy_Mode_Points = win(Easy_Mode_Points)
                Winstreak = Winstreak + 1
                if Winstreak > 3:
                    Easy_Mode_Points = Easy_Mode_Points + 5
                if Winstreak == 3:
                    print("You have a win streak of 3! You will get double points for this question!")
                    print()
            else:
                Easy_Mode_Points = update_points(Easy_Mode_Points)
                Winstreak = 0
                if Easy_Mode_Points <= 0:
                    loss()
                    return

    print()
    print("You successfully completed the quiz! You are cultured!")
    print()
    print("Final Score:", Easy_Mode_Points, "points!")
    play_again = input("Do you want to try again? Yes/No: ").lower()
    if play_again == "yes":
        quiz()