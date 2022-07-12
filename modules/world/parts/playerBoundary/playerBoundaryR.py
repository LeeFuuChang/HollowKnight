#  U
#L   R
#  D



from .constructionLine import ConstructionLine
from .... import util
class LineR(ConstructionLine):
    correctionDirection = (1, 0)

    def correction(self, targetPos, 
        targetCollideboxOffsetX, targetCollideboxOffsetY, 
        targetCollideboxWidth, targetCollideboxHeight
    ):return util.classes.Vec2(
            self.p1.x - (targetPos[0]+targetCollideboxOffsetX), 0
        )