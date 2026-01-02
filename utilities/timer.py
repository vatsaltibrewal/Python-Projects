"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

while True:
    try:
        endTime : int = int(input("Enter The Number of Seconds to set the Timer: "))
        if endTime < 1:
            continue
        break
    except Exception as e:
        print("Error Occured - " , e)


print("Timer Started!")
for i in range(endTime, 0, -1):
    MM : int = endTime // 60
    SS : int = endTime % 60
    print(f"Time Remaning {MM}:{SS}!")
    endTime -= 1
    time.sleep(1)
print("Timer Completed!")