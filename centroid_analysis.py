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

#Calculate centroid for every file

#Distance 1
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_1")]
res_list_1 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_1.extend(cen)

#Get list of all values for distance 1
'''print(res_list_1)'''

#Get mean centroid and stdev for distance 1
c_1 = (statistics.mean(res_list_1))
c_sd_1 = (statistics.stdev(res_list_1))


#Distance 2
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_2")]
res_list_2 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_2.extend(cen)

#Get list of all values for distance 2
'''print(res_list_2)'''

#Get mean centroid and stdev for distance 2
c_2 = (statistics.mean(res_list_2))
c_sd_2 = (statistics.stdev(res_list_2))


#Distance 3
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_3")]
res_list_3 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_3.extend(cen)

#Get list of all values for distance 3
'''print(res_list_3)'''

#Get mean centroid and stdev for distance 3
c_3 = (statistics.mean(res_list_3))
c_sd_3 = (statistics.stdev(res_list_3))


#Distance 4
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_4")]
res_list_4 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_4.extend(cen)

#Get list of all values for distance 4
'''print(res_list_4)'''

#Get mean centroid and stdev for distance 4
c_4 = (statistics.mean(res_list_4))
c_sd_4 = (statistics.stdev(res_list_4))


#Distance 5
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_5")]
res_list_5 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_5.extend(cen)

#Get list of all values for distance 5
'''print(res_list_5)'''

#Get mean centroid and stdev for distance 5
c_5 = (statistics.mean(res_list_5))
c_sd_5 = (statistics.stdev(res_list_5))


#List with averaged centroid values for each distance
print("Mean centroid from category 1 to 5:")
final_list_mean = [c_1, c_2, c_3, c_4, c_5]
print(final_list_mean)

#List with standard deviation for each category
print("Standard deviation from category 1 to 5:")
final_list_stdev = [c_sd_1, c_sd_2, c_sd_3, c_sd_4, c_sd_5]
print(final_list_stdev)

#Relative centroid values compared to distance 1
print("Relative centroids:")
rel_cen = [x / c_1 for x in final_list_mean]
print(rel_cen)


#Creating boxplot
#Overall list with all values for each distance
overall_list = [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5]

fig = plt.figure()
fig.suptitle('Centroid over distance categories', fontsize=10)

ax = fig.add_subplot(111)
ax.boxplot(overall_list)

ax.set_xlabel('Distance category')
ax.set_ylabel('Centroid')

plt.show()
'''
plt.savefig("Centroid")
'''