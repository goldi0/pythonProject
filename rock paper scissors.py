import random
l= ["rock","scissor","paper"]

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start...
    1 yes
    # 2 No | Exit 
    '''))

    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
            1 Rock
            2 Scissor
            3 Paper
            
            '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Scissor"
            elif userinput==3:
                uchoice="Paper"
            cchoice=random.choice(l)
            if  cchoice==uchoice:
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1

            elif (uchoice=="rock" and cchoice=="Scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("You Win")
                uconut=ucount+1

            else:
                print("Computer Value",cchoice)
                print("User Value",uchoice)
                print("Computer Win")
                ccount=ccount+1

            if ucount==ccount:
                print("Final Game Draw.....")
                print("User score",ucount)
                print("Computer score",ccount)
            elif ucount>ccount:
                print("Final You Win The Game.....")
                print("User score", ucount)
                print("Computer score", ccount)
            else:
                print("Final Computer Win The Game.....")
                print("User score", ucount)
                print("Computer score", ccount)
        else :
            break






