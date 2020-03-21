# kc-automated-login
Zerodha Kite Connect automatic login, from start to finish by just running a script

# Dependencies
* requests

# Usage

1. (FIRST USE ONLY) Open data/credentials.json in a text editor and fill every field up inside quotes. Ignore "access_token" field.

"user":Your login ID

"pswd":Your password

"twofa":Your 2 factor auth pin

and your kiteconnect credentials

2. Run account.py. It'll auto update your access-token from now every time you run it. 
``` python
login()
```
If you want the instruments csv dump from "http://api.kite.trade/instruments", 

``` python
login(getInstruments = True)
```
This will store all instruments in data/instruments.csv

3. After this you can simply import account into your own projects.
For example:
```python
import account
myAccount = account.account() #KiteConnectObject
myTicker = account.ticker() #KiteTickerObject (kws in docs)
print(myAccount.orders())
```
and it'll all work like usual.
