import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
      name = 'spoken_english_to_written_english',
      packages = ['spoken_english_to_written_english'],
      version='0.01',
      description='Spoken english to written english conversion system',
      author='Shubham Bindal',
      author_email='201751054@iiitvadodara.ac.in',
      url='https://github.com/Shubhambindal2017/spoken_english_to_written_english',
     )
