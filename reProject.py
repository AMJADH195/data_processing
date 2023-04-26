import os
import time
import subprocess as subp

basepath='/home/azureuser/ndvirectified/ndvirect/cog/'
arr = os.listdir('/home/azureuser/ndvirectified/ndvirect/cog')
for i in arr:
    cmd="gdalwarp -of GTIFF  -r cubic -t_srs '+proj=longlat +datum=WGS84 +no_defs'"+" "+basepath+str(i)+" /home/azureuser/ndvirectified/reproj/"+str(i)
    print(cmd)
    try:
        subp.check_call(str(cmd), shell=True)
    except:
        print("end")
    time.sleep(1)