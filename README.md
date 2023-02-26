# Log-Writer
A simple log writing script in Python with a timestamp, title, and description

# How to Use
This is a simple Python script that will allow you to write log files in order to keep track of whatever you want by only needing to enter a title for the log entry as well as a description. The purpose behind this was to assist with keeping track of a workflow during a penetration test and having things organized by a timestamp. As of right now, there is only one current version of the script. I plan on creating a few different versions to allow added functionality. Currently, the only thing to edit is the path and name of the file to write to. I plan on using the os library rather than hardcoding a path in. Future plans include using the sys library as well so that output from a command can be piped directly into the description without needing to copy/paste.
