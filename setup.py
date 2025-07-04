from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappepilot/__init__.py
from frappepilot import __version__ as version

setup(
	name="frappepilot",
	version=version,
	description="An intelligent, role-based AI assistant for ERPNext",
	author="kbtisuu",
	author_email="kbtisuu@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

