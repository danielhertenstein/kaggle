from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer, OneHotEncoder, StandardScaler


class DataFrameSelector(BaseEstimator, TransformerMixin):
    """Returns a subset of columns of a DataFrame"""

    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.loc[:, self.attribute_names]


class CategoryFactorizer(BaseEstimator, TransformerMixin):
    """
    Takes a single column DataFrame of type object (usually
    strings) and converts it into integer categories.
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        encoded = X.factorize()[0].reshape(-1, 1)
        return encoded


class SumColumns(BaseEstimator, TransformerMixin):
    """
    Creates a new column for the sum of
    the values in a given set of columns
    """

    def __init__(self, in_cols, out_col):
        self.in_cols = in_cols
        self.out_col = out_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X[self.out_col] = X.loc[:, self.in_cols].sum(axis=1)
        return X


def numerics_pipeline(attribute_names, scaling=False):
    pieces = [
        ('selector', DataFrameSelector(attribute_names)),
        ('imputer', Imputer(strategy="median")),
    ]
    if scaling:
        pieces.append(('std_scaler', StandardScaler()))
    return Pipeline(pieces)


def ordinal_category_pipeline(attribute_name):
    return Pipeline([
        ('selector', DataFrameSelector(attribute_name)),
        ('one_hot', OneHotEncoder())
    ])


def str_category_pipeline(attribute_name):
    return Pipeline([
        ('selector', DataFrameSelector(attribute_name)),
        ('factorize', CategoryFactorizer()),
        ('one_hot', OneHotEncoder())
    ])
