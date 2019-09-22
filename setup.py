from setuptools import setup, find_packages
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).parent


def readme():
    readme = REPO_ROOT / 'README.md'
    if readme.exists():
        return readme.read_text()
    return ''

setup(name='colorlogging',
      version='0.1',
      description='ColorFormatter class for logging module.',
      long_description=readme(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
      ],
      keywords='logging color',
      url='https://github.com/filwie/cologging',
      author='Filip Wiechec',
      author_email='filip.wiechec@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['incolor'],
      include_package_data=True,
      zip_safe=False)
