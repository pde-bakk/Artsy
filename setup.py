#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="Artsy Coding Contest",
	version="0.0.0.1",
	description="Terminal art.",
	long_description="Create some beautifull terminal art.",
	url="https://github.com/pde-bakk/Artsy",
	author=":kissahomie:",
	license='MIT',
	packages = find_packages(),
	install_requires = ['Pillow'],
)