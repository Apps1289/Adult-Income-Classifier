from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, df, y=None):
        return self

    def transform(self, df):
        df = df.copy()

        df["net_capital_gain"] = df["capital_gain"] - df["capital_loss"]
        df["capital_gain_ratio"] = df["capital_gain"] / (df["net_capital_gain"] + 1)
        df["capital_loss_ratio"] = df["capital_loss"] / (df["net_capital_gain"] + 1)

        df["has_capital_impact"] = (
            df["capital_gain_ratio"].apply(lambda x: 1 if x > 0 else 0).astype(int)
        )

        df["age_group"] = pd.cut(
            df["age"],
            bins=[0, 25, 45, 65, 100],
            labels=["Entry_Level", "Mid_Career", "Senior", "Retired"],
        ).astype(str)

        df["experience"] = df["age"] - df["education_num"] - 5
        df["experience"] = df["experience"].clip(lower=0)

        return df
