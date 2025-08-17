Crawling Project: Digikala Crawling
This project is a web scraper designed to extract product information from the Digikala website. The main goal is to collect specific data from product pages for analysis and review.

🚀 Features
Extracts key product information (name, price, discount, seller).

Ability to navigate through different category pages.

Stores extracted data in various formats (e.g., CSV, JSON).

(Optional) Error Handling and Retries.

🛠️ Technologies Used
In this section, list the technologies and libraries you have used in your project. For example:

Programming Language: Python 3.x

Main Scraping Library: (e.g., Scrapy, Beautiful Soup, Selenium, Requests)

Data Handling Library: (e.g., Pandas)

Virtual Environment: (e.g., venv, conda)

⚙️ Installation and Setup
To run this project locally, follow these steps:

Clone the repository:

```bash
git clone https://github.com/Saman-naruee/digikala_crawling.git
cd digikala_crawling
```

Create and activate a virtual environment:

```bash
python -m venv venv

On Windows
venv\Scripts\activate

On macOS/Linux
source venv/bin/activate
```

Install dependencies:
Create a file named requirements.txt and list the project's libraries in it. Then, install them using the following command:

```bash
pip install -r requirements.txt
```

If you are using a library like Selenium, be sure to mention the installation of the WebDriver for your browser as well.

▶️ How to Run
In this section, explain how the user should run your script.

Example for a simple Python script:

```bash
python main.py
```

Example for Scrapy projects:

```bash
scrapy crawl digikala_spider -o output.csv
```

Mention any input arguments or specific configurations required to run the project here.

🗂️ Project Structure
Display the overall structure of your project files and folders to help others understand your code more easily.

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
└── (Output files are stored here)
```

🤝 Contributing
If you would like to contribute to this project, please submit a Pull Request. We welcome any collaboration.

