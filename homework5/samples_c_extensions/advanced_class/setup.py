from distutils.core import setup, Extension

module = Extension("custom2", sources=["sample.c"])
setup(name="PackageName",
      version="1.0",
      description="this is a package for myModule",
      ext_modules=[module])