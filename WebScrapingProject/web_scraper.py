import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
service = Service('C:/Users/sacho/OneDrive/Desktop/webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get('https://oxylabs.io/blog')

# Get the page content
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

# Extract data
results = []
other_results = []
for element in soup.findAll(attrs={'class': 'blog-card__content-wrapper'}):
    name = element.find('h2')
    if name and name.text not in results:
        results.append(name.text)

for element in soup.findAll(attrs={'class': 'blog-card__date-wrapper'}):
    date = element.find('p')
    if date and date.text not in other_results:
        other_results.append(date.text)

# Print extracted names and dates to verify
print("Extracted Names:")
for name in results:
    print(name)

print("\nExtracted Dates:")
for date in other_results:
    print(date)

# Save the data to a CSV file
df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
print("Data saved to names.csv")
