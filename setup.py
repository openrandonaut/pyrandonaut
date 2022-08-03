from setuptools import setup
from sys import argv, exit
import glob
import os


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    exit()
elif argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('pyrandonaut.egg-info'):
        shutil.rmtree('pyrandonaut.egg-info')


setup(
    name="pyrandonaut",
    version="0.1.5",
    description="Open-source quantum random coordinate generation for randonauts.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    url="https://github.com/openrandonaut/pyrandonaut",
    author="narkopolo",
    author_email="openrandonaut@riseup.net",
    license="GPL-3.0",
    packages=["pyrandonaut"],
    python_requires=">=3.9",
    install_requires=[
    "numpy==1.23.1",
    "pandas==1.4.3",
    "quantumrandom==1.9.0",
    "scipy==1.9.0",
    "setuptools==58.1.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        'Topic :: System :: Installation/Setup',
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
