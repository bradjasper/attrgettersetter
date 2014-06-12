from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='attrgettersetter',
      version=version,
      description="Attribute getter and setter helper tools (useful for attribute.dot.syntax)",
      long_description="""\
This module provides a more flexible version of operator.attrgetter (supports default params) and a new attrsetter function""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='attr attribute getter setter',
      author='Brad Jasper',
      author_email='contact@bradjasper.com',
      url='http://bradjasper.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
