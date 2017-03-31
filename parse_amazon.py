#! python3
# parse_amazon.py

import bs4

def parse_amazon_data(number):

    soupAmazon = bs4.BeautifulSoup(open("amazon.html"), "lxml")
    rows = soupAmazon.select('div.s-item-container')

    range_price = soupAmazon.find_all("span", "sx-price-whole")

    # Initialize lists
    matched_rows = []
    prices = []
    ratings = []
    descs = []

    for i in range(len(rows)):
        temp_string = str(rows[i])
        if "sx-price-whole" in temp_string:
            matched_rows.append(rows[i])

    for card in matched_rows:
        price = card.find_all("span", "sx-price-whole")
        rating = card.find_all("a", "a-popover-trigger")
        desc_h2 = card.find_all("h2",{"data-attribute":True})
        for des in desc_h2:
            desc = des["data-attribute"]

        prices.append(str(price))
        ratings.append(str(rating))
        descs.append(desc.encode('ascii', errors='ignore'))
    
    char1 = '>'
    char2 = '</span>,'
    char3 = ', <span class="sx-price-whole">'
    char4 = '</span>]'

    amazon_price_string = []
    amazon_rating_string = []

    for i in prices:
       if len(i) > 60:
        lower = i.partition(char1)[-1].rpartition(char2)[0]
        higher = i.partition(char3)[-1].rpartition(char4)[0]
        amazon_price_string.append(str("$"+lower+"-"+"$"+higher))
       else:
        indv = i.partition(">")[-1].rpartition("<")[0]
        amazon_price_string.append(str("$"+indv))

    for j in ratings:
        rate = j.partition('<span class="a-icon-alt">')[-1].rpartition('</span></i><i class="a-icon a-icon-popover">')[0]
        amazon_rating_string.append(rate)

    for i in range(len(amazon_rating_string)):
        if amazon_rating_string[i] == '':
            amazon_rating_string[i] = "No ratings."

    print ('*'*80)
    print ('*'*80)
    if int(number) > int(len(descs)):
        number = len(descs)
    print ('Displaying top %s results from amazon.com' %number)

    if len(descs) == 0:
        print ('*'*40)
        print ("No search results for the keyword. Please try again.")
    else:
        for i in range(int(number)):
            print ('*'*40)
            print ('Name: %s' %descs[i])
            print ('Price: %s' %amazon_price_string[i])
            print ('Rating: %s' %amazon_rating_string[i])
