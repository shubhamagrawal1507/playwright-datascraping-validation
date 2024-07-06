# Playwright Country Data Scraper and Validator

## Description

This project is a web scraping and data validation tool built with Playwright, pytest, and pandas. It scrapes country data (such as names, capitals, and currencies) from a specified website and validates it against expected results. The project follows the Page Object Model (POM) design pattern for better maintainability and readability.

## Features

- Scrapes country data from a website
- Validates scraped data against expected results stored in a CSV file
- Generates detailed HTML test reports using pytest-html
- Automatically reruns failed tests to ensure robustness

## Project Structure

country_scraper/
│
├── data/
│ ├── expected_results.csv # Expected data for validation
│ └── scraped_data.csv # Scraped data from the website
│
├── pages/
│ └── country_page.py # Page Object Model for the country data page
│
├── reports/
│ └── test_report.html # HTML test report
│
├── tests/
│ └── test_country_data.py # Test script for scraping and validation
│
├── src/
│ ├── data_loader.py # Utility functions for loading and saving data
│ └── validation.py # Utility functions for data validation
│
├── README.md # Project documentation
|
├── requirements.txt # List of Python dependencies
|
└── pytest.ini # Pytest configuration file



## Installation

-Clone the repository:
   git clone https://github.com/yourusername/country-data-scraper.git

-Install the dependencies:

    pip install -r requirements.txt
    playwright install

## Usage

-Run the tests:
    python -m pytest

-View the HTML report:
    After running the tests, open reports/test_report.html in your web browser to view the detailed test report.


