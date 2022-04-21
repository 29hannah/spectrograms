import slab
import statistics
import os
import pathlib
from os.path import join

#Get files
def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))
folder_path = pathlib.Path
all_file_names = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2")]


names_of_files = ['%{0}%'.format(filenames) for filenames in all_file_names]
sound_id=[elem[39:60] for elem in names_of_files]#edit the right numbers!
projected_distance=[elem[50:54] for elem in names_of_files]#edit the right numbers!

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

with open('Pilot_stimuli_analysis.csv', 'w') as f:
    for key in features_object.keys():
        f.write("%s, %s\n" % (key, features_object[key]))
