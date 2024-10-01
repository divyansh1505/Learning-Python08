import random 

ans = input("Do you trust your instincts?(Yes/No) : " ).lower()

if (ans == "Yes" or ans == "yes"):
       ans2 = input("Type 'Play' to play the game! : ").lower()
       if (ans2 == "Play" or ans2 == "play"):
              print("Instructions : A random number will be generated from your chosen range. You have to guess it")
              
              print ("""Choose range set : 
                       a = 1-100
                       b = 1-250
                       c = 1-500
                       d = 1-1000
                       """)
              rnge = (input("So you decided? : ")).lower()
              if (rnge == "a"):
                    number = random.randint(1,100)
              elif (rnge == "b"):
                     number = random.randint(1,250)
              elif (rnge == "c"):
                     number = random.randint(1,500)
              elif (rnge == "d"):
                     number = random.randint(1,1000)
                    

              Guess = int(input("Enter your guess : "))
              Guess_count = 1
            
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

  