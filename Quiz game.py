from tkinter.messagebox import YES
print("WELCOME TO MY QUIZ GAME")
playing = input("DO YOU WANT TO PLAY?")
if playing.lower() != "yes":
    quit()
    print("OKAY! LET US PLAY :)")
    score = 1

answer= input("what does RAM stand of?")
if answer.lower() == "Random Access Memory":
    print("correct!")
    score += 10
else :
    print("incorrect!")
    
answer= input("what does GPS stand of?")
if answer.lower() == "Global Positioning System":
    print("correct!")
    score +=10
else :
    print("incorrect!")
    
answer= input("what does CPU stand of?")
if answer.lower() == "Central Processing Unit":
    print("correct!")
    score += 10
else :
    print("incorrect!")
answer= input("what does GPU stand of?")
if answer.lower() == "Graphics Processing Unit":
    print("correct!")
    score += 10
else :
    print("incorrect!")

print("You Got" + str(score) + "questions correct!")
print("You Got" + str((score/4)*100) + "%.")
