#! python3
# parse_nike.py

import bs4

def parse_nike_data(number):

    char1 = '>'
    char2 = '<'

    soupNike = bs4.BeautifulSoup(open("nike.html"), "lxml")
    nameElemsNike = soupNike.select('p.product-display-name')
    priceElemsNike = soupNike.select('span.local.nsg-font-family--base')
    typeElemsNike = soupNike.select('p.product-subtitle')

    nike_price_class = [str(i) for i in priceElemsNike]
    nike_type_class = [str(i) for i in typeElemsNike]
    nike_name_class = [str(i) for i in nameElemsNike]

    nike_price = [i.partition(char1)[-1].rpartition(char2)[0] \
    for i in nike_price_class]
    nike_type = [i.partition(char1)[-1].rpartition(char2)[0] \
    for i in nike_type_class]
    nike_name = [i.partition(char1)[-1].rpartition(char2)[0] \
    for i in nike_name_class]

    print ('*'*80)
    print ('*'*80)

    if int(number) > int(len(nike_name)):
        number = len(nike_name)
    print ('Displaying top %s results from nike.com' %number)
    
    if len(nike_name) == 0:
        print ('*'*40)
        print ("No search results for the keyword. Please try again.")
    else:
        for i in range(int(number)):
            print ('*'*40)
            print ('Name: %s' %nike_name[i])
            print ('Price: %s' %nike_price[i])
            print ('Type: %s' %nike_type[i])

