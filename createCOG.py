import os
import time
import subprocess as subp

arr = os.listdir('/home/azureuser/ndvirectified/clipped')
for i in arr:
    cmd="gdal_translate /home/azureuser/ndvirectified/clipped/"+str(i)+" /home/azureuser/ndvirectified/cog/"+str(i)+" -co COMPRESS=LZW -co TILED=YES"
    print(cmd)
    try:
        subp.check_call(str(cmd), shell=True)
    except:
        print("end")
    time.sleep(1)