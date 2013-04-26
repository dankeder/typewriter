#!/usr/bin/env python

from evdev import InputDevice, ecodes
from select import select
import pyglet

def main():
    dev = InputDevice('/dev/input/by-path/platform-i8042-serio-0-event-kbd')
    allowed = range(ecodes.KEY_A, ecodes.KEY_Z + 1) + \
            range(ecodes.KEY_0, ecodes.KEY_9 + 1) + \
            [ecodes.KEY_ENTER, ecodes.KEY_BACKSPACE]
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.type == ecodes.EV_KEY and event.value == 0:
                if event.code in allowed:
                    play('/home/dan/tmp/typewriter/sounds/stroke.wav')
                    # if event.code == ecodes.KEY_ENTER:
                    #     play('/home/dan/tmp/typewriter/sounds/cink.wav')
                    # else:
                    #     play('/home/dan/tmp/typewriter/sounds/stroke.wav')


def play(fname):
    snd = pyglet.media.load(fname, streaming=False)
    snd.play()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
