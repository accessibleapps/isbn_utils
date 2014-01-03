from distutils.core import setup

__version__ = "0.1"
__doc__ = """Utilities for handling ISBNs"""

setup(
 name = "isbn_utils",
 version = __version__,
 description = __doc__,
 py_modules = ["isbn_utils"],
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
