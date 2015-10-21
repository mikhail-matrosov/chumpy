"""
See LICENCE.txt for licensing and contact information.
"""

from distutils.core import setup
from version import version

setup(name='chumpy',
      version=version,
      packages=['chumpy'],
      package_dir={'chumpy': '.'},
      author='Matthew Loper',
      author_email='matt.loper@gmail.com',
      url='https://github.com/mattloper/chumpy',
      description='chumpy',
      license='MIT',
      install_requires=['numpy >= 1.8.1', 'scipy >= 0.13.0'],

      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: POSIX :: Linux'
                   ],
      )
