import time


# # Read
# with open('records.txt', 'r') as f:
#     for line in f:
#         print(line, end='')

# time.sleep(10)

# Append


# with open('records.txt', 'a') as q:
#     q.write('write' + "\n")

# # time.sleep(10)
# print(time.localtime())


import datetime

# get the current date and time
now = datetime.datetime.now()
localTime = now.strftime("%Y-%m-%d %H:%M:%S")

word = 'Test'

with open('records.txt', 'a') as docWrite:
    docWrite.write( localTime + ' : ' + word + '\n')

# print the local time
print("Local time is:", localTime)

time.sleep(10)