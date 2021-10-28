import random

reward = 0
die_roll = 0

while die_roll != 1 and die_roll != 2:
    print("1. Stay")
    print("2. Quit")
    val = -1
    try:
        val = input("Select 1 or 2: ")
        if int(val) > 2 or int(val) < 1:
            raise Exception()
        if int(val) == 2:
            reward = reward + 10
            break
        else:
            reward = reward + 4
            die_roll = random.randint(1,6)
            print(f'you rolled a {die_roll}')
    except KeyboardInterrupt:
        quit()
    except:
        print("Please enter valid number")
    
print(f"Your final balance is ${reward}")