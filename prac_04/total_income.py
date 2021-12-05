"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """
    Display income report for incomes over a given number of months.
    """
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(number_of_months):
        income = float(input("Enter income for month " + str(month + 1) + ": "))
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """
    Print income report.
    """
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


main()
