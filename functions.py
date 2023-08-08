import pandas as pd
import numpy as np
import re

def clean_and_prepare(df):
    #Replace NaNs with 0
    df['LotFrontage'].replace(np.nan, 0.0, inplace=True)

    #FillNAs from dataset
    df.fillna('NA', inplace=True)

    #Create dictionaries to transform categorical features into ordinal features
    score_dictionary_1= {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa': 2, 'Po': 1, 'NA': 0}
    basement_exposure_dictionary={'Gd':4, 'Av':3, 'Mn':2, 'No':1, 'NA':0}
    basement_rating_dictionary={'GLQ':6, 'ALQ':5, 'BLQ':4, 'Rec':3, 'LwQ':2, 'Unf':1, 'NA':0}
    yes_no_dictionary={'N':0, 'Y':1}
    home_functionality_dictionary={'Sal':0, 'Sev':1, 'Maj2':2, 'Maj1':3, 'Mod':4, 'Min2':5, 'Min1':6, 'Typ':7}
    garage_finish={'Fin':3, 'RFn':2, 'Unf':1, 'NA':0}

    #Replace values on columns using dictionaries
    for element in ['ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'HeatingQC', 'KitchenQual', 'FireplaceQu', 'GarageQual', 'GarageCond', 'PoolQC']:
        df[element].replace(score_dictionary_1, inplace=True)
    df['BsmtExposure'].replace(basement_exposure_dictionary, inplace=True)
    for element in ['BsmtFinType1', 'BsmtFinType2']:
        df[element].replace(basement_rating_dictionary, inplace=True)
    df['CentralAir'].replace(yes_no_dictionary, inplace=True)
    df['Functional'].replace(home_functionality_dictionary, inplace=True)
    df['MasVnrArea'].replace('NA', 0.0, inplace=True)
    df['GarageYrBlt'].replace('NA', 0.0, inplace=True)

    #Drop Id of the houses
    df.drop('Id', axis=1, inplace=True)

    #Split columns into categorical and non categorical
    categorical_columns = []
    non_categorical_columns = []
    for element in df.columns:
        if isinstance(df[element][0], str):
            categorical_columns.append(element)
        else:
            non_categorical_columns.append(element)
    
    #Create dummies for categorical variables
    df_final = pd.get_dummies(df, columns=categorical_columns)

    #Return final dataset
    return df_final