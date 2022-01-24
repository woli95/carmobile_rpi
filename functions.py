import shutil
def getHardDiskUsage():
    total, used, free = shutil.disk_usage("/")
    return total // (2**30), used // (2**30), free // (2**30)