continuous_columns = [
    'LotFrontage',
    'LotArea',
    'MasVnrArea',
    'BsmtFinSF1',
    'BsmtFinSF2',
    'BsmtUnfSF',
    'TotalBsmtSF',
    '1stFlrSF',
    '2ndFlrSF',
    'LowQualFinSF',
    'GrLivArea',
    'GarageArea',
    'WoodDeckSF',
    'OpenPorchSF',
    'EnclosedPorch',
    '3SsnPorch',
    'ScreenPorch',
    'PoolArea',
    'MiscVal',
]

categorical_unordered_columns = [
    'MSSubClass',
    'MSZoning',
    'Street',  # Debatable
    'Alley',
    'LotShape',
    'LandContour',
    'Utilities',  # Debatable
    'LotConfig',
    'LandSlope',
    'Neighborhood',
    'Condition1',
    'Condition2',
    'BldgType',
    'HouseStyle',
    'RoofStyle',
    'RoofMatl',
    'Exterior1st',
    'Exterior2nd',
    'MasVnrType',
    'Foundation',
    'Heating',
    'CentralAir',
    'Electrical',  # Debatable
    'GarageType',  # Debatable
    'GarageFinish',  # Debatable
    'MiscFeature',
    'MoSold',
    'SaleType',
    'SaleCondition',
]

categorical_ordered_columns = [
    'OverallQual',
    'OverallCond',
    'YearBuilt',  # Debatable
    'YearRemodAdd',  # Debatable
    'ExterQual',
    'ExterCond',
    'BsmtQual',
    'BsmtCond',
    'BsmtExposure',  # Debatable
    'BsmtFinType1',  # Debatable
    'BsmtFinType2',  # Debatable
    'HeatingQC',
    'BsmtFullBath',
    'BsmtHalfBath',
    'FullBath',
    'HalfBath',
    'BedroomAbvGr',
    'KitchenAbvGr',
    'KitchenQual',
    'TotRmsAbvGrd',
    'Functional',
    'Fireplaces',
    'FireplaceQu',
    'GarageYrBlt',  # Debatable
    'GarageCars',
    'GarageQual',
    'GarageCond',
    'PavedDrive',  # Debatable
    'PoolQC',
    'Fence',
    'YrSold',  # Debatable
]
