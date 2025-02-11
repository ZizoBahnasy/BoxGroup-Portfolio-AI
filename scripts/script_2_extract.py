from bs4 import BeautifulSoup
import json
import requests
import time
import os

def extract_companies():
    # Define data path
    base_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_path, 'data')
    
    # Create data directory if it doesn't exist
    os.makedirs(data_path, exist_ok=True)
    
    companies = []
    seen_urls = set()  # Track unique URLs to prevent duplicates
    page = 1
    consecutive_duplicate_pages = 0  # Track pages that add no new companies
    
    while True:
        url = f"https://www.boxgroup.com/portfolio?8fdb4535_page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Track how many new companies we find on this page
        new_companies_count = 0
        
        # Find all portfolio items
        portfolio_items = soup.find_all('div', class_='port_tabs-item')
        
        if not portfolio_items:
            break
            
        for item in portfolio_items:
            link = item.find('a', class_='port_tabs-item_link')
            if link:
                company_url = link.get('href')
                # Skip if we've seen this URL before
                if company_url in seen_urls:
                    continue
                    
                seen_urls.add(company_url)
                new_companies_count += 1
                
                company = {
                    'name': company_url.replace('https://', '').replace('http://', '').split('/')[0],
                    'url': company_url,
                    'is_ipo': bool(item.find('div', class_='port_tabs-ipo') and 
                                 not 'w-condition-invisible' in item.find('div', class_='port_tabs-ipo').get('class', [])),
                    'is_exit': bool(item.find('div', class_='port_tabs-acquired') and 
                                  not 'w-condition-invisible' in item.find('div', class_='port_tabs-acquired').get('class', [])),
                    'is_boxgroup_office': bool(item.find('div', class_='port_tabs_box-office') and 
                                             not 'w-condition-invisible' in item.find('div', class_='port_tabs_box-office').get('class', []))
                }
                companies.append(company)
        
        print(f"Extracted page {page} - Found {new_companies_count} new companies")
        
        # If we didn't find any new companies on this page
        if new_companies_count == 0:
            consecutive_duplicate_pages += 1
        else:
            consecutive_duplicate_pages = 0
            
        # If we've seen 2 pages in a row with no new companies, we're done
        if consecutive_duplicate_pages >= 2:
            break
            
        page += 1
        time.sleep(1)

    # Save to JSON file
    output_path = os.path.join(data_path, 'portfolio_1_extracted.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(companies, f, indent=2)

    print(f"Extracted {len(companies)} unique companies to {output_path}")

if __name__ == "__main__":
    extract_companies()