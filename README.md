# stock-tickers
List of all stock ticker symbols - updated daily at midnight EST.

# Description
Pulls all data from old.nasdaq.com nightly, generates ticker symbol files, then pushes changes to github.

# Usage
    $ wget https://github.com/abbadata/stock-tickers/blob/main/data/allsymbols.txt
(or whichever file you're interested in)

OR

clone the project and
    $ python tickerlist.py

# Files
Ticker symbol list. Sorted and contains no duplicates.
- data/allsymbols.txt

The following ticker symbol files are pulled verbatim from nasdaq.com. Contains additional fields such as company name, market cap, etc.
- data/nasdaq.csv : pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
- data/amex.csv : pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download
- data/nyse.csv : pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download

Combination of the above files.
- data/all.csv : all 

# Dependencies
All data is currently pulled from old.nasdaq.com . If it is no longer available there, this will need to grab data from somewhere else.

# Disclaimer
No guarantees are made about accuracy or up-to-dateness of the data.
