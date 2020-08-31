"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    given_month = int(input("How many months? "))

    for month in range(1, given_month + 1):
        income = float(input("Enter income for month {}: ").format(str(month)))
        incomes.append(income)

    income_report(given_month, incomes)


def income_report(given_month, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, given_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
