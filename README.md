<p align="center">
    <a href="/">
        <img src="https://img.shields.io/badge/build-failed-brightgreen.svg" alt="Build" />
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

# bankrates
A web scraping project to apply python knowledge. It will collect Bangladeshi banks currency rates. Currently only IBBL bank currency web page data is scraping. 

This project will help to anyone who want to apply Python programming knowledge in real time project.

## Prerequisite 
To understand the code minimum python knowledge required are written below. 

- Fundamental of Python 3 | [বাংলা]()
- Object oriented programming | [বাংলা]()
- Exception Handling | [বাংলা]()
- Files I/O | [বাংলা]()
- pipenv packaging | [বাংলা]()
- Modules and Package | [বাংলা]()
- Unit Test | [বাংলা]()
- Regular Expression | [বাংলা]()

[My English Python Tutorial Course]()

All of these programming concepts are discussed in my Bangla youtube channel named [Mahmud Ahsan](https://www.youtube.com/channel/UCtHlgyUw0wLE5Ous9swfFlg/playlists) or [PythonBangla.com](http://pythonbangla.com)

## Installation
[pipenv Bangla Video Tutorial](https://www.youtube.com/watch?v=imuxt5iHy_A)

```
pipenv install bs4
pipenv shell
```

## How to use
If user types in terminal/powershell. Valid commands
```
python3 rates.py ibbl usd=100(optional) browser(optional)
```

### Example 1:
- Input ``` python3 rates.py ibbl ``` | ibbl means islamic bank bangladesh ltd
Output 
It represents 1 Foreign Rate = Bangladeshi Taka Amount
```
USD 82.75
GBP 106.9792
EUR 95.1625
JPY 0.7345
CHF 81.9307
SGD 60.1599
AED 22.465
SAR 22.0285
CAD 62.8083
Update on: 30 Jul, 2018
 ```

### Example 2:
- Input ``` python3 rates.py ibbl usd=100```
- Output ```USD 100 = ?TAKA and a beautiful table with currency rates ```

### Example 3:
- Input ``` python3 rates.py ibbl usd=100 browser```
- Output ```create and open html file in a browser with data ```

## Contribution
If you want to contribute on this project, you're welcome to fork the project and submit a pull request. 

## Questions or feedback?

Feel free to [open an issue](https://github.com/mahmudahsan/bankrates/issues/new), or find me [@mahmudahsan on Twitter](https://twitter.com/mahmudahsan).
