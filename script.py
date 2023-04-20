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
print(colors.GREEN + "3. Delete the stored data" + colors.GREEN)
response = input()


# 1. Record data
if response == "1":
    print("\nSelected: 1")
    response = "0"


# 2. View data
elif response == "2":
    print("\nSelect: 2")
    response = "0"
    

# 3. Delete data
elif response == "3": 
    print("\nSelect: 3")
    response = "0"
    

# Record key strokes


# Copy key strokes to document

# Testing
time.sleep(10)
