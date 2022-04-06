import os
import pathlib
from os import listdir
import matplotlib.pyplot as plt
import slab
from tkinter import Tcl



# Getting list of file names
DIR = pathlib.Path(os.getcwd())
file_path = DIR / "Stimuli_spectrogram_test_2"
file_names = [file_path / f for f in listdir(file_path) if not f.startswith('.')]



Tcl().call('lsort', '-dict', file_names)

print(file_names)

sound_files = [slab.Binaural(file_name) for file_name in file_names]

for index, sound_file in enumerate(sound_files[0:6]):
    slab.Binaural.spectrogram(sound_file.left, show=True)