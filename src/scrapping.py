
from bs4 import BeautifulSoup
from selenium import webdriver
import hashlib
import io
from pathlib import Path
import pandas as pd
from PIL import Image
import requests
import os

def get_content_from_url(url):
   driver = webdriver.Chrome()  # Add "executable_path=" if the driver is in a custom directory.
   driver.get(url)
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   page_content = driver.page_source
   driver.quit()  # You don't need the browser instance for further steps.
   return page_content


def parse_image_urls(content, classes, location, source):
    soup = BeautifulSoup(content,features="html.parser")
    results = []
    for a in soup.findAll(attrs={"class": classes}):
       name = a.find(location)
       if name not in results:
           results.append(name.get(source))
    print("classes : ",classes)
    return results


def save_urls_to_csv(image_urls):
    csv_file_path = "links.csv"

    if os.path.exists(csv_file_path):
        # If the CSV file already exists, read the existing data
        df_existing = pd.read_csv(csv_file_path)
        existing_urls = set(df_existing["links"])

        # Append new unique URLs to the existing data
        new_urls = [url for url in image_urls if url not in existing_urls]
        df_new = pd.DataFrame({"links": new_urls})
        df_updated = pd.concat([df_existing, df_new], ignore_index=True).drop_duplicates()

        # Save the updated data back to the same file
        df_updated.to_csv(csv_file_path, index=False, encoding="utf-8")
    else:
        # If the CSV file doesn't exist, create a new one
        df = pd.DataFrame({"links": image_urls})
        df.to_csv(csv_file_path, index=False, encoding="utf-8")


def get_and_save_image_to_file(image_url, output_dir):
    if image_url is None:
        print("Skipping None URL")
        return

    response = requests.get(image_url, headers={
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"})

    if response.status_code == 200:
        image_content = response.content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        filename = hashlib.sha1(image_content).hexdigest()[:10] + ".png"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_path = output_dir / filename
        image.save(file_path, "PNG", quality=80)
    else:
        print(f"Failed to fetch image from URL: {image_url}, Status Code: {response.status_code}")


def scrapp():
    for i in range(1,20):
       url = f"https://www.etsy.com/fr/search?q=painting+in+living+room&page={i}&ref=pagination"
       print(f"Scraping URL: {url}")
       content = get_content_from_url(url)
       image_urls = parse_image_urls(
           content=content, classes="v2-listing-card__img wt-position-relative", location="img", source="src",
       )
       save_urls_to_csv(image_urls)

       for image_url in image_urls:
           get_and_save_image_to_file(
               image_url, output_dir=Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images/")),
           )

