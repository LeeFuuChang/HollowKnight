from ... import util

def getPlayerSkills():
    return util.classes.NamedObject(
        dash = True,
        superDash = True,

        midAirJump = True,
    )