# stock-tickers
List of all stock ticker symbols - updated daily at midnight EST.

# Description
Pulls all data from old.nasdaq.com nightly, generates ticker symbol files, then pushes changes to github.

# Usage
    $ wget https://github.com/abbadata/stock-tickers/blob/main/data/allsymbols.txt
(or whichever file you're interested in)

OR

clone the project and run it yourself using:
```
$ python tickerlist.py
```
Symbol files are created in data/ .

# Files
## Main symbol files
- [data/allsymbols.txt](https://github.com/abbadata/stock-tickers/blob/main/data/allsymbols.txt)
  - Ticker symbol list. Sorted and contains no duplicates.
- [data/nasdaqsymbols.txt](https://github.com/abbadata/stock-tickers/blob/main/data/nasdaqsymbols.txt)
  - Ticker symbol list for stock listed on Nasdaq. Sorted and contains no duplicates.
- [data/nysesymbols.txt](https://github.com/abbadata/stock-tickers/blob/main/data/nysesymbols.txt)
  - Ticker symbol list for stock listed on NYSE. Sorted and contains no duplicates.
- [data/amexsymbols.txt](https://github.com/abbadata/stock-tickers/blob/main/data/amexsymbols.txt)
  - Ticker symbol list for stock listed on AMEX. Sorted and contains no duplicates.

## The following ticker symbol files are pulled verbatim from nasdaq.com. Contains additional fields such as company name, market cap, etc.
- [data/nasdaq.csv](https://github.com/abbadata/stock-tickers/blob/main/data/nasdaq.csv)
  - List of all stock listed on Nasdaq. Pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
- [data/amex.csv](https://github.com/abbadata/stock-tickers/blob/main/data/amex.csv)
  - List of all stock listed on AMEX. Pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download
- [data/nyse.csv](https://github.com/abbadata/stock-tickers/blob/main/data/nyse.csv)
  - List of all stock listed on NYSE. Pulled verbatim from https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download

## Combination of nasdaq.csv, amex.csv, and nyse.csv . Still contains all fields.
- [data/all.csv](https://github.com/abbadata/stock-tickers/blob/main/data/all.csv)

# Dependencies
All data is currently pulled from old.nasdaq.com . If it is no longer available there, this will need to grab data from somewhere else.

# Disclaimer
This runs nightly from a cron job so assuming there are no problems, the data should generally be accurate and up-to-date. However, no guarantees can be made.

