from request import RequestHime
import json

class gs:
    def __init__(self, reqhime: RequestHime):
        self.reqhime = reqhime

    def searchSinglePlayer(self, uid: int):
        url = 'https://ak-gs.hypergryph.com:8443/social/searchPlayer'
        data = {"idList":[str(uid)]}
        res = self.reqhime.post(url, data)
        j = json.loads(res.text)
        players = list(j['players'])
        if players.__len__() > 0:
            return j['players'][0]
        else:
            return False
    
    def searchPlayers(self, uids):
        url = 'https://ak-gs.hypergryph.com:8443/social/searchPlayer'
        uidlist = []
        for uid in uids:
            uidlist.append(str(uid))
        data = {"idList":uidlist}
        res = self.reqhime.post(url, data)
        j = json.loads(res.text)
        players = list(j['players'])
        if players.__len__() > 0:
            return list(j['players'])
        else:
            return False
