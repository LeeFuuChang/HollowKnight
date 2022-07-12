#  U
#L   R
#  D



from .constructionLine import ConstructionLine
from .... import util
class LineD(ConstructionLine):
    correctionDirection = (0, 1)

    def correction(self, targetPos, 
        targetCollideboxOffsetX, targetCollideboxOffsetY, 
        targetCollideboxWidth, targetCollideboxHeight
    ):return util.classes.Vec2(
            0, self.p1.y - (targetPos[1]+targetCollideboxOffsetY)
        )