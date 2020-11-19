"""Demo of sys.argv().

Call this script with arguments. For example, the following command...

$ python3 argv.py this is a test

...prints out...

sys.argv is ['argv.py', 'this', 'is', 'a', 'test']"""

import sys
print('sys.argv is', sys.argv)
