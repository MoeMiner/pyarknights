class ArkCharacter:
    uniqueid: str
    mainSkillLv: int
    # 精英化等级
    evolve: int
    # 潜能
    potential: int
    favorPoint: int
    level: int
    skinid: str
    def __init__(self, uniqueid):
        self.uniqueid = uniqueid
    def __repr__(self):
        return "[ArkCharacter <{0}>, mainSkullLv={1}, evolve={2}, skinId={3}, level={4}]".format(self.uniqueid, self.mainSkillLv, self.evolve, self.skinid, self.level)
    def getUniqueName(self):
        return self.uniqueid
    def setMainSkillLv(self, lv):
        self.mainSkillLv = lv
    def setEvolveLevel(self, lv):
        self.evolve = lv
    def setFavor(self, p):
        self.favorPoint = p
    def setPotentialLevel(self, lv):
        self.potential = lv
    def setLevel(self, lv):
        self.level = lv
    def setSkinId(self, id):
        self.skinid = id
    def import(self, json: dict):
        self.uniqueid = json['charId']
        self.mainSkillLv = json['mainSkillLvl']
        self.evolve = json['evolvePhase']
        self.favorPoint = json['favorPoint']
        self.potential = json['potentialRank']
        self.level = json['level']
        self.skinid = json['skinId']
        return self
