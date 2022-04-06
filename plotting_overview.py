import os
import pathlib
from os import listdir
import matplotlib.pyplot as plt
import slab
from tkinter import Tcl



# Getting list of file names
DIR = pathlib.Path(os.getcwd())
file_path = DIR / "Stimuli_spectrogram_test_1"
file_names = [file_path / f for f in listdir(file_path) if not f.startswith('.')]



Tcl().call('lsort', '-dict', file_names)

print(file_names)

# Creating slab Objects
sound_files = [slab.Binaural(file_name) for file_name in file_names]


# Creating plot, then saving subplots in a list, so we can iterate through them
_, [[ax1, ax2, ax3], [ax4, ax5, ax6]] = plt.subplots(
                nrows=2, ncols=3, constrained_layout=True)
ax = [ax1, ax2, ax3, ax4, ax5, ax6]



#Creating spectrogram

for index, sound_file in enumerate(sound_files[0:6]):
    slab.Binaural.spectrogram(sound_file.left, axis=ax[index], show=False)


plt.savefig("spectrograms_test_stimuli_1")