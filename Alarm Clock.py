import winsound, time, os, platform

def sound():
    """
    Defines the sound played, number of times,
    delay between beeps, and how many times it is repeated.
    """
    for i in range(2):
        for j in range(9):
            winsound.MessageBeep(-1)
        time.sleep(2)


def input_destinations(user_input):
    """
    Sets delay for alarm to go off based on user input.
    """
    if user_input == '1':
        user_input = int(input("Enter the desired hours: "))

        wait_time = (user_input * 60) * 60
        countdown(wait_time)


    elif user_input == "2":
        user_input = int(input("Enter the desired minutes: "))

        wait_time = user_input * 60
        countdown(wait_time)


    elif user_input == "3":
        user_input = int(input("Enter the desired seconds: "))

        wait_time = user_input
        countdown(wait_time)


    elif user_input == "4":
        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))

        wait_time = ((hours*60)*60) + (minutes*60) + seconds
        countdown(wait_time)
        # alarm(wait_time)

    else:
            try:
                os.system('cls')
                main()

            except:
                os.system('clear')
                main()


def countdown(wait_time):
    print("Wait time:", wait_time, "seconds.")
    while wait_time:
        mins, secs = divmod(wait_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r',timer, end='')
        time.sleep(1)
        wait_time -= 1

    sound()


def main():
    print("What unit of time do you want to wait?\n (1) Hours\n (2) Minutes\n (3) Seconds\n (4) Combination")
    main_input = input(": ")

    input_destinations(main_input)

    return

main()