from tax import calculate_tax
from loan import calculate_emi

def main():
    print("Welcome to the Finance App!\n")

    # Tax calculation
    try:
        income = float(input("Enter your annual income: "))
        tax_rate = float(input("Enter tax rate (%): "))
        tax = calculate_tax(income, tax_rate)
        print(f"Your tax amount is: Rs {tax:.2f}\n")
    except ValueError:
        print("Invalid income or rate input.\n")

    # EMI calculation
    try:
        principal = float(input("Enter loan amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter loan time in years: "))
        emi = calculate_emi(principal, rate, time)
        print(f"Your monthly EMI is: Rs {emi:.2f}")
    except ValueError:
        print("Invalid loan input.")

main()
