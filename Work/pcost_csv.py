# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    if(type(filename) == str):
        try:
            with open(filename) as file:
                total_cost = 0
                rows = csv.reader(file)
                headers = next(rows)
                for rown, row in enumerate(rows):
                    record = dict(zip(headers, row))
                    try:
                        nshares = int(record['shares'])
                        price = float(record['price'])
                        total_cost += nshares*price
                    except ValueError:
                        print(f"Row {rown}: Bad row: {row}")
            return total_cost
        except FileNotFoundError:
            print("Error: File Not found")
        except ValueError:
            print("Error: Enter Valid file adress")
    else:
        print("Opps, somethig is wrong")

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '.\Data\portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")