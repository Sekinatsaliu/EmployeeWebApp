import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
long_description = fh.read()
setuptools.setup(
name="emplyee_properties-pkg-YOUR-USERNAME-HERE",
# Replace with your own username above
version="0.0.1",
author="Sekinat Saliu",
author_email="x20219253@student.ncirl.ie",
description="A employee properties library",
long_description=long_description,
long_description_content_type="text/markdown",
url="",
packages=setuptools.find_packages(),
# if you have libraries that your module/package/library
#you would include them in the install_requires argument
install_requires=[''],
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires='>=3.6',
)
