typewriter
==========

Turn your computer into a typewriter, i.e. play typewriting sounds when you
type.


How to use it
-------------

Install:

    $ python setup.py install

Run:

    $ typewriter /dev/input/platform-i8042-serio-0-event-kbd

Or something like that. Just point it to your keyboard device. Note that you
will have to probably run it under the root account so it's able to read the
device.


Known issues
------------

  * Segfault when exiting. This seems to be a bug in pyglet.


Licence
=======

Public domain.
