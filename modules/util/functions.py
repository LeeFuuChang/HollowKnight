def sgn(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return n


def rectCollideWithStraightLine(RectPTL, RectPBR, LineP1, LineP2):
    if LineP1[1] == LineP2[1]:
        onX = (
            LineP1[0]  < RectPTL[0] and RectPTL[0] < LineP2[0]
        ) or (
            LineP1[0]  < RectPBR[0] and RectPBR[0] < LineP2[0]
        ) or (
            RectPTL[0] < LineP1[0]  and LineP1[0]  < RectPBR[0]
        ) or (
            RectPTL[0] < LineP2[0]  and LineP2[0]  < RectPBR[0]
        )
        onY = RectPTL[1] <= LineP1[1] and LineP1[1] <= RectPBR[1]
        return onX and onY
    elif LineP1[0] == LineP2[0]:
        onY = (
            LineP1[1]  < RectPTL[1] and RectPTL[1] < LineP2[1]
        ) or (
            LineP1[1]  < RectPBR[1] and RectPBR[1] < LineP2[1]
        ) or (
            RectPTL[1] < LineP1[1]  and LineP1[1]  < RectPBR[1]
        ) or (
            RectPTL[1] < LineP2[1]  and LineP2[1]  < RectPBR[1]
        )
        onX = RectPTL[0] <= LineP1[0] and LineP1[0] <= RectPBR[0]
        return onX and onY


def rectCollideWithRect(Rect1PTL, Rect1PBR, Rect2PTL, Rect2PBR):
    return (
        Rect1PBR[0] > Rect2PTL[0]) and (
        Rect1PTL[0] < Rect2PBR[0]) and (
        Rect1PBR[1] > Rect2PTL[1]) and (
        Rect1PTL[1] < Rect2PBR[1])