print("Welcome to my computer quiz! ")

playing= input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    print("okay! let's play :)")
    score = 0


answer = input ("what dose CPU stand for? ")
if  answer.lower() == "cenrteal processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


answer=input("what dose GPU stand for? ")
if  answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


answer=input("what dose RAM stand for? ")
if  answer.lower() == "random memory access":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


answer=input("what dose PSU stand for? ")
if  answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print("You Got" + str(score) + "question correct! ")
print("You Got" + (str (score/4) * 100), "%.")

