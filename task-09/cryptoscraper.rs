
extern crate csv;
extern crate reqwest;

use select::document::Document;
use select::predicate::{Class, Name};

fn main() {
    // Set the URL of the page to scrape
    let url = "https://www.crypto.com/coins/";

    // Send an HTTP request to the URL and retrieve the response
    let resp = reqwest::get(url);
    assert!(resp.status().is_success());

    // Parse the HTML from the response
    let document = Document::from_read(resp).unwrap();

    // Create a new CSV writer
    let mut writer = csv::Writer::from_path("cryptocurrencies.csv").unwrap();

    // Write the header row
    writer.write_record(&["NAME", "PRICE", "24H CHANGE", "24H VOLUME", "MARKET CAP"]).unwrap();

    // Get the table of cryptocurrencies
    let table = document.find(Class("cmc-table__table-wrapper-outer")).next().unwrap();

    // Iterate over the rows of the table
    for row in table.find(Name("tr")) {
        // Get the cells of the row
        let cells = row.find(Name("td"));

        // Get the name and price of the cryptocurrency
        let name = cells.next().unwrap().text();
        let price = cells.next().unwrap().text();

        // Skip rows without a name and price (these are the header and footer rows)
        if name.is_empty() || price.is_empty() {
            continue;
        }

        // Get the 24-hour change, 24-hour volume, and market cap of the cryptocurrency
        let change = cells.skip(1).next().unwrap().text();
        let volume = cells.skip(1).next().unwrap().text();
        let market_cap = cells.skip(1).next().unwrap().text();

        // Write the data as a record in the CSV file
        writer.write_record(&[name, price, change, volume, market_cap]).unwrap();
    }

    // Flush the writer to ensure all data is written to the CSV file
    writer.flush().unwrap();
}

