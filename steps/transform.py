"""
This module defines the following routines used by the 'transform' step of the regression pipeline:

- ``transformer_fn``: Defines customizable logic for transforming input data before it is passed
  to the estimator during model inference.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import *


def transformer_fn():
    """
    Returns an *unfitted* transformer that defines ``fit()`` and ``transform()`` methods.
    The transformer's input and output signatures should be compatible with scikit-learn
    transformers.
    """
    return Pipeline(
            steps=[(
                "encoder",
                ColumnTransformer(
                    transformers=[
                        #(
                        #    "year_encoder",
                        #    MinMaxScaler(),
                        #    ["roughYear"]
                        #),
                        (
                            "ordinal_encoder",
                            OrdinalEncoder(),
                            ["continent", "disasterType"]
                        )
                    ]
                )
            )]
        )
