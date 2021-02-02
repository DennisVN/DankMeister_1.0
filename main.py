print("DankMeister_1.0 W3lcomes you. Few have survived, are you worthy ? ")

name = input("Choose your Nickname ")
age = int(input ("How old are you ? This game contains drugsabuse and bad dad jokes :3 "))

print("Thank you", name, ", You are", age, "years old ! ")

health = 666

if age >= 18:
    print("You are ripe enough for this journey !")

    wants_to_play = input("Ready to become the ultimate M4Dl4D (yes/no) ? ").lower()

    if wants_to_play == "yes":
        print("COME ON IIN ! time to GIT GUD. ") 
        print("You start off with ", health, "health.")

        acoldone_or_bigdoink = input("First choice... a cold one or a big doink (acoldone/bigdoink)? ").lower()
        if acoldone_or_bigdoink == "bigdoink":
            print("hell yeah my dude. You got so baked that you fell asleep on a park bench. ")
            print("You woke up in the park and lost 333 health. they stole your kidney. Time for revenge.")
            health -= 333
            print("you Have", health,"health left. ")



            car_or_foot = input("Do you go by car or by foot (car/foot)? ").lower()
            if car_or_foot == "car":
                print("bruh, you were to baked to drive and hit a pedestrian. The pedestrian laughed his ass off, because you are dead now. REKT. ")
                health -= 753
                print("You lost all your health and have", health,"health left. ...GAME OVER BRUH...")
                print ("Don't drink and drive, you might spill your beer. - NOFX")
            elif car_or_foot == "foot":
                print("Right behind the corner there's a slimy type holding your kidney. grab him dude !" )
                print("As you are chasing your kidney, you find an SMG. ")
                print("Everyone is watching you on the street.")
                headshot_or_stealth = input("Headshot or go stealth mode(headshot/stealth) ? ").lower()

                if headshot_or_stealth == "headshot":
                    print("...BOOM HEADSHOT...from the police...you got sniped by a law enforcer. GAME OVER RAMBO. ")
                    health -= 666

                elif headshot_or_stealth == "stealth":
                    print("Smart guy.He got trapped in an alley so you shanked all the blood out of him.")
                    print("You safely got away !")

                    hospital_or_buyweed = input ("You go to the hospital first or buy weed first (hospital/buyweed)? ").lower()
                    
                    if hospital_or_buyweed == "hospital":
                        health += 333
                        print("You got your kidney back ! You now have", health, "health left.")
                        print("Too bad terrorists came and blew up the entire hospital. RIP", name,"what a waste...")
                        health -= 1068
                        print("you have", health, "health left." )
                        print("Too bad this game doesn't support stealthy and campy pussyplay. Grow a pair will ya.")
                        print("INSERT COIN")

                    elif hospital_or_buyweed =="buyweed":
                        print("You truly are a M4DL4D. You went to the plug but got shanked on the way back. ")
                        print("You lost 333 health.")
                        health -= 333
                        if health <= 0:
                            print("You have", health, "health left. You suck... GAME OVER... ")
                else: print("HAHA FUNNY GUY! That was not an option. You died now, try again !")


        elif acoldone_or_bigdoink == "acoldone":
            print("You cracked a cold one in your car and caused an accident. -333 health.")
            health -= 333
            print("You now have", health,"health left. ")

            print("You managed to get away from the crime scene. That kid looked young tho, what a shame...")
            morebeer_or_bigdoink = input("Do we drink more beer now, or smoke a bigdoink (morebeer/bigdoink)? ").lower()
            if morebeer_or_bigdoink == "morebeer":
                print("You got issues bro, your liver exploded so badly, the dinosaurs came back to life. Rest in Pabst bro.")
                health-=333
                if health <= 0:
                 print("You have", health, "health left. You suck... GAME OVER... ")
            elif morebeer_or_bigdoink == "bigdoink":
                print("That's whatsup, you just proven yourself worthy. ")
                print("You've learned the true value of cracking a cold one, beeing a menace to society, and smoking bigdoinks afterwards.")
                print("Better not fall asleep on a park bench with all those kidney thiefs out there. ")
                casino_or_cartoons = input("So what do we do, we go to the casino or watch some cartoons (casino/cartoons)? ").lower()
                if casino_or_cartoons =="casino":
                    health -= 333
                    print("You couldn't enter the casino as the bodyguard spotted your car. The front bumper is completely smashed and covered in childs blood from the crash. You started a fight with him but he shanked you instantly. ")
                    if health <= 0:
                        print("You have", health,"health left.What a fucking stupid idea. Try again FFS.")
                elif casino_or_cartoons =="cartoons":
                    print("!!! CONGRATULATIONS, YOU WON DankMeister_1.0 !!! ")
                    print("You now have the capacity to drink first, act stupid later, and THEN calm down by smoking big doinks.")
                    print("You have the godlike capacity of not giving a fuck, you are the coolest piece of shit out there !")
                    print("We love you, and hope to see you again in DankMeister_1.01 you sexy POS.")
                    print("THVNKS FXR PLVYING")
    if wants_to_play == "no":
            print("I thought so. Your weakness disgusts me... Please Uninstall.")
else:
    print("Your immaturity disgusts me. Please get out ! ") 


''''
string "hello" ,"hi" ,"9"
int 1, 10, 100, -9999
float 1.0, 11.3, 100.8, -22.3
bool True, False
'''