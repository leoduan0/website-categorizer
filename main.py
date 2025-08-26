import argparse
import json
from pathlib import Path

from src.classifier import classify_text
import src.db as db
from src.fetcher import get_website_html, get_website_text


def main():
    parser = argparse.ArgumentParser(
        prog="Website Categorizer",
        description="The Website Categorizer (WC) scrapes websites, analyzes the site content using AI, and then categorizes them.",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to JSON file containing the website URLs",
    )
    parser.add_argument(
        "-l",
        "--limit",
        help="Set the maximum number of sites to classify from the input.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print("Whomp. File doesn't exist.")
        return

    with input_path.open("r", encoding="utf8") as input_file:
        urls_json = json.load(input_file)

    urls = []
    for site in urls_json:
        domain = site.get("domain")
        urls.append(domain)

    db.init_db()

    for i, url in enumerate(urls):
        if args.limit:
            if i > int(args.limit) - 1:
                return

        print(f"{i}: {url}")

        html = get_website_html(url)
        text = get_website_text(html)
        if text == "":
            print(f"{url} returned no text to analyze.")
            pass
        pred = classify_text(text)

        db.save_result(url, pred)

    print("Done")


if __name__ == "__main__":
    main()
