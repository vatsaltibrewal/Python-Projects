"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

no_of_people : int = int(input("Enter no. OF People: "))
names : list[str] = []
for i in range(1 ,no_of_people + 1):
    name : str = input(f"Enter {i}th Name: ")
    names.append(name)
total : int = int(input("Enter Total Bill Amount: "))

each_owes : float = round(total / no_of_people, 2)

print("Final Output")
for i in names:
    print(f"{i} owes ₹{each_owes}\n")