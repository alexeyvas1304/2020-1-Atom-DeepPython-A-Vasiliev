from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('ctest.pyx'))

# python setup.py build_ext --inplace
