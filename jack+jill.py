'''
This file is part of the HARP Python program for exploring
financial retirement decisions.

In this file, we use the same example of Jack and Jill but using
a command line python script to explore Monte-Carlo simulations
and historical rates.

Copyright -- Martin-D. Lacasse (2023)

This program comes with no garantee. Use at your own risks.

'''
import sys
import harp as rp


def runOnce(stype, frm, to, plot=False):
    '''
    Run one instance of a simulation.
    '''
    rp.setVerbose(False)

    plan = rp.Plan(YOB=[1961, 1964], expectancy=[89, 92])

    plan.setAssetBalances(taxable=[60000, 20000],
                          taxDeferred=[500000, 120000],
                          taxFree=[80000, 25000],
                          beneficiary=[1., 1.])

    plan.setInitialAR(taxableAR=[[0, 25, 50, 25], [0, 25, 50, 25]],
                      taxDeferredAR=[[60, 40, 0, 0], [60, 40, 0, 0]],
                      taxFreeAR=[[100, 0, 0, 0], [100, 0, 0, 0]])

    plan.setFinalAR(taxableAR=[[0, 50, 50, 0], [0, 50, 50, 0]],
                    taxDeferredAR=[[60, 40, 0, 0], [60, 40, 0, 0]],
                    taxFreeAR=[[60, 40, 0, 0], [60, 40, 0, 0]])

    plan.interpolateAR('linear')

    # Specify rate of returns for each class of assets.
    # Valid entries are 'historical', 'stochastic', 'default',
    # or a list of fixed average values.
    # myrates = [6.0, 3.0, 3.0, 3.08]
    # plan.setRates(myrates)
    # plan.setRates('default')
    if stype == 'historical':
        plan.setRates('historical', frm, to)
    else:
        plan.setRates('stochastic', frm, to)

    # Enter desired value for net income in retirementi, and spending profile.
    plan.setDesiredIncome(79500, 'smile')

    # How to handle withdrawals between spouses.
    plan.setSpousalSplit('auto')

    # Now enter fixed income.\n",
    plan.setPension([0, 10000], [65, 65])

    # And social security income.
    plan.setSocialSecurity([30000, 28000], [70, 70])

    # Name of spreadsheet containing financial events (contributions, etc).
    plan.readContributions('jack+jill.xlsx')

    plan.run()

    if plot:
        # Pick what you would like to plot:
        # plan.plotAccounts()
        # plan.plotSources()
        # plan.plotTaxableIncome()
        # plan.plotTaxes()

        plan.plotRates()
        plan.plotNetIncome()

        # plan.showAndSave()
        pass

    return plan

##############################################################
# Performing a historical simulation of N stochastic cases.


def runHistorical(frm, plot=False):
    '''
    Run historical simulation passing through the dreaded
    1966 year.
    '''
    span = 35
    to = frm + span
    N = 2022 - span - frm
    success = 0
    total = 0
    for i in range(N):
        print('--------------------------------------------')
        print('Running case #', i, '(', frm+i, ')')
        plan = runOnce('historical', frm+i, to+i, plot=plot)
        print('Plan success:', plan.success)
        if plan.success:
            success += 1

        # Assume 30% tax on taxable part of estate.
        estate, factor = plan.estate(30)
        print('Estate: (today\'s $)', rp.d(estate),
              ', cum. infl.:', rp.pc(factor))
        total += estate
        if plot:
            # Number of seconds to wait.
            # For embedding in jupyter set to a low value.
            # plan.show(0.000001)
            plan.show(2)
            # plan.showAndSave()

    print('============================================')
    print('Success rate:', success, 'out of', N, '('+rp.pc(100*success/N)+')')
    print('Average estate value (today\'s $): ', rp.d(total/N))


def runMonteCarlo(N, plot=False):
    '''
    Run N simulations using a stochastic sinulation.
    '''
    success = 0
    total = 0
    for i in range(N):
        print('--------------------------------------------')
        print('Running case #', i)
        plan = runOnce('stochastic', 1940, 2022, plot=plot)
        print('Plan success:', plan.success)
        if plan.success:
            success += 1

        # Assume 30% tax on taxable part of estate.
        estate, factor = plan.estate(30)
        print('Estate: (today\'s $)', rp.d(estate),
              ', cum. infl.:', rp.pc(factor))
        total += estate

    print('============================================')
    print('Success rate:', success, 'out of', N, '('+rp.pc(100*success/N)+')')
    print('Average estate value (today\'s $): ', rp.d(total/N))


######################################################################

# Pick the one you want to run from the command line argument:
if len(sys.argv) >= 2:
    if sys.argv[1] == 'historical':
        runHistorical(1960, True)
    elif sys.argv[1] == 'Monte-Carlo':
        if len(sys.argv) == 3:
            N = int(sys.argv[2])
            runMonteCarlo(N, False)
        else:
            print('Monte-Carlo needs a number.')
    else:
        print('Unknown case:', sys.argv[1])
else:
    print("Script requires one argument: 'historical' or 'Monte-Carlo'.")

