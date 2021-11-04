print("do you live in iran")
answer = input ("yes/no)")
if answer == "yes":
    answer = input("you live in a country where there is a law that you need to the army if you older than 18 years old, (run/stay) ")
    if answer == "run":
        print("you run to turkeye, there you run to the borders where you get the choice to get on the boat or land")
        answer = input ("(land/boat)")
        if answer == "land":
            print("you run to, (Bulgarije/greece)")
            answer = input ("(Bulgarije/greece)")
            if answer == "greece":
                print("you are send to the netherlands, their give you a job, what is it, (fisher/teacher)")
                answer = input ("(fisher/teacher)")
                if answer == "teacher":
                    print("you findt love, and make a family")
                elif answer == "fisher":
                    print("you findt love, and make a family")
                elif answer == "Bulgarije":
                    print("you are send to the netherlands, their give you a job, what is it, (fisher/teacher) ")
                    answer = input ("(fisher/teacher)")
                    if answer == "teacher":
                        print("you findt love, and make a family")
                    elif answer == "fisher":
                        print("you findt love, and make a family")  
                    elif answer == "boat":
                        print("their take you in as a asiel locker, where you get a choose asia or africa")
                        answer = input ("go to asia or africa")
                        if answer == "asia":
                            print("you go to asia and live a life of misery")
                        elif answer == "africa":
                            print("you die")                 
                        elif answer == "stay":
                            print("the army is infront or your door to take you to the army, (army/run)")
                            answer = input ("army/run")
                            if answer == "run":
                                print("you run away to turkeye")
                            elif answer == "army":
                                print(" you go to the army where you train and sent to war, to you go to war or stay at the camp")
                                answer = input ("(stay/war)")
                                if answer == "stay":
                                    print("death")
                                elif answer == "war":
                                    print("death")  
elif answer == "no":
    print("do you live in syrie")
    answer = input ("(yes/no)")
