#!/usr/bin/env python

import os
from setuptools import setup, find_packages

fileDir = os.path.dirname(__file__)

LONG_DESCRIPTION = """
Pandashells is a set of unix command-line tools that provide accessibility
to the python data stack directly from the bash prompt.  Users can utilize
pandas-based data-munging, perform linear regression, and even take
the spectral decomposition of non-uniformly sampled time series.
"""

setup(
    name="pandashells",
    version="0.1.4",
    author="Rob deCarvalho",
    author_email="unlisted",
    description=("Command line data tools"),
    license="BSD",
    keywords="pandas plot plotting data dataframe command line cli statistics stats",
    url="https://github.com/robdmc/pandashells",
    packages=find_packages(),
    package_data={'pandashells': ['example_data/*.csv']},
    # include_package_data=True,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
    ],
    # If you add/remove a requirement, please also update full
    extras_require = {
        'pandas': ['numpy', 'pandas', 'scipy', 'statsmodels'],
        'full': [
            'numpy', 'pandas', 'scipy', 'statsmodels',
            'astroML', 'supersmoother', 'gatspy',
            'matplotlib', 'mpld3', 'seaborn',
        ],
    },
    entry_points={
        'console_scripts': [
            'p.config = pandashells.bin.p_config:main',
            'p.crypt = pandashells.bin.p_crypt:main',
            'p.format = pandashells.bin.p_format:main',
            'p.parallel = pandashells.bin.p_parallel:main',

            'p.df = pandashells.bin.p_df:main [pandas]',
            'p.example_data = pandashells.bin.p_example_data:main [pandas]',
            'p.linspace = pandashells.bin.p_linspace:main [pandas]',
            'p.merge = pandashells.bin.p_merge:main [pandas]',
            'p.rand = pandashells.bin.p_rand:main [pandas]',
            'p.regress = pandashells.bin.p_regress:main [pandas]',
            'p.sig_edit = pandashells.bin.p_sig_edit:main [pandas]',

            'p.cdf = pandashells.bin.p_cdf:main [full]',
            'p.facet_grid = pandashells.bin.p_facet_grid:main [full]',
            'p.hist = pandashells.bin.p_hist:main [full]',
            'p.plot = pandashells.bin.p_plot:main [full]',
            'p.regplot = pandashells.bin.p_regplot:main [full]',

            'p.lomb_scargle = pandashells.bin.p_lomb_scargle:main [full]',
        ],
    }
)
