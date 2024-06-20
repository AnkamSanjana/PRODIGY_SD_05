import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website
url = 'https://www.amazon.com/s?k=python+books'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product listings
products = soup.find_all('div', {'data-component-type': '-search-result'})

# Create a list to store the product data
product_data = []

# Iterate over the product listings
for product in products:
    # Extract the product name
    name = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()

    # Extract the product price
    price = product.find('span', {'class': 'a-price-whole'}).text.strip()

    # Extract the product rating
    rating = product.find('span', {'class': 'a-icon-alt'}).text.strip()

    # Append the product data to the list
    product_data.append([name, price, rating])

# Print the product data to the console
print("Product Data:")
print("------------")
for product in product_data:
    print(f"Name: {product[0]}, Price: {product[1]}, Rating: {product[2]}")

# Write the product data to a CSV file
with open('product_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Price', 'Rating'])
    writer.writerows(product_data)

print("Product data saved to product_data.csv")