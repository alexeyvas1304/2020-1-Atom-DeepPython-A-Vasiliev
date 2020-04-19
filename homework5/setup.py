from distutils.core import setup, Extension

module = Extension("matrix", sources=["matrix.c"])
setup(name="PackageName",
      version="1.0",
      description="this is a package for matrix",
      ext_modules=[module])