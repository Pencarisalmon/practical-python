#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
import sys
import report


def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''

    return report.read_portfolio(filename).total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    print('Total cost:', portfolio_cost(args[1]))


if __name__ == '__main__':
    main(sys.argv)
