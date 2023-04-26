import os
import time
import subprocess as subp

basepath='/home/azureuser/ndvirectified/reproj'
arr = os.listdir('/home/azureuser/ndvirectified/reproj')
for i in arr:
    cmd="gdalwarp -dstnodata -9999 -cutline tsdm/District_Boundary.shp -crop_to_cutline "+basepath+"/"+str(i)+" /home/azureuser/ndvirectified/clipped/"+i
    print(cmd)
    try:
        subp.check_call(str(cmd), shell=True)
    except:
        print("end")
    time.sleep(1)