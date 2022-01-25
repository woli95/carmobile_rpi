import shutil
import glob

def getHardDiskUsage():
    total, used, free = shutil.disk_usage("/")
    return total // (2**30), used // (2**30), free // (2**30)

def getSavedVideoFilenames():
    return glob.glob("/home/pi/Desktop/PD/carmobile_rpi/videos/*")
    