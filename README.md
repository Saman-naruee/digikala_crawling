# Digikala Crawling Project

A web crawler designed to extract detailed product information from the Digikala website for analysis and review.

## 🚀 Features

- Extracts product details: name, price, discount, seller, and more.
- Navigates category pages and explores deep product listings.
- Stores results in multiple formats (CSV, JSON).
- Resilient scraping with error handling and retry logic.

## 🛠️ Technologies & Libraries

- **Programming Language:** Python 3.x
- **Scraping Libraries:** (Scrapy, Beautiful Soup, Selenium, Requests)
- **Data Handling:** Pandas
- **Virtual Environment:** venv or conda

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saman-naruee/digikala_crawling.git
   cd digikala_crawling
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   > Ensure you have a `requirements.txt` file listing necessary libraries.
   ```bash
   pip install -r requirements.txt
   ```
   If using Selenium, download the appropriate WebDriver for your browser.

## ▶️ Usage

- For a simple Python script:
  ```bash
  python src/main.py
  ```
- For a Scrapy project:
  ```bash
  scrapy crawl digikala_spider -o output.csv
  ```
- Adjust input arguments or configuration files as needed (see code comments for details).

## 🗂️ Project Structure

```
digikala_crawling/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── src/
│   ├── main.py
│   ├── scraper.py
│   └── utils.py
│
└── data/
    └── (Output files)
```

## 🤝 Contributing

Contributions are welcome! Please fork the repo, create your feature branch, and submit a Pull Request. For major changes, open an issue first to discuss what you would like to change.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📝 Contact

For questions or suggestions, open an issue or reach out via GitHub.
