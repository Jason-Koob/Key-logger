import time

# File start
class colors:
    PINK = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

print(colors.CYAN + "Welcome to Koob's Key Logger\n" + colors.CYAN)
time.sleep(1)

# Start menu
print(colors.GREEN + "What would you like to do?:\n" + colors.GREEN)
print(colors.GREEN + "1. Record key strokes in your device" + colors.GREEN)
print(colors.GREEN + "2. View the key strokes stored" + colors.GREEN)
print(colors.GREEN + "3. Delete the stored data\n" + colors.GREEN)
response = input()


# 1. Record data
if response == "1":
    with open('records.txt', 'a') as docWrite:
        docWrite.write('Test' + "\n")


# 2. View data
elif response == "2":
    with open('records.txt', 'r') as docRead:
        docContents = docRead.read()
        print("\n" + docContents)
    

# 3. Overwrite data
elif response == "3": 
    with open('records.txt', 'w') as docOverWrite:
        docOverWrite.write()
    
# Record key strokes

time.sleep(10)