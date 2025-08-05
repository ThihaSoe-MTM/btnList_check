import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL
url = "https://artoftesting.com/samplesiteforselenium"

# Step 2: Fetch the page content
response = requests.get(url)
html_content = response.text

# Step 3: Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find only real button elements
buttons = soup.find_all(['button', 'input'])

# Step 5: Filter input elements to only button types
real_buttons = []
for tag in buttons:
    if tag.name == 'input' and tag.get('type') not in ['button', 'submit']:
        continue
    real_buttons.append(tag)

# Step 6: Print formatted output
print(f"Total buttons found: {len(real_buttons)}\n")

for i, btn in enumerate(real_buttons, start=1):
    print(f"Button {i}:")
    print(f"  Tag: <{btn.name}>")
    print(f"  Text: {btn.get_text(strip=True) if btn.name == 'button' else btn.get('value')}")
    print(f"  Attributes: {btn.attrs}")
    print("-" * 40)
