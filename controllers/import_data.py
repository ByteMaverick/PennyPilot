from PyQt5.QtWidgets import QFileDialog, QApplication
import  pandas as pd

import pdfplumber
import re

from dao.balance_dao import BalanceDAO
from dao.bankrecords_dao import BankRecordsDAO
from dao.category_dao import CategoryDAO
from dao.expense_dao import ExpenseDAO
from dao.income_dao import IncomeDAO


from utils import extractor

from controllers import AiTools, ui_controller


def import_file(clear_existing=False, dev=False):

    if dev:
        path = "/Users/ansari/PycharmProjects/PennyPilot/View/assets/sample.csv"
    else:

        ui_controller.show_popup(" The CSV file must have the following columns: Date, Description, Credit,Debit, Balance")
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open File",
            directory="",
            filter="CSV Files (*.csv);;All Files (*)"
        )
        if not file_path:
            return
        elif not check_csv_structure(file_path):
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


    for row in df.itertuples():

        BalanceDAO().add_balance(account_id=row.id, amount=row.balance, date=row.date)
        CategoryDAO().add_category(account_id=row.id, name=row.category)
        BankRecordsDAO().add_record(id= row.id, date = row.date, description = row.description, credit =row.credit, debit = row.debit, actionId = row.actionId, balance = row.balance,category = row.category)
        ExpenseDAO().add_expense(account_id=row.id, amount= row.debit, date=row.date,category=row.category)
        IncomeDAO().add_income(account_id=row.id, amount=row.credit, date=row.date, category=row.category)


def get_all_records():
    records = BankRecordsDAO().get_all()

    data = [record.__dict__ for record in records]

    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])


    df["credit"] =df["credit"].fillna(0)
    df["debit"] =df["debit"].fillna(0)


    return df

def get_all_records_view():
    records = BankRecordsDAO().get_all()

    data = [record.__dict__ for record in records]

    df = pd.DataFrame(data)
    if "_sa_instance_state" in df.columns:
        df = df.drop(columns=["_sa_instance_state"])

    df =df.fillna("-")

    df = df[['date', 'description',"category",'credit','debit', 'balance']]
    return df


def import_bank_statement(clear_existing=False):
    file_path, _ = QFileDialog.getOpenFileName(
        parent=None,
        caption="Open File",
        directory="",
        filter="PDF Files (*.pdf);;All Files (*)"
    )

    if not file_path:
        return

    if clear_existing:
        BankRecordsDAO().delete_all()
        BalanceDAO().delete_all()
        ExpenseDAO().delete_all()
        IncomeDAO().delete_all()
        CategoryDAO().delete_all()


    pdf_path = file_path

    # Step 1: Read text from PDF
    with pdfplumber.open(pdf_path) as pdf:
        full_text = "\n".join([page.extract_text() for page in pdf.pages])

    lines = full_text.splitlines()


    accepted_formats = ["Date Details Withdrawals Deposits Balance", "Date Description Credit Debit Balance"]

    df = pd.DataFrame(columns=["date", "description", "credit", "debit", "balance"])
    table_start_index = 0
    for data in lines:
        if data.strip() in accepted_formats:
            table_start_index = lines.index(data)

    for data in lines[table_start_index:]:

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

    print(df)
    index_data(df,False)


def check_csv_structure(file, isCSV=True):
    df = pd.DataFrame()

    if isCSV:
        df = pd.read_csv(file)

    if df.shape[1] != 5:
        return ui_controller.show_popup("Incompatible CSV Shape!")

    cols = [col.strip().lower() for col in df.columns.tolist()]

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
