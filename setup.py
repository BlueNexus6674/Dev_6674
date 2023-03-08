import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dev-6674",
    version = "0.0.4",
    author = "Andrew Carter",
    author_email = "andrewjcarter@gmail.com",
    description = ("An demonstration "),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "https://github.com/BlueNexus6674/Dev_6674",
    packages = ['devpip/Main'],
    scipts = ['devpip'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
