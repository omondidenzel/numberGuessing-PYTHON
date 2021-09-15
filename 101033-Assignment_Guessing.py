import random 

randomGen = random.randint(0, 20)

print("Random number: ", randomGen)

def guessNumber(randomGen):
    trial = 0

    while trial < 3:
        randomGuess = int(input("Enter number"))
        
        if randomGuess == randomGen:
            print(f"{randomGen} : Congratulations")
            break

        elif randomGuess < randomGen:
            print(f"{randomGuess} : Too low")

        else: 
            print(f"{randomGuess} : Too high")

        trial += 1
guessNumber(randomGen)