from time import sleep

def start():
    name = input("Type your name here: ")
    print("\t\t    i i i")
    sleep(1)
    print("\t\t    i i i")
    sleep(1)
    print("\t----------------------:")
    print("\t   Happy     +++++++++:")
    sleep(1)
    print("\t   ++++      Birthday :")
    sleep(1)
    print(f"   {name}     ++++   |  :")
    print("\t/_____________________ \ ")
    sleep(1)
    print("\t:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.15)
    print("\t:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.15)
    print("\t:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.15)
    print("\t:-:-:-:-:-:-:-:-:-:-:-:")
    sleep(.15)
    sleep(.25)
    print("\t|| || || || || || || ||")
    sleep(.25)
    print("\t|| || || || || || || ||")
    sleep(.25)
    print("\t|| || || || || || || ||")
    sleep(.25)
    print("\t|| || || || || || || ||")
    sleep(.25)
    print("\t_______________________")
    sleep(.5)
    print("Loading.......")
    sleep(1)
    print("A massage was sent to you")
    sleep(.75)
    print("Reaading massege.....")
    sleep(.75)
    print("Decoding......")
    sleep(4)
    print("Wish you a very happy birthday... May god bless you :)")

while True:
    command = input("Type 'START' for starting. \n Type 'QUIT' for exit. \n Don't forget to press enter! \n > ").lower()
    if command == 'start':
        start()
        break
    elif command == 'quit':
        print('Thanks for your visit. Have a nice day.')

        break
    elif command != 'start' and 'quit':
        print("I don't understand that!")