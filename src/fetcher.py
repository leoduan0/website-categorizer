from bs4 import BeautifulSoup
import requests


def get_website_html(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        return html
    else:
        return ""


def get_website_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text().strip().lower()

    return text
