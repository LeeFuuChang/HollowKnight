#  U
#L   R
#  D


from ..part import MapConstructionLine
from .... import util
class LineU(MapConstructionLine):
    correctionDirection = (0, -1)
    def correction(self, targetPos, 
        targetCollideboxOffsetX, targetCollideboxOffsetY, 
        targetCollideboxWidth, targetCollideboxHeight
    ):return util.classes.Vec2(
            0, self.p1.y - (targetPos[1]+targetCollideboxOffsetY+targetCollideboxHeight)
        )