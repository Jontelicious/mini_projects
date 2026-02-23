print("Welcome to the Quiz!")

score = 0

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's play!")

answer = input("what does CPU stand for? ")

if answer.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does PSU stand for? ")

if answer.lower() == "power supply unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does ROM stand for? ")

if answer.lower() == "read-only memory":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("That's " + str((score / 5) * 100) + "%!")
