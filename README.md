# Website Categorizer

Website Categorizer allows you to scrape and categorize websites.

## Usage

```sh
python3 main.py -i <input_file> -l <limit>
```

- `-i <input_file>`: path to JSON file containing a list of websites
- `-l <limit>`: number of sites from the input file to categorize

### Example

```sh
python3 main.py -i sites.json -l 10
```

This will scrape and categorize the first 10 sites from sites.json.
