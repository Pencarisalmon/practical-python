# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                totalSaham = int(row[1])
                hargaSaham = float(row[2])
                total_cost += totalSaham * hargaSaham
        return total_cost
    except ValueError:
        print("Warning")


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
