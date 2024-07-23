A trick that I've found useful is to make a toolbox of methods that I re-use often. That way, when I need to, say, read and parse a quirky file format I can just do this

from toolbox import texttools as ttl
ttl.parse_weird_file(filename)
where parse_weird_file() is a function that I meticulously copied, pasted, and tweaked from StackOverflow a long time ago. There are a few steps at the command line to set this up, but nothing too hairy.

Navigate to the directory you want this to live.
mkdir -p toolbox/toolbox.
touch toolbox/toolbox/__init__.py.
echo "from setuptools import setup" > toolbox/setup.py
echo "setup(name='toolbox')" >> toolbox/setup.py
python3 -m pip install -e toolbox
Create toolbox/toolbox/texttools.py containing the function parse_weird_file() and you are good to go!
Now any changes you make to texttools.py or any other files you add to toolbox/toolbox will be available for python3 to import, no matter which directory you're working in. It's guaranteed to cut your googling time in half.