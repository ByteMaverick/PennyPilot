from controllers.import_data import get_all_records
from utils.extractor import month_extractor


def current_balance():
    df = get_all_records()

    return df["balance"].iloc[-1]

def average_balance():
    df = get_all_records()

    return df["balance"].mean()

def get_monthly_total_by_type(transaction_type):
    months_dict = {
        "01": "january", "02": "february", "03": "march", "04": "april", "05": "may", "06": "june",
        "07": "july", "08": "august", "09": "september", "10": "october", "11": "november", "12": "december"
    }

    df = get_all_records()
    latest_timestamp = df["timestamp"].iloc[-1]
    current_month_num = month_extractor(latest_timestamp)
    current_month_name = months_dict[current_month_num]

    total_amount = 0

    for row in df.itertuples():
        if month_extractor(row.timestamp) == current_month_num:
            total_amount += getattr(row, transaction_type)

    return current_month_name, total_amount, current_month_num


def money_spent_compared_last_month():
    df = get_all_records()
    last_month_spent = 0

    current_month_word, current_month_spent, current_month_num = get_monthly_total_by_type("debit")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    for row in df.itertuples():
        if month_extractor(row.timestamp) == last_month_num:
            last_month_spent += row.debit

    difference = current_month_spent - last_month_spent

    if difference > 0 and last_month_spent != 0:
        percentage = difference/last_month_spent*100
        return  f"Spent {percentage: 0.2f} % more money compared to last month"

    elif last_month_spent == 0:
        return f"You spent ${current_month_spent:0.2f} "

    else:
        percentage = difference / last_month_spent * 100
        return  f"Spent {abs(percentage): 0.2f} % less money compared to last month"


def balance_compared_last_month():

    df = get_all_records()

    balance_last_month =  0
    count =0

    current_month_name, total_amount, current_month_num = get_monthly_total_by_type("balance")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    for row in df.itertuples():
        if month_extractor(row.timestamp) == last_month_num:
            balance_last_month += row.balance
            count = count + 1

    if count > 0:
        average_balance_last_month = balance_last_month/count
    if count == 0:
        average_balance_last_month = balance_last_month

    difference = current_balance() - average_balance_last_month

    if difference > 0:
        percentage = difference/current_balance()*100
        return f"{percentage: 0.2f} % more money compared to last month"
    if total_amount == 0:
        return "You lost 100% of the money"




def money_made_compared_last_month():
    df = get_all_records()
    last_month_income = 0

    current_month_word, current_month_income, current_month_num = get_monthly_total_by_type("credit")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    for row in df.itertuples():
        if month_extractor(row.timestamp) == last_month_num:
            last_month_income += row.credit

    difference = current_month_income - last_month_income

    if difference > 0 and last_month_income != 0:
        percentage = difference/last_month_income*100
        return  f"Made {percentage: 0.2f} % more money compared to last month"

    elif last_month_income == 0:
        return f" You made ${current_month_income:0.2f} "

    else:
        percentage = difference / last_month_income * 100
        return  f"Made {percentage: 0.2f} % less money compared to last month"



