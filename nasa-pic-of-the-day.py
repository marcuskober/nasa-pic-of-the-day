import requests
from bs4 import BeautifulSoup
import os
from datetime import date

# Define the URL of the NASA image of the day website
url = 'https://apod.nasa.gov/apod/'

# Send a GET request to the website and get the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the link to the highest resolution image
link_element = soup.find('a', {'href': lambda href: href and href.endswith('.jpg')})

# Get the URL of the highest resolution image
image_url = url + link_element['href']

today = date.today()
filename = 'nasa_image-' + today.strftime("%Y%m%d") + '.jpg'

# Download the image to a file
response = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Set the desktop background using osascript
os.system('osascript -e "tell application \\"Finder\\" to set desktop picture to POSIX file \\"' + os.path.abspath(filename) + '\\""')

