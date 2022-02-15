import random, sys, time


print("It's time to draw sooo.......DRAW!")
input("Press Enter to begin")

while True:
    print()
    print("It's high noon...")
    time.sleep(random.randint(20,50) / 10.0)
    print('DRAW!')
    drawTime = time.time()
    input() # This function call doesn't return until "Enter" is pressed
    timeElapsed = time.time() - drawTime

    #Conditions:
    if timeElapsed < 0.01:
    #if the player pressed Enter before DRAW! appeared,
    #the input() call return almost instantly
        print('You draw before "DRAW!" appeared! you lose')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. Therefore, your TOO SLOW SUCKAA!!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed,'seconds to draw.')
        print('You are now the fastest gunslinger in the west!! way to go partna! YOU WIN!!!')

    #Player options
        print('Enter QUIT to stop, or press "Enter" to play again')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing. See you soon Partna! YEEEEEEHAWWWW!!!')
            sys.exit()