"""
This module defines the following routines used by the 'ingest' step of the regression pipeline:

- ``load_file_as_dataframe``: Defines customizable logic for parsing dataset formats that are not
  natively parsed by MLflow Pipelines (i.e. formats other than Parquet, Delta, and Spark SQL).
"""

import logging

from pandas import DataFrame

_logger = logging.getLogger(__name__)


def load_file_as_dataframe(file_path: str, file_format: str) -> DataFrame:
    """
    Load content from the specified dataset file as a Pandas DataFrame.

    This method is used to load dataset types that are not natively  managed by MLflow Pipelines
    (datasets that are not in Parquet, Delta Table, or Spark SQL Table format). This method is
    called once for each file in the dataset, and MLflow Pipelines automatically combines the
    resulting DataFrames together.

    :param file_path: The path to the dataset file.
    :param file_format: The file format string, such as "csv".
    :return: A Pandas DataFrame representing the content of the specified file.
    """

    if file_format == "csv":
        _logger.warning(
            "Loading dataset CSV using `pandas.read_csv()` with default arguments and assumed index"
            " column 0 which may not produce the desired schema. If the schema is not correct, you"
            " can adjust it by modifying the `load_file_as_dataframe()` function in"
            " `steps/ingest.py`"
        )

        import requests
        data = requests.get('http://localhost:8008/api/disasters').json()

        return DataFrame(data)
    else:
        raise NotImplementedError
