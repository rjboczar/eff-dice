# eff-dice
## Usage
```
usage: eff.py [-h] [-n N] [-s {lc,uc,cap}] [-d DELIMITER] [seed]

EFF Diceware passphrase generator (https://www.eff.org/dice).

positional arguments:
  seed                  seed for random dice roll generation (default: 12345)

options:
  -h, --help            show this help message and exit
  -n N                  number of words in passphrase (default: 6)
  -s {lc,uc,cap}, --style {lc,uc,cap}
                        passphrase style (lower/upper/capitalized) (default:
                        lc)
  -d DELIMITER, --delimiter DELIMITER
                        passphrase delimiter (default: -)
```