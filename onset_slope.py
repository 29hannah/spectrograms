import slab
import statistics
import os
import pathlib
from os.path import join
import matplotlib.pyplot as plt


def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


folder_path = pathlib.Path

#Calculate onset_slope for every file

#Distance 1
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2/pilot_2_J/laughter_J_dis1")]
res_list_1 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    onset = sound.onset_slope()
    res_list_1.append(onset)

#Get list of all values for distance 1:
'''print(res_list_1)'''

#Get mean onset slope and stdev for distance 1
onset_1 = (statistics.mean(res_list_1))
o_sd_1 = (statistics.stdev(res_list_1))


#Distance 2
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2/pilot_2_J/laughter_J_dis2")]
res_list_2 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    onset = sound.onset_slope()
    res_list_2.append(onset)

#Get list of all values for distance 2:
'''print(res_list_2)'''

#Get mean onset slope and stdev for distance 2
onset_2 = (statistics.mean(res_list_2))
o_sd_2 = (statistics.stdev(res_list_2))


#Distance 3
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2/pilot_2_J/laughter_J_dis3")]
res_list_3 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    onset = sound.onset_slope()
    res_list_3.append(onset)

#Get list of all values for distance 3:
'''print(res_list_3)'''

#Get mean onset slope and stdev for distance 3
onset_3 = (statistics.mean(res_list_3))
o_sd_3 = (statistics.stdev(res_list_3))


#Distance 4
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2/pilot_2_J/laughter_J_dis4")]
res_list_4 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    onset = sound.onset_slope()
    res_list_4.append(onset)

#Get list of all values for distance 4:
'''print(res_list_4)'''

#Get mean onset slope and stdev for distance 4
onset_4 = (statistics.mean(res_list_4))
o_sd_4 = (statistics.stdev(res_list_4))

#Distance 5
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Pilot_stimuli_2/pilot_2_J/laughter_J_dis5")]
res_list_5 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.onset_slope()
    res_list_5.append(cen)

#Get list of all values for distance 5:
'''print(res_list_5)'''

#Get mean onset slope and stdev for distance 5
onset_5 = (statistics.mean(res_list_5))
o_sd_5 = (statistics.stdev(res_list_5))


#List with averaged values of onset_slope for every distance
print("Mean onset slope from category 1 to 5:")
final_list_mean = [onset_1, onset_2, onset_3, onset_4, onset_5]
print(final_list_mean)

#List with standard deviation for each distance
print("Standard deviation for category 1 to 5:")
final_list_stdev = [o_sd_1, o_sd_2, o_sd_3, o_sd_4, o_sd_5]
print(final_list_stdev)

#Relative onset_slope values compared to distance 1
print("Relative onset_slope:")
rel_onset = [x / onset_1 for x in final_list_mean]
print(rel_onset)


#Creating boxplot
#Overall list with all values for each distance
overall_list = [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5]

fig = plt.figure()
fig.suptitle('Onset_slope', fontsize=10)

ax = fig.add_subplot(111)
ax.boxplot(overall_list)

ax.set_xlabel('Distance category')
ax.set_ylabel('Onset slope')

plt.show()
'''
plt.savefig("Onset_slope")
'''