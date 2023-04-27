# python_assessment


To fetch product data from Amazon based on a particular keyword search, we can use web scraping techniques. 
There are several Python libraries available to perform web scraping, such as BeautifulSoup and Scrapy. For this task, we will be using the BeautifulSoup library.




In this code, we first set the URL of Amazon and the search keyword. We also set the number of products to scrape. 
We then set up the headers for the request to simulate a web browser.

We create a CSV file and write the headers. We then loop through the pages of the search results and extract the required data from each product. We use try-except blocks to handle cases where the data is not available or the layout of the product page is different.
We then write the extracted data to the CSV file.
