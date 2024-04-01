# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename:str='.\Data\portfolio.csv') -> list[dict]:
    if(type(filename) == str):
        try:
            with open(filename) as file:
                portfolio = []
                rows = csv.reader(file)
                headers = next(rows)
                for share in rows:
                    if share:
                        record = dict(zip(headers, share))
                        if 'shares' in record:
                            record['shares'] = int(record['shares'])
                        if 'price' in record:
                            record['price'] = float(record['price'])
                        portfolio.append(record)
            return portfolio
        except FileNotFoundError:
            print("Error: File Not found")
        except ValueError:
            print("Error: Enter Valid file address")
    else:
        print("Oops, something is wrong")


def read_prices(filename:str= '.\Data\prices.csv') -> dict:
    if(type(filename) == str):
        try:
            with open(filename) as file:
                prices = {}
                rows = csv.reader(file)
                for share in rows:
                    if share:
                        prices[share[0]] = float(share[1])
            return prices
        except FileNotFoundError:
            print("Error: File Not found")
        except ValueError:
            print("Error: Enter Valid file address")
    else:
        print("Oops, something is wrong")

def gain_loss(portfolio:list[dict], current_price:dict) -> dict:
    '''
    Calculate the gain/loss in a portfolio based on current prices
    Inputs:
        portfolio: A list containing each share as on object with
                  ['name','shares', 'price'] as keys.
        current prices: A dictionary containing each share name as key
                        and current price ass its value
    Return:
        The function return a dictionary with share name as keys and gain/loss
        as it's value (negative value mean loss). 
    '''
    gain = {}
    for item in portfolio:
        share = item['name']
        if share in current_price:
            gain[share] = current_price[share] -item['price']
    return gain


def make_report(stocks:list[dict], prices:dict) -> list[tuple]:
    report = []
    headers = tuple(list(stocks[0].keys()) + ["change"])
    report.append(headers)
    for item in stocks:
        name = item['name']
        if name in prices:
            item['change'] = float(item['price']) - prices[name]
        else:
            item['change'] = '-'
        report.append( tuple([rec[1] for rec in item.items()]) )
    return report

def print_report(report, headers = True):
    if headers:
        header = report[0]
        del report[0]
        for h in header:
            print(f"{h:^10s} ", end="")
        print(f"\n{(('-'*10)+ ' ')*len(header)}")
    for record in report:
        for item in record:
            if type(item) == str:
                print(f"{item:^10s} ", end="")
            elif type(item) == int:
                print(f"{item:<10d} ", end="")
            else:
                print(f"{item:<10.2f} ", end="")
        print()

def portfolio_report(portfolio_filename:str = '.\Data\portfolio.csv', prices_filename:str = '.\Data\prices.csv'):
    if len(sys.argv) == 2:
        portfolio_filename = sys.argv[1]
    elif len(sys.argv) == 3:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
    else:
        portfolio_filename = '.\Data\portfolio.csv'
        prices_filename = '.\Data\prices.csv'

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report(portfolio_filename= '.\Data\portfolio.csv', prices_filename = '.\Data\prices.csv')
