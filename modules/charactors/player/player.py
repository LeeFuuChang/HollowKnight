from ... import const
from ... import util
from ... import time
from .damageData import getPlayerDamageData
from .statesData import getPlayerStatesData
from .skills import getPlayerSkills
from .spells import getPlayerSpells
from .states import getPlayerStates
import pygame




class Player:
    attackTimer = time.Timer(const.player.PLAYER_ATTACK_TIME)

    knockbackTimer = time.Timer(const.player.PLAYER_ATTACK_KNOCKBACK_TIME)

    jumpHeldTimer = time.Timer(const.player.PLAYER_JUMP_HELD_MAX_TIME)

    dashTimer = time.Timer(const.player.PLAYER_DASH_TIME)
    dashCooldownTimer = time.Timer(const.player.PLAYER_DASH_COOLDOWN)

    superDashHeldTimer = time.Timer(const.player.PLAYER_DASH_TIME)

    midAirJumpTimer = time.Timer(const.player.PLAYER_MID_AIR_JUMP_TIME)


    def __init__(self, displaySize, areaID):
        self.damageData = getPlayerDamageData()
        self.statesData = getPlayerStatesData()
        self.skillUnlocked = getPlayerSkills()
        self.spellUnlocked = getPlayerSpells()
        self.states = getPlayerStates()

        self.areaID = areaID

        self.facingLR = 1
        self.facingUD = 0

        self.currentImageGroup = self.statesData.idol.imageGroup

        self.animateTimer = time.Timer(
            self.currentImageGroup.gap
        )

        self.displaySize = displaySize
        self.imageWidth, self.imageHeight = self.currentImageGroup.getImage().get_size()

        self.collidedCountV = 0
        self.collidedCountH = 0
        self.collideboxOffsetX = const.player.PLAYER_COLLIDEBOX_OFFSET_X
        self.collideboxOffsetY = const.player.PLAYER_COLLIDEBOX_OFFSET_Y
        self.collideboxWidth = const.player.PLAYER_COLLIDEBOX_WIDTH
        self.collideboxHeight = const.player.PLAYER_COLLIDEBOX_HEIGHT

        self.damageBoxes = util.classes.NamedObject(
            attack = [],
            spell = util.classes.NamedObject(
                **{spellName : [] for spellName in self.spellUnlocked.names}
            )
        )

        self.lastLandedFloor = None
        self.lastLandedPosition = None

        self.healthNow = 5
        self.healthMax = 5

        self.position = util.classes.Vec2(
            int(self.displaySize[0] / 2) - (self.imageWidth if self.facingLR>0 else 0),
            self.displaySize[1]-(self.imageHeight*2)
        )
        self.velocity = util.classes.Vec2(0, 0)





    def checkPlayerCanDash(self):
        return (
            not self.states.attack) and (
            self.dashCooldownTimer.check(autoReset=False))

    def updatePlayerDash(self, pressedKeys, movementboundaries):
        if not self.skillUnlocked.dash: return

        self.states.dashAvailable = self.checkPlayerCanDash()

        if pressedKeys[pygame.K_c] and self.states.dashAvailable and not self.states.dash:
            self.states.dash = True
            self.position.y -= 1 #lift player up
            self.dashTimer.reset()
        elif not self.dashTimer.check(autoReset=False) and self.states.dash:
            self.velocity.x = min(
                abs(self.velocity.x + (const.player.PLAYER_DASH_MAX_VELOCITY*const.player.PLAYER_DASH_ACCELERATION)),
                const.player.PLAYER_DASH_MAX_VELOCITY
            ) * self.facingLR
            for i in range( max(1, int(self.velocity.x / self.collideboxWidth )) ):
                for line in movementboundaries:
                    if not line.isVertical: continue
                    if self.checkCollideWithLine(line=line, position=self.position + util.classes.Vec2(self.collideboxWidth*(i+1)*self.facingLR, 0)): 
                        self.dashTimer.setTrue()
                        if line.correctionDirection == (1, 0):
                            self.position.x = line.p1.x - self.collideboxOffsetX
                        elif line.correctionDirection == (-1, 0):
                            self.position.x = line.p1.x - self.collideboxWidth - self.collideboxOffsetX
                        break
        elif self.states.dash:
            self.dashCooldownTimer.reset()
            self.velocity.x = 0
            self.states.dash = False
            self.position.y += 1 #lower player back down

    def checkPlayerCanSuperDash(self):
        return (
            not self.states.attack) and (
            self.states.grounded)

    def updatePlayerSuperDash(self, pressedKeys, movementboundaries):
        if not self.skillUnlocked.superDash: return

        self.states.superDashAvailable = self.checkPlayerCanSuperDash()

        if pressedKeys[pygame.K_s] and not self.states.superDash and self.states.superDashAvailable:
            self.velocity.x = 0
            if self.superDashHeldTimer.check(autoReset=False):
                self.states.superDash = True
                self.position.y -= 1 #lift player up
        else:
            self.superDashHeldTimer.reset()

        if self.states.superDash:
            self.velocity.x = min(
                abs(self.velocity.x + (const.player.PLAYER_SUPER_DASH_MAX_VELOCITY*const.player.PLAYER_SUPER_DASH_ACCELERATION)),
                const.player.PLAYER_SUPER_DASH_MAX_VELOCITY
            ) * self.facingLR
            for i in range( max(1, int(self.velocity.x / self.collideboxWidth )) ):
                for line in movementboundaries:
                    if not line.isVertical: continue
                    if self.checkCollideWithLine(line=line, position=self.position + util.classes.Vec2(self.collideboxWidth*(i+1)*self.facingLR, 0)): 
                        self.states.superDash = False
                        self.position.y += 1 #lower player back down
                        self.superDashHeldTimer.reset()
                        if line.correctionDirection == (1, 0):
                            self.position.x = line.p1.x - self.collideboxOffsetX
                        elif line.correctionDirection == (-1, 0):
                            self.position.x = line.p1.x - self.collideboxWidth - self.collideboxOffsetX
                        break

    def updatePlayerSkills(self, pressedKeys, movementboundaries):
        skills = [
            (self.updatePlayerDash, lambda : self.states.dash),
            (self.updatePlayerSuperDash, lambda : self.states.superDash)
        ]
        casted = [pair[1]() for pair in skills]
        if True in casted:
            idx = casted.index(True)
            skills[idx][0](pressedKeys=pressedKeys, movementboundaries=movementboundaries)
        else:
            for updateFunction, checkCasted in skills:
                updateFunction(pressedKeys=pressedKeys, movementboundaries=movementboundaries)
                if checkCasted(): break





    def checkPlayerCanAttack(self):
        return (
            not self.states.dash) and (
            not self.states.superDash)

    def updatePlayerAttack(self, pressedKeys):
        if not self.checkPlayerCanAttack(): 
            self.states.attackAvailable = False
            return

        if pressedKeys[pygame.K_x] and self.states.attackAvailable:
            self.states.attackAvailable = False
            if self.facingUD < 0:
                self.states.attack = 1
            elif self.facingUD > 0 and not self.states.grounded:
                self.states.attack = 2
            elif self.facingLR < 0:
                self.states.attack = 3
            elif self.facingLR > 0:
                self.states.attack = 4
            self.attackTimer.reset()
        elif self.attackTimer.check(autoReset=False) and self.states.attack:
            self.states.attack = 0
            self.states.knockback = False
        elif not pressedKeys[pygame.K_x] and not self.states.attack:
            self.updatePlayerFacing(pressedKeys=pressedKeys)
            self.states.attackAvailable = True

    def updatePlayerAttackKnockback(self, knockbackLines):
        for attackDamageBoxPTL, attackDamageBoxPBR in self.damageBoxes.attack:
            for line in knockbackLines:
                hit = util.functions.rectCollideWithStraightLine(
                    RectPTL = attackDamageBoxPTL, 
                    RectPBR = attackDamageBoxPBR, 
                    LineP1 = line.p1, 
                    LineP2 = line.p2
                )
                if not hit: continue
                if not self.states.knockback:
                    self.states.knockback = True
                    self.knockbackTimer.reset()
                if not self.knockbackTimer.check(autoReset=False):
                    if (self.states.attack == 2) and (line.correctionDirection == (0, -1)):
                        self.velocity.y = max(
                            self.velocity.y - const.player.PLAYER_ATTACK_KNOCKBACK_VELOCITY,
                            -const.player.PLAYER_ATTACK_KNOCKBACK_MAX_VELOCITY
                        )
                    elif (self.states.attack == 3) and (line.correctionDirection == (1, 0)):
                        self.velocity.x = min(
                            self.velocity.x + const.player.PLAYER_ATTACK_KNOCKBACK_VELOCITY,
                            const.player.PLAYER_ATTACK_KNOCKBACK_MAX_VELOCITY
                        )
                    elif (self.states.attack == 4) and (line.correctionDirection == (-1, 0)):
                        self.velocity.x = min(
                            self.velocity.x - const.player.PLAYER_ATTACK_KNOCKBACK_VELOCITY,
                            -const.player.PLAYER_ATTACK_KNOCKBACK_MAX_VELOCITY
                        )





    def getPlayerAttackDamageBox(self):
        if not self.states.attack: return []
        playerCenter = self.position + (
            int(const.images.PLAYER_IMAGES_DEFAULT_WIDTH/2),
            int(const.images.PLAYER_IMAGES_DEFAULT_HEIGHT/2)
        )
        attackDamageBoxPTL, attackDamageBoxPBR = self.damageData.__getattribute__(
            f"attack{self.states.attack}"
        ).damageBox.getDamageBox(playerCenter)
        return [
            [attackDamageBoxPTL, attackDamageBoxPBR],
        ]

    def updatePlayerDamageBoxes(self):
        self.damageBoxes.attack = self.getPlayerAttackDamageBox()

    def getPlayerAllDamageBoxes(self):
        spellDamageBoxes = []
        for spellName in self.damageBoxes.spell.names:
            for box in self.damageBoxes.spell[spellName]:
                spellDamageBoxes.append(box)
        return self.damageBoxes.attack + spellDamageBoxes





    def checkPlayerCanRun(self):
        return (
            not self.states.dash) and (
            not self.states.superDash)

    def updatePlayerRun(self, pressedKeys):
        if not self.checkPlayerCanRun(): 
            self.states.run = False
            return

        moveInput = 0
        if pressedKeys[pygame.K_RIGHT] and pressedKeys[pygame.K_LEFT]:
            moveInput = 0
        elif not (pressedKeys[pygame.K_RIGHT] or pressedKeys[pygame.K_LEFT]):
            moveInput = 0
        elif pressedKeys[pygame.K_LEFT]:
            if self.states.attack == 0:
                moveInput = -1
            elif self.states.attack != 4 and self.facingLR == -1:
                moveInput = -1
        elif pressedKeys[pygame.K_RIGHT]:
            if self.states.attack == 0:
                moveInput = 1
            elif self.states.attack != 3 and self.facingLR == 1:
                moveInput = 1

        if moveInput != 0:
            self.velocity.x = const.player.PLAYER_VELOCITY_HORIZONTAL*moveInput
        else:
            self.velocity.x = 0

        self.states.run = self.velocity.x!=0





    def checkPlayerCanJump(self):
        return (
            not self.states.dash) and (
            not self.states.superDash)

    def updatePlayerJump(self, pressedKeys):
        if not self.checkPlayerCanJump(): 
            self.states.jump = False
            return

        # havn't unlock midAirJump skill
        if not self.skillUnlocked.midAirJump:
            # midAirJump not available
            self.states.midAirJumpAvailable = False

        if pressedKeys[pygame.K_SPACE]:
            if self.states.grounded:
                self.jumpHeldTimer.reset()
                self.states.jump = True
                self.states.grounded = False
            elif self.states.midAirJumpAvailable and self.skillUnlocked.midAirJump:
                self.midAirJumpTimer.reset()
                self.states.midAirJump = True
                self.states.midAirJumpAvailable = False
                self.states.fall = False

            # holding jump and still in jumpHolding available time
            if self.states.jump and not self.jumpHeldTimer.check(autoReset=False):
                self.velocity.y = -const.player.PLAYER_VELOCITY_VERTICAL # accelerate up

        # (jumped or falling) and not grounded and haven't midAirJumped yet and also unlocked skill to midAirJump
        elif (self.states.jump or self.states.fall) and not self.states.grounded and not self.states.midAirJump and self.skillUnlocked.midAirJump:
            self.states.midAirJumpAvailable = True # midAirJump available

        # midAirJumped and still in midAirJump acceleration time
        if self.states.midAirJump and not self.midAirJumpTimer.check(autoReset=False) and self.skillUnlocked.midAirJump:
            self.velocity.y = -const.player.PLAYER_VELOCITY_VERTICAL # accelerate up





    def checkPlayerCanTurnUD(self):
        return (
            not self.states.attack)

    def checkPlayerCanTurnLR(self):
        return (
            not self.states.dash) and (
            not self.states.superDash)

    def updatePlayerFacing(self, pressedKeys):
        if self.checkPlayerCanTurnUD():
            if pressedKeys[pygame.K_UP]:
                self.facingUD = -1
            elif pressedKeys[pygame.K_DOWN]:
                self.facingUD = 1
            else:
                self.facingUD = 0

        if self.checkPlayerCanTurnLR():
            if self.states.attack in [0, 3] and pressedKeys[pygame.K_LEFT]:
                self.facingLR = -1
            elif self.states.attack in [0, 4] and pressedKeys[pygame.K_RIGHT]:
                self.facingLR = 1





    def applyGravity(self):
        if self.states.grounded or self.states.dash or self.states.superDash:
            self.velocity.y = 0
        else:
            self.velocity.y = min(
                self.velocity.y+const.game.GAME_GRAVITY, 
                const.player.PLAYER_TERMINAL_VELOCITY_VERTICAL
            )

        if self.velocity.y < 0:
            self.states.jump = True
            self.states.fall = False
        elif self.velocity.y > 0:
            self.states.jump = False
            self.states.fall = True





    def playerLanded(self):
        self.jumpHeldTimer.reset()
        self.velocity.y = 0
        self.states.jump = False
        self.states.midAirJump = False
        self.states.midAirJumpAvailable = False
        self.states.fall = False
        self.states.grounded = True





    def getImage(self):
        img = self.currentImageGroup.getImage()
        img = pygame.transform.flip(img, self.facingLR<0, False)
        return img

    def setImageGroup(self, stateName):
        desiredImageGroup = self.statesData.__getattribute__(stateName).imageGroup
        if self.currentImageGroup == desiredImageGroup: return
        self.currentImageGroup = desiredImageGroup
        self.currentImageGroup.reset()
        self.animateTimer.setTime(self.currentImageGroup.gap)

    def updateImageGroupBaseOnState(self):
        if self.states.attack > 0: return self.setImageGroup(f"attack{self.states.attack}")
        if self.states.superDash: return self.setImageGroup("superDash")
        if self.states.dash: return self.setImageGroup("dash")
        if self.states.midAirJump: return self.setImageGroup("midAirJump")
        if self.states.jump: return self.setImageGroup("jump")
        if self.states.fall: return self.setImageGroup("fall")
        if self.states.run: return self.setImageGroup("run")
        if self.states.grounded: return self.setImageGroup("idol")





    def checkCollideWithLine(self, line:util.classes.Line, position=None):
        if not position: position = self.position
        collideboxPTL = (
            position.x + self.collideboxOffsetX,
            position.y + self.collideboxOffsetY
        )
        collideboxPBR = (
            position.x + self.collideboxOffsetX + self.collideboxWidth,
            position.y + self.collideboxOffsetY + self.collideboxHeight
        )
        collideboxPoints = [
            [self.collideboxOffsetX                     , self.collideboxOffsetY],
            [self.collideboxOffsetX+self.collideboxWidth, self.collideboxOffsetY],
            [self.collideboxOffsetX+self.collideboxWidth, self.collideboxOffsetY+self.collideboxHeight],
            [self.collideboxOffsetX                     , self.collideboxOffsetY+self.collideboxHeight],
        ]
        if line.isHorizontal or line.isVertical:
            return util.functions.rectCollideWithStraightLine(
                RectPTL = collideboxPTL, 
                RectPBR = collideboxPBR, 
                LineP1 = line.p1, 
                LineP2 = line.p2
            )
        else:
            for i in range(len(collideboxPoints)):
                a = collideboxPoints[i]
                b = collideboxPoints[
                    (i+1) if(i+1 != len(collideboxPoints))else 0
                ]
                if line.checkCollided(a, b):
                    return True
        return False

    def getPrioritizedCollision(self, collidedLines) -> util.classes.Line:
        lineTypes = {}
        for line in collidedLines:
            correctionLength = line.correction(
                targetPos=self.position, 
                targetCollideboxOffsetX=self.collideboxOffsetX, 
                targetCollideboxOffsetY=self.collideboxOffsetY, 
                targetCollideboxWidth=self.collideboxWidth, 
                targetCollideboxHeight=self.collideboxHeight
            ).length()

            # if correctionLength == 0: continue

            if not lineTypes.get(line.__class__, None):
                lineTypes[line.__class__] = {
                    "minCorrection": float("inf"),
                    "minCorrectionLine": line
                }
            elif correctionLength < lineTypes[line.__class__]["minCorrection"]:
                lineTypes[line.__class__]["minCorrection"] = correctionLength
                lineTypes[line.__class__]["minCorrectionLine"] = line
        return [line["minCorrectionLine"] for line in sorted([
                lineTypes[name] for name in lineTypes
            ], key=lambda line:line["minCorrection"]
        )]

    def checkMovementCollisions(self, boundaries):
        collidedLines = []
        self.collidedCountV = 0
        self.collidedCountH = 0
        for line in boundaries:
            if self.checkCollideWithLine(line=line):
                collidedLines.append(line)
                if line.isVertical: self.collidedCountV+=1
                if line.isHorizontal: self.collidedCountH+=1
        if not collidedLines: 
            self.states.grounded = False
            return
        prioritizedLines = self.getPrioritizedCollision(collidedLines=collidedLines)

        maxHorizontalCorrectionAllowed = abs(self.velocity.x)
        maxVerticalCorrectionAllowed = abs(self.velocity.y)

        for line in prioritizedLines:
            correctionVector = line.correction(
                targetPos=self.position, 
                targetCollideboxOffsetX=self.collideboxOffsetX, 
                targetCollideboxOffsetY=self.collideboxOffsetY, 
                targetCollideboxWidth=self.collideboxWidth, 
                targetCollideboxHeight=self.collideboxHeight
            )
            if abs(correctionVector.x) > maxHorizontalCorrectionAllowed: continue
            if abs(correctionVector.y) > maxVerticalCorrectionAllowed: continue
            if line.isHorizontal:
                if correctionVector.y < 0: #floor push player up
                    if self.velocity.y > 0: #if still going down
                        self.states.grounded = True
                        self.playerLanded() #land on a floor

                        self.lastLandedFloor = line
                        self.lastLandedPosition = self.position.clone()
                        self.lastLandedPosition.y = self.lastLandedFloor.p1.y - self.collideboxHeight - self.collideboxOffsetY
                        LcollideX = self.lastLandedPosition.x + self.collideboxOffsetX
                        RcollideX = LcollideX + self.collideboxWidth
                        if LcollideX < self.lastLandedFloor.p1.x:
                            self.lastLandedPosition.x = self.lastLandedFloor.p1.x-self.collideboxOffsetX
                        elif RcollideX > self.lastLandedFloor.p2.x:
                            self.lastLandedPosition.x = self.lastLandedFloor.p2.x-self.collideboxWidth-self.collideboxOffsetX
                    # elif self.velocity.y < 0:
                    #     # player just started jumping but yet to leave this floor
                    #     pass
                elif correctionVector.y > 0: #roof push player down
                    if self.velocity.y < 0: #if still going up
                        self.midAirJumpTimer.setTrue()
                        self.states.jump = False
                        self.states.fall = True
                        self.velocity.y = 0 #stop going up
                    # elif self.velocity.y > 0:
                    #     # there should be no way for a player to fall on to a roof of a map
                    #     print("ERRORRRRRRRRRRRRRRRRRRRR")
            elif line.isVertical:
                self.velocity.x = 0 # player hit wall

            self.position.add(correctionVector)

    def checkDamageCollisions(self, damageBoxes):
        pTL = (self.position.x + self.collideboxOffsetX, self.position.y + self.collideboxOffsetY)
        pBR = (pTL[0] + self.collideboxWidth, pTL[1] + self.collideboxHeight)
        points = [
            pTL, (pBR[0], pTL[1]),
            (pTL[0], pBR[1]), pBR
        ]
        for box in damageBoxes:
            for point in points:
                if box.collideWithPoint(point):
                    self.healthNow = max(0, self.healthNow-box.damageAmount)
                    if box.respawnType == const.game.RESPAWN_TYPE_SAVE_POINT or self.healthNow == 0:
                        self.healthNow = self.healthMax
                    elif box.respawnType == const.game.RESPAWN_TYPE_NO_RESPAWN:
                        pass
                    elif box.respawnType == const.game.RESPAWN_TYPE_NEAREST_GROUND:
                        self.position = self.lastLandedPosition.clone()
                    return True
        return False

    def teleportTo(self, areas, areaID, portalID):
        self.areaID = areaID
        arrivePosition = areas[areaID].portalRects[portalID].getArrivePosition(
            targetCollideboxOffset=(self.collideboxOffsetX, self.collideboxOffsetY),
            targetCollideboxSize=(self.collideboxWidth, self.collideboxHeight)
        )
        self.position.x = arrivePosition[0]
        self.position.y = arrivePosition[1]

    def checkPortalCollisions(self, portalRects, areas):
        pTL = (self.position.x + self.collideboxOffsetX, self.position.y + self.collideboxOffsetY)
        pBR = (pTL[0] + self.collideboxWidth, pTL[1] + self.collideboxHeight)
        points = [
            pTL, (pBR[0], pTL[1]),
            (pTL[0], pBR[1]), pBR
        ]
        for portal in portalRects:
            for vertex in points:
                if portal.collideWithPoint(point=vertex):
                    if self.states.teleportAvailable:
                        self.states.teleportAvailable = False
                        self.teleportTo(areas=areas, areaID=portal.destAreaID, portalID=portal.destPortalID)
                    return
        self.states.teleportAvailable = True

    def cliffDetection(self, movementboundaries):
        if not (self.lastLandedFloor and self.states.grounded):
            self.states.onCliff = False
            return self.states.onCliff

        U_detection = (self.position.y+self.collideboxOffsetY) - self.collideboxHeight*const.player.PLAYER_CLIFF_DETECTION_DISTANCE_VERTICAL_MULTIPLIER
        D_detection = U_detection + self.collideboxHeight*(const.player.PLAYER_CLIFF_DETECTION_DISTANCE_VERTICAL_MULTIPLIER*2 + 1)
        L_detection = (self.position.x+self.collideboxOffsetX) - self.collideboxWidth*const.player.PLAYER_CLIFF_DETECTION_DISTANCE_HORIZONTAL_MULTIPLIER
        R_detection = L_detection + self.collideboxWidth*(const.player.PLAYER_CLIFF_DETECTION_DISTANCE_HORIZONTAL_MULTIPLIER*2 + 1)

        L_walls = []
        R_walls = []

        minStandingMessX = self.lastLandedFloor.p1.x
        maxStandingMessX = self.lastLandedFloor.p2.x
        for line in movementboundaries:
            if line.isVertical:
                if line.p2.y < U_detection or line.p1.y > D_detection: continue
                if line.correctionDirection == (1, 0):
                    L_walls.append(line.p1.x)
                elif line.correctionDirection == (-1, 0):
                    R_walls.append(line.p1.x)

            if not line.correctionDirection == (0, -1): continue
            if U_detection > line.p1.y: continue
            if D_detection < line.p1.y: continue
            if line.p1.x < minStandingMessX:
                if line.p2.x >= minStandingMessX:
                    minStandingMessX = line.p1.x
                    if line.p2.x > maxStandingMessX:
                        maxStandingMessX = line.p2.x
            if line.p2.x > maxStandingMessX:
                if line.p1.x <= maxStandingMessX:
                    maxStandingMessX = line.p2.x
                    if line.p1.x < minStandingMessX:
                        minStandingMessX = line.p1.x

        self.states.onCliff = (
            L_detection <= minStandingMessX and minStandingMessX not in L_walls
        ) or (
            R_detection >= maxStandingMessX and maxStandingMessX not in R_walls
        )
        return self.states.onCliff





    def update(self, pressedKeys, allAreas, movementboundaries, damageBoxes, portalRects):
        if self.animateTimer.check(): self.currentImageGroup.next()

        self.applyGravity()
        self.updatePlayerFacing(pressedKeys=pressedKeys)
        self.updatePlayerRun(pressedKeys=pressedKeys)
        self.updatePlayerJump(pressedKeys=pressedKeys)
        self.updatePlayerSkills(pressedKeys=pressedKeys, movementboundaries=movementboundaries)
        self.position.add(self.velocity)

        self.updatePlayerAttack(pressedKeys=pressedKeys)
        self.updatePlayerDamageBoxes()
        self.updatePlayerAttackKnockback(knockbackLines=[line for box in damageBoxes for line in box.lines])

        self.checkMovementCollisions(boundaries=movementboundaries)
        self.checkDamageCollisions(damageBoxes=damageBoxes)
        self.checkPortalCollisions(portalRects=portalRects, areas=allAreas)
        self.cliffDetection(movementboundaries=movementboundaries)

        self.updateImageGroupBaseOnState()




    def drawCollidebox(self, window, cameraWorldPos):
        pTL = (
            self.position.x+self.collideboxOffsetX,
            self.position.y+self.collideboxOffsetY
        )
        pBR = (
            self.position.x+self.collideboxOffsetX+self.collideboxWidth,
            self.position.y+self.collideboxOffsetY+self.collideboxHeight
        )
        pygame.draw.rect(
            window, const.game.COLLIDEBOX_DISPLAY_COLOR,
            pygame.Rect(
                pTL[0]-cameraWorldPos.x, pTL[1]-cameraWorldPos.y, pBR[0]-pTL[0], pBR[1]-pTL[1]
            ),
            width=1
        )

    def drawDamagebox(self, window, cameraWorldPos):
        spellDamageBoxes = []
        for spellName in self.damageBoxes.spell.names:
            for box in self.damageBoxes.spell[spellName]:
                spellDamageBoxes.append(box)
        boxes = self.damageBoxes.attack + spellDamageBoxes
        for pTL, pBR in boxes:
            pygame.draw.rect(
                window, const.game.DAMAGEBOX_DISPLAY_COLOR,
                pygame.Rect(
                    pTL[0]-cameraWorldPos.x, pTL[1]-cameraWorldPos.y, pBR[0]-pTL[0], pBR[1]-pTL[1]
                ),
                width=1
            )

    def draw(self, window, cameraWorldPos):
        displayPos = (self.position - cameraWorldPos)
        displayImg = self.getImage()
        if self.facingLR < 0:
            displayPos.x += const.images.PLAYER_IMAGES_DEFAULT_WIDTH
            displayPos.x -= displayImg.get_width()
        if self.facingUD < 0:
            displayPos.y += const.images.PLAYER_IMAGES_DEFAULT_HEIGHT
            displayPos.y -= displayImg.get_height()

        window.blit(displayImg, displayPos.toTuple())

        if const.player.PLAYER_COLLIDEBOX_DISPLAY: 
            self.drawCollidebox(window=window, cameraWorldPos=cameraWorldPos)
        if const.player.PLAYER_DAMAGEBOX_DISPLAY: 
            self.drawDamagebox(window=window, cameraWorldPos=cameraWorldPos)