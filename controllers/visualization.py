from controllers.import_data import get_all_incomes, get_all_expenses
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def histogram_income_by_week():
    """
    Retrieves histogram of user's total income by week.
    :return: FigureCanvas containing the histogram.
    """

    # Retrieve DataFrame from database
    df = get_all_incomes()

    # Convert date column to datetime and extract the week
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)

    # Sum income per week
    weekly_income = df.groupby('week')['amount'].sum().reset_index()

    # Create histogram using matplotlib
    fig = Figure(figsize=(6,4))
    ax = fig.add_subplot(111)
    ax.bar(weekly_income['week'].astype(str), weekly_income['amount'])
    ax.set_title('Income by Week')
    ax.set_xlabel('Week')
    ax.set_ylabel('Income')
    fig.autofmt_xdate()

    return FigureCanvas(fig)

def histogram_expenses_by_week():
    """
    Retrieves histogram of user's total expenses by week.
    :return: FigureCanvas containing the histogram.
    """

    # Retrieve DataFrame from database
    df = get_all_expenses()

    # Convert date column to datetime and extract the week
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)

    # Sum expenses per week
    weekly_expenses = df.groupby('week')['amount'].sum().reset_index()

    # Create histogram using matplotlib
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.bar(weekly_expenses['week'].astype(str), weekly_expenses['amount'])
    ax.set_title('Expenses by Week')
    ax.set_xlabel('Week')
    ax.set_ylabel('Expenses')
    fig.autofmt_xdate()

    return FigureCanvas(fig)









