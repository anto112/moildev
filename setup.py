import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'Moildev'
AUTHOR = 'Haryanto'
AUTHOR_EMAIL = 'm07158031@o365.mcut.edu.tw'
URL = 'https://github.com/anto112/moildev'

LICENSE = 'MIT License '
DESCRIPTION = 'Moildev is a library that provides a sophisticated image processing'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'numpy',
    'opencv-python'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      include_package_data=True,
      package_data={"": ['moildev.so']},
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      python_requires='>=3.6',
      )
