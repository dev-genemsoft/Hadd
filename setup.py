#!/usr/bin/python

# Hadd framework
 
# An open source application development framework for Python 3.x or newer

# NOTICE OF LICENSE
 
# Licensed under the Open Software License version 3.0
 
# This source file is subject to the Open Software License (OSL 3.0) that is
# bundled with this package in the files license.txt / license.rst.  It is
# also available through the world wide web at this URL:
# http://opensource.org/licenses/OSL-3.0
# If you did not receive a copy of the license and are unable to obtain it
# through the world wide web, please send an email to
# contacto@genemsoft.com so we can send you a copy immediately. 

from Application.Configuration import Configuration
# Imports the configuration file for the application.

if not Configuration.enviroment:
    Configuration.enviroment = "development"
# Checks if the application enviroment is set to something.
# Set the application enviroment to development in case is not set.




