from ... import util

def getPlayerStates():
    return util.classes.NamedObject(
        isInvulnerable = False,
        teleportAvailable = False,

        attack = 0,
        attackAvailable = False,

        knockback = False,

        idol = True,

        run = False,

        dash = False,
        dashAvailable = False,

        superDash = False,
        superDashAvailable = False,

        jump = False,
        midAirJump = False,
        midAirJumpAvailable = False,

        fall = False,

        grounded = True,

        onCliff = False,
    )