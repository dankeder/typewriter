import os

from setuptools import setup, find_packages
from subprocess import Popen, PIPE

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


setup(name='typewriter',
        version='0.1',
        description='Play typewriter sounds when pressing keys',
        long_description=README,
        classifiers=[
                "Programming Language :: Python",
            ],
        author='Dan Keder',
        author_email='dan.keder@gmail.com',
        url='http://github.com/dankeder/typewriter',
        keywords='typewriter sounds',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[],
        entry_points={
                'console_scripts': [ 'typewriter = typewriter:main' ]
            }
    )

# vim: expandtab
