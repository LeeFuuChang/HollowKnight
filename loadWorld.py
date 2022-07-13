import requests as rq
import json
import os

res = rq.get(
    "https://api.figma.com/v1/files/CUGHECfRwO8wzX1Ivqs6Z6",
    headers={
        'X-Figma-Token': 'figd_NH8m-D7zNXdGOZWfKX73xW-81pXgxj-oR1nirf5j'
    }
)

data = res.json()
for area in data["document"]["children"][0]["children"]:
    AREA_ID = int(area["name"])
    data = area["children"]

    exportData = {
        "collideboxData": None,
        "portalData": None,
        "breakableData": None,
        "cameraboundData": None,
        "damageboxData": None,
    }
    outputData = {
        "collideboxLines": [],
        "portalRects": [],
        "breakableRects": [],
        "cameraboundBoxes": [],
        "damageBoxes": [],
    }

    for child in data:
        if child["name"] == "collidebox":
            exportData["collideboxData"] = child["children"]
        elif child["name"] == "portal":
            exportData["portalData"] = child["children"]
        elif child["name"] == "breakable":
            exportData["breakableData"] = child["children"]
        elif child["name"] == "camerabound":
            exportData["cameraboundData"] = child["children"]
        elif child["name"] == "damagebox":
            exportData["damageboxData"] = child["children"]


    BASE_PATH = r"C:\Users\a0962\Desktop\hollow-knight\HollowKnight\modules\world\data"
    PATH = os.path.join(BASE_PATH, f"{AREA_ID}")
    if not os.path.exists(PATH):os.mkdir(PATH)


    # player collidebox
    if exportData["collideboxData"] is not None:
        for line in exportData["collideboxData"]:
            x1 = round(line["absoluteBoundingBox"]["x"])
            y1 = round(line["absoluteBoundingBox"]["y"])
            x2 = round(line["absoluteBoundingBox"]["x"] + line["absoluteBoundingBox"]["width"])
            y2 = round(line["absoluteBoundingBox"]["y"] + line["absoluteBoundingBox"]["height"])
            rx = abs(x1-x2)
            ry = abs(y1-y2)
            # if rx > ry:

            lineData = line["name"].split("-")
            outputData["collideboxLines"].append(
                [
                    lineData[0], 
                    [x1, y1], [x2, y2], 
                    [int(lineData[1]), int(lineData[2])]
                ]
            )
        with open(os.path.join(PATH, "playerBoundaries.json"), "w") as f:
            json.dump(outputData["collideboxLines"], f)




    # camera boundaries
    if exportData["cameraboundData"] is not None:
        for rect in exportData["cameraboundData"]:
            pTL = [round(rect["absoluteBoundingBox"]["x"]), round(rect["absoluteBoundingBox"]["y"])]
            pBR = [pTL[0]+round(rect["absoluteBoundingBox"]["width"]), pTL[1]+round(rect["absoluteBoundingBox"]["height"])]
            ptp = rect["name"]
            outputData["cameraboundBoxes"].append([ptp, pTL, pBR])
        with open(os.path.join(PATH, "cameraBoundaries.json"), "w") as f:
            json.dump(outputData["cameraboundBoxes"], f)


    

    # damage boxes
    if exportData["damageboxData"] is not None:
        for rect in exportData["damageboxData"]:
            pTL = [round(rect["absoluteBoundingBox"]["x"]), round(rect["absoluteBoundingBox"]["y"])]
            pBR = [pTL[0]+round(rect["absoluteBoundingBox"]["width"]), pTL[1]+round(rect["absoluteBoundingBox"]["height"])]
            ptp = [int(_) for _ in rect["name"]]
            outputData["damageBoxes"].append([pTL, pBR, ptp])
        with open(os.path.join(PATH, "damageBoxes.json"), "w") as f:
            json.dump(outputData["damageBoxes"], f)




    # breakable rects
    if exportData["breakableData"] is not None:
        for rect in exportData["breakableData"]:
            pTL = [round(rect["absoluteBoundingBox"]["x"]), round(rect["absoluteBoundingBox"]["y"])]
            pBR = [pTL[0]+round(rect["absoluteBoundingBox"]["width"]), pTL[1]+round(rect["absoluteBoundingBox"]["height"])]
            durability = int(rect["name"])
            outputData["breakableRects"].append([pTL, pBR, durability])
        with open(os.path.join(PATH, "breakableRects.json"), "w") as f:
            json.dump(outputData["breakableRects"], f)




    # portal rects
    if exportData["portalData"] is not None:
        for rect in exportData["portalData"]:
            pTL = [round(rect["absoluteBoundingBox"]["x"]), round(rect["absoluteBoundingBox"]["y"])]
            pBR = [pTL[0]+round(rect["absoluteBoundingBox"]["width"]), pTL[1]+round(rect["absoluteBoundingBox"]["height"])]
            portalID, destAreaID, destPortalID, stikyT, stikyD, stikyL, stikyR = [int(_) for _ in rect["name"].split("-")]
            outputData["portalRects"].append([pTL, pBR, portalID, destAreaID, destPortalID, stikyT, stikyD, stikyL, stikyR])
        with open(os.path.join(PATH, "portalRects.json"), "w") as f:
            json.dump(outputData["portalRects"], f)

