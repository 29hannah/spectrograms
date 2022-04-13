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

#Calculate centroid for every sound file and average for each distance

print("Averaged centroid from distance 1 to distance 5:")

#Distance 1
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_1")]
res_list_1 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_1.extend(cen)

'''
#To see all values separately:
print("Values for distance 1:")
print(res_list_1)
#To see which values matches which file:
print(sound_file_paths)
'''

c_1=(statistics.mean(res_list_1))
c_sd_1= (statistics.stdev(res_list_1))


#Distance 2
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_2")]
res_list_2 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_2.extend(cen)
'''
#To see all values separately:
print("Values for distance 2:")
print(res_list_2)
#To see which values matches which file:
print(sound_file_paths)
'''

c_2=(statistics.mean(res_list_2))
c_sd_2= (statistics.stdev(res_list_2))


#Distance 3
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_3")]
res_list_3 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_3.extend(cen)

'''
#To see all values separately:
print("Values for distance 3:")
print(res_list_3)
#To see which values matches which file:
print(sound_file_paths)
'''

c_3=(statistics.mean(res_list_3))
c_sd_3= (statistics.stdev(res_list_3))


#Distance 4
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_4")]
res_list_4 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_4.extend(cen)

'''
#To see all values separately:
print("Values for distance 4:")
print(res_list_4)
#To see which values matches which file:
print(sound_file_paths)
'''

c_4 = (statistics.mean(res_list_4))
c_sd_4= (statistics.stdev(res_list_4))


#Distance 5
sound_file_paths = [f for f in abs_file_paths("/Users/hannahsmacbook/Stimuli/Stimuli_J/dis_5")]
res_list_5 = []
for sound_file_path in sound_file_paths:
    sound = slab.Binaural(sound_file_path)
    cen = sound.spectral_feature(feature='centroid')
    res_list_5.extend(cen)

'''
#To see all values separately:
print("Values for distance 5:")
print(res_list_5)
#To see which values matches which file:
print(sound_file_paths)
'''

c_5 = (statistics.mean(res_list_5))
c_sd_5= (statistics.stdev(res_list_5))


#Final list with averaged centroid values for each distance
final_list_mean = [c_1, c_2, c_3, c_4, c_5]
print(final_list_mean)

#Calculate standard deviation for each distance
print("Standard deviation for each distance:")
final_list_stdev = [c_sd_1, c_sd_2, c_sd_3, c_sd_4, c_sd_5]
print(final_list_stdev)

#Relative centroid values compared to distance 1
print("Relative centroids:")
rel_cen = [x / c_1 for x in final_list_mean]
print(rel_cen)



#Creating boxplot
#Overall list with all values for each distance
overall_list= [res_list_1, res_list_2, res_list_3, res_list_4, res_list_5]

'''
print(overall_list)
'''

fig = plt.figure()
fig.suptitle('Centroid over distance categories', fontsize=10)

ax = fig.add_subplot(111)
ax.boxplot(overall_list)

ax.set_xlabel('Distance category')
ax.set_ylabel('Centroid')

'''
plt.show()
'''
plt.savefig("Centroid_pilot")

