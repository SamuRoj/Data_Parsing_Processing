import pandas as pd

def drop_columns(df):
    print("Dropping unused columns")
    columns = ["phone_number", "address", "zip_code", "country", "emergency_contact", "ssn", "bank_account"]
    for column in columns:
        df = df.drop([column], axis=1)

    print(print(f"Remaining columns {df.shape[1]}"))
    return df

def drop_na_rows(df):
    print("Dropping NA rows")
    df = df.dropna()
    print(f"Remaining rows {df.shape[0]}")
    return df

def drop_duplicates(df):
    print("Dropping duplicates")
    df = df.drop_duplicates(subset="employee_id")
    print(f"Remaining rows {df.shape[0]}")
    return df

def to_datetime(df):
    print("Turning dates into datetime")
    df["birth_date"] = pd.to_datetime(df["birth_date"])
    df["hire_date"] = pd.to_datetime(df["hire_date"])
    df["last_review_date"] = pd.to_datetime(df["last_review_date"])
    print("Turned to dates")
    return df

def verify_numeric_types(df):
    print("Verifying numeric types")
    columns =  ["days_service", "base_salary", "bonus_percentage", "performance_score", 
                "vacation_days", "sick_days"]
    for column in columns:
        df = df[df[column] >= 0]
        
    print(f"Remaining rows {df.shape[0]}")
    return df

def verify_date(df):
    print("Verifying dates")
    df = df[df["birth_date"] < df["hire_date"]]
    df = df[df["hire_date"] <= df["last_review_date"]]
    print(f"Remaining rows {df.shape[0]}")
    return df

def clean(df):
    df = drop_columns(df)
    df = drop_na_rows(df)
    df = drop_duplicates(df)
    df = to_datetime(df)
    df = verify_numeric_types(df)
    df = verify_date(df)
    return df
