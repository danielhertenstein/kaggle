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
    n = confusion_matrix.values.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def association_matrix(dataframe, column, with_cols):
    associations = pd.Series(index=with_cols)
    for col in with_cols:
        if col == column:
            continue
        confusion_matrix = pd.crosstab(dataframe[column], dataframe[col])
        cramers_v = cramers_corrected_stat(confusion_matrix)
        associations[col] = cramers_v
    return associations.sort_values(ascending=False)


def anova_with_effect_size(data, nominal, continuous):
    """
    Computes the p-value and intraclass correlation coefficient effect size
    for the correlation between a nominal and a continuous variable.

    Pretty much taken from: https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
    """
    data = data.loc[:, [nominal, continuous]].copy().dropna()
    total_obs = data.shape[0]
    groups = data.groupby(nominal, sort=False)
    obs_per_group = groups.size().values
    num_groups = len(groups)

    df_between = num_groups - 1
    df_within = total_obs - num_groups

    group_sum_squared_average = sum(groups.sum()[continuous].values ** 2 / obs_per_group)
    y_sum_squared_average = data[continuous].values.sum() ** 2 / total_obs
    sum_y_squared = sum(value ** 2 for value in data[continuous].values)

    ss_between = group_sum_squared_average - y_sum_squared_average
    ss_within = sum_y_squared - group_sum_squared_average

    ms_between = ss_between / df_between
    ms_within = ss_within / df_within

    f = ms_between / ms_within
    p = ss.f.sf(f, df_between, df_within)
    icc = (ms_between - ms_within) / (ms_between + df_between * ms_within)

    return p, icc


def anova_matrix(data, nominal, continuous_cols):
    anovas = pd.DataFrame(index=continuous_cols, columns=['p_value', 'effect_size'])
    for col in continuous_cols:
        p, icc = anova_with_effect_size(data, nominal, col)
        anovas.at[col, 'p_value'] = p
        anovas.at[col, 'effect_size'] = icc
    return anovas.sort_values(by='effect_size', ascending=False)
