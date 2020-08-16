import requests
from bs4 import BeautifulSoup

code = "088980"


def get_current_price(code):

    url = f"http://asp1.krx.co.kr/servlet/krx.asp.XMLSiseEng?code={code}"

    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        soup = BeautifulSoup(text, "html.parser")
        day_endprice = soup.find("dailystock")["day_endprice"]
        return day_endprice
    else:
        return 0


if __name__ == "__main__":
    get_current_price(code)
