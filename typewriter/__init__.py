from evdev import InputDevice, ecodes
from select import select
import pyglet
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
            description='Typewriter sounds')

    parser.add_argument('device',
            type=str,
            help="path to the input device",
            )

    return parser.parse_args()


def main():
    args = parse_args()

    dev = InputDevice(args.device)

    allowed_keys = [
            ecodes.KEY_A, ecodes.KEY_B, ecodes.KEY_D, ecodes.KEY_E,
            ecodes.KEY_F, ecodes.KEY_G, ecodes.KEY_H, ecodes.KEY_I,
            ecodes.KEY_J, ecodes.KEY_K, ecodes.KEY_L, ecodes.KEY_M,
            ecodes.KEY_N, ecodes.KEY_O, ecodes.KEY_P, ecodes.KEY_Q,
            ecodes.KEY_R, ecodes.KEY_S, ecodes.KEY_T, ecodes.KEY_U,
            ecodes.KEY_V, ecodes.KEY_W, ecodes.KEY_X, ecodes.KEY_Y,
            ecodes.KEY_Z, ecodes.KEY_0, ecodes.KEY_1, ecodes.KEY_2,
            ecodes.KEY_3, ecodes.KEY_4, ecodes.KEY_5, ecodes.KEY_6,
            ecodes.KEY_7, ecodes.KEY_8, ecodes.KEY_9, ecodes.KEY_DOT,
            ecodes.KEY_COMMA, ecodes.KEY_ENTER, ecodes.KEY_BACKSPACE,
            ecodes.KEY_SPACE, ecodes.KEY_PAGEUP, ecodes.KEY_PAGEDOWN,
            ecodes.KEY_LEFT, ecodes.KEY_RIGHT, ecodes.KEY_UP, ecodes.KEY_DOWN,
            ecodes.KEY_TAB, ecodes.KEY_GRAVE, ecodes.KEY_SEMICOLON,
            ecodes.KEY_APOSTROPHE, ecodes.KEY_RIGHTBRACE, ecodes.KEY_LEFTBRACE,
            ecodes.KEY_BACKSLASH, ecodes.KEY_MINUS, ecodes.KEY_SLASH,
            ecodes.KEY_EQUAL, ecodes.KEY_HOME, ecodes.KEY_END
        ]

    snd_stroke = pyglet.media.load('sounds/stroke.wav', streaming=False)
    snd_cink = pyglet.media.load('sounds/cink.wav', streaming=False)

    player_cink = pyglet.media.Player()
    player_cink.queue(snd_cink)
    player_cink.eos_action = pyglet.media.Player.EOS_PAUSE

    player_stroke = pyglet.media.Player()
    player_stroke.queue(snd_stroke)
    player_stroke.eos_action = pyglet.media.Player.EOS_PAUSE
    while True:
        select([dev], [], [])
        for event in dev.read():
            if event.type == ecodes.EV_KEY and event.value in (0, 2):
                if event.code in allowed_keys:
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
