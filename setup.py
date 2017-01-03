from setuptools import setup, find_packages

from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='brownian-manifold',
    maintainer='Hank Besser',
    maintainer_email='hbess1113@gmail.com',
    description='Tools to simulate and visualize Brownian motion on manifolds',
    long_description=long_description,
    license='MIT',
    version='0.1.0',
    url = 'https://github.com/hankbesser/brownian-manifold',
    download_url='https://github.com/hankbesser/brownian-manifold.git',
    packages=find_packages(),
)