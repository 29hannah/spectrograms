import random
import slab
import os
import pathlib
from os.path import join


# Get files
def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


# Speaker specific?
folder_path = pathlib.Path

path_1 = list(pathlib.Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis1*'))
path_2 = list(pathlib.Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis2*'))
path_3 = list(pathlib.Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis3*'))
path_4 = list(pathlib.Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis4*'))
path_5 = list(pathlib.Path('/Users/hannahsmacbook/Pilot_stimuli_2').glob('*dis5*'))
sound_file_names = [path_1, path_2, path_3, path_4, path_5]


seq = slab.Trialsequence(conditions=[1, 2, 3, 4, 5], n_reps=1)

for condition in seq:
    file_name_group = sound_file_names[condition - 1]
    file_name = random.choice(file_name_group)
    slab.Sound.play_file(file_name)
    with slab.key() as key:  # wait for a key press
        key_code = key.getch()
    if key_code == 49:
        response = 1
    elif key_code == 50:
        response = 2
    elif key_code == 51:
        response = 3
    elif key_code == 52:
        response = 4
    elif key_code == 53:
        response = 5
    response_obj = {
        'sound_id': file_name.stem,
        'response': response
    }
    seq.add_response(response_obj)
out_file = 'participant_name'
seq.save_json(out_file + '.json')
