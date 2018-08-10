# bankrates
A web scraping project to collect bank currency rates.

## Installation
[pipenv Bangla Video Tutorial](https://www.youtube.com/watch?v=imuxt5iHy_A)

```
pipenv install bs4
pipenv shell
```

## How to use
If user types in terminal/powershell. Valid commands
```
python3 rates.py ibbl usd:100(optional) browser(optional)
```

### Example 1:
- Input ``` python3 rates.py ibbl ```
- Output ```A beautiful table with currency rates ```

### Example 2:
- Input ``` python3 rates.py ibbl usd=100```
- Output ```USD 100 = ?TAKA and a beautiful table with currency rates ```

### Example 3:
- Input ``` python3 rates.py ibbl usd=100 browser```
- Output ```create and open html file in a browser with data ```

## Python Knowledge 
To understand the code minimum python knowledge required:

- Fundamental of Python 3 
- Object oriented programming
- Exception Handling
- Files I/O
- pipenv packaging
- Modules and Package

## Contribution
If you want to contribute on this project, you're welcome to fork the project and submit a pull request. 

## Questions or feedback?

Feel free to [open an issue](https://github.com/mahmudahsan/bankrates/issues/new), or find me [@mahmudahsan on Twitter](https://twitter.com/mahmudahsan).
