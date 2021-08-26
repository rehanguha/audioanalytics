from pathlib import Path
import os

def extractFilename(PATH, withextension=False):
    if withextension:
        path, filename = os.path.split(PATH)
        return path, filename
    else:
        return str(Path(PATH).stem)

def mkDIR(PATH):
    try:
        os.mkdir(PATH)
        return None
    except Exception as e:
        return "Error: " + str(e)
