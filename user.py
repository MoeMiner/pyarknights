import json
from character import ArkCharacter

class Player:
    def __init__(self, uid: int):
        self.uid = uid
    
    def importJSON(self, json: dict):
        if json == None: return False
        self.uid = int(json['uid'])
        self.nickname = json['nickName']
        self.nicknumber = json['nickNumber']
        self.displayname = "{0}#{1}".format(self.nickname, self.nicknumber)
        self.friendlimit = json['friendNumLimit']
        self.servername = json['serverName']
        self.level = json['level']
        self.lastonline = json['lastOnlineTime']
        
        # assistChar
        self.assistCharList = list(json['assistCharList'])
        if self.assistCharList.__len__() == 0 or self.assistCharList[0] == None:
            self.assist = []
            self.assist_slot = 0
        else:
            self.assist = []
            self.assist_slot = self.assistCharList.__len__()
            for chara in self.assistCharList:
                if chara == None:
                    break
                arkc = ArkCharacter(chara['charId'])
                arkc.import(chara)
                self.assist.append(arkc)
        return self
