<p align="center">
    <a href="/">
        <img src="https://img.shields.io/badge/build-passed-brightgreen.svg" alt="Build" />
    </a>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-3.7-yellow.svg" alt="Python" />
    </a>
    <a href="https://github.com/mahmudahsan/bankrates/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License" />
    </a>
    <a href="https://twitter.com/mahmudahsan">
        <img src="https://img.shields.io/badge/contact%40-mahmudahsan-red.svg" alt="Twitter: @mahmudahsan" />
    </a>
</p>

# Bank Currency Rates
A web scraping project to apply python knowledge. It will collect Bangladeshi banks currency rates. Currently only IBBL bank currency web page data is scraping. 

This project will help to anyone who want to apply Python programming knowledge in real time project.

## Prerequisite 
To understand the code minimum python knowledge required are written below. 

- Fundamental of Python 3 | [বাংলা](https://www.youtube.com/watch?v=qcRlYt28WPM&list=PLlMOodDAsO4y8_pYiKnweAz0MjR61VByU)
- Object oriented programming | [বাংলা](https://www.youtube.com/watch?v=xA43kBnuglE&list=PLlMOodDAsO4xV_Fr-j25BmwuD2V5B18ra)
- Exception Handling | [বাংলা](https://www.youtube.com/watch?v=sUWaEBe7UfU)
- Files I/O | [বাংলা](https://www.youtube.com/watch?v=k1rFag1W2WM)
- pipenv packaging | [বাংলা](https://www.youtube.com/watch?v=imuxt5iHy_A)
- Modules and Package | [বাংলা](https://www.youtube.com/watch?v=cdBiyCxmeRg)
- Unit Test | [বাংলা](https://www.youtube.com/watch?v=UhIwkjwz6Ek)
- Regular Expression | [বাংলা](https://www.youtube.com/watch?v=yygyryPAJH0)

## Learning Resources 
1. **[ENGLISH PYTHON COURSE](https://bit.ly/2v7lT74)**
2. **[বাংলা ওয়েবপেজ স্ক‍্র‍্যাপিং সিরিজ](https://www.youtube.com/watch?v=3YLyT4LRJUc&list=PLlMOodDAsO4zLUcrCyUJ8aclYqOOcSMfn)**
3. **[বাংলা ইউটিউব চ‍্যানেল](https://www.youtube.com/channel/UCtHlgyUw0wLE5Ous9swfFlg/playlists)**
4. **[PythonBangla.com](http://pythonbangla.com)**

## Installation
[pipenv Bangla Video Tutorial](https://www.youtube.com/watch?v=imuxt5iHy_A)

```
pipenv install bs4
pipenv shell
```

## How to use
- In **macOs terminal** use `python3`
- In **windows powershell** use `python`

Valid commands examples:
```
python rates.py ibbl usd=100(optional) browser(optional)
```

### Example 1:
- Input ` python3 rates.py ibbl ` | ibbl means islamic bank bangladesh ltd

**Output**
It represents 1 Foreign Rate = Bangladeshi Taka Amount
```
-----------------------------
Islami Bank Bangladesh Ltd.
-----------------------------
USD 1 = BDT 82.75
GBP 1 = BDT 106.9792
EUR 1 = BDT 95.1625
JPY 1 = BDT 0.7345
CHF 1 = BDT 81.9307
SGD 1 = BDT 60.1599
AED 1 = BDT 22.465
SAR 1 = BDT 22.0285
CAD 1 = BDT 62.8083
Update on: 30 Jul, 2018
 ```

### Example 2:
- Input ``` python rates.py ibbl usd=100```
- Output ```USD 100 = ?TAKA and a beautiful table with currency rates ```

### Example 3:
- Input ``` python rates.py ibbl usd=100 browser```
- Output ```create and open html file in a browser with data ```

## Contribution
If you want to contribute on this project, you're welcome to fork the project and submit a pull request. 

## Questions or feedback?

Feel free to [open an issue](https://github.com/mahmudahsan/bankrates/issues/new), or find me [@mahmudahsan on Twitter](https://twitter.com/mahmudahsan).
