isOn = False
isAuto = False

ui = 0

def setMode(isAuto):
    import gui

    isAuto = isAuto
    gui.load(isAuto)
