#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from . import fileparse
from .portfolio import Portfolio
from . import tableformat


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''

    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    reports = []

    for s in portfolio:
        hold = (s.name, s.shares, prices[s.name],
                prices[s.name]-s.price)
        reports.append(hold)

    return reports


def print_report(report, format):
    format.headings(['Name', 'Shares', 'Price', 'Change'])

    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        format.row(rowdata)


def portfolio_report(filenamePort, filenamePrices, fmt='txt'):
    portfolio = read_portfolio(filenamePort)
    prices = read_prices(filenamePrices)
    report = make_report(portfolio, prices)
    format = tableformat.create_formatter(fmt)
    print_report(report, format)


def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(
        # Name of the log file (omit to use stderr)
        filename='app.log',
        filemode='w',                  # File mode (use 'a' to append)
        # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
        level=logging.WARNING,
    )

    main(sys.argv)
