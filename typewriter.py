#!/usr/bin/env python

from evdev import InputDevice, ecodes
from select import select
import pyglet
import time

def main():
    dev = InputDevice('/dev/input/by-path/platform-i8042-serio-0-event-kbd')

    allowed = range(ecodes.KEY_A, ecodes.KEY_Z + 1) + \
            range(ecodes.KEY_0, ecodes.KEY_9 + 1) + [   
                    ecodes.KEY_DOT, ecodes.KEY_COMMA, ecodes.KEY_ENTER,
                    ecodes.KEY_BACKSPACE, ecodes.KEY_SPACE, ecodes.KEY_PAGEUP,
                    ecodes.KEY_PAGEDOWN, ecodes.KEY_LEFT, ecodes.KEY_RIGHT,
                    ecodes.KEY_UP, ecodes.KEY_DOWN
                ]

    snd_stroke = pyglet.media.load('/home/dan/tmp/typewriter/sounds/stroke.wav', streaming=False)
    snd_cink = pyglet.media.load('/home/dan/tmp/typewriter/sounds/cink.wav', streaming=False)
    player_stroke = pyglet.media.ManagedSoundPlayer()
    player_stroke.queue(snd_stroke)
    player_cink = pyglet.media.ManagedSoundPlayer()
    player_cink.queue(snd_cink)
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.type == ecodes.EV_KEY and event.value == 0:
                if event.code in allowed:
                    if event.code == ecodes.KEY_ENTER:
                        player_cink.seek(0)
                        player_cink.play()
                    else:
                        player_stroke.seek(0)
                        player_stroke.play()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
