#! python3
# webscrape.py

from get_data import get_data
from parse_nike import parse_nike_data
from parse_amazon import parse_amazon_data

def present_prices(keyword, number):
    get_data(keyword)
    parse_amazon_data(number)
    parse_nike_data(number)

if __name__ == '__main__':
	mykeyword = raw_input("Please enter a keyword to search: ")
	mynumber =  raw_input("Please enter the number of search results you want to see: ")
	present_prices(mykeyword, mynumber)
	print ('*'*80)
