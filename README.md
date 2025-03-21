# HEPTools-Scripts
# Introduction
When we generate events in MadGraph, a subfolder <Process/Events/run_x_y> is created which contains the events files on parton level by Madevent <unweighted_events.lhe.gz>, hadron level file via Pythia <tag_1_pythia8_events.hepmc.gz> and reco level via root <tag_1_delphes_events.root> or <tag_1_delphes_events.lhco>. 

In addition, this subfolder contains a summery report to the process <run_01_tag_1_banner.txt> which includes the seetings and results of the run and desirably at the end of the file, the cross section.

HEPTools Scripts

1. Copy, Delete, Rename&Order Scrpts
   Bash shell scripts to delete undesired events files and keep only the root and lhco files and to rename the output run_i_j files into run_k files in order
   [scripts_copy_delete_rename_ordr.tar.gz]
   (del_empty.sh, count.sh, delcp_subrun.sh, rename_order.sh, del.sh, del1.sh, delcp.sh, append_newline.sh, rename_tag_files.sh)
3. Cross Section Scripts
   [scripts_xsection.tar.xz]
