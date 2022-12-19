from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event_booking/__init__.py
from event_booking import __version__ as version

setup(
	name="event_booking",
	version=version,
	description="Event Management System",
	author="OPS",
	author_email="admin@onpointsoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
