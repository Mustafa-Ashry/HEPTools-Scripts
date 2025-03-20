
#bkg
path1w="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HWW"
path1z="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/HZZ"
path1h="/HEP_DATA/Mostafa/H400_BLSSM_Bkg/Hhhaabb"
#sg
path2w="/HEP_DATA/Mostafa/H400_BLSSM/HWW"
path2z="/HEP_DATA/Mostafa/H400_BLSSM/HZZ"
path2h="/HEP_DATA/Mostafa/H400_BLSSM/Hhhaabb"

for k in $(seq 200 450)
do
	for j in $(seq 2 10)
	do
#bkg
			mv $path1w'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path1w'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path1w'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path1w'/run_'"$k"'/tag_1_delphes_events.root'
			mv $path1z'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path1z'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path1z'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path1z'/run_'"$k"'/tag_1_delphes_events.root'
			mv $path1h'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path1h'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path1h'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path1h'/run_'"$k"'/tag_1_delphes_events.root'
#sg
			mv $path2w'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path2w'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path2w'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path2w'/run_'"$k"'/tag_1_delphes_events.root'
			mv $path2z'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path2z'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path2z'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path2z'/run_'"$k"'/tag_1_delphes_events.root'
			mv $path2h'/run_'"$k"'/tag_'"$j"'_delphes_events.lhco.gz' $path2h'/run_'"$k"'/tag_1_delphes_events.lhco.gz'
			mv $path2h'/run_'"$k"'/tag_'"$j"'_delphes_events.root' $path2h'/run_'"$k"'/tag_1_delphes_events.root'
			echo $k $j
	done
done






