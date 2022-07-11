from ... import util
class MapConstructionLine(util.classes.Line):
    def __init__(self, p1, p2, force):
        super().__init__(p1[0], p1[1], p2[0], p2[1])
        self.force = util.classes.Vec2(force[0], force[1])

    def correction(self, targetPos, 
        targetCollideboxOffsetX, targetCollideboxOffsetY, 
        targetCollideboxWidth, targetCollideboxHeight
    ) -> util.classes.Vec2: raise NotImplementedError
