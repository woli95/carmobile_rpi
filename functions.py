import shutil
def getHardDiskUsage():
    total, used, free = shutil.disk_usage("/")
    return {
        total: total // (2**30),
        used: used // (2**30),
        free: free // (2**30)
        }