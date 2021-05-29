
### DEPENDENCIES ###
import pandas as pd
import re
import json


### INPUTS ###
numberOfReviews =    # number of reviews in .csv file outputted by Etsy
numberOfOrders =    # number of orders in .csv file outputted by Etsy


# Replace all runs of whitespace with a single dash (syntax for shopify product catalogue upload)
def urlify(s):
    s = re.sub(r"\s+", '-', s)
    return s


# reads reviews xls and imports order IDs into a list
reviews = pd.read_excel (r'[INSERT FILE PATH]')
reviews_order_id_list = []
for i in range(numberOfReviews):
    reviews_order_id_list.append(reviews.iat[i, 4])


# reads orders xls and imports order IDs into a list
orders = pd.read_excel (r'[INSERT FILE PATH]')
orders_order_id_list = []
for i in range(numberOfOrders):
    orders_order_id_list.append(orders.iat[i, 5])


# matches order IDs and stores corresponding product name in a list
product_names_list = []
for order in reviews_order_id_list:
    try:
        row = orders_order_id_list.index(order)
        product_names_list.append(orders.iat[row,3])
    except:
        continue


final_list = []
for element in product_names_list:
    almost = urlify(element)
    done = almost.replace("---","-")
    final_list.append(done)


# saves list to .json file for easy import in to .csv files commonly used for product catalogue importing
with open('product_names.json', 'w') as f:
    json.dump(final_list, f)
