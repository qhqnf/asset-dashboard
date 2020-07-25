import requests
import datetime
import re
import io
import pandas as pd


def get_stock_data():
    generate_otp_url = "http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&market_gubun=ALL&indx_ind_cd=&sect_tp_cd=ALL&isu_cdnm=%EC%A0%84%EC%B2%B4&isu_cd=&isu_nm=&isu_srt_cd=&secugrp=ST&stock_gubun=on&schdate=20200724&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp"

    yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
    yesterday = re.sub("[^0-9]", "", yesterday)

    headers = {"User-Agent": "Mozilla/5.0"}

    params = {
        "name": "fileDown",
        "filetype": "xls",
        "url": "MKD/04/0406/04060200/mkd04060200",
        "market_gubun": "ALL",
        "sect_tp_cd": "ALL",
        "isu_cdnm": "전체",
        "secugrp": "ST",
        "secugrp": "EF",
        "stock_gubun": "on",
        "schdate": yesterday,
        "pagePath": "/contents/MKD/04/0406/04060200/MKD04060200.jsp",
    }

    otp = requests.get(generate_otp_url, headers=headers)

    print(otp.text)
    headers.update({"Referer": "http://marketdata.krx.co.kr/mdi"})
    print(headers)

    down_url = "http://file.krx.co.kr/download.jspx"

    data = requests.post(down_url, params={"code": otp.text}, headers=headers)

    data.encoding = "utf-8-sig"

    stock_data = pd.read_csv(io.BytesIO(data.content), header=0, thousands=",").iloc[
        :, [1, 2]
    ]

    print(stock_data)


get_stock_data()

