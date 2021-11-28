"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
from . import utils

CIK_TICKER_MAP_URL = 'https://www.sec.gov/files/company_tickers.json'
company_profile_url = 'https://data.sec.gov/submissions/CIK{}.json'


class Company:

    def __init__(self, identifier: str):
        self.identifier = str(identifier).upper().lstrip('0')

        data = self._find_ticker_cik()
        self.ticker = data.get(self.identifier).get('ticker')
        self.cik = data.get(self.identifier).get('cik')
        self.title = data.get(self.identifier).get('title')
        self._profile_url = company_profile_url.format(self.cik.zfill(10))

        self._info = None
        self._recent_filings = None

    def __repr__(self):
        return 'sec-downloader.Company object(' + self.identifier + ')'

    def _find_ticker_cik(self) -> dict:
        data = utils.get_json_data(CIK_TICKER_MAP_URL)
        data = {self.identifier: {
            'cik': str(data[c].get('cik_str')),
            'ticker': data[c].get('ticker'),
            'title': data[c].get('title')
        } for c in data if str(data[c].get('cik_str')) == self.identifier or data[c].get('ticker') == self.identifier}

        return data

    def get_info(self):
        data = utils.get_json_data(self._profile_url)
        data = {key: val for key, val in data.items() if key != 'filings'}

        return data

    def get_recent_filings(self):
        data = utils.get_json_data(self._profile_url).get('filings').get('recent')
        data = utils.transform_recent_filings(data)

        return data

    @property
    def info(self):
        if self._info is None:
            self._info = self.get_info()

        return self._info

    @property
    def recent_filings(self):
        if self._recent_filings is None:
            self._recent_filings = self.get_recent_filings()

        return self._recent_filings
