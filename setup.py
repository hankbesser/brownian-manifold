from setuptools import find_packages
from numpy.distutils.core import setup

descr = """Tools to simulate and visualize Brownian motion on manifolds."""

DISTNAME = 'brownian-manifold'
DESCRIPTION = descr
MAINTAINER = 'Hank Besser'
MAINTAINER_EMAIL = 'hbess1113@gmail.com'
LICENSE = 'MIT'
URL = 'https://github.com/hankbesser/brownian-manifold'
DOWNLOAD_URL = 'https://github.com/hankbesser/brownian-manifold.git'
VERSION = '0.1.dev0'

if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          url=URL,
          download_url=DOWNLOAD_URL,
          long_description=open('README.md').read(),
          classifiers=[
              'Programming Language :: Python',
          ],
          platforms='any',
          packages=['brownian_manifold'],
          )
