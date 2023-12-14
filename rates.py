'''
This class provides the historical annual rate of returns for different
classes of assets: S&P500, AA corporate bonds, AAA corporate bonds,
10-year Treasury bonds, and inflation as measured by CPI all from
1928 until now.

Values were extracted from NYU's Stern School of business:
https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html

Rate lists will need to be updated with values for current year.
When doing so, the TO bound defined below will need to be adjusted
to the last current data year.

Copyright Martin-D. Lacasse (2023)

Last updated: December 2023

'''

###################################################################
import numpy as np
import utils as u

# All data goes from 1928 to 2022. Update the TO value when data
# becomes available for subsequent years.
FROM = 1928
TO = 2022

# Annual rate of return (%) of S&P 500 since 1928, including dividends.
SP500 = [
    43.81, -8.30,
    # 1930
    -25.12, -43.84, -8.64, 49.98, -1.19, 46.74, 31.94, -35.34, 29.28, -1.10,
    # 1940
    -10.67, -12.77, 19.17, 25.06, 19.03, 35.82, -8.43, 5.20, 5.70, 18.30,
    # 1950
    30.81, 23.68, 18.15, -1.21, 52.56, 32.60, 7.44, -10.46, 43.72, 12.06,
    # 1960
    0.34, 26.64, -8.81, 22.61, 16.42, 12.40, -9.97, 23.80, 10.81, -8.24,
    # 1970
    3.56, 14.22, 18.76, -14.31, -25.90, 37.00, 23.83, -6.98, 6.51, 18.52,
    # 1980
    31.74, -4.70, 20.42, 22.34, 6.15, 31.24, 18.49, 5.81, 16.54, 31.48,
    # 1990
    -3.06, 30.23, 7.49, 9.97, 1.33, 37.20, 22.68, 33.10, 28.34, 20.89,
    # 2000
    -9.03, -11.85, -21.97, 28.36, 10.74, 4.83, 15.61, 5.48, -36.55, 25.94,
    # 2010
    14.82, 2.10, 15.89, 32.15, 13.52, 1.38, 11.77, 21.61, -4.23, 31.21,
    # 2020
    18.02, 28.47, -18.01,
    ]

# Annual rate of return (%) of AA Corporate Bonds since 1928.
BondsAA = [
    3.22, 3.02,
    # 1930
    0.54, -15.68, 23.59, 12.97, 18.82, 13.31, 11.38, -4.42, 9.24, 7.98,
    # 1940
    8.65, 5.01, 5.18, 8.04, 6.57, 6.80, 2.51, 0.26, 3.44, 5.38,
    # 1950
    4.24, -0.19, 4.44, 1.62, 6.16, 2.04, -2.35, -0.72, 6.43, 1.57,
    # 1960
    6.66, 5.10, 6.50, 5.46, 5.16, 3.19, -3.45, 0.90, 4.85, -2.03,
    # 1970
    5.65, 14.00, 11.41, 4.32, -4.38, 11.05, 19.75, 9.95, 3.14, -2.01,
    # 1980
    -3.32, 8.46, 29.05, 16.19, 15.62, 23.86, 21.49, 2.29, 15.12, 15.79,
    # 1990
    6.14, 17.85, 12.17, 16.43, -1.32, 20.16, 4.79, 11.83, 7.95, 0.84,
    # 2000
    9.33, 7.82, 12.18, 13.53, 9.89, 4.92, 7.05, 3.15, -5.07, 23.33,
    # 2010
    8.35, 12.58, 10.12, -1.06, 10.38, -0.70, 10.37, 9.72, -2.76, 15.33,
    # 2020
    10.41, 0.93, -14.49,
    ]

# Annual rate of return (%) of AAA Corporate Bonds since 1928.
BondsAAA = [
    3.28, 4.14,
    # 1930
    5.86, -1.56, 11.07, 5.30, 10.15, 6.90, 6.33, 2.17, 4.31, 4.28,
    # 1940
    4.93, 1.93, 2.71, 3.42, 3.09, 3.48, 2.61, 0.46, 3.46, 4.62,
    # 1950
    1.80, -0.23, 3.35, 1.61, 5.10, 0.78, -1.78, 3.26, 1.63, 0.14,
    # 1960
    6.41, 3.79, 5.86, 3.36, 3.64, 2.56, -0.70, -0.45, 4.32, -2.18,
    # 1970
    8.27, 10.35, 8.44, 3.00, -0.12, 9.54, 14.23, 6.58, 2.01, -0.25,
    # 1980
    -2.55, 7.94, 27.89, 7.74, 15.04, 24.15, 21.12, -1.42, 13.49, 14.15,
    # 1990
    7.64, 13.95, 10.53, 15.38, -3.13, 20.08, 4.18, 10.32, 10.69, -2.89,
    # 2000
    9.92, 10.33, 10.85, 10.63, 6.75, 6.23, 5.75, 4.04, 8.88, 3.45,
    # 2010
    7.11, 13.89, 6.24, -3.98, 11.42, 2.33, 3.24, 8.63, -0.62, 12.63,
    # 2020
    9.93, -1.93, -12.74,
    ]

# Annual rate of return (%) for 10y Treasury notes since 1928.
TBonds = [
    0.84, 4.20,
    # 1930
    4.54, -2.56, 8.79, 1.86, 7.96, 4.47, 5.02, 1.38, 4.21, 4.41,
    # 1940
    5.40, -2.02, 2.29, 2.49, 2.58, 3.80, 3.13, 0.92, 1.95, 4.66,
    # 1950
    0.43, -0.30, 2.27, 4.14, 3.29, -1.34, -2.26, 6.80, -2.10, -2.65,
    # 1960
    11.64, 2.06, 5.69, 1.68, 3.73, 0.72, 2.91, -1.58, 3.27, -5.01,
    #  1970
    16.75, 9.79, 2.82, 3.66, 1.99, 3.61, 15.98, 1.29, -0.78, 0.67,
    #  1980
    -2.99, 8.20, 32.81, 3.20, 13.73, 25.71, 24.28, -4.96, 8.22, 17.69,
    # 1990
    6.24, 15.00, 9.36, 14.21, -8.04, 23.48, 1.43, 9.94, 14.92, -8.25,
    #  2000
    16.66, 5.57, 15.12, 0.38, 4.49, 2.87, 1.96, 10.21, 20.10, -11.12,
    # 2010
    8.46, 16.04, 2.97, -9.10, 10.75, 1.28, 0.69, 2.80, -0.02, 9.64,
    # 2020
    11.33, -4.42, -17.83,
    ]

# Inflation rate as U.S. CPI index (%) since 1928 (1914).
Inflation = [
    # 1.00, 1.98, 12.62, 18.10, 20.44, 14.55, 2.65,  # 1920
    # -10.82, -2.31, 2.37, 0.00, 3.47, -1.12, -2.26,
    -1.16, 0.58,
    # 1930
    -6.40, -9.32, -10.27, 0.76, 1.52, 2.99, 1.45, 2.86, -2.78, 0.00,
    # 1940
    0.71, 9.93, 9.03, 2.96, 2.30, 2.25, 18.13, 8.84, 2.99, -2.07,
    # 1950
    5.93, 6.00, 0.75, 0.75, -0.74, 0.37, 2.99, 2.90, 1.76, 1.73,
    # 1960
    1.36, 0.67, 1.33, 1.64, 0.97, 1.92, 3.46, 3.04, 4.72, 6.20,
    # 1970
    5.57, 3.27, 3.41, 8.71, 12.34, 6.94, 4.86, 6.70, 9.02, 13.29,
    # 1980
    12.52, 8.92, 3.83, 3.79, 3.95, 3.80, 1.10, 4.43, 4.42, 4.65,
    # 1990
    6.11, 3.06, 2.90, 2.75, 2.67, 2.54, 3.32, 1.70, 1.61, 2.68,
    # 2000
    3.39, 1.55, 2.38, 1.88, 3.26, 3.42, 2.54, 4.08, 0.09, 2.72,
    # 2010
    1.50, 2.96, 1.74, 1.50, 0.76, 0.73, 2.07, 2.11, 1.91, 2.29,
    # 2020
    1.36, 7.10, 6.42,
    ]


def getDistributions(frm, to):
    '''
    Pre-compute normal distribution parameters for each of the series above.
    This calculation does not yet take into account the correlations
    between the different rates. This will need to be fixed in the future,
    and return cross-correlations as a 4x4 matrix.
    '''
    series = {'SP500': SP500, 'BondsAA': BondsAA,
              'T. Bonds': TBonds, 'Inflation': Inflation}

    means = np.zeros(len(series))
    stdDev = np.zeros(len(series))

    # Check if called direclty by year instead of by index.
    if frm >= 1000:
        frm -= FROM
        to = to - FROM + 1

    assert (0 <= frm and frm <= len(SP500))
    assert (0 <= to and to <= len(SP500))
    assert (frm <= to)

    i = 0
    u.vprint('Series\t\tMean (%)\t\t\tStd-Deviation (%)')
    for key in series:
        means[i] = np.mean(series[key][frm:to])
        stdDev[i] = np.std(series[key][frm:to])
        u.vprint(key, '  \t', means[i], '\t\t', stdDev[i])
        i += 1

    # Convert from percent to decimal
    means /= 100
    stdDev /= 100

    return means, stdDev


class rates:
    '''
    Rates are stored in a 4-array in the following order:
    Stocks, Bonds, Fixed assets, inflation.
    Rate are stored in decimal, but API is in percent.
    '''

    # Default rates are average over last 30 years.
    _defRates = np.array([0.11008387, 0.0736, 0.05028387, 0.02513871])

    def __init__(self):
        self.frm = 0
        self.to = len(SP500)

        self._myRates = np.array(self._defRates)
        self._setFixedRates(self._defRates)

        # Default values for rates.
        self.method = 'fixed'
        self._rateMethod = self._fixedRates

        self.means = np.zeros((4))
        self.stdDev = np.zeros((4))

    def setMethod(self, method, frm=FROM, to=TO):
        if method is None or method == 'default':
            self.method = 'fixed'
            u.vprint('Using default fixed rates values: (%)\n',
                     100.*self._defRates)
            self._setFixedRates(self._defRates)
            return
        elif type(method) == list:
            self.method == 'fixed'
            method = np.array(method, dtype=float)
            u.vprint('Setting rates using fixed values: (%)\n', method)
            # Convert percent to decimal.
            method /= 100.
            self._setFixedRates(method)
            return

        assert (FROM <= frm and frm <= TO)
        assert (FROM <= to and to <= TO)
        assert (frm < to)

        self.frm = int(frm - FROM)
        self.to = int(to - FROM + 1)

        if method == 'historical':
            u.vprint('Using', method, 'rates representing data from', frm, 'to', to)
            self._rateMethod = self._histRates
        elif method == 'stochastic':
            u.vprint('Using', method, 'rates from', frm, 'to', to)
            self._rateMethod = self._stochRates
            self.means, self.stdDev = getDistributions(frm, to)
        else:
            u.xprint('Method not supported:', method)

        self.method = method

    def _setFixedRates(self, rates):
        assert len(rates) == 4
        self._myRates = np.array(rates)

    def genSeries(self, i, n):
        '''
        Generate a series of nx4 entries of rates representing S&P500,
        corporate AA bonds, 10-y treasury bonds, and inflation,
        respectively. Value 'i' is used to shift the series from
        the first year requested. If there are less than 'n' entries
        in sub-series selected by 'setMethod()', values will be repeated
        modulo the length of the sub-series.
        '''

        rateSeries = np.zeros((n, 4))

        for k in range(n):
            rateSeries[k][:] = self.getRates(i, k)[:]

        return rateSeries

    def getRates(self, i, j=0):
        '''
        This function is the front-end for getting rate values depending
        on the method and the year range selected.

        Values of 'i' allows to set a starting year for the series
        allowing to explore risk sequence. The other 'j' parameter
        is the offset from the start 'i'. Both indices are in
        array coordinates, i.e., not in year coordinates.
        '''

        assert (0 <= i and 0 <= j)
        return self._rateMethod(i, j)

    def _fixedRates(self, i, j):
        '''
        Return average rates set through setRatesMethod().
        If not specified, default average rates are provided.
        For fixed rates, values are time-independent, and therefore
        the 'i' and 'j' arguments are ignored.
        '''
        return self._myRates

    def _histRates(self, i, j):
        '''
        Return a list of 4 values representing the historical rates
        of stock, Corporate AA bonds, Treasury bonds, and inflation,
        respectively. Values are for year (frm + i + j)%(to - frm),
        with values recycled back to 'frm' for years after 'to' year.
        Reason for using two values is to allow Monte-Carlo simulations
        to start at a different year while cycling though the whole series.
        '''

        hrates = np.array([
              SP500[(self.frm+i+j) % (self.to-self.frm)],
              BondsAA[(self.frm+i+j) % (self.to-self.frm)],
              TBonds[(self.frm+i+j) % (self.to-self.frm)],
              Inflation[(self.frm+i+j) % (self.to-self.frm)]
              ])
        # Convert from percent to decimal.
        return hrates/100

    def _stochRates(self, i, j):
        '''
        Return a list of 4 values representing the historical rates
        of stock, Corporate AA bonds, Treasury bonds, and inflation,
        respectively. Values are pulled from normal distributions
        having the same characteristics as the historical data for
        the range of years selected.
        For 1928-2022, mean and std-deviations are:

        SP500: 11.506631578947369 19.494020708683514
        BondsAA:  6.957578947368422 7.7547925712242405
        BondsAAA:  5.732000000000001 6.196953512985656
        TBonds:  4.86842105263158 7.950702096212301
        Inflation:  3.112315789473685 3.9364045718026226

        Current code assumes that distributions are independent.
        They are not! Code needs to account for colinearities
        between stocks, bonds, and inflation. TODO.

        '''

        srates = np.array([
            np.random.normal(self.means[0], self.stdDev[0]),
            np.random.normal(self.means[1], self.stdDev[1]),
            np.random.normal(self.means[2], self.stdDev[2]),
            np.random.normal(self.means[3], self.stdDev[3])
            ])

        return srates
