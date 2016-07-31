import os
import re
from distutils.sysconfig import get_python_lib

from setuptools import setup

long_description = """
TortoiseSVN plugin for RIDE(robotframework IDE) adds additional menu item
to trigger TortoiseSVN (it has to be installed separately) commands.
So that RIDE users can update/commit/etc. directly from RIDE.""".strip()

# set DISTUTILS_DEBUG=1
# plugin_file_dir = os.path.normpath(os.path.expandvars("%APPDATA%/RobotFramework/ride/plugins/"))
PLUGIN_FILE = 'TortoiseSVNPlugin.py'


def get_version():
    with open(PLUGIN_FILE) as file:
        match = re.search("VERSION\s*=\s*'(.*?)'", file.read())
        if match:
            version = match.group(1)
        else:
            raise ValueError("Cannot get current version of plugin.")
        return version


plugin_file_dir_siteplugins = os.path.join(get_python_lib(), 'robotide', 'site-plugins')

setup(
    name='robotframework_ride_tortoisesvn',
    version=get_version(),
    # package_dir={'robotide.site-plugins': '.'},
    # py_modules=['TortoiseSVNPlugin'],
    # package_data={'robotide.site-plugins': ['TortoiseSVNPlugin.py']},
    # packages=find_packages(),
    data_files=[(plugin_file_dir_siteplugins, [PLUGIN_FILE])],
    url='https://github.com/ukostas/robotframework-ride-tortoisesvn',
    license=None,
    author='ukostas',
    author_email=None,
    description='TortoiseSVN plugin for Robotframework IDE (RIDE).',
    long_description=long_description,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Environment :: Plugins',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Framework :: Robot Framework',
                 'Operating System :: Microsoft :: Windows'],
    keywords='robotframework testing testautomation tortoise svn plugin ride',
    install_requires=['robotframework-ride']
)
