**Final Capstone Project — Python Beginner Course**

Introduction

This project is a **web‑scraping automation tool** developed as part of the **Final Capstone Project for the Python Beginner Course**. It demonstrates practical skills in HTTP requests, HTML parsing, data extraction, error handling, and exporting structured data to Excel.

The script scrapes product information from the **City Mall Myanmar** website, automatically navigating through all pages in a category. It extracts:

- Product Name  
- Current Price  
- Sale Price  
- Original Price  

Using **BeautifulSoup**, the scraper parses HTML content and handles messy price formats with custom cleaning logic. It also uses a persistent `requests.Session()` with retry logic to ensure stable scraping even when encountering rate limits or temporary server errors. A progress bar powered by **tqdm** provides real‑time feedback during scraping.

After collecting all product data, the script compiles everything into a **pandas DataFrame** and exports it to an Excel file with a timestamped filename.

This project showcases essential Python skills:

- Web scraping with `requests` and `BeautifulSoup`
- Data cleaning and transformation
- Retry and session handling
- Pagination automation
- Progress visualization
- Excel export using `pandas`
- Clean, modular code with reusable functions

---

Installation

Follow these steps to set up the project:

1. Clone or download the repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

2. Create a virtual environment**
```bash
python3 -m venv venv
```

3. Activate the virtual environment**
```bash
source venv/bin/activate
```

4. Install dependencies**
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, generate one with:
```bash
pip freeze > requirements.txt
```

Required packages:
- requests  
- beautifulsoup4  
- html5lib  
- pandas  
- tqdm  
- openpyxl  

---

▶️ Usage

Run the scraper with:

```bash
python main.py
```

The script will:

1. Start scraping from the initial City Mall category URL  
2. Automatically follow the “Next” button across all pages  
3. Extract product names and pricing  
4. Display progress with a loading bar  
5. Save results to an Excel file named:

```
Output HH-MM-SS.xlsx
```

Each run generates a unique timestamped file.

---

Features

Multi‑Page Scraping  
Automatically detects and follows pagination links.

Robust HTTP Handling  
Retry logic prevents failures from temporary server issues.

Clean Price Extraction  
Removes commas, currency labels, and whitespace.

Excel Export  
Outputs clean, structured data ready for analysis.

Progress Visualization  
`tqdm` progress bars show scraping progress in real time.

Maintainable Code  
Functions like `clean_price()` and `extract_product_info()` keep logic modular and easy to extend.

Project Structure

```
project-folder/
│
├── main.py                 # Main scraping script
├── requirements.txt        # Python dependencies
├── venv/                   # Virtual environment (optional)
│
└── README.md               # Project documentation
```

Key Components**

| Component | Description |
|----------|-------------|
| `main.py` | Handles scraping, pagination, retries, and Excel export |
| `clean_price()` | Cleans and converts price strings |
| `extract_product_info()` | Extracts product name and pricing from HTML |
| `requests.Session()` | Ensures stable HTTP communication |
| `pandas.DataFrame()` | Stores and structures scraped data |
| `tqdm` | Displays progress bars |


