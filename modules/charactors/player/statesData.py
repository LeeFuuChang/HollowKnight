from ... import display
from ... import const
from ... import util
import os

def getPlayerStatesData():
    return util.classes.NamedObject(
        attack1 = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_ATTACK_UPPER_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_ATTACK_UPPER_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_ATTACK_UPPER_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_ATTACK_UPPER_IMAGE_GAP
            )
        ),
        attack2 = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_ATTACK_LOWER_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_ATTACK_LOWER_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_ATTACK_LOWER_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_ATTACK_LOWER_IMAGE_GAP
            )
        ),
        attack3 = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_ATTACK_NORMAL_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_ATTACK_NORMAL_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_ATTACK_NORMAL_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_ATTACK_NORMAL_IMAGE_GAP
            )
        ),
        attack4 = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_ATTACK_NORMAL_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_ATTACK_NORMAL_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_ATTACK_NORMAL_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_ATTACK_NORMAL_IMAGE_GAP
            )
        ),
        idol = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_IDOL_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_IDOL_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_IDOL_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_IDOL_IMAGE_GAP
            )
        ),
        run = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_RUN_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_RUN_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_RUN_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_RUN_IMAGE_GAP
            )
        ),
        dash = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_DASH_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_DASH_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_DASH_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_DASH_IMAGE_GAP
            )
        ),
        superDash = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_SUPER_DASH_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_SUPER_DASH_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_SUPER_DASH_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_SUPER_DASH_IMAGE_GAP
            )
        ),
        jump = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_JUMP_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_JUMP_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_JUMP_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_JUMP_IMAGE_GAP
            )
        ),
        midAirJump = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_MID_AIR_JUMP_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_MID_AIR_JUMP_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_MID_AIR_JUMP_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_MID_AIR_JUMP_IMAGE_GAP
            )
        ),
        fall = util.classes.NamedObject(
            imageGroup = display.ImageGroup(
                images = [
                    display.SpriteImage(
                        fromPath=os.path.join(
                            const.path.ASSETS_PATH, "charactors", "TheKnight", path
                        )
                    ) for path in const.images.PLAYER_FALL_IMAGE_PATHS
                ],
                startAt = 0,
                loopFrom = const.images.PLAYER_FALL_IMAGE_LOOP_FROM,
                loopTo = const.images.PLAYER_FALL_IMAGE_LOOP_TO,
                gap = const.images.PLAYER_FALL_IMAGE_GAP
            )
        )
    )
