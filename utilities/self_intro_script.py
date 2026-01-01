"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

from datetime import *

name : str = input("Enter Your Name: ")
age : int = int(input("Enter Your Age: "))
city : str = input("Enter Your City: ")
profession : str = input("Enter Your Profession: ")
hobby : str = input("Enter Your Hobby: ")

current_date : str = datetime.now().date().isoformat()

print("Your Self Intro:")
print(f"Hello! My name is {name}. I'm {age} years old and live in {city}. I work as a {profession} and I absolutely enjoy {hobby} in my free time. Nice to meet you!")
print(f"Logged on: {current_date}")

# OUTPUT
"""
Enter Your Name: Vatsal
Enter Your Age: 21
Enter Your City: Siwan
Enter Your Profession: Student
Enter Your Hobby: Listning Music
Your Self Intro:
Hello! My name is Vatsal. I'm 21 years old and live in Siwan. I work as a Student and I absolutely enjoy Listning Music in my free time. Nice to meet you!
Logged on: 2026-01-01
"""