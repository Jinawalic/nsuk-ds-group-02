import numpy as np
import pandas as pd

LGA_FIXES = {
    "Nasarawa-Eggon": "Nasarawa Eggon",
    "N/Eggon": "Nasarawa Eggon",
    "Nassarawa": "Nasarawa",
    "Akwaga": "Akwanga",
}

YES_NO_COLUMNS = [
    "staking",
    "organic_manure",
    "intercropped",
    "cooperative_member",
    "access_to_credit",
]
YES_NO_MAP = {"yes": "Yes", "y": "Yes", "no": "No", "n": "No"}

GENDER_MAP = {
    "male": "Male",
    "m": "Male",
    "female": "Female",
    "f": "Female",
}

MONTH_MAP = {
    "dec": "December", "12": "December",
    "jan": "January",  "01": "January",
    "feb": "February", "02": "February",
    "mar": "March",    "03": "March",
    "apr": "April",    "04": "April",
}

VALID_RANGES = {
    "farmer_age": (15, 90),
    "farm_size_ha": (0.05, 50),
    "mound_density_per_ha": (2000, 25000),
    "yield_t_per_ha": (0.5, 40),
}


def clean_yam_data(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Clean raw Nasarawa State yam survey records without imputing features."""
    df = df_raw.copy()
    df.columns = df.columns.str.strip().str.lower()

    # 2.1 Remove exact duplicate rows
    df = df.drop_duplicates()

    # 2.2 Standardise LGA names
    df["lga"] = df["lga"].str.strip().str.title().replace(LGA_FIXES)

    # 2.3 Standardise Yes/No columns
    for col in YES_NO_COLUMNS:
        df[col] = df[col].str.strip().str.lower().map(YES_NO_MAP)

    # 2.4 Standardise gender
    df["gender"] = df["gender"].str.strip().str.lower().map(GENDER_MAP)

    # 2.5 Standardise planting month
    df["planting_month"] = (
        df["planting_month"].astype(str).str.strip().str.lower().str[:3].map(MONTH_MAP)
    )

    # 2.6 Convert text-formatted numbers and sentinel codes
    df["fertilizer_kg_per_ha"] = pd.to_numeric(
        df["fertilizer_kg_per_ha"], errors="coerce"
    )
    df["harvest_revenue_naira"] = pd.to_numeric(
        df["harvest_revenue_naira"].astype(str).str.replace(r"[N₦,]", "", regex=True),
        errors="coerce",
    )
    df["rainfall_mm"] = df["rainfall_mm"].replace(-999, np.nan)

    # 2.7 Set impossible numeric values outside valid ranges to NaN
    for col, (low, high) in VALID_RANGES.items():
        outside = ~df[col].between(low, high) & df[col].notna()
        df.loc[outside, col] = np.nan

    # 2.8 Drop rows missing the outcome variable
    df = df.dropna(subset=["yield_t_per_ha"]).reset_index(drop=True)

    return df