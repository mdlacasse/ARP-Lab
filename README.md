# ARP Lab
## A retirement planning laboratory

This package is a retirement modeling framework for exploring the sensitivity of retirement financial decisions. Strictly speaking, it is not a planning tool, but more an environment for exploring *what if* scenarios. It provides different realizations of a financial strategy. One can certainly have a savings plan, but due to the volatility of financial investments, it is impossible to have an exact and certain asset earnings plan. Moreover, it is very likely that tax laws will change in the future. That does not mean that one cannot make decisions. This is where this tool fits it. Given one's savings and spending desires, it can generate different future realizations of a given strategy under different market assumptions, helping to better understand one's financial situation, and the impact of near-term and future decisions.

Many individuals contemplating retirement use Excel to build their own plans, often involving different worksheets. But there is only so much that one can do in Excel. ARP Lab brings more capabilities, allowing for better planning by generating future scenarios under different market assumptions and providing easy graphing capabilities for comparing the different outcomes. Using this platform, one can test the robustness of a retirement plan under historical or statistical rates of return and inflation. It can also be used to reproduce the historical success of a 4% withdrawal rate, measure the effect of a part-time income at retirement, compare different strategies for Roth conversions, evaluate the possibility of purchasing a second house in your 60's, and so on. ARP Lab is currently appropriate for U.S. individuals as federal income tax calculations are automatically performed. However, no state income tax are currenty included, but they can easily be. If you're in Texas or Washington State, you're all set!

ARP Lab requires some rudimentary programming skills. It is written in Python and designed so that user-friendly functions can be called through an interactive jupyter notebook interface. Therefore, target users need to be young enough to have some basic Python skills (or at least have enough intellectual plasticity left to acquire those skills ;-), while being old enough to contemplate retirement. 

Copyright Martin-D. Lacasse (2023)

Disclaimer: I am not a financial planner. You make your own decisions. This program comes with no guaranteee. Use at your own risk.
---------------------------------------------------------------------------------------------------------------------------------

## Capabilities
ARP Lab contains historical data from 1928 to last year and can generate scenarios using this data,
or using random data created from historical statistics. It has many graphing capabilities as well
as many heuristics for optimizing wealth over the time span of a scenario.
These include smart banking strategies, coordinated assets allocations between types of accounts and optionally between spouses, and a Roth conversion optimizer using a heuristic approach. 

There are currently 4 classes of assets supported in ARP Lab:

- Assets tracking the S&P 500 index;
- Assets representative of corporate bonds Baa;
- Assets similar to the 10-year Treasury notes;
- Common assets tracking inflation.

The goal of ARP lab is not to be able to track all available indices and assets, but rather to allow choosing from a limited selection of classes of assets representative of dissimilar volatilities and returns. New classes of assets could easily be added to ARP Lab, but it would be at the cost of complicating the user's experience. 

## Rules and assumptions
ARP Lab relies on a few implicit assumptions:

- To minimize income tax, all withdrawals are taken in the following order:
    1) taxable investment accounts (CD's, bank savings accounts, stock investment accounts, etc.);
    2) tax-deferred savings accounts (e.g., 401k, 403b, etc.);
    3) tax-free savings accounts (Roth IRA, Roth 401k, etc.).
- RMDs are made. Table used for spouses assumes they are less than 10 years apart;
- Single and Married Filing Jointly are currently the only two choices for income tax calculations;
- Rates of return provided for the S&P 500 data include dividends;
- No investment administration fees are accounted for;
- No elaborate tax strategies are considered, such as tax-loss harvesting strategy, net unrealized appreciation, step-up in basis, or even reduced rates on long-term capital gains;
- Contributions to savings accounts are assumed to be made at half-year, in the hope of averaging periodic contributions made evenly through the year;
- No estate tax calculations are included. Only tax on the tax-deferred portion of the estate is accounted for when reporting estate value in today's $;
- For spouses, surplus over the desired joint income will be deposited in taxable accounts proportionally to that year's spousal income ratio;
- Tax and IRMAA brackets are assumed to follow inflation;
- Roth conversions are assumed to be performed at the beginning of the year;
- Social security benefits are assumed to be adjusted for inflation, and are assumed to be taxed at 85%;
- Most importantly, tax rules are only inflation-adjusted and projected in the future without any consideration on likely changes to happen with new administrations. As of this release, the tax code of 2017 is assumed to be returning at the expiration of the TCJA after 2025.

## Default values for parameters
When a new plan is created, ARP Lab will list all the default assumptions as a reminder. All these parameters can be changed with simple commands.
The default choices include:

- Assets allocation is 60% S&P 500 and 40% corporate bonds for tax-deferred and tax-free savings accounts;
- Assets allocation is 25% corporate bonds, 55% 10-year Treasury notes, and %25 common assets for taxable investment accounts; 
- Income for surviving spouse will be %60 of the income of the couple; 
- Spousal withdrawals are set to *auto*, allowing coordination between both accounts; 
- Income tax on tax-deferred portion of estate is assumed to be 25% on the taxable portion of the estate; 
- Default rates are average rates over the last 30 years.

These choices have no particular value, except to provide a default case that one can run for demonstration purposes.
It is anticipated that you will change these default values by using `set___()` functions. The *jack+jill* notebook contains configuration examples describing how to make these values
match your own assumptions. These include the following calls:
    `setInitialAR()`, `setFinalAR()`, `setSurvivorFraction()`, `setSpousalSplit()`, `setHeirsTaxRate()`,  `setRates()`, for examples.

## Case studies
ARP Lab comes with a few notebooks as examples:
- [jack+jill](https://github.com/mdlacasse/ARP-Lab/blob/main/jack+jill.ipynb): describes the case of a fictitious couple about to enter retirement. This case introduces most of the capabilities of the ARP Lab platform.
- [bengen_4%](https://github.com/mdlacasse/ARP-Lab/blob/main/bengen_4%.ipynb): reproduces the 4% rule proposed by Bill Bengen in 1994. It uses a case where all assets are in a tax-free account and therefore avoids triggering income tax, which was not considered in the original paper.
- [mary+john](https://github.com/mdlacasse/ARP-Lab/blob/main/mary+john.ipynb): explores the case of more elaborate asset allocation coordination schemes and its effect on final wealth.
- [roth](https://github.com/mdlacasse/ARP-Lab/blob/main/roth.ipynb): looks at Roth conversions for a couple with tax-deferred assets.

## Tutorial
The best way to start is to read the example files described above. These files are meant to be run in a jupyter notebook, but these files can also be read in preview mode. Once familiar with their contents, go to the next section that will get you started.

## Requirements to run this program
ARP Lab is coded in Python and is best run using either the *JupyterLab* or the *jupyter* applications. Therefore, I strongly recommend installing *Anaconda* on your computer. It can be found at [anaconda.com](https://anaconda.com). Follow the instructions in the Jupyter tutorial included (link below) for installing anaconda on your computer. The Jupyter Notebook interface is a browser-based application for authoring documents that combines live-code with narrative text, equations and visualizations. Jupyter will run in your default web browser, from your computer to your browser, and therefore no data is ever transferred on the Internet (your computer, i.e., `localhost`, is the server).

You will also need the capability to read and edit Excel files. One can have an Excel license, or use the LibreOffice free alternative.

The intent of using a notebook is that one can configure calculations that suit one's needs. Moreover, running calculations in *jupyter* is made to be relatively easy. There are many tutorials on this topic and a summary including installation procedures is given [here](https://github.com/mdlacasse/ARP-Lab/blob/main/Jupyter_tutorial.md).

### Getting started
To run the demo version describing the case of Jack and Jill, a ficticious couple entering retirement:
1) Start the Anaconda Navigator. This has a green circle representative icon.
2) Launch a JupyterLab session by clicking *Launch* under the *JupyterLab* icon.
3) Using the navigation panel on the left, get to the directory where you unzipped ARP Lab.
4) Open the *jack+jill.ipynb* notebook from the browser interface of JupyterLab.
5) Follow instructions therein.

To edit files and run your own cases:
1) Make a copy of the files *template.ipynb* and *template.xlxs*.
2) Rename the copied files to something relevant to your case, say *kim+sam.ipynb* and *kim+sam.xlsx* if you are Kim and Sam.
3) Edit each tab of the *kim+sam.xlsx* file to reflect your names, wages, contributions, and large financial events (a.k.a., big-ticket items).
4) Open *kim+sam.ipynb* notebook in the JupyterLab interface.
5) Add the additional information and assumptions required to run a case;
6) Give me some feedback for improvement.

