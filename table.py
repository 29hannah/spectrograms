import slab
import statistics
import os
import pathlib
from os.path import join
import pandas as pd

#Get files
def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))
folder_path = pathlib.Path
all_file_names = [f for f in abs_file_paths("/Users/hannahsmacbook/Original files_pilot2/pilot_2_J")]


names_of_files = ['%{0}%'.format(filenames) for filenames in all_file_names]
sound_id=[elem[39:60] for elem in names_of_files]#edit the right numbers!
pre_projected_distance=[elem[85:86] for elem in names_of_files]#edit the right numbers!
projected_distance=[int(elem) for elem in pre_projected_distance]

centroid_list=[]
onset_slope_list=[]
rolloff_list=[]

for file_name in all_file_names:
    sound = slab.Binaural(file_name)
    centroid = statistics.mean(sound.spectral_feature(feature='centroid'))
    centroid_list.append(centroid)
    onset_slope = sound.onset_slope()
    onset_slope_list.append(onset_slope)
    rolloff = statistics.mean(sound.spectral_feature(feature='rolloff'))
    rolloff_list.append(rolloff)


features_object = dict(zip(sound_id, zip (projected_distance,centroid_list, onset_slope_list, rolloff_list)))

with open('Pilot_stimuli_analysis_J.csv', 'w') as f:
    for key in features_object.keys():
        f.write("%s, %s\n" % (key, features_object[key]))

#Add column names
df = pd.read_csv('Pilot_stimuli_analysis_J.csv', header=None)
df.rename(columns={0: 'sound_id', 1: 'projected_distance', 2:'centroid', 3: 'onset_slope', 4: 'rolloff'}, inplace=True)
df.to_csv('Final_Pilot_stimuli_analysis_J.csv', index=False)
