from ... import const
from ... import util


class DamageBox:
    def __init__(self,
        PTLoffsetX, PTLoffsetY,
        PBRoffsetX, PBRoffsetY):
        self.PTLoffsetX = PTLoffsetX
        self.PTLoffsetY = PTLoffsetY
        self.PBRoffsetX = PBRoffsetX
        self.PBRoffsetY = PBRoffsetY

    def getDamageBox(self, playerCenter):
        return [
            [
                playerCenter[0]+self.PTLoffsetX,
                playerCenter[1]+self.PTLoffsetY,
            ],[
                playerCenter[0]+self.PBRoffsetX,
                playerCenter[1]+self.PBRoffsetY,
            ]
        ]


def getPlayerDamageData():
    return util.classes.NamedObject(
        attack1 = util.classes.NamedObject(
            damageBox = DamageBox(
                PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *0.5),
                PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*1.5),
                PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *0.5),
                PBRoffsetY= 0,
            ),
            damage = const.player.PLAYER_ATTACK_DAMAGE
        ),
        attack2 = util.classes.NamedObject(
            damageBox = DamageBox(
                PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *0.5),
                PTLoffsetY= 0,
                PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *0.5),
                PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*1.5),
            ),
            damage = const.player.PLAYER_ATTACK_DAMAGE
        ),
        attack3 = util.classes.NamedObject(
            damageBox = DamageBox(
                PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *1.5),
                PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*0.5),
                PBRoffsetX= 0,
                PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*0.5),
            ),
            damage = const.player.PLAYER_ATTACK_DAMAGE
        ),
        attack4 = util.classes.NamedObject(
            damageBox = DamageBox(
                PTLoffsetX= 0,
                PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*0.5),
                PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *1.5),
                PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*0.5),
            ),
            damage = const.player.PLAYER_ATTACK_DAMAGE
        ),
    )