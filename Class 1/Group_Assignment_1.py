'''
Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. 

The program should at first create a variable for the number of days. 

Use loops and functions to write your code.

Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies'''


def penny_count(n):
    penny_sum = 0.5
    total_sum = 0
    for i in range(1,n+1):
        penny_sum = penny_sum * 2
        total_sum = total_sum + penny_sum
        print(f"Day {i}'s salary is {int(penny_sum)} pennies and the total is ${int(total_sum)/100}.")
    return (total_sum/100)

n = int(input("Enter a number: "))
print(f"The total sum after {n} days is ${penny_count(n)} dollars.")
