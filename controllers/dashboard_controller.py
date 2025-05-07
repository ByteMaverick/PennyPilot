from controllers.import_data import get_all_records
from utils.extractor import month_extractor


def current_balance():
    """
    Get current balance of user.
    :return: Most recent balance of user.
    """
    df = get_all_records()

    return df["balance"].iloc[-1]

def average_balance():
    """
    Get average balance of user.
    :return: Mean balance of user.
    """
    df = get_all_records()

    return df["balance"].mean()

def get_monthly_total_by_type(transaction_type):
    """
    Get monthly total by transaction type.
    :param transaction_type: Type of transaction.
    :return: Tuple, containing name of current month, total amount, and number of current month
    """

    # Map number of month to name of month
    months_dict = {
        "01": "january", "02": "february", "03": "march", "04": "april", "05": "may", "06": "june",
        "07": "july", "08": "august", "09": "september", "10": "october", "11": "november", "12": "december"
    }

    # Get DataFrame containing all bank records of user
    df = get_all_records()
    latest_timestamp = df["date"].iloc[-1]
    current_month_num = month_extractor(latest_timestamp)
    current_month_name = months_dict[current_month_num]

    # Sum amount in the current month
    total_amount = 0
    for row in df.itertuples():
        if month_extractor(row.date) == current_month_num:
            total_amount += getattr(row, transaction_type)

    return current_month_name, total_amount, current_month_num


def money_spent_compared_last_month():
    """
    Money spent by user compared to last month.
    :return: String, message displaying how much money the user spent compared to previous month.
    """

    # Get DataFrame containing all bank records of user.
    df = get_all_records()
    last_month_spent = 0

    current_month_word, current_month_spent, current_month_num = get_monthly_total_by_type("debit")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    # Get money spent in last month
    for row in df.itertuples():
        if month_extractor(row.date) == last_month_num:
            last_month_spent += row.debit

    # Calculate difference
    difference = current_month_spent - last_month_spent

    # Return corresponding message based on difference and how much money spent in last month
    if difference > 0 and last_month_spent != 0:
        percentage = difference/last_month_spent*100
        return  f"Spent {percentage: 0.2f} % more money compared to last month"

    elif last_month_spent == 0:
        return f"You spent ${current_month_spent:0.2f} "

    else:
        percentage = difference / last_month_spent * 100
        return  f"Spent {abs(percentage): 0.2f} % less money compared to last month"


def balance_compared_last_month():
    """
    Balance of user compared to the last month.
    :return: String, message displaying how much money the user spent compared to previous month.
    """

    # Get DataFrame containing all bank records of user.
    df = get_all_records()

    balance_last_month =  0
    count =0

    current_month_name, total_amount, current_month_num = get_monthly_total_by_type("balance")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    # Calculate balance last month.
    for row in df.itertuples():
        if month_extractor(row.date) == last_month_num:
            balance_last_month += row.balance
            count = count + 1

    # Calculate average balance of last month
    if count > 0:
        average_balance_last_month = balance_last_month/count
    if count == 0:
        average_balance_last_month = balance_last_month

    difference = current_balance() - average_balance_last_month

    # Return message depending on difference
    if difference > 0:
        percentage = difference/current_balance()*100
        return f"{percentage: 0.2f} % more money compared to last month"
    if total_amount == 0:
        return "You lost 100% of the money"




def money_made_compared_last_month():
    """
    Money made compared to last month.
    :return: String, message displaying how much money the user spent compared to previous month.
    """

    # Get DataFrame containing all bank records of user.
    df = get_all_records()
    last_month_income = 0

    current_month_word, current_month_income, current_month_num = get_monthly_total_by_type("credit")

    last_month_num = str(int(current_month_num) - 1).zfill(2)

    # Calculate income of last month
    for row in df.itertuples():
        if month_extractor(row.date) == last_month_num:
            last_month_income += row.credit

    # Calculate difference
    difference = current_month_income - last_month_income

    # Return message depending on percentage difference
    if difference > 0 and last_month_income != 0:
        percentage = difference/last_month_income*100
        return  f"Made {percentage: 0.2f} % more money compared to last month"

    elif last_month_income == 0:
        return f" You made ${current_month_income:0.2f} "

    else:
        percentage = difference / last_month_income * 100
        return  f"Made {abs(percentage): 0.2f} % less money compared to last month"



