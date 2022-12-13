#Deividas Ilgunas
#Test Quiz Game
#The point of the project is to test my skills but also have a little fun.
#The quiz has no specific category just a bunch of random questions

name=input("What is your name: ")
print("Your name is", name +"?")
option=input("yes/no ")
if option=="yes":
  print("Welcome to the game show,", name+"!")  
while option!="yes":
    name=input("What is your name: ")
    print("Your name is", name +"?")
    option=input("yes/no ")
    if option=="yes":
        print("Welcome to the game show,", name+"!")
    else:
        print("How do you not know your name...")
age=int(input("What is your age: "))
if age>=26:
    print("We recommend 21 but its fine, good luck :)")
elif age>=21 or age>=18:
    print("Perfect, good luck :)")
elif age>=15:
    print("A little to young, might have trouble with some questions but good luck :)")
else:
    print("TO YOUNG!!")
print("It is all mutliple choice if listed, so type the number if listed. \nThere will be some EASY math equations,")
start_menu=int(input("Type 1 to start: "))
while start_menu != 1: #This is serving as a loop, so if the user dosen't type one it will keep asking until 1 is typed.
    start_menu=int(input("Type 1 When ready: ")) 
    if start_menu==1:
       True #I put True because thats how my loop is broken.
print("Let the Games begin!")
score=0
print("What the Capital of California?")
print("1. Tallahassee \n2. Sacramento \n3. Helena")
questionOne=int(input("Select an answer: "))
if questionOne ==2:
    print("Good Job!")
    score+=1
else: #Basically all the problems have this format, the correct answers code is the if and the else is if they type the wrong number for the answer.
    print("Better luck next time.\nCorrect Answer is Sacramento.")       
print("What company does Elon Musk Own?")
print("1. Tesla \n2. Publix \n3. Amazon")
questionTwo=int(input("Select an answer: "))
if questionTwo ==1:
    print("Good Job!")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is Tesla.")
print("MATH TIME: What is 36+22.22*2.5555-2//2**3/2%2.2?"+"\nTYPE ONLY THE FIRST 3 DECIMAL POINTS")#The math equation for the part of the project needed.
Answer= 36+22.22*2.5555-2//2**3/2%2.2
questionThree=float(input("Type in your answer: "))
if questionThree == 92.783: #couldn't get "answer" to replace 92.783 without a error so I just caculated it
    print("Good Job!")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is "+ format(Answer,".3f"), sep='')
print("What team is Lebron playing for in the NBA?")
print("1. Clippers \n2. Celtics \n3. Lakers")
questionFour=int(input("Select an answer: "))
if questionFour ==3:
    print("Good Job!"+"\nCletics better, by the way ;)")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is Lakers.")
print("Who is the 16th president?")
print("1. Joe Biden \n2. Andrew Jackson \n3. Abraham Lincoln")
questionFive=int(input("Select an answer: "))
if questionFive ==3:
    print("Good Job!")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is Abraham Lincoln.")
print("Who does Jim Halpert fall in love with in The Office?")
print("1. Michael \n2. Pam \n3. Karen")
questionSix=int(input("Select an answer: "))
if questionSix ==2:
    print("Good Job!")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is Pam.")
print("What Year was WW2?\n(You can type a year that was during WW2 or the end if you would like.")
questionSeven=int(input("type your answer: "))
if questionSeven>1938 and questionSeven<1946:
    print("Good Job!\nWW2 was from 1939-1945.")
    score+=1
else:
    print("Better luck next time.\nCorrect Answer is between 1939-1945")
print("Analyze the patter below: ")
for x in range(1,12,2):
    print(x)
questionEight=int(input("What will be the next number? "))
if questionEight==13:
    print("Good Job!")
    score+=1
else:
    print("Bertter luck next time.\nCorrect Answer is 13")
print("All done!(For this version)")
print("Your final score is:", score ,"out of 8")





        

    


    
                
















































