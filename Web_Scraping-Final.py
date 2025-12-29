import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pandas as pd
from datetime import datetime
from tqdm import tqdm
import time

#remove comma, blank & ks from the price
def clean_price(text):
    """Clean and convert a price string to int, or None."""
    try:
        return int(text.replace(",", "").replace("Ks", "").strip())
    except:
        return None

def extract_product_info(dm_tag):
    """Extract product name & prices from a product card."""
    # Extract product name
    pd_name_tag = dm_tag.find('a', class_='name')
    if pd_name_tag:
        pd_name = pd_name_tag.text.strip()  
    else:
        pd_name = None
        
    # Extract price tags
    pd_price_tag = dm_tag.find('p', class_='product-price mt-1')

    sale_price = None
    original_price = None
    price_only = None

    if pd_price_tag:
        sale_tag = pd_price_tag.find('span', class_='product-sale-price')
        original_tag = pd_price_tag.find('span', class_='product-original-price')

        # Both sale + original price exist
        if sale_tag and original_tag:
            sale_price = clean_price(sale_tag.text.strip())
            original_price = clean_price(original_tag.text.strip())
        else:
            # Only one price exists
            price_only = clean_price(pd_price_tag.text.strip())

    return{
        "Name": pd_name,
        "Sale_price": sale_price,
        "Original_price": original_price,
        "Current_Price": price_only
        }

def main ():
    results = [] #storage list for excel
    page_num = 1
    url = "https://www.citymall.com.mm/citymall/my/c/id05011"
    
    headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
             "AppleWebKit/537.36 (KHTML, like Gecko)"
             "Chrome/120.0.0.0 Safari/537.36",
             "Accept-Encoding": "identity"
             }
    
    session = requests.Session()

    retry = Retry(
           total=5,
           backoff_factor=1,
           status_forcelist=[429, 500, 502, 503, 504]
           )

    session.mount("https://", HTTPAdapter(max_retries=retry))

    response = session.get(url, headers=headers, timeout=30)

    print(response.status_code)

    soup = BeautifulSoup(response.text, "html5lib")
    
    while url:  # loop until no "Next" page
        print(f"Scraping page {page_num}")
        response = session.get(url, headers=headers, timeout=30)
        soup = BeautifulSoup(response.text, "html5lib")
        
        #find main div tags
        main_tag = soup.find_all('div',class_='product-info')
                   
        for dm_tag in tqdm(main_tag):
            product = extract_product_info(dm_tag)
            results.append({
                "Product Name": product["Name"],
                "Current Price": product["Current_Price"],
                "Sale Price": product["Sale_price"],
                "Original Price": product["Original_price"],
            })
            
        # Find the "Next" button
        """Scrape all pages of a category starting from start_url."""
        next_link = soup.find("a", class_="page-link next")
        if next_link:
            next_href = next_link.get("href")                       
            if next_href.startswith("http"):
                url = next_href
            else:
                url = "https://www.citymall.com.mm" + next_href    
        else:
            url = None  # stop loop
        page_num += 1
        time.sleep(0.10)

    # Create a dataframe
    df = pd.DataFrame(results)

    # Create filename version
    time_str = datetime.now().strftime("%H-%M-%S")
    print(time_str)

    df.to_excel("Output " + time_str + ".xlsx", index=False)

    print("All steps are completed!")
    
# Run main only when executed directly
if __name__ == "__main__":
    main()