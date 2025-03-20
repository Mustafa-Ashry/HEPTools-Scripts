###############################################################
## This file code was created by Mustafa Ashry in March 2020 ##
###############################################################
with open("/home/mashry/hep/SSP-1.2.5/Output/TanBeta.dat") as wh:
  with open("/home/mashry/hep/SSP-1.2.5/Output/x1.dat") as xh:
    with open('/home/mashry/hep/SSP-1.2.5/Output/x2.dat') as yh:
      with open("/home/mashry/hep/SSP-1.2.5/Output/z1.dat","w") as z1h:
        with open("/home/mashry/hep/SSP-1.2.5/Output/z.dat","w") as zh:
          #Read first file
          xlines = xh.readlines()
          #Read second file
          ylines = yh.readlines()
          wlines = wh.readlines()
          z1lines = z1h.readlines()
          #Combine content of both lists
          #combine = list(zip(ylines,xlines))
          #Write to third file
          for i in range(len(xlines)):
            line = ylines[i].strip() + ' ' + xlines[i].strip()+ ' ' +wlines[i].strip()+ ' ' +z1lines[i]
            zh.write(line)
