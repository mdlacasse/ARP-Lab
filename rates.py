'''

This class provides the historical annual rate of returns for different
classes of assets: S&P500, Baa corporate bonds, Aaa corporate bonds,
10-year Treasury notes, and inflation as measured by CPI all from
1928 until now.

Values were extracted from NYU's Stern School of business:
https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
from references therein.

Rate lists will need to be updated with values for current year.
When doing so, the TO bound defined below will need to be adjusted
to the last current data year.

Copyright -- Martin-D. Lacasse (2023)

Last updated: December 2023

Disclaimer: This program comes with no guarantee. Use at your own risk.

'''

###################################################################
import numpy as np
import utils as u

# All data goes from 1928 to 2023. Update the TO value when data
# becomes available for subsequent years.
FROM = 1928
TO = 2023

# Annual rate of return (%) of S&P 500 since 1928, including dividends.
SP500 = [
    43.81,
    -8.30,
    # 1930
    -25.12,
    -43.84,
    -8.64,
    49.98,
    -1.19,
    46.74,
    31.94,
    -35.34,
    29.28,
    -1.10,
    # 1940
    -10.67,
    -12.77,
    19.17,
    25.06,
    19.03,
    35.82,
    -8.43,
    5.20,
    5.70,
    18.30,
    # 1950
    30.81,
    23.68,
    18.15,
    -1.21,
    52.56,
    32.60,
    7.44,
    -10.46,
    43.72,
    12.06,
    # 1960
    0.34,
    26.64,
    -8.81,
    22.61,
    16.42,
    12.40,
    -9.97,
    23.80,
    10.81,
    -8.24,
    # 1970
    3.56,
    14.22,
    18.76,
    -14.31,
    -25.90,
    37.00,
    23.83,
    -6.98,
    6.51,
    18.52,
    # 1980
    31.74,
    -4.70,
    20.42,
    22.34,
    6.15,
    31.24,
    18.49,
    5.81,
    16.54,
    31.48,
    # 1990
    -3.06,
    30.23,
    7.49,
    9.97,
    1.33,
    37.20,
    22.68,
    33.10,
    28.34,
    20.89,
    # 2000
    -9.03,
    -11.85,
    -21.97,
    28.36,
    10.74,
    4.83,
    15.61,
    5.48,
    -36.55,
    25.94,
    # 2010
    14.82,
    2.10,
    15.89,
    32.15,
    13.52,
    1.38,
    11.77,
    21.61,
    -4.23,
    31.21,
    # 2020
    18.02,
    28.47,
    -18.04,
    26.06,
]

# Annual rate of return (%) of Baa Corporate Bonds since 1928.
BondsBaa = [
    3.22,
    3.02,
    # 1930
    0.54,
    -15.68,
    23.59,
    12.97,
    18.82,
    13.31,
    11.38,
    -4.42,
    9.24,
    7.98,
    # 1940
    8.65,
    5.01,
    5.18,
    8.04,
    6.57,
    6.80,
    2.51,
    0.26,
    3.44,
    5.38,
    # 1950
    4.24,
    -0.19,
    4.44,
    1.62,
    6.16,
    2.04,
    -2.35,
    -0.72,
    6.43,
    1.57,
    # 1960
    6.66,
    5.10,
    6.50,
    5.46,
    5.16,
    3.19,
    -3.45,
    0.90,
    4.85,
    -2.03,
    # 1970
    5.65,
    14.00,
    11.41,
    4.32,
    -4.38,
    11.05,
    19.75,
    9.95,
    3.14,
    -2.01,
    # 1980
    -3.32,
    8.46,
    29.05,
    16.19,
    15.62,
    23.86,
    21.35,
    2.81,
    14.38,
    15.95,
    # 1990
    6.28,
    18.93,
    11.31,
    15.47,
    -0.97,
    21.29,
    3.42,
    12.75,
    7.63,
    0.91,
    # 2000
    9.39,
    8.54,
    12.14,
    12.32,
    10.35,
    5.30,
    5.20,
    4.84,
    -3.54,
    20.21,
    # 2010
    9.41,
    12.26,
    9.33,
    -0.98,
    10.78,
    -1.50,
    11.52,
    9.23,
    -3.27,
    15.25,
    # 2020
    10.60,
    0.93,
    -15.14,
    8.74,
]

# Annual rate of return (%) of Aaa Corporate Bonds since 1928.
BondsAaa = [
    3.28,
    4.14,
    # 1930
    5.86,
    -1.56,
    11.07,
    5.30,
    10.15,
    6.90,
    6.33,
    2.17,
    4.31,
    4.28,
    # 1940
    4.93,
    1.93,
    2.71,
    3.42,
    3.09,
    3.48,
    2.61,
    0.46,
    3.46,
    4.62,
    # 1950
    1.80,
    -0.23,
    3.35,
    1.61,
    5.10,
    0.78,
    -1.78,
    3.26,
    1.63,
    0.14,
    # 1960
    6.41,
    3.79,
    5.86,
    3.36,
    3.64,
    2.56,
    -0.70,
    -0.45,
    4.32,
    -2.18,
    # 1970
    8.27,
    10.35,
    8.44,
    3.00,
    -0.12,
    9.54,
    14.23,
    6.58,
    2.01,
    -0.25,
    # 1980
    -2.55,
    7.94,
    27.89,
    7.85,
    14.80,
    25.97,
    18.95,
    -0.85,
    12.87,
    14.39,
    # 1990
    7.72,
    14.98,
    9.84,
    14.30,
    -2.78,
    21.16,
    2.83,
    11.26,
    10.20,
    -3.39,
    # 2000
    10.99,
    11.09,
    10.42,
    9.54,
    7.14,
    6.73,
    3.75,
    5.84,
    10.97,
    -0.09,
    # 2010
    8.83,
    13.99,
    4.59,
    -3.43,
    11.56,
    1.13,
    4.53,
    8.40,
    -0.93,
    12.08,
    # 2020
    10.23,
    -1.93,
    -12.88,
    5.09,
]

# Annual rate of return (%) for 10-y Treasury notes since 1928.
TNotes = [
    0.84,
    4.20,
    # 1930
    4.54,
    -2.56,
    8.79,
    1.86,
    7.96,
    4.47,
    5.02,
    1.38,
    4.21,
    4.41,
    # 1940
    5.40,
    -2.02,
    2.29,
    2.49,
    2.58,
    3.80,
    3.13,
    0.92,
    1.95,
    4.66,
    # 1950
    0.43,
    -0.30,
    2.27,
    4.14,
    3.29,
    -1.34,
    -2.26,
    6.80,
    -2.10,
    -2.65,
    # 1960
    11.64,
    2.06,
    5.69,
    1.68,
    3.73,
    0.72,
    2.91,
    -1.58,
    3.27,
    -5.01,
    #  1970
    16.75,
    9.79,
    2.82,
    3.66,
    1.99,
    3.61,
    15.98,
    1.29,
    -0.78,
    0.67,
    #  1980
    -2.99,
    8.20,
    32.81,
    3.20,
    13.73,
    25.71,
    24.28,
    -4.96,
    8.22,
    17.69,
    # 1990
    6.24,
    15.00,
    9.36,
    14.21,
    -8.04,
    23.48,
    1.43,
    9.94,
    14.92,
    -8.25,
    #  2000
    16.66,
    5.57,
    15.12,
    0.38,
    4.49,
    2.87,
    1.96,
    10.21,
    20.10,
    -11.12,
    # 2010
    8.46,
    16.04,
    2.97,
    -9.10,
    10.75,
    1.28,
    0.69,
    2.80,
    -0.02,
    9.64,
    # 2020
    11.33,
    -4.42,
    -17.83,
    3.88,
]

# Annual rates of return for 3-month Treasury bills since 1928.
TBills = [
    3.08,
    3.16,
    # 1930
    4.55,
    2.31,
    1.07,
    0.96,
    0.28,
    0.17,
    0.17,
    0.28,
    0.07,
    0.05,
    # 1940
    0.04,
    0.13,
    0.34,
    0.38,
    0.38,
    0.38,
    0.38,
    0.60,
    1.05,
    1.12,
    # 1950
    1.20,
    1.52,
    1.72,
    1.89,
    0.94,
    1.72,
    2.62,
    3.22,
    1.77,
    3.39,
    # 1960
    2.87,
    2.35,
    2.77,
    3.16,
    3.55,
    3.95,
    4.86,
    4.29,
    5.34,
    6.67,
    # 1970
    6.39,
    4.33,
    4.06,
    7.04,
    7.85,
    5.79,
    4.98,
    5.26,
    7.18,
    10.05,
    # 1980
    11.39,
    14.04,
    10.60,
    8.62,
    9.54,
    7.47,
    5.97,
    5.78,
    6.67,
    8.11,
    # 1990
    7.50,
    5.38,
    3.43,
    3.00,
    4.25,
    5.49,
    5.01,
    5.06,
    4.78,
    4.64,
    # 2000
    5.82,
    3.40,
    1.61,
    1.01,
    1.37,
    3.15,
    4.73,
    4.36,
    1.37,
    0.15,
    # 2010
    0.14,
    0.05,
    0.09,
    0.06,
    0.03,
    0.05,
    0.32,
    0.93,
    1.94,
    2.06,
    # 2020
    0.35,
    0.05,
    2.02,
    5.07,
]

# Inflation rate as U.S. CPI index (%) since 1928 (1914).
Inflation = [
    # 1.00, 1.98, 12.62, 18.10, 20.44, 14.55, 2.65,  # 1920
    # -10.82, -2.31, 2.37, 0.00, 3.47, -1.12, -2.26,
    -1.16,
    0.58,
    # 1930
    -6.40,
    -9.32,
    -10.27,
    0.76,
    1.52,
    2.99,
    1.45,
    2.86,
    -2.78,
    0.00,
    # 1940
    0.71,
    9.93,
    9.03,
    2.96,
    2.30,
    2.25,
    18.13,
    8.84,
    2.73,
    -1.83,
    # 1950
    5.80,
    5.96,
    0.91,
    0.60,
    -0.37,
    0.37,
    2.83,
    3.04,
    1.76,
    1.52,
    # 1960
    1.36,
    0.67,
    1.23,
    1.65,
    1.20,
    1.92,
    3.36,
    3.28,
    4.71,
    5.90,
    # 1970
    5.57,
    3.27,
    3.41,
    8.94,
    12.10,
    7.13,
    5.04,
    6.68,
    8.99,
    13.25,
    # 1980
    12.35,
    8.91,
    3.83,
    3.79,
    4.04,
    3.79,
    1.19,
    4.33,
    4.41,
    4.64,
    # 1990
    6.25,
    2.98,
    2.97,
    2.81,
    2.60,
    2.53,
    3.38,
    1.70,
    1.61,
    2.68,
    # 2000
    3.44,
    1.60,
    2.48,
    2.04,
    3.34,
    3.34,
    2.52,
    4.11,
    -0.02,
    2.81,
    # 2010
    1.44,
    3.06,
    1.76,
    1.51,
    0.65,
    0.64,
    2.05,
    2.13,
    2.00,
    2.31,
    # 2020
    1.32,
    7.19,
    6.44,
    3.12,
]


def getDistributions(frm, to):
    '''
    Pre-compute normal distribution parameters for the series above.
    This calculation takes into account the correlations between
    the different rates. Function returns means and covariance matrix.
    '''
    import pandas as pd

    series = {
        'SP500': SP500,
        'BondsBaa': BondsBaa,
        'T. Notes': TNotes,
        'Inflation': Inflation,
    }

    df = pd.DataFrame(series)

    # Check if were called direclty by year instead of by index.
    if frm >= 1000:
        frm -= FROM
        to = to - FROM

    assert 0 <= frm and frm <= len(SP500)
    assert 0 <= to and to <= len(SP500)
    assert frm <= to

    df = df.truncate(before=frm, after=to)

    means = df.mean()
    covar = df.cov()

    u.vprint('means: (%)\n', means)
    u.vprint('covariance: (%^2)\n', covar)

    # Convert from percent to decimal.
    means /= 100.0
    covar /= 10000.0

    return means, covar


class rates:
    '''
    Rates are stored in a 4-array in the following order:
    Stocks, Bonds, Fixed assets, inflation.
    Rate are stored in decimal, but API is in percent.
    '''

    def __init__(self):
        '''
        Default constructor.
        '''
        # Default rates are average over last 30 years.
        self._defRates = np.array([0.1101, 0.0736, 0.0503, 0.0251])

        # Realistic rates are average predictions of major firms
        # as reported by MorningStar in 2023.
        self._realisticRates = np.array([0.086, 0.049, 0.033, 0.025])

        # Conservative rates.
        self._conservRates = np.array([0.06, 0.04, 0.035, 0.028])

        self.frm = 0
        self.to = len(SP500)

        self._myRates = np.array(self._defRates)
        self._setFixedRates(self._defRates)

        # Default values for rates.
        self.method = 'default'
        self._rateMethod = self._fixedRates

        self.means = np.zeros((4))
        self.covar = np.zeros((4))

    def setMethod(self, method, frm=FROM, to=TO, values=None):
        '''
        Select the method to generate the annual rates of return
        for the different classes of assets.
        '''
        if method == 'default':
            self.method = 'default'
            # Convert decimal to percent for reporting.
            u.vprint('Using default fixed rates values: (%)\n', 100.0 * self._defRates)
            self._setFixedRates(self._defRates)
            return
        elif method == 'realistic':
            u.vprint(
                'Using realistic fixed rates values: (%)\n',
                100.0 * self._realisticRates,
            )
            self._setFixedRates(self._realisticRates)
            return
        elif method == 'conservative':
            u.vprint(
                'Using conservative fixed rates values: (%)\n',
                100.0 * self._conservRates,
            )
            self._setFixedRates(self._conservRates)
            return
        elif method == 'fixed':
            self.method == 'fixed'
            if values is None:
                u.xprint('Rates must be provided with the fixed option.')
            values = np.array(values, dtype=float)
            u.vprint('Setting rates using fixed values: (%)\n', values)
            # Convert percent to decimal for storing.
            values /= 100.0
            self._setFixedRates(values)
            return

        assert FROM <= frm and frm <= TO
        assert FROM <= to and to <= TO
        assert frm < to

        self.frm = int(frm - FROM)
        self.to = int(to - FROM + 1)

        if method == 'historical':
            u.vprint('Using', method, 'rates representing data from', frm, 'to', to)
            self._rateMethod = self._histRates
        elif method == 'average':
            u.vprint('Using', method, 'rates from', frm, 'to', to)
            self.means, self.covar = getDistributions(frm, to)
            self._setFixedRates(self.means)
        elif method == 'stochastic':
            u.vprint('Using', method, 'rates from', frm, 'to', to)
            self._rateMethod = self._stochRates
            self.means, self.covar = getDistributions(frm, to)
        else:
            u.xprint('Method not supported:', method)

        self.method = method

    def _setFixedRates(self, rates):
        assert len(rates) == 4
        self._myRates = np.array(rates)
        self._rateMethod = self._fixedRates

    def genSeries(self, frm=FROM, to=TO, n=TO - FROM + 1):
        '''
        Generate a series of nx4 entries of rates representing S&P500,
        corporate Baa bonds, 10-y treasury notes, and inflation,
        respectively. If there are less than 'n' entries
        in sub-series selected by 'setMethod()', values will be repeated
        modulo the length of the sub-series.
        '''
        rateSeries = np.zeros((n, 4))

        # Convert years to indices.
        frm -= FROM
        to -= FROM

        # Add one since bounds are inclusive.
        span = to - frm + 1
        first = frm

        # Assign 4 values at the time.
        for k in range(n):
            rateSeries[k][:] = self.getRates(first + (k % span))[:]

        return rateSeries

    def getRates(self, n):
        '''
        This function is the front-end for getting rate values depending
        on the method and the year range selected.

        Index is in array coordinates, i.e., not in year coordinates.
        '''
        assert 0 <= n and n < len(SP500)

        return self._rateMethod(n)

    def _fixedRates(self, n):
        '''
        Return rates provided.
        For fixed rates, values are time-independent, and therefore
        the 'n' argument is ignored.
        '''
        return self._myRates

    def _histRates(self, n):
        '''
        Return a list of 4 values representing the historical rates
        of stock, Corporate Baa bonds, Treasury notes, and inflation,
        respectively. Values are for year (frm + i + j)%(to - frm),
        with values recycled back to 'frm' for years after 'to' year.
        Reason for using two values is to allow Monte-Carlo simulations
        to start at a different year while cycling though the whole series.
        '''
        hrates = np.array([SP500[n], BondsBaa[n], TNotes[n], Inflation[n]])

        # Convert from percent to decimal.
        return hrates / 100

    def _stochRates(self, n):
        '''
        Return a list of 4 values representing the historical rates
        of stock, Corporate Baa bonds, Treasury notes, and inflation,
        respectively. Values are pulled from normal distributions
        having the same characteristics as the historical data for
        the range of years selected.

        But these variables need to be looked at together
        through multivariate analysis. Code below accounts for
        covariance between stocks, bonds, and inflation.

        '''
        srates = np.random.multivariate_normal(self.means, self.covar)

        return srates
