"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
from bs4 import BeautifulSoup

from . import utils as _utils

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
        self.form_type = _utils.get_form_type(self.url)

        self._files = None

    def __repr__(self):
        return 'sec-downloader.Filing object(' + self.accession_number + ')'

    def _get_files(self) -> dict:
        """Retrieves the data from the table listing the files associated with the filing.

        This method is automatically called when the user calls :instance_attribute:'Filing.files' and
        :instances_attribute:'Filing._files is None.

        :return: A dict of data of the files associated with the filing.
        :rtype: dict.
        """
        filing_page = _utils.get_page_contents(self.url)
        soup = BeautifulSoup(filing_page, 'html.parser')
        table = soup.find('table', {'summary': 'Document Format Files'})
        headers = [header.text for header in table.find_all('th')]
        files = {i: {headers[j]: cell.text if j != 2 else 'https://www.sec.gov/' + cell.find('a', href=True)['href']
                     for j, cell in enumerate(row.find_all('td'))}
                 for i, row in enumerate(table.find_all('tr')[1:])}

        return files

    @property
    def files(self):
        """Returns a dict of files associated with the filing and their data.

        :return: A dict of files and their data.
        :rtype: dict.
        """
        if self._files is None:
            self._files = self._get_files()

        return self._files
