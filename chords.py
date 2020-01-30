import os
import random
import sys
from itertools import product, chain
from time import sleep

KEYS = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']

FLAVOUR = {
    'major': 'maj7',
    'minor': 'm7',
    'dominant': '7',
    'half_diminished': 'm7b5',
    'diminished': '-7'
}

if __name__ == '__main__':
    major_chords = [f"{key}{FLAVOUR['major']}" for key in KEYS]
    minor_chords = [f"{key}{FLAVOUR['minor']}" for key in KEYS]
    dominant_chords = [f"{key}{FLAVOUR['dominant']}" for key in KEYS]
    half_diminished_chords = [f"{key}{FLAVOUR['half_diminished']}" for key in KEYS]
    diminished_chords = [f"{key}{FLAVOUR['diminished']}" for key in KEYS]

    all_chords = list(chain(major_chords, minor_chords, dominant_chords, half_diminished_chords, diminished_chords))

    while True:
        os.system('clear')
        sys.stdout.write(f"{random.choice(all_chords)}           \r")
        sys.stdout.flush()
        sleep(1)
