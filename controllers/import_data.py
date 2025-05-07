from PyQt5.QtWidgets import QFileDialog, QApplication
import  pandas as pd

import pdfplumber
import re

from dao.balance_dao import BalanceDAO
from dao.bankrecords_dao import BankRecordsDAO
from dao.category_dao import CategoryDAO
from dao.expense_dao import ExpenseDAO
from dao.income_dao import IncomeDAO

from controllers import AiTools, ui_controller


def import_file(clear_existing=False, dev=False,  profile_use= False):
    """
    Import data from csv file given by user.
    :param clear_existing: Boolean, whether to clear existing data.
    :param dev: Used for testing.
    :param profile_use: Used as a flag, to accept both pdf and csv files.
    :return: None or filepath.
    """

    path = ""
    if dev:
        path = "/Users/ansari/PycharmProjects/PennyPilot/View/assets/sample.csv"
    if profile_use:
        ui_controller.show_popup(
            "Please open a CSV file. The CSV file must have the following columns: Date, Description, Credit,Debit, Balance  or PDF Bankstatement")
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open File",
            directory="",
            filter="CSV or PDF Files (*.csv *.pdf);;CSV Files (*.csv);;PDF Files (*.pdf);;All Files (*)"
        )
        if file_path.lower().endswith('.csv'):
            if not check_csv_structure(file_path):
                return

            path = file_path
        elif file_path.lower().endswith('.pdf'):
            import_bank_statement(file_path=file_path)
            return file_path



    else:

        ui_controller.show_popup(
            "Please open a CSV file. The CSV file must have the following columns: Date, Description, Credit,Debit, Balance")
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open File",
            directory="",
            filter="CSV Files (*.csv);;All Files (*)"
        )
        if not check_csv_structure(file_path):
            return

        path = file_path

    QApplication.processEvents()

    if clear_existing:
        BankRecordsDAO().delete_all()
        BalanceDAO().delete_all()
        ExpenseDAO().delete_all()
        IncomeDAO().delete_all()
        CategoryDAO().delete_all()

    index_data(path)


def index_data(file, ispath =True):
    """
    Index data from file given by user.
    :param file: File of user.
    :param ispath: Boolean, whether file is CSV.
    :return: None.
    """
    df = pd.DataFrame
    if ispath:
        df = AiTools.generate_categories(file,load_popup =True)

    else:
        df = AiTools.generate_categories(file, False, load_popup =True)
    #df = pd.read_csv(file_path)
    existing_ids =  BankRecordsDAO().get_ids()
    existing_actionIds = BankRecordsDAO().get_actionIds()


    next_id = max(existing_ids) + 1 if existing_ids else 1
    df["id"] = list(range(next_id, next_id + len(df)))

    # Add action Ids
    new_Actionids = []
    i = 1
    while len(new_Actionids) < len(df):
        new_id = f"TXN{str(i).zfill(3)}"
        if new_id not in existing_actionIds:
            new_Actionids.append(new_id)
        i += 1

    # Add the ID column to the DataFrame
    df["actionId"] = new_Actionids

    load_data(df)


def load_data(df):
    """
    Load data from DataFrame into the SQLite database.
    :param df: DataFrame containing user's data.
    :return: None.
    """

    # Iterate through each row of the DataFrame
    for row in df.itertuples():
        # Use DAO objects to add rows into the corresponding table in the database
        BalanceDAO().add_balance(account_id=row.id, amount=row.balance, date=row.date)
        CategoryDAO().add_category(account_id=row.id, name=row.category)
        BankRecordsDAO().add_record(id= row.id, date = row.date, description = row.description, credit =row.credit, debit = row.debit, actionId = row.actionId, balance = row.balance,category = row.category)
        ExpenseDAO().add_expense(account_id=row.id, amount= row.debit, date=row.date,category=row.category)
        IncomeDAO().add_income(account_id=row.id, amount=row.credit, date=row.date, category=row.category)


def get_all_records():
    """
    Retrieve all bank records of the user.
    :return: DataFrame containing all bank records.
    """

    # Get records from database
    records = BankRecordsDAO().get_all()

    # Convert records into a dictionary
    data = [record.__dict__ for record in records]

    # Turn dictionary into a DataFrame
    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])

    # Handle missing values
    df["credit"] =df["credit"].fillna(0)
    df["debit"] =df["debit"].fillna(0)

    return df


def get_all_incomes():
    """
    Retrieve all incomes of the user.
    :return: DataFrame containing all incomes.
    """

    # Get incomes from database
    incomes = IncomeDAO().get_all()

    # Convert incomes into a dictionary
    data = [income.__dict__ for income in incomes]

    # Convert dictionary into a DataFrame
    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])

    return df

def get_all_expenses():
    """
    Retrieve all expenses of the user.
    :return: DataFrame containing all expenses.
    """

    # Get expenses from database
    expenses = ExpenseDAO().get_all()

    # Convert expenses into a dictionary
    data = [expense.__dict__ for expense in expenses]

    # Turn dictionary into a DataFrame
    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])

    return df




def get_all_records_view():
    """
    Retrieve all bank records of the user to be displayed as a table in the view.
    :return: DataFrame containing records.
    """

    # Get records from database
    records = BankRecordsDAO().get_all()

    # Convert records into a dictionary
    data = [record.__dict__ for record in records]

    # Turn dictionary into a DataFrame
    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])

    # Fill missing values with "-"
    df =df.fillna("-")

    # Retrieve relevant columns only
    df = df[['date', 'description',"category",'credit','debit', 'balance']]
    return df



def import_bank_statement(clear_existing=False, profile_use = False, file_path= None):
    """
       Read bank statement as PDF file.
       :param clear_existing: Boolean, whether to clear existing values in database.
       :param profile_use: Used as a flag, to accept both pdf and csv files.
       :param file_path: Path to the file, used with import_file() method.
       :return: None.
       """

    # Locate File from System
    if file_path is None:
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open File",
            directory="",
            filter="PDF Files (*.pdf);;All Files (*)"
        )


    # File not found
    if not file_path:
        return

    # Clear existing values in database if specified
    if clear_existing:
        BankRecordsDAO().delete_all()
        BalanceDAO().delete_all()
        ExpenseDAO().delete_all()
        IncomeDAO().delete_all()
        CategoryDAO().delete_all()


    pdf_path = file_path

    # Read text from PDF using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        full_text = "\n".join([page.extract_text() for page in pdf.pages])

    lines = full_text.splitlines()


    accepted_formats = ["Date Details Withdrawals Deposits Balance", "Date Description Credit Debit Balance"]

    # Create DataFrame
    df = pd.DataFrame(columns=["date", "description", "credit", "debit", "balance"])
    table_start_index = 0
    for data in lines:
        if data.strip() in accepted_formats:
            table_start_index = lines.index(data)

    for data in lines[table_start_index:]:
        # Regex pattern to detect 2 kinds of formated data
        pattern = r"(\d{1,2}/\d{1,2}/\d{2,4})\s+(.+?)\s+(?:([\d,]+\.\d{2})\s+-\s+)?(?:-?\s*([\d,]+\.\d{2})\s+)?([\d,]+\.\d{2})"
        data = data.replace(",", "")
        match = re.match(pattern, data)
        if match:
            date = match.group(1)
            desc = match.group(2)
            credit = match.group(3)
            debit = match.group(4)
            balance = match.group(5)

            df.loc[len(df)] = [date, desc, credit, debit, balance]

    index_data(df,False)


def check_csv_structure(file, isCSV=True):
    """
    Verify if CSV file given by user is in correct structure.
    :param file: CSV file of user.
    :param isCSV: Boolean, whether file is CSV.
    :return: Boolean, whether CSV has correct structure.
    """

    # Create DataFrame
    df = pd.DataFrame()

    # Read CSV if isCSV is True
    if isCSV:
        df = pd.read_csv(file)

    # Check shape of DF
    if df.shape[1] != 5:
        return ui_controller.show_popup("Incompatible CSV Shape!")

    cols = [col.strip().lower() for col in df.columns.tolist()]

    # Check column names
    if cols[0] != "date":
        return ui_controller.show_popup("Incompatible CSV Shape!")
    elif cols[1] != "description":
        return ui_controller.show_popup("Incompatible CSV Shape!")
    elif cols[2] != "credit":
        return ui_controller.show_popup("Incompatible CSV Shape!")
    elif cols[3] != "debit":
        return ui_controller.show_popup("Incompatible CSV Shape!")
    elif cols[4] != "balance":
        return ui_controller.show_popup("Incompatible CSV Shape!")

    return True  # success
