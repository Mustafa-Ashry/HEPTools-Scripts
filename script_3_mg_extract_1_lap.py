# PART II ## Extract xsection and parameters from MG #
import re
import os
import shutil

#variables and paths
n=50;
m=2000;
ssp="/home/mashry/hep/SSP-1.2.5/Output/";
mg="/home/mashry/hep/MG5_aMC_v2_6_4/";
dat=["TanBeta","gBL","gYB","mC12","mC22","x1","x2","hh_2","M1","M2","M3","HS total Chi^2","pphhaabb_xsection","ppzz4l_xsection"];
par=["TanBeta","gBL","gYB","mC12","mC22","x1","x2"];
mass=["mh2"];
xsec=["pphhaabb_xsection","ppzz4l_xsection"];

#Copy scan results from DB
for i in range(0,n):
	if(os.path.exists("/home/mashry/Dropbox/00/BLSSMScanLowmh"+str(i))):
		shutil.move("/home/mashry/Dropbox/00/BLSSMScanLowmh"+str(i),ssp+"BLSSMScanLowmh"+str(i))
		print("DB/BLSSMScanLowmh"+str(i))
#remove old cross sections and parameters files
for i in range(len(dat)):
	if(os.path.isfile(ssp+dat[i]+".dat")):
		os.remove(ssp+dat[i]+".dat")

#pphhaabb-Copy MC reports and delete other unwanted MG output files
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile(mg+"pphhaabb_blssm_low/pphhaabb_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt")):
			shutil.copyfile(mg+"pphhaabb_blssm_low/pphhaabb_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt", mg+"pphhaabb_blssm_low/run_"+str(i)+"_"+str(j)+".txt") and shutil.rmtree(mg+"pphhaabb_blssm_low/pphhaabb_blssm_"+str(i)+"_"+str(j))
			print("pphhaabb_"+str(i)+"_"+str(j))
#pphhaabb-Copy from DB
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile("/home/mashry/Dropbox/00/pphhaabb/"+"run_"+str(i)+"_"+str(j)+".txt")):
			shutil.move("/home/mashry/Dropbox/00/pphhaabb/"+"run_"+str(i)+"_"+str(j)+".txt",mg+"pphhaabb_blssm_low/run_"+str(i)+"_"+str(j)+".txt")
			print("DB/pphhaabb_"+str(i)+"_"+str(j))
#pphhaabb-extract cross sections and parameters
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile(mg+"pphhaabb_blssm_low/run_"+str(i)+"_"+str(j)+".txt")):
			open(ssp+"pphhaabb_xsection.dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.strip("#  Integrated weight (pb)  :") for l in open(mg+"pphhaabb_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "#  Integrated weight (pb)  :" in l]) 
			for k in range(len(dat)-2):
				open(ssp+dat[k]+".dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.replace("  # "+dat[k],"") for l in open(mg+"pphhaabb_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "# "+dat[k]+"\n" in l]) 
			print("pphhaabb_"+str(i)+"_"+str(j))

print("\nEnd of process: pphhaabb")

#ppzz4l-Copy MC reports and delete other unwanted MG output files
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile(mg+"ppzz4l_blssm_low/ppzz4l_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt")):
			shutil.copyfile(mg+"ppzz4l_blssm_low/ppzz4l_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt", mg+"ppzz4l_blssm_low/run_"+str(i)+"_"+str(j)+".txt") and shutil.rmtree(mg+"ppzz4l_blssm_low/ppzz4l_blssm_"+str(i)+"_"+str(j))
			print("ppzz4l_"+str(i)+"_"+str(j))
#ppzz4l-Copy from DB
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile("/home/mashry/Dropbox/00/ppzz4l/"+"run_"+str(i)+"_"+str(j)+".txt")):
			shutil.move("/home/mashry/Dropbox/00/ppzz4l/"+"run_"+str(i)+"_"+str(j)+".txt",mg+"ppzz4l_blssm_low/run_"+str(i)+"_"+str(j)+".txt")
			print("DB/ppzz4l_"+str(i)+"_"+str(j))
#ppzz4l-extract cross sections and parameters
for i in range(0,n):
	for j in range(0,m):
		if(os.path.isfile(mg+"ppzz4l_blssm_low/run_"+str(i)+"_"+str(j)+".txt")):
			open(ssp+"ppzz4l_xsection.dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.strip("#  Integrated weight (pb)  :") for l in open(mg+"ppzz4l_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "#  Integrated weight (pb)  :" in l]) 
			for k in range(len(dat)-2):
				open(ssp+dat[k]+".dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.replace("  # "+dat[k],"") for l in open(mg+"ppzz4l_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "# "+dat[k]+"\n" in l]) 
			print("ppzz4l_"+str(i)+"_"+str(j))

print("\nEnd of process: ppzz4l")

# PART III ## Create MG script #
#pphhaabb
myfile = open(mg+'pphhaabb_blssm_low.txt', 'w')
myfile.write("#./bin/mg5_aMC pphhaabb_blssm_low.txt\n")
myfile.write("import model BLSSM/ -modelname\n")
myfile.write("define p=g u1 u1bar u2 u2bar d1 d1bar d2 d2bar d3 d3bar\n")
for i in range(0,n):
    for j in range(0,m):
        if(os.path.isfile(ssp+"BLSSMScanLowmh/SPheno.spc.BLSSM_"+str(i)+"_"+str(j))):
            myfile.write("generate p p > h1 h1 $ h1 / h3 h4  u1 u1bar u2 u2bar u3 u3bar d1 d1bar d2 d2bar d3 d3bar, h1 > a a, h1 > d3 d3bar\n")
            myfile.write("output pphhaabb_blssm_low/pphhaabb_blssm_"+str(i)+"_"+str(j)+"\n")
            myfile.write("launch\n")
            myfile.write("0\n")
            myfile.write("set nevents 10\n")
            myfile.write("#set ickkw 1\n")
            myfile.write("#set xqcut 10.0\n")
            myfile.write("#set ebeam1 6500\n")
            myfile.write("#set ebeam2 6500\n")
            myfile.write(ssp+"BLSSMScanLowmh/SPheno.spc.BLSSM_"+str(i)+"_"+str(j)+"\n")
            myfile.write("0\n")
myfile.close()

#ppzz4l
myfile = open(mg+'ppzz4l_blssm_low.txt', 'w')
myfile.write("#./bin/mg5_aMC ppzz4l_blssm_low.txt\n")
myfile.write("import model BLSSM/ -modelname\n")
myfile.write("define p=g u1 u1bar u2 u2bar d1 d1bar d2 d2bar d3 d3bar\n")
myfile.write("define l- = e1 e2\n")
myfile.write("define l+ = e1bar e2bar\n")
for i in range(0,n):
    for j in range(0,m):
        if(os.path.isfile(ssp+"BLSSMScanLowmh/SPheno.spc.BLSSM_"+str(i)+"_"+str(j))):
            myfile.write("generate p p > z z $ h1 / h3 h4  u1 u1bar u2 u2bar u3 u3bar d1 d1bar d2 d2bar d3 d3bar, (z > l+ l-, z > l+ l-)\n")
            myfile.write("output ppzz4l_blssm_low/ppzz4l_blssm_"+str(i)+"_"+str(j)+"\n")
            myfile.write("launch\n")
            myfile.write("0\n")
            myfile.write("set nevents 10\n")
            myfile.write("#set ickkw 1\n")
            myfile.write("#set xqcut 10.0\n")
            myfile.write("#set ebeam1 6500\n")
            myfile.write("#set ebeam2 6500\n")
            myfile.write(ssp+"BLSSMScanLowmh/SPheno.spc.BLSSM_"+str(i)+"_"+str(j)+"\n")
            myfile.write("0\n")
myfile.close()

