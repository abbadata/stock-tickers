import sys
import requests
import csv
import traceback


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

NASDAQFILE = "data/nasdaq.csv"
AMEXFILE = "data/amex.csv"
NYSEFILE = "data/nyse.csv"
ALLFILE = "data/all.csv"
ALLSYMBOL_FILE = "data/allsymbols.txt"

class ResponseError(Exception):
    pass

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def create_file_from_url(outfile, url):
    r = requests.get(url, headers=headers)

    # check if we're actually getting the csv file
    if (r.status_code != 200):
        raise ResponseError("Bad server response from url. url=" + url)
    if (r.headers["Content-Type"] != "application/text"):
        raise ResponseError("Response likely not in CSV format. url=" + url)

    with open(outfile, 'wb') as f:
        f.write(r.content)
    return r.content

def get_symbols_from_file(file):
    symbols = []
    lines = []
    with open(file, newline='') as csvfile:
        symbolreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        # assuming there's always a header line
        next(symbolreader)
        for row in symbolreader:
            symbols.append(row[0])
            lines.append(','.join(['"' + i + '"' for i in row]))
            #print(row[0])
    return symbols, lines

def get_all_tickers():
    all_lines = []
    all_symbols = []
    create_file_from_url(NASDAQFILE, "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download")
    create_file_from_url(AMEXFILE, "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download")
    create_file_from_url(NYSEFILE, "https://old.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download")

    symbols, lines = get_symbols_from_file(NASDAQFILE)
    all_lines.extend(lines)
    all_symbols.extend(symbols)
    symbols, lines = get_symbols_from_file(NYSEFILE)
    all_lines.extend(lines)
    all_symbols.extend(symbols)
    symbols, lines = get_symbols_from_file(AMEXFILE)
    all_lines.extend(lines)
    all_symbols.extend(symbols)

    all_symbols = sorted(set(all_symbols))
    with open(ALLFILE, 'w', newline='\n') as f:
        for line in all_lines:
            f.write(line)
            f.write('\n')

    with open(ALLSYMBOL_FILE, 'w', newline='\n') as f:
        for line in all_symbols:
            f.write(line)
            f.write('\n')


if __name__ == "__main__":
    try:
        get_all_tickers()
    except Exception as e:
        eprint(e)
        traceback.print_exc()
