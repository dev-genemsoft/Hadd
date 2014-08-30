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
 
"""
Package         Application.Configuration 
Author          Fernando de la Cruz
Copyright       Copyright (c) 2014, Genemsoft, Inc. (http://www.genemsoft.com)
License         http://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)
Link            http://www.genemsoft.com/Hadd
Since           Version 0.1
"""

enviroment = "development"
"""
|-------------------------------------------------------------------------------|
|  Application Enviroment                                                       |
|-------------------------------------------------------------------------------|
|                                                                               |
| You can load different configurations depending on your                       |
| current environment. Setting the environment also influences                  |
| things like logging and error reporting.                                      |
|                                                                               |
| This can be set to anything, but default usage is:                            |
|                                                                               |
|    development                                                                |
|    testing                                                                    |
|    production                                                                 |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
index_page = "index.html"
"""
|-------------------------------------------------------------------------------|
| Base Site URL                                                                 |
|-------------------------------------------------------------------------------|
|                                                                               |
| URL to your Hadd application root. Typically this will be your base URL,   |
| WITH a trailing slash:                                                        |
|                                                                               |
|   http://www.example.com/                                                     |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
language = "English"
"""
|-------------------------------------------------------------------------------|
| Default Language                                                              |
|-------------------------------------------------------------------------------|
|                                                                               |
| This determines which set of language files should be used. Make sure         |
| there is an available translation if you intend to use something other        |
| than English.                                                                 |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
charset = "UTF-8"
"""
|-------------------------------------------------------------------------------|
| Default Character Set                                                         |
|-------------------------------------------------------------------------------|
|                                                                               |
| This determines which character set is used by default in various methods     |
| that require a character set to be provided.                                  |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
enable_extensions = False
"""
|-------------------------------------------------------------------------------|
| Enable/Disable System Extensions                                              |
|-------------------------------------------------------------------------------|
|                                                                               |
| If you would like to use the 'extensions' feature you must enable it by       |
| setting this variable to TRUE (boolean).  See the user guide for details.     |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
subclass_prefix = "MY_"
"""
|-------------------------------------------------------------------------------|
| Class Extension Prefix                                                        |
|-------------------------------------------------------------------------------|
|                                                                               |
| This item allows you to set the filename/classname prefix when extending      |
| native libraries.                                                             |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
permitted_uri_chars = "a-z 0-9~%.:_\-"
"""
|-------------------------------------------------------------------------------|
| Allowed URL Characters                                                        |
|-------------------------------------------------------------------------------|
|                                                                               |
| This lets you specify which characters are permitted within your URLs.        |
| When someone tries to submit a URL with disallowed characters they will       |
| get a warning message.                                                        |
|                                                                               |
| As a security measure you are STRONGLY encouraged to restrict URLs to         |
| as few characters as possible.  By default only these are allowed:            |
| a-z 0-9~%.:_-                                                                 |
|                                                                               |
| Leave blank to allow all characters -- but only if you are insane.            |
|                                                                               |
| The configured value is actually a regular expression character group         |
| and it will be executed as: ! preg_match('/^[<permitted_uri_chars>]+$/i       |
|                                                                               |
| DO NOT CHANGE THIS UNLESS YOU FULLY UNDERSTAND THE REPERCUSSIONS!!            |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
log_threshold = 0
"""
|-------------------------------------------------------------------------------|
| Error Logging Threshold                                                       |
|-------------------------------------------------------------------------------|
|                                                                               |
| If you have enabled error logging, you can set an error threshold to          |
| determine what gets logged. Threshold options are:                            |
| You can enable error logging by setting a threshold over zero. The            |
| threshold determines what gets logged. Threshold options are:                 |
|                                                                               |
|	0 = Disables logging, Error logging TURNED OFF                          |
|	1 = Error Messages (including python errors)                            |
|	2 = Debug Messages                                                      |
|	3 = Informational Messages                                              |
|	4 = All Messages                                                        |
|                                                                               |
| You can also pass in a array with threshold levels to show individual error   |
| types                                                                         |
|                                                                               |
| 	array(2) = Debug Messages, without Error Messages                       |
|                                                                               |
| For a live site you'll usually only enable Errors (1) to be logged otherwise  |
| your log files will fill up very fast.                                        |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
log_path = ""
"""
|-------------------------------------------------------------------------------|
| Error Logging Directory Path                                                  |
|-------------------------------------------------------------------------------|
|                                                                               |
| Leave this BLANK unless you would like to set something other than the default|
| application/logs/ directory. Use a full server path with trailing slash.      |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
log_file_extension = ""
"""
|-------------------------------------------------------------------------------|
| Log File Extension                                                            |
|-------------------------------------------------------------------------------|
|                                                                               |
| The default filename extension for log files. The default 'php' allows for    |
| protecting the log files via basic scripting, when they are to be stored      |
| under a publicly accessible directory.                                        |
|                                                                               |
| Note: Leaving it blank will default to 'py'.                                  |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
log_date_format = "Y-m-d H:i:s"
"""
|-------------------------------------------------------------------------------|
| Date Format for Logs                                                          |
|-------------------------------------------------------------------------------|
|                                                                               |
| Each item that is logged has an associated date. You can use Python date      |
| codes to set your own date formatting                                         |
|                                                                               |
|-------------------------------------------------------------------------------|
"""
error_views_path = ""
"""
|-------------------------------------------------------------------------------|
| Error Views Directory Path                                                    |
|-------------------------------------------------------------------------------|
|                                                                               |
| Leave this BLANK unless you would like to set something other than the default|
| application/views/errors/ directory.  Use a full server path with trailing    |
| slash.                                                                        |
|                                                                               |
|-------------------------------------------------------------------------------|
"""