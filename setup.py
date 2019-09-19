from setuptools import setup, find_packages
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).parent


def readme() -> str:
    readme = REPO_ROOT / 'README.md'
    if readme.exists():
        return readme.read_text()
    return ''


def requirements() -> List[str]:
    requirements = REPO_ROOT / 'requirements.txt'
    if requirements.exists():
        r = requirements.read_text()
        return r.split()
    return []


setup(name='colorlogging',
      version='0.0.1',
      description='Logging formatter ',
      long_description=readme(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
      ],
      keywords='',
      url='',
      author='',
      author_email='',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements(),
      include_package_data=True,
      zip_safe=False)
