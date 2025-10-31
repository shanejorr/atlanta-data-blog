# Data import and cleaning functions

import re
import pandas as pd


def extract_numeric_value(value):
    """
    Extract first numeric value from string using regex.
    Returns NaN if no numeric value found.

    Handles cases like:
    - '100.00+' → 100.0
    - '85.99' → 85.99
    - 'NA', 'TFS', or any non-numeric string → NaN
    """
    if pd.isna(value):
        return pd.NA

    # Extract first numeric sequence (digits, optional decimal, digits)
    match = re.search(r"\d+\.?\d*", str(value))

    return float(match.group(0)) if match else pd.NA
