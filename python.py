import requests
from bs4 import BeautifulSoup
import csv

# URL to be scraped
url = 'https://www.amazon.com/s?k='

# Search keyword
keyword = 'laptop'

# Number of products to scrape
num_products = 2000

# Set up headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Create a CSV file and write the headers
with open('products.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Product Title', 'Price', 'Rating', 'Reviews', 'Product Description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Scrape the product data
    count = 0
    for i in range(1, 21):
        page_url = url + keyword + '&page=' + str(i)
        page = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Extract product details from the page
        products = soup.find_all('div', {'class': 's-result-item'})
        for product in products:
            count += 1
            if count > num_products:
                break

            # Here we are extracted required date, such as product title, price, rating, reviews, and product description
            try:
                title = product.find('h2', {'class': 'a-size-mini'}).text.strip()
            except:
                title = ''

            try:
                price = product.find('span', {'class': 'a-offscreen'}).text.strip()
            except:
                price = ''

            try:
                rating = product.find('span', {'class': 'a-icon-alt'}).text.strip()
            except:
                rating = ''

            try:
                reviews = product.find('span', {'class': 'a-size-base'}).text.strip()
            except:
                reviews = ''

            try:
                desc_url = 'https://www.amazon.com' + product.find('a', {'class': 'a-link-normal'})['href']
                desc_page = requests.get(desc_url, headers=headers)
                desc_soup = BeautifulSoup(desc_page.content, 'html.parser')
                description = desc_soup.find('div', {'id': 'productDescription'}).text.strip()
            except:
                description = ''

            # Write the extracted data to the CSV file
            writer.writerow({'Product Title': title, 'Price': price, 'Rating': rating, 'Reviews': reviews, 'Product Description': description})

        if count > num_products:
            break
