"""
Read a file and determine if content is valid JSON syntax.

Usage: jsonsyntax filename
   filename   JSON file to check syntax of

Exit code
    exit code: 0 for success, 1 for failure.
"""

# import modules
import sys
import os.path
import json

class CheckSyntaxError (Exception):
    """
    Error definition thrown when an error occurs.

    - error code 1: Invalid name.
    - error code 2: File does not exist.
    - error code 3: Error reading file.
    - error code 4: JSON syntax error.

    """
    def __init__ (self, code, message):
        """
        Create error instance holding ``code`` and ``message``.
        :param code: Error number.
        :type code: int
        :param message: Text message, suitable for display.
        :type message: str
        """
        super (CheckSyntaxError, self).__init__ ()
        self.code = code
        self.message = message

def checkSyntax (file):
    """
    Check syntax of ``file`` passed in command line argument.

    :param file: File to check
    :type file: str
    :raises: CheckSyntaxError
    """
    # verify file provided
    if file is None:
        raise CheckSyntaxError (1, "Invalid name")

    # verify file exists
    if not os.path.isfile (file):
        raise CheckSyntaxError (2, "File not found")

    # read specified file
    try:
        data = open (file).read ()
    except IOError as e:
        raise CheckSyntaxError (3, "Error reading file: " + e.strerror)

    # parse the data as JSON
    try:
        json.loads (data)
    except ValueError as e:
        raise CheckSyntaxError (4, str (e.args))

def main ():
    """
    Main - parse file name from command and call syntax check.
    """
    # if wrong number of arguments, print usage message and exit
    if len (sys.argv) != 2:
        print ("Usage: jsonsyntax filename")
        print ("  filename   JSON file to check syntax of")
        sys.exit (1)

    # check syntax, displaying result message. Exit with success/fail code.
    try:
        # assign command line argument to file name
        file = sys.argv[1]
        checkSyntax (file)
        print ("File contains valid JSON content.")
        sys.exit (0)
    except CheckSyntaxError as e:
        print ("Error: " + e.message)
        sys.exit (1)

if __name__ == "__main__":
    main ()
