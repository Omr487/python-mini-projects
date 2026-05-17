questions = (("HOW MANY ELEMENTS ARE IN THE PERIODIC TABLE?:"),
             ("WHICH ANIMAL LAYS LARGEST EGGS ?:"),
             ("WHAT IS THE mOST ABUNDANT GAS IN THE ATMOSPHERE?:"),
             ("HOW MANY BONES ARE THERE IN HUMAN BODY?:"),
             ("WHICH PLANET IN THE SOLAR SYSTEM IS THE HOTTEST?:"))

options = (("A.116","B.117","C.118","D.119"),
           ("A.WHALE","B.CROCODILE","C.ELEPHANT","D.OSTRICH"),
           ("A.NITROGEN","B.OXYGEN","C.CARBON-DIOXIDE","D.HYDROGEN"),
           ("A.206","B.207","C.208","D.209"),
           ("A.MERCURY","B.VENUS","C.EARTH","D.MARS"))

answers =("C","D","A","A","B")
guesses = []
score  = 0 
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess ==answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1
    

print("-------------------------")
print("---------RESULTS---------")
print("-------------------------")


print("answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions) *100)
print(f"Your score is :{score}%")
