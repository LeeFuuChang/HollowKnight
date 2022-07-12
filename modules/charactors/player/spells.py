from ... import util

def getPlayerSpells():
    return util.classes.NamedObject(
        focus = True,
        # Focus collected SOUL to repair your shell and heal damage.
        # Strike enemies to gather SOUL.

        vengefulSpirit = False,
        # Conjure a spirit that will fly forward and burn foes in its path.
        # The spirit requires SOUL to be conjured. Strike enemies to gather SOUL.

        desolateDive = False,
        # Strike the ground with a concentrated force of SOUL. This force can destroy foes or break through fragile structures.
        # The force requires SOUL to be conjured. Strike enemies to gather SOUL.

        howlingWraiths = False,
        # Blast foes with screaming SOUL.
        # The Wraiths requires SOUL to be conjured. Strike enemies to gather SOUL.

        shadeSoul = False,
        # Conjure a shadow that will fly forward and burn foes in its path.
        # The shadow requires SOUL to be conjured. Strike enemies to gather SOUL.

        descendingDark = False,
        # Strike the ground with a concentrated force of SOUL and Shadow. This force can destroy foes or break through fragile structures.
        # The force requires SOUL to be conjured. Strike enemies to gather SOUL.

        abyssShriek = False,
        # Blast foes with screaming SOUL and Shadow.
        # The Wraiths requires SOUL to be conjured. Strike enemies to gather SOUL.
    )