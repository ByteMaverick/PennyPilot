from PyQt5.QtWidgets import QFileDialog
import  pandas as pd

from dao.balance_dao import BalanceDAO
from dao.bankrecords_dao import BankRecordsDAO
from dao.category_dao import CategoryDAO
from dao.expense_dao import ExpenseDAO
from dao.income_dao import IncomeDAO


from utils import extractor

from controllers import  AiTools


def import_file(clear_existing=False, dev=False):
    if dev:
        path = "/Users/ansari/PycharmProjects/PennyPilot/View/assets/sample.csv"
    else:
        file_path, _ = QFileDialog.getOpenFileName(
            parent=None,
            caption="Open File",
            directory="",
            filter="CSV Files (*.csv);;All Files (*)"
        )
        if not file_path:
            return
        path = file_path

    if clear_existing:
        BankRecordsDAO().delete_all()
        BalanceDAO().delete_all()
        ExpenseDAO().delete_all()
        IncomeDAO().delete_all()
        CategoryDAO().delete_all()

    index_data(path)





def index_data(file_path):

    df = AiTools.generate_categories(file_path)
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

    df["time"] = df["timestamp"].map(extractor.time_extractor)
    df["date"] = df["timestamp"].map(extractor.date_extractor)

    # Ai feature

    for row in df.itertuples():

        BalanceDAO().add_balance(account_id=row.id, amount=row.balance, timestamp=row.timestamp)
        CategoryDAO().add_category(account_id=row.id, name=row.category)
        BankRecordsDAO().add_record(id= row.id, timestamp = row.timestamp, description = row.description, credit =row.credit, debit = row.debit, actionId = row.actionId, balance = row.balance,category = row.category)
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

    df.fillna("-",inplace =True)

    df = df[['timestamp', 'description',"category",'credit','debit', 'balance']]



    return df