# sec-downloader
<table border=1 cellpadding="10"><tr><td>
    <p style="text-align:center;"><strong>*THIS IS NOT AN OFFICIAL LIBRARY BY THE SEC*</strong></p>
</td></tr></table>

The ```sec-downloader``` library offers a light downloader of Company data and their filings from the SEC.

## Installation
You can install sec_downloader with pip:
```
pip install -i https://test.pypi.org/simple/ sec-downloader==0.0.1.4
```

### Requirements
* certifi==2021.10.8
* charset-normalizer==2.0.8
* idna==3.3
* requests==2.26.0
* urllib3==1.26.7

## How to use
### Company module
```
import sec_downloader as sec

tpr = sec.Company('TPR')  # or tpr = sec.Company('1116132') or tpr = sec.Company(1116132)

# Get identifiers
tpr.title
tpr.ticker
tpr.cik
### 'TAPESTRY, INC.'
### 'TPR'
### '1116132'

# Get basic info
tpr.info
### {'cik': '1116132', 'entityType': 'operating', 'sic': '3100', 'sicDescription': 'Leather & Leather Products',
### 'insiderTransactionForOwnerExists': 0, 'insiderTransactionForIssuerExists': 1, 'name': 'TAPESTRY, INC.',
### 'tickers': ['TPR'], 'exchanges': ['NYSE'], 'ein': '522242751', 'description': '', 'website': '',
### 'investorWebsite': '', 'category': 'Large accelerated filer', 'fiscalYearEnd': '0627', 'stateOfIncorporation':
### 'MD', 'stateOfIncorporationDescription': 'MD', 'addresses': {'mailing': {'street1': '10 HUDSON YARDS',
### 'street2': None, 'city': 'NEW YORK', 'stateOrCountry': 'NY', 'zipCode': '10001', 'stateOrCountryDescription': 'NY'},
### 'business': {'street1': '10 HUDSON YARDS', 'street2': None, 'city': 'NEW YORK', 'stateOrCountry': 'NY',
### 'zipCode': '10001', 'stateOrCountryDescription': 'NY'}}, 'phone': '2129468400', 'flags': '', 'formerNames':
### [{'name': 'COACH INC', 'from': '2000-10-04T00:00:00.000Z', 'to': '2017-10-11T00:00:00.000Z'}]}

# Get recent filings
tpr.recent_filings
### {'accession_number': '0001225208-21-014047', 'filing_date': '2021-11-22', 'report_date': '2021-11-19',
### 'acceptance_datetime': '2021-11-22T17:58:20.000Z', 'act': '', 'form': '4', 'file_number': '', 'items': '',
### 'size': 9216, 'is_xbrl': 0, 'is_inline_xbrl': 0, 'primary_document': 'xslF345X03/doc4.xml',
### 'primary_doc_ description': ''}
```

### Filing module
The filing module is currently <strong><i>unavailable</i></strong> but should be included in the next update. This
module should then be used to download data for individual forms filed with the SEC.

## License
<strong>MIT License</strong>

Copyright (c) 2021 David Lojkasek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Author
Let me know if you have any questions or feedback!!!

**David Lojkasek, 2021**<br>
Email: [lojkasek.david@gmail.com](mailto:lojkasek.david@gmail.com)<br>
Twitter: [@DavidLojkasek](https://twitter.com/DavidLojkasek)
