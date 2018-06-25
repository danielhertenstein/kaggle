import numpy as np
import pandas as pd
import scipy.stats as ss


def cramers_corrected_stat(confusion_matrix):
    """
    Calculate Cramers V statistic for categorial-categorial association.
    Uses correction from Bergsma and Wicher, Journal of the Korean Statistical 
    Society 42 (2013): 323-328
    """
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))    
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def association_matrix(dataframe, column, with_cols):
    associations = pd.Series(index=with_cols)
    for col in with_cols:
        confusion_matrix = pd.crosstab(dataframe[column], dataframe[col])
        cramers_v = cramers_corrected_stat(confusion_matrix)
        associations[col] = cramers_v
    return associations.sort_values(ascending=False)
