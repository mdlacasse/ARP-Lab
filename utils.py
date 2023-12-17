'''

Python file for handling error messages.

Copyright -- Martin-D. Lacasse (2023)

This program comes with no guarantee. Use at your own risks.

'''

######################################################################
import sys


######################################################################
verbose = False


def setVerbose(val):
    '''
    Set verbose to True if you want the module to be chatty.
    '''
    global verbose
    verbose = val
    # Force the use of the verbose variable through this following call.
    vprint("Setting verbose to", val)


def vprint(*args, **kwargs):
    '''
    Conditional print depending on the value of the verbose variable.
    '''
    global verbose
    if verbose:
        print(*args)


def xprint(*args, **kwargs):
    '''
    Print and exit. Use to print error messages on stderr.
    '''
    print("ERROR:", *args, file=sys.stderr, **kwargs)
    print("Exiting...", file=sys.stderr)
    sys.exit(-1)


