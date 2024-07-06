def validate_data(scraped_data, expected_data):
    
    for index, row in expected_data.iterrows():
        country = row['Country']
        capital = row['Capital(s)']
        currency = row['Currency']
        language = row['Primary Language(s)']   

        scraped_row = scraped_data[scraped_data['Country'] == country]
        
        assert not scraped_row.empty, f"Country {country} not found in scraped data"
        assert scraped_row['Capital(s)'].values[0] == capital, f"Capital for {country} is incorrect"
        assert scraped_row['Currency'].values[0] == currency, f"Currency for {country} is incorrect"
        assert scraped_row['Primary Language(s)'].values[0] == language, f"Primary Language(s) for {country} is incorrect"
