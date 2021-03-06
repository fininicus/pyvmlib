"""Setup config for pyvmlib."""

from setuptools import setup

setup(name='pyvmlib',
      version='2.3.0',
      description='A simple library for controlling VMware vSphere servers.',
      url='http://github.com/cambridgeconsultants/pyvmlib',
      author='Cambridge Consultants',
      author_email='jonathan.pallant@cambridgeconsultants.com',
      license='Apache-2.0',
      install_requires=[
        'pyvmomi',
        'requests',
        'six',
      ],
      packages=['pyvmlib'],
      zip_safe=False)
