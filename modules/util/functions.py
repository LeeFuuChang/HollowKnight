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