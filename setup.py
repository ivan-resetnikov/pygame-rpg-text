from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = ''


setup(
	name="RPG-text-engine",
	version=VERSION,
	author="LowRezCat (Ivan Resetnikov)",
	author_email="ivan.resetnikov.alpha@gmail.com",
	description=DESCRIPTION,
	packages=find_packages(),
	install_requires=['pygame'],
	keywords=['python', 'pygame', 'text', 'rpg', 'font', 'text effects'],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Microsoft :: Windows",
	]
)