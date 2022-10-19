#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: 10.13.22
# This program checks the month using numbers 1-12.


# month will match number 1-12
def month_match():
    # month_user covers 0-12 and goes according to the month.
    month_user = input("What is the number of the month?: ")
    match (month_user):
        case "1":
            print("The month is January")
        case "2":
            print("The month is February")
        case "3":
            print("The month is March")
        case "4":
            print("The month is April")
        case "5":
            print("The month is May")
        case "6":
            print("The month is June")
        case "7":
            print("The month is July")
        case "8":
            print("The month is August")
        case "9":
            print("The month is September")
        case "10":
            print("The month is October")
        case "11":
            print("The month is November")
        case "12":
            print("The month is December")
            # Any other number or input will trigger this.
        case _:
            print("Invalid input.")


# This just runs our program.
if __name__ == "__main__":
    month_match()
