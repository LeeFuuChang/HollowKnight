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


def getPlayerDamageBoxes():
    return util.classes.NamedObject(
        attack1 = DamageBox(
            PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*0.5),
            PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*1.5),
            PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*0.5),
            PBRoffsetY= 0,
        ),
        attack2 = DamageBox(
            PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*0.5),
            PTLoffsetY= 0,
            PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*0.5),
            PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*1.5),
        ),
        attack3 = DamageBox(
            PTLoffsetX=-int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*1.5),
            PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*0.5),
            PBRoffsetX= 0,
            PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*0.5),
        ),
        attack4 = DamageBox(
            PTLoffsetX= 0,
            PTLoffsetY=-int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*0.5),
            PBRoffsetX= int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH *const.game.GAME_SIZE_RATIO*1.5),
            PBRoffsetY= int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT*const.game.GAME_SIZE_RATIO*0.5),
        ),
    )