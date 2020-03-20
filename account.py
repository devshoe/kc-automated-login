import requests,json
from kiteconnect import KiteConnect, KiteTicker



f            = open("data/credentials.json","r")
credentials  = json.load(f)
user = credentials["user"]
pswd = credentials["pswd"]
twofa = credentials["twofa"]
api_key = credentials["api_key"]
api_secret = credentials["api_secret"]
access_token = credentials["access_token"]
f.close()
# api_key = [x.rstrip("\n") for x in open("data/credentials.txt", "r").readlines()[0]]
def kiteLogin(): #automated login
    print("Logging in...")
    sesh2 = requests.Session()
    url = "https://kite.zerodha.com/api/login"
    twofaUrl = "https://kite.zerodha.com/api/twofa"
    reqId = eval(sesh2.post(url, {"user_id":user, "password":pswd}).text)["data"]["request_id"]
    login = sesh2.post(twofaUrl, {"user_id":user, "request_id":reqId, "twofa_value":twofa})
    reqToken = sesh2.get("https://kite.trade/connect/login?api_key="+api_key)
    accessToken = (reqToken.url).split("request_token=")
    accessToken = accessToken[1].split("&")
    print("Logged in successfully.")
    return accessToken[0]


def account(): #kite connect obj
    myAccount = KiteConnect(api_key=api_key)
    myAccount.set_access_token(access_token)
    return myAccount

def ticker(): #kite ticker obj
    myAccount = KiteConnect(api_key=api_key)
    myAccount.set_access_token(access_token)
    kws = KiteTicker(api_key, access_token)
    return kws

def updateInstruments():
    print("Updating instrument list...")
    instrumentUrl = "http://api.kite.trade/instruments"
    with open("data/instruments.csv", "wb") as f:f.write(requests.get(instrumentUrl).content)
    print("Update finished")


def login(getInstruments=False):
    request_token = kiteLogin()
    kite          = KiteConnect(api_key=api_key)
    data          = kite.generate_session(request_token, api_secret)
    credentials["access_token"] = data['access_token']
    with open("data/credentials.json", "w") as f:json.dump(credentials, f)
    if getInstruments:updateInstruments()

try:print(account().ltp("NSE:INFY"))
except:login()
if __name__=="__main__": pass