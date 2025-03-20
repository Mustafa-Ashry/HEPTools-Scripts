###############################################################
## This file code was created by Mustafa Ashry in March 2020 ##
###############################################################
# PART II ## Extract xsection and parameters from MG #
import re
import os
import shutil
import subprocess
#from distutils.dir_util import copy_tree

#variables and paths
n=150;
m=2000;
ssp="/home/mashry/hep/SSP-1.2.5/Output/";
mg="/home/mashry/hep/MG5_aMC_v2_6_4/";
dat=["TanBeta","gBL","gYB","mC12","mC22","x1","x2","hh_2","M1","M2","M3","HB Result (1: allowed, 0: excluded, -1: unphysical)","HS total Chi^2","xsection"];
prcs=["pphhaabb","ppzz4l"];
prcs1=["pphhaabb"];
prcs2=["ppzz4l"];
#prcs=prcs1;
mdl=["blssm"];
scale=["high","low"];

# Copy scan results from DB
""" for i in range(0,n):
	if(os.path.exists("/home/mashry/Dropbox/00/BLSSMScanLowmh"+str(i))):
		copy_tree("/home/mashry/Dropbox/00/BLSSMScanLowmh"+str(i),ssp+"BLSSMScanLowmh"+str(i))
		shutil.move("/home/mashry/Dropbox/00/BLSSMScanLowmh"+str(i),ssp+"BLSSMScanLowmh"+str(i))
		print("DB/BLSSMScanLowmh"+str(i))
 """
# Calling the shell script for splitting
#subprocess.call(['sh','./script_split.sh'])

#Read Order xsection
import csv
datContent = [i.strip().split() for i in open(ssp+"pphhaabb_xsection_order.dat")).readlines()]

""" # Remove old cross sections and parameters files
for p in range(len(prcs)):
	for i in range(len(dat)):
		if(os.path.isfile(ssp+prcs[p]+"_"+dat[i]+".dat")):
			os.remove(ssp+prcs[p]+"_"+dat[i]+".dat")

# Copy MC reports and delete other unwanted MG output files
for p in range(len(prcs)):
	for i in range(0,n):
		for j in range(0,m):
			if(os.path.isfile(mg+prcs[p]+"_blssm_low/pphhaabb_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt")):
				shutil.copyfile(mg+prcs[p]+"_blssm_low/"+prcs[p]+"_blssm_"+str(i)+"_"+str(j)+"/Events/run_01/run_01_tag_1_banner.txt", mg+prcs[p]+"_blssm_low/run_"+str(i)+"_"+str(j)+".txt") and shutil.rmtree(mg+prcs[p]+"_blssm_low/"+prcs[p]+"_blssm_"+str(i)+"_"+str(j))
				print(prcs[p]+"_"+str(i)+"_"+str(j))
# Copy run files from DB
for p in range(len(prcs)):
	for i in range(0,n):
		for j in range(0,m):
			if(os.path.isfile("/home/mashry/Dropbox/00/"+prcs[p]+"/"+"run_"+str(i)+"_"+str(j)+".txt")):
				shutil.move("/home/mashry/Dropbox/00/"+prcs[p]+"/"+"run_"+str(i)+"_"+str(j)+".txt",mg+prcs[p]+"_blssm_low/run_"+str(i)+"_"+str(j)+".txt")
				print("DB/"+prcs[p]+"_"+str(i)+"_"+str(j))

# Extract cross sections and parameters
for p in range(len(prcs)):
	for i in range(0,n):
		for j in range(0,m):
			if(os.path.isfile(mg+prcs[p]+"_blssm_low/run_"+str(i)+"_"+str(j)+".txt")):
				open(ssp+prcs[p]+"_xsection.dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.strip("#  Integrated weight (pb)  :") for l in open(mg+prcs[p]+"_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "#  Integrated weight (pb)  :" in l]) 
				for k in range(len(dat)):
					open(ssp+prcs[p]+"_"+dat[k]+".dat", "a").writelines([str(i)+"_"+str(j)+"  "+l.replace("  # "+dat[k],"") for l in open(mg+prcs[p]+"_blssm_low/run_"+str(i)+"_"+str(j)+".txt").readlines() if "# "+dat[k]+"\n" in l]) 
				print(prcs[p]+"_"+str(i)+"_"+str(j))
	print("\nEnd of process: "+prcs[p])
 """ 
# PART III ## Create MG script #
""" gen=["generate p p > h1 h1 $ h1 / h3 h4  u1 u1bar u2 u2bar u3 u3bar d1 d1bar d2 d2bar d3 d3bar, h1 > a a, h1 > d3 d3bar\n","generate p p > z z $ h1 / h3 h4  u1 u1bar u2 u2bar u3 u3bar d1 d1bar d2 d2bar d3 d3bar, (z > l+ l-, z > l+ l-)\n"];
#defn=["define p=g u1 u1bar u2 u2bar d1 d1bar d2 d2bar d3 d3bar\n","0"];
for p in range(len(prcs)):
	myfile = open(mg+prcs[p]+'_blssm_low.txt', 'w')
	myfile.write("#./bin/mg5_aMC "+prcs[p]+"_blssm_low.txt\n")
	myfile.write("import model BLSSM/ -modelname\n")
	myfile.write("define p=g u1 u1bar u2 u2bar d1 d1bar d2 d2bar d3 d3bar\n")
	for i in range(0,n):
	    for j in range(0,m):
        	if(os.path.isfile(ssp+"BLSSMScanLowmh/SPheno.spc.BLSSM_"+str(i)+"_"+str(j))):
            	myfile.write(gen[p])
            	myfile.write("output "+prcs[p]+"_blssm_low/"+prcs[p]+"_blssm_"+str(i)+"_"+str(j)+"\n")
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
	print("MG command line was written for: "+prcs[p]) """

""" #pphhaabb
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
print("MG command line was written for: pphhaabb")

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
print("MG command line was written for: ppzz4l")
 """
