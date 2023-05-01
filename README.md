# excur-script

This script gets the current exchange rate from the https://excur.ru/

## Supported currency pairs
- RUB/USD
- RUB/EUR

## How to use
Install dependencies before first run
> pip install -r requirements.txt

Running the script
> ./excur.py --city=Novosibirsk

Running the script (interactive option)
> watch -n 5 -t ./excur.py --city=Novosibirsk

Example of output
```
Date: 01.05.2023; Time: 13:07
Сurrency    Buy    Sell
----------  -----  ------
USD         81,50  78,65
EUR         89,75  87,25
```
