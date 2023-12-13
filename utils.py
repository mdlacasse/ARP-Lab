'''

A short Python program for retirement planning.
Calculations are done on a yearly basis,
and default for a married couple filing jointly.
Feel free to modify for other cases.

Martin-D. Lacasse - 2023

This program comes with no guarantee. Use at your own risks.

'''

######################################################################
import sys


######################################################################


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


