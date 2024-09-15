import random 

ans = input("Do you trust your instincts?(Yes/No) : " ).lower()

if (ans == "Yes" or ans == "yes"):
       ans2 = input("Type 'Play' to play the game! : ")
       if (ans2 == "Play" or ans2 == "play"):
              print("Instructions : A random number will be generated between 1 to 100. You have to guess it")
              Guess = int(input("Enter your guess : "))
              Guess_count = 1
              number = random.randint(1, 100)
              if(number == Guess):
                       print("YOU GOT IT.")
                    
              else:
                     while(number != Guess):                
                          if(Guess>number):
                                print("Try lower")
                          elif(Guess<number):
                                print("Try Higher")
                          Guess_count +=1      
                          Guess = int(input("Enter your guess : "))
                         
                     print("You got it!")
                     print(f"You took {Guess_count} attempts")

       else:
               print("Invalid Response")                    

elif(ans == "No" or ans == "no"):
       print("What a looser!")
else:
       print("Invalid Response")

  