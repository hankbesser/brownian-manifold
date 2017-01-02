#! /usr/bin/env python3


import setuptools 
from numpy.distutils.core import setup

descr = """Tools to simulate and visualize Brownian motion on manifolds"""


DISTNAME = 'brownian-manifold'
DESCRIPTION = descr
MAINTAINER = 'Hank Besser'
MAINTAINER_EMAIL = 'hbess1113@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/hankbesser/brownian-manifold.git'
VERSION = '0.1.0'



if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.md').read(),
          platforms='any',
          package_dir={'brownian-manifold': 'brownian_manifold'},
          packages=['brownian-manifold'],
          )