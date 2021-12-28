"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
from bs4 import BeautifulSoup

from . import utils as _utils
from . import constants as _constants

CIK_TICKER_MAP_URL = _constants.CIK_TICKER_MAP_URL
filing_page_url = 'https://www.sec.gov/Archives/edgar/data/{}/{}/{}'


class Filing:
    """A class representing a single form filed with the SEC.

    :param accession_number: The accession_number of the form in question (with dashes).
    :type accession_number: str.
    """

    def __init__(self, accession_number: str):
        """
        Constructor method for the Filing object.

        Pass the company identifier, either the CIK or the ticker.

        :param accession_number: The accession_number of the form in question (with dashes).
        :type accession_number: str.
        """
        self.accession_number = accession_number
        self.cik = accession_number.split('-')[0]

        self.url = filing_page_url.format(
            self.cik,
            self.accession_number.replace('-', ''),
            self.accession_number + '-index.htm'
        )
        self._files = None

    def __repr__(self):
        return 'sec-downloader.Filing object(' + self.accession_number + ')'

    def _get_files(self):
        filing_page = _utils.get_page_contents(self.url)
        soup = BeautifulSoup(filing_page, 'html.parser')
        table = soup.find('table')
        headers = [header.text for header in table.find_all('th')]
        files = {i: {headers[j]: cell.text if j != 2 else 'https://www.sec.gov/' + cell.find('a', href=True)['href']
                     for j, cell in enumerate(row.find_all('td'))}
                 for i, row in enumerate(table.find_all('tr')[1:])}

        return files

    @property
    def files(self):
        if self._files is None:
            self._files = self._get_files()

        return self._files
