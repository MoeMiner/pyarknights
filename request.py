import requests, json

class RequestHime:
    def __init__(self, uid, secret, device, current_seq=0):
        self.uid = uid
        self.secret = secret
        # for continuing the request.
        # this should not be zero unless you have not finished the log-in process yet.
        # value zero only appears at the beginning of /account/login.
        self.seqnum = current_seq + 2
        self._header = {
            'X-Unity-Version': '2017.4.39f1',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'User-Agent': 'arknights/355 CFNetwork/1125.2 ' + device,
            'Connection': 'keep-alive',
        }
        self.header_put_account(self.uid, self.secret, self.seqnum)
    
    def header_put_account(self, uid, secret):
        if not self._header:
            raise KeyError("Initialize the header first")
        self._header = dict(**self._header, **{'uid':str(uid), 'secret':secret})
    
    def header_flush_seqnum(self):
        if not self._header:
            raise KeyError("Initialize the header first")
        self.seqnum += 2
        self._header['seqnum'] = str(self.seqnum)

    def post(self, url, datadict: dict):
        data = json.dumps(datadict)
        response = requests.post(url, headers=self._header, data=data)
        return response

    def get_response_status(self, response: requests.Response):
        if not response.status_code == 200:
            return False
