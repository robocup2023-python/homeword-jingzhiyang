import json
from flask import Flask, request, render_template
from hashlib import md5
import random
import requests
import threading

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
    
appid = '20231012001844838'
appkey = 'HymwulVeEZA0Q5K57i7y'

from_lang = 'zh'
to_lang = 'en'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def translateHandler():
    with app.app_context():
        data = request.get_json()
        query = data["content"]["_value"]
        
        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
        
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        english = ""
        for eachline in result["trans_result"]:
            english += eachline["dst"] + "\n"
        print(english)
        print(json.dumps(result, indent=4, ensure_ascii=False))
        return english


@app.route('/api/translate', methods=['POST'])
def translate():
    # handler = threading.Thread(target=translateHandler)
    # handler.start()
    return translateHandler()


if __name__ == "__main__":
    app.run(debug=True,threaded=True,port=5010)
