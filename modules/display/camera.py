from .. import const
from .. import util
import pygame
from PIL import Image
from .interface import Interface



class CameraModes:
    def __init__(self, defaultActiveMode=const.camera.CAMERA_MODE_CENTER_LEFT_NORMAL):
        self.mode = defaultActiveMode

    @staticmethod
    def getCameraDesiredPosition__CenterLeftNormal(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__CenterLeftUpper(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
             + targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__CenterLeftLower(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
             - targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__CenterRightNormal(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__CenterRightUpper(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
             + targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__CenterRightLower(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (
            int( (cameraHeight-targetHeight) /2)
             - targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL
        )
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomLeftNormal(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomLeftUpper(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight
         + targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomLeftLower(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - (int(cameraWidth/2)-targetWidth) # center right
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight
         - targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomRightNormal(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomRightUpper(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight
         + targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__BottomRightLower(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        desiredX = targetPosition.x - int(cameraWidth/2) # center left
        desiredY = targetPosition.y - (cameraHeight
         - targetHeight*const.camera.CAMERA_MODE_BOTTOM_OFFSET_TARGET_RATIO
         - targetHeight
         - targetHeight*const.camera.CAMERA_SHIFTING_TARGET_RATIO_VERTICAL)
        return util.classes.Vec2(desiredX, desiredY)

    @staticmethod
    def getCameraDesiredPosition__LockedBoth(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        return cameraPosition.clone()

    @staticmethod
    def getCameraDesiredPosition__LockedHorizontal(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        return cameraPosition.clone()

    @staticmethod
    def getCameraDesiredPosition__LockedVertical(targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        return cameraPosition.clone()


    @classmethod
    def getCameraDesiredPosition(cls, mode, targetPosition, targetWidth, targetHeight, cameraPosition, cameraWidth, cameraHeight):
        if mode == const.camera.CAMERA_MODE_CENTER_LEFT_NORMAL:
            return cls.getCameraDesiredPosition__CenterLeftNormal(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_CENTER_LEFT_UPPER:
            return cls.getCameraDesiredPosition__CenterLeftUpper(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_CENTER_LEFT_LOWER:
            return cls.getCameraDesiredPosition__CenterLeftLower(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_CENTER_RIGHT_NORMAL:
            return cls.getCameraDesiredPosition__CenterRightNormal(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_CENTER_RIGHT_UPPER:
            return cls.getCameraDesiredPosition__CenterRightUpper(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_CENTER_RIGHT_LOWER:
            return cls.getCameraDesiredPosition__CenterRightLower(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_LEFT_NORMAL:
            return cls.getCameraDesiredPosition__BottomLeftNormal(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_LEFT_UPPER:
            return cls.getCameraDesiredPosition__BottomLeftUpper(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_LEFT_LOWER:
            return cls.getCameraDesiredPosition__BottomLeftLower(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_RIGHT_NORMAL:
            return cls.getCameraDesiredPosition__BottomRightNormal(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_RIGHT_UPPER:
            return cls.getCameraDesiredPosition__BottomRightUpper(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_BOTTOM_RIGHT_LOWER:
            return cls.getCameraDesiredPosition__BottomRightLower(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )
        if mode == const.camera.CAMERA_MODE_LOCKED_BOTH:
            return cls.getCameraDesiredPosition__LockedBoth(
                targetPosition, targetWidth, targetHeight,
                cameraPosition, cameraWidth, cameraHeight
            )





class Camera(CameraModes):
    def __init__(self, displaySize, displayOffset, target, defaultActiveMode=const.camera.CAMERA_MODE_BOTTOM_RIGHT_NORMAL):
        self.mode = defaultActiveMode

        self.displayWidth = displaySize[0]
        self.displayHeight = displaySize[1]
        self.displayOffset = displayOffset

        self.surface = pygame.Surface(displaySize)

        self.interface = Interface(displaySize=displaySize)

        self.target = target
        self.targetWidth, self.targetHeight = self.target.imageWidth, self.target.imageHeight

        self.position = util.classes.Vec2(
            self.target.position.x - (int(self.displayWidth/2)-self.targetWidth),
            self.target.position.y - (int( (self.displayHeight-self.targetHeight) /2))
        )
        self.desiredPosition = self.position.clone()
        self.velocity = util.classes.Vec2(0, 0)





    def checkCollideWithLine(self, line:util.classes.Line, extend=0):
        collideboxX = self.position.x - (self.displayWidth * (extend/2))
        collideboxY = self.position.y - (self.displayHeight * (extend/2))
        collideboxW = self.displayWidth + (self.displayHeight * extend)
        collideboxH = self.displayHeight + (self.displayHeight * extend)
        if line.isHorizontal:
            onX = (
                line.p1.x < collideboxX and collideboxX < line.p2.x
            ) or (
                line.p1.x < collideboxX+collideboxW and collideboxX+collideboxW < line.p2.x
            ) or (
                collideboxX < line.p1.x and line.p1.x < collideboxX+collideboxW
            ) or (
                collideboxX < line.p2.x and line.p2.x < collideboxX+collideboxW
            )
            onY = collideboxY <= line.p1.y and line.p1.y <= collideboxY+collideboxH
            return onX and onY
        elif line.isVertical:
            onY = (
                line.p1.y < collideboxY and collideboxY < line.p2.y
            ) or (
                line.p1.y < collideboxY+collideboxH and collideboxY+collideboxH < line.p2.y
            ) or (
                collideboxY < line.p1.y and line.p1.y < collideboxY+collideboxH
            ) or (
                collideboxY < line.p2.y and line.p2.y < collideboxY+collideboxH
            )
            onX = collideboxX <= line.p1.x and line.p1.x <= collideboxX+collideboxW
            return onX and onY
        return False

    def filterVisibleLines(self, lines):
        visibleLines = []
        for line in lines:
            if self.checkCollideWithLine(line, extend=const.camera.CAMERA_VISIBLE_EXTENSION_LENGTH_RATIO):
                visibleLines.append(line)
        return visibleLines





    def fastChase(self):
        idx1, idx2, idx3 = self.getCameraModeIndex()
        self.mode = const.camera.CAMERA_MODE_MATRIX[idx1][idx2][idx3]
        self.updateDesiredCameraPosition()
        self.position = self.desiredPosition.clone()

    def getCameraLockedMode(self):
        pass

    def getCameraModeIndex(self):
        if self.target.states.onCliff:
            index1 = const.camera.CAMERA_MODE_CENTER_INDEX
        else:
            index1 = const.camera.CAMERA_MODE_BOTTOM_INDEX

        if index1 == const.camera.CAMERA_MODE_LOCKED_INDEX:
            index2 = self.getCameraLockedMode()
        elif self.target.facingUD < 0: # shift camera upper
            index2 = const.camera.CAMERA_MODE_UPPER_INDEX
        elif self.target.facingUD > 0: # shift camera lower
            index2 = const.camera.CAMERA_MODE_LOWER_INDEX
        else: # back to normal
            index2 = const.camera.CAMERA_MODE_NORMAL_INDEX

        if self.target.facingLR > 0:
            index3 = const.camera.CAMERA_MODE_LEFT_INDEX
        else:
            index3 = const.camera.CAMERA_MODE_RIGHT_INDEX

        return index1, index2, index3

    def updateDesiredCameraPosition(self):
        self.desiredPosition = self.getCameraDesiredPosition(
            mode = self.mode,
            targetPosition = self.target.position, 
            targetWidth = self.targetWidth, 
            targetHeight = self.targetHeight, 
            cameraPosition = self.position, 
            cameraWidth = self.displayWidth, 
            cameraHeight = self.displayHeight
        )
        return self.desiredPosition

    def updateVelocity(self):
        idx1, idx2, idx3 = self.getCameraModeIndex()
        self.mode = const.camera.CAMERA_MODE_MATRIX[idx1][idx2][idx3]
        self.updateDesiredCameraPosition()

        distX = (self.desiredPosition.x - self.position.x)
        distY = (self.desiredPosition.y - self.position.y)
        self.velocity.x = distX * const.camera.CAMERA_SHIFTING_VELOCITY_RATIO_HORIZONTAL
        self.velocity.y = distY * const.camera.CAMERA_SHIFTING_VELOCITY_RATIO_VERTICAL

        if self.target.velocity.x > 0:
            self.velocity.x += min(
                self.target.velocity.x * const.camera.CAMERA_FOLLOW_VELOCITY_RATIO_POSITIVE_HORIZONTAL, 
                const.player.PLAYER_VELOCITY_HORIZONTAL*const.camera.CAMERA_FOLLOW_MAX_VELOCITY_RATIO_POSITIVE_HORIZONTAL
            )
        elif self.target.velocity.x < 0:
            self.velocity.x += max(
                self.target.velocity.x * const.camera.CAMERA_FOLLOW_VELOCITY_RATIO_NEGATIVE_HORIZONTAL, 
                -const.player.PLAYER_VELOCITY_HORIZONTAL*const.camera.CAMERA_FOLLOW_MAX_VELOCITY_RATIO_NEGATIVE_HORIZONTAL
            )

        if self.target.velocity.y > 0:
            self.velocity.y += min(
                self.target.velocity.y * const.camera.CAMERA_FOLLOW_VELOCITY_RATIO_POSITIVE_VERTICAL, 
                const.player.PLAYER_VELOCITY_VERTICAL*const.camera.CAMERA_FOLLOW_MAX_VELOCITY_RATIO_POSITIVE_VERTICAL
            )
        elif self.target.velocity.y < 0:
            self.velocity.y += max(
                self.target.velocity.y * const.camera.CAMERA_FOLLOW_VELOCITY_RATIO_NEGATIVE_VERTICAL, 
                -const.player.PLAYER_VELOCITY_VERTICAL*const.camera.CAMERA_FOLLOW_MAX_VELOCITY_RATIO_NEGATIVE_VERTICAL
            )

        if self.mode == const.camera.CAMERA_MODE_LOCKED_BOTH:
            self.velocity.mul(0)
        elif self.mode == const.camera.CAMERA_MODE_LOCKED_HORIZONTAL:
            self.velocity.x *= 0
        elif self.mode == const.camera.CAMERA_MODE_LOCKED_VERTICAL:
            self.velocity.y *= 0

        return self.velocity

    def getCurrentBoundingBox(self, boundingBoxes):
        targetCTX = self.target.position.x + self.target.collideboxOffsetX + round(self.target.collideboxWidth/2)
        targetCTY = self.target.position.y + self.target.collideboxOffsetY + round(self.target.collideboxHeight/2)
        for box in boundingBoxes:
            if box.collideWithPoint( (targetCTX, targetCTY) ):
                return box

    def update(self, boundingBoxes):
        self.updateVelocity()

        self.position.add(self.velocity)

        currentBoundingBox = self.getCurrentBoundingBox(boundingBoxes=boundingBoxes)
        if currentBoundingBox:
            correctionVector = currentBoundingBox.getCorrection(self.position, self.displayWidth, self.displayHeight)
            self.position.add(correctionVector)





    def draw(self, window, currentLevel):
        baseBackground = currentLevel.background.getView(self.position.x, self.position.y, self.displayWidth, self.displayHeight)
        self.surface.blit(baseBackground, (0, 0))

        self.target.draw(window=self.surface, cameraWorldPos=self.position)

        self.interface.drawPlayerHealth(window=self.surface, playerHealthNow=self.target.healthNow, playerHealthMax=self.target.healthMax)

        window.blit(self.surface, self.displayOffset)