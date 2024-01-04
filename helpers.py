import os

import gspread
import boto3
import pathlib
from dateutil import parser
import urllib.parse
import json
import pandas as pd


def google_sheets_connection():
    """Helper function to pull json credentials
    file from storage and authorise gspread library
    for Google Sheets manipulation.
    Returns:
        Authorised gspread account
        gc = gspread.service_account()
    """

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    # Download credentials file if not present
    file = pathlib.Path("creds.json")
    if not file.exists():

        # access environment variables
        key = os.getenv("DO_ACCESS_KEY")
        secret = os.getenv("DO_SECRET_KEY")

        session = boto3.session.Session()
        client = session.client(
            "s3",
            region_name="sgp1",
            endpoint_url="https://sgp1.digitaloceanspaces.com",
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )

        client.download_file(
            "marquin-space-object-storage-01",
            "web-resources/marquin-personal-tools-5f84ef73756b.json",
            "creds.json",
        )

    gc = gspread.service_account(filename="creds.json")

    return gc



def valid_username_check(a_username:str):
    """Checks to see if the username is valid.
    Returns True if the username is valid, False otherwise.

    
    Args:
        a_username (str): _description_
    """

    valid_names_list = ["marquin", "quinny", "m", "quin", "caroline", "caz", "cas", "c"]

    if a_username.lower in valid_names_list:
        valid = True
    else:
        valid = False

    return valid

def load_workout_data():

    gc = google_sheets_connection()

    ## Load Sheet
    #sh = gc.open_by_key('1aKIpmgm1pkNOMNCLN8RFn8a1E_BgeSHheHUTB46vpCo')
    sh = gc.open("Reps and Sets")

    ## Load data
    #data_worksheet = sh.worksheet("data_v2")
    data_worksheet = sh.worksheet("Sheet1")
    rows = data_worksheet.get_all_values()

    df = pd.DataFrame.from_records(rows)
    my_columns = df.iloc[0]
    df.columns = my_columns
    df = df.iloc[1:]

    # select first 31 columns in spreadsheet
    #df = df.iloc[:, 0:31]
    df = df.reset_index(drop=True)
    df["reps"] = pd.to_numeric(df["reps"])
    #df = get_as_dataframe(data_worksheet, usecols=[0,1,2,7,11,13])

    return df