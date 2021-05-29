# Etsy-Product-Review-Matcher


THE PROBLEM:

Whilst attempting to import product reviews from Etsy to my newly created Shopify store, it quickly became apparent that there was no free or cheap way to do so.
Shopify does however, allow you to import reviews from other sales channels through uploading a specificly formatted .csv file.
However, the specific format of said file does not match with data able to be exported from Etsy.

THE SOLUTION:

Etsy can export shop reviews paired with order numbers but does not include the product being reviewed.
Etsy can also, separately, export all orders, linking order numbers to product names.
The software presented in this repository matches Etsy reviews to product names through order numbers using the standard .csv files outputted by Etsy. 
It then formats the data to conform with Shopify's review importer requirements.


