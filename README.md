

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



# Etsy-Product-Review-Matcher


### THE PROBLEM:

Whilst attempting to import product reviews from Etsy to my client's newly created Shopify store, it quickly became apparent that there was no free or cheap way to do so.
Shopify does however, allow you to import reviews from other sales channels through uploading a specificly formatted .csv file.
Unfortunately, the specific format of said file does not match that of the data Etsy is able to export.

### THE SOLUTION:

Etsy can export shop reviews paired with order numbers but does not include the name of the product being reviewed.
Etsy can also, separately, export all orders, thus linking order numbers to product names.
The software presented in this repository matches Etsy reviews to product names through order numbers using the standard .csv files outputted by Etsy. 
It then formats the data to conform with Shopify's review importer requirements making migrating stores far easier and quicker.




### Development-Goals


🧰 Improve data structure handling using the Pandas library 

🤖 Ease e-commerce store migration





## Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)

  

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@TraderTDF](https://twitter.com/TraderTDF)

LinkedIn - [https://www.linkedin.com/in/RAMWatson/](https://www.linkedin.com/in/RAMWatson/)

Project Link: [https://github.com/Elisik/Etsy-Product-Review-Matcher](https://github.com/Elisik/Etsy-Product-Review-Matcher)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/RAMWatson/

