'''

Python file handling US tax code.

Currently, it supports single filers and married
filing jointly. Feel free to modify for other cases.

This file needs to be updated every year.

Copyright -- Martin-D. Lacasse (2023)

Disclaimer: This program comes with no guarantee. Use at your own risk.

'''

######################################################################
# Our own required modules:
import utils as u


def inflationAdjusted(base, year, rates, refIndex=0):
    '''
    Return inflation-adjusted amount for year provided
    with respect to referenced year. Rate is annual rate.
    If refYear is zero, current year will be used as a reference.
    Rate can be a single number or a rate series of 4-tuples
    provided by the rates() class. In the latter case, each tuple
    contains stocks, bonds, fixed assets, and inflation rates.
    Note that refIndex can be non-zero, indication an offset in
    the calculation. Year can be the nth year from now,
    or a year in the future.
    '''
    # Were we given a year? Make it in reference to this update.
    if year > 1000:
        index = year - 2024
    else:
        index = year

    assert index >= refIndex

    fac = 1
    if type(rates) == float:
        # Sign will take care of division.
        fac *= (1 + rates)**(index - refIndex)
    elif index >= refIndex:
        for i in range(refIndex, index):
            fac *= (1 + rates[i][3])
    else:
        for i in range(index, refIndex):
            fac /= (1 + rates[i][3])

    return base*fac


def irmaa(magi, filingStatus, year, rates):
    '''
    Return inflation-adjusted annual irmaa costs for Part B
    premium with magi and filing status provided. The magi
    to be used is the gross income from 2 years ago, while
    the rates for adjustments are for the current time.
    '''

    table2024_MFJ = {206000: 0, 258000: 838.80,
                     322000: 2096.40, 386000: 3354.00,
                     750000: 4611.60, 99999999: 5031.60}
    table2024_S = {103000: 0, 129000: 838.80,
                   161000: 2096.40, 193000: 3354.00,
                   500000: 4611.60, 99999999: 5031.60}

    if filingStatus == 'married':
        table = table2024_MFJ
    elif filingStatus == 'single':
        table = table2024_S
    else:
        u.xprint('In irmaa function: Unknown filing status', filingStatus)

    for bracket in table:
        if magi < inflationAdjusted(bracket, year, rates):
            return inflationAdjusted(table[bracket], year, rates)

    u.xprint('In irmaa function: Logical flaw for magi.', magi)


def stdDeduction(yobs, filingStatus, year, rates):
    '''
    Return standard income deduction for year provided
    depending on filing status. Additional deduction will
    be added for individuals 65 and over.
    '''
    # [Single, married filing jointly] numbers.
    # ded2017 = [6350, 12700] #  Original 2017 values
    # Inflation-adjusted (+30%) to 2024
    ded2017 = [8250, 16500]
    ded2024 = [14600, 29200]

    # Add inflation-adjusted $1,850 for single over 65 yo.
    # Or $1,500/indiv for couples.
    ded65 = 0
    if filingStatus == 'single':
        k = 0
        ded65 += inflationAdjusted(1950, year, rates)
    elif filingStatus == 'married':
        k = 1
        for i in range(len(yobs)):
            if year - yobs[i] >= 65:
                ded65 += inflationAdjusted(1550, year, rates)
    else:
        u.xprint('In stdDeduction: Unknown status', filingStatus)

    # Use the TCJA numbers for years before 2025 (Tax Cuts and Jobs Act).
    if year <= 2025:
        return ded65 + inflationAdjusted(ded2024[k], year, rates)

    # Tax code returns to 2017 code in 2026.
    # Guestimated to be around 16k$ in 2026.
    return ded65 + inflationAdjusted(ded2017[k], year, rates)


def rmdFraction(year, yob):
    '''
    Return fraction of tax-deferred investment that
    needs to be distributed.
    '''

    table = [27.4, 26.5, 25.5, 24.6, 23.7, 22.9, 22.0, 21.1, 20.2, 19.4, 18.5,
             17.7, 16.8, 16.0, 15.2, 14.4, 13.7, 12.9, 12.2, 11.5, 10.8, 10.1,
             9.5, 8.9, 8.4, 7.8, 7.3, 6.8, 6.4, 6.0, 5.6, 5.2, 4.9, 4.6
             ]

    yage = year - yob
    # Account for increase of RMD age between 2023 and 2032.
    if (year > 2032 and yage < 75) or (year > 2023 and yage < 73) \
            or (yage < 72):
        return 0

    return 1./table[yage-72]


def incomeTax(agi, yobs, filingStatus, year, rates):
    '''
    Return tax liability for a given income.
    Married filing jointly or single status only.
    '''
    # TCJA rates
    # Married filing jointly
    tax2024_MFJ = {23200: 0.10,
                   94300: 0.12,
                   201050: 0.22,
                   383900: 0.24,
                   487450: 0.32,
                   731200: 0.35,
                   99999999: 0.37
                   }

    # Single
    tax2024_S = {11600: 0.10,
                 47150: 0.12,
                 100525: 0.22,
                 191950: 0.24,
                 243725: 0.32,
                 609350: 0.35,
                 99999999: 0.37
                 }

    '''
    # Original 2017 rates
    # Married filing jointly
    tax2017_MFJ = {18650: 0.10,
                   75900: 0.15,
                   153100: 0.25,
                   233350: 0.28,
                   416700: 0.33,
                   470700: 0.35,
                   99999999: 0.396
                   }

    # Single
    tax2017_S = {9325: 0.10,
                 37950: 0.15,
                 91900: 0.25,
                 191650: 0.28,
                 416700: 0.33,
                 418400: 0.35,
                 99999999: 0.396
                 }
    '''

    # 2017 rates inflation-adjusted to 2024 (+30.0% increase)
    # Married filing jointly
    tax2017_MFJ = {24200: 0.10,
                   98700: 0.15,
                   199000: 0.25,
                   303350: 0.28,
                   541700: 0.33,
                   611900: 0.35,
                   99999999: 0.396
                   }

    # Single
    tax2017_S = {12100: 0.10,
                 49300: 0.15,
                 119500: 0.25,
                 249100: 0.28,
                 541700: 0.33,
                 543900: 0.35,
                 99999999: 0.396
                 }

    taxbleIncome = agi - stdDeduction(yobs, filingStatus, year, rates)

    if filingStatus == 'single':
        if year < 2026:
            taxTable = tax2024_S
        else:
            taxTable = tax2017_S
    elif filingStatus == 'married':
        if year < 2026:
            taxTable = tax2024_MFJ
        else:
            taxTable = tax2017_MFJ
    else:
        u.xprint('In tax calculation: Unknown status', filingStatus)

    return calcTax(taxbleIncome, year, rates, taxTable)


def calcTax(income, year, rates, taxTable):
    '''
    Compute the income tax on taxable income provided using the
    referenced tax table. Bracket are inflation-adjusted for the
    year provided.
    '''
    if income <= 0:
        return 0

    prevBracket = 0
    tax = 0
    for bracket, txrate in taxTable.items():
        nowBracket = inflationAdjusted(bracket, year, rates)
        if income > nowBracket:
            tax += (nowBracket - prevBracket)*txrate
        else:
            tax += (income - prevBracket)*txrate
            return tax

        prevBracket = nowBracket

    u.xprint('Logic error in calcTax! Income: $', income)

