# Installation
## Windows
To use the Python example you need an installed version of Python 3.X and the python package manager pip to install dependencies.
Download the latest Python for Windows at
https://www.python.org/downloads/windows/
Python 3.4 and higher includes pip

install necessary packages in the general section

## Mac OS
To use the Python example you need an installed version of Python 3.X and the python package manager pip to install dependencies.
Download the latest Python for Mac OS at
https://www.python.org/downloads/mac-osx/
Python 3.4 and higher includes pip

install necessary packages in the general section

## Linux 
Use your distributions package manager to install Python 3.X and pip
### Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip
```
note : some distributions may use the command pip3 instead of pip, you can check by looking for the Python version number specified in
```bash
pip --version
```

install necessary packages in the general section

### RHEL
```bash 
dnf install python3 python3-pip
# Set python3 default (optional)
alternatives --set python /usr/bin/python3
```
## General  
To run the example 2 Python libraries need to be installed
* requests
* numpy

run the following command to install, use the pip (or pip3 depending on installation) command

```bash
pip install requests numpy
```