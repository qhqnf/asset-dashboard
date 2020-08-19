import requests
import datetime
import re
import io
import pandas as pd


def get_stock_data():

    date = str(datetime.date.today())
    date = re.sub("[^0-9]", "", date)

    generate_otp_url = f"https://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?name=fileDown&filetype=csv&url=MKD/04/0406/04060200/mkd04060200&market_gubun=ALL&indx_ind_cd=&sect_tp_cd=ALL&isu_cdnm=%EC%A0%84%EC%B2%B4&isu_cd=&isu_nm=&isu_srt_cd=&secugrp=ST&secugrp=EF&stock_gubun=on&schdate={date}&pagePath=%2Fcontents%2FMKD%2F04%2F0406%2F04060200%2FMKD04060200.jsp"
    headers = {"User-Agent": "Mozilla/5.0"}
    """
    params = {
        "name": "fileDown",
        "filetype": "csv",
        "url": "MKD/04/0406/04060200/mkd04060200",
        "market_gubun": "ALL",
        "sect_tp_cd": "ALL",
        "isu_cdnm": "%EC%A0%84%EC%B2%B4",
        "secugrp": "ST",
        "secugrp": "EF",
        "stock_gubun": "on",
        "schdate": today,
        "pagePath": "/contents/MKD/04/0406/04060200/MKD04060200.jsp",
    }
    """

    otp = requests.get(generate_otp_url, headers=headers)

    headers.update({"Referer": "http://marketdata.krx.co.kr/mdi"})

    down_url = "http://file.krx.co.kr/download.jspx"

    data = requests.post(down_url, params={"code": otp.text}, headers=headers)

    data.encoding = "utf-8-sig"

    stock_data = pd.read_csv(io.BytesIO(data.content), header=0, thousands=",").iloc[
        :, 0:3
    ]

    return stock_data

