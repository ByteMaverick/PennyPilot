from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFormLayout, QFrame, QAction, QGraphicsDropShadowEffect, QMenu,
    QStackedWidget, QTableWidgetItem, QTableWidget, QHeaderView
)
from PyQt5.QtGui import QFont, QCursor, QIcon, QColor
from PyQt5.QtCore import Qt
import sys
from controllers import ui_controller as ui_controller, import_data, dashboard_controller, visualization

""" 
   main_layout is the entire dashboard  window. We will multiple layout managers inside this layout. Where is a brief overview of the structure:
   
   - Header(QHBoxLayout()) = contains Logo, and two drop down menus. First is the three dots menu and the import menu
   - view_change_layout(QHBoxLayout()) = contains the buttons that changes main panel view(Graphs or Transactions) and the search bar 
   - money_tracking_layout(QHBoxLayout()) = contains three   panels which display the money tracking info
      -  current_balance_layout(QVBoxLayout()) = contains balance  info
      -  monthly_spending_layout(QVBoxLayout()) = contains monthly spending info
      -  monthly_income_layout = contains monthly income info
   - dashboard_layout (Stacked with transaction_layout) = Contains all the graphs(TO-DO)
   - transaction_layout(Stacked with dashboard_layout) = Display all the records 
      
    """

class Dashboard(QWidget):
    def __init__(self, email=None, number=None):
        super().__init__()
        self.email = email
        self.number = number

        self.clean_all()
        self.setWindowTitle("PennyPilot")
        self.setGeometry(700, 500, 900, 700)
        self.setStyleSheet("background-color: white;")



        main_layout = QVBoxLayout()


        # Header
        ## Setting Title
        header_layout = QHBoxLayout()
        logo_label = QLabel("PennyPilot")
        logo_label.setAlignment(Qt.AlignLeft)
        logo_label.setStyleSheet(
            """
            color: #000;
            font-family: Inter;
            font-size: 30px;
            font-style: normal;
            font-weight: 600;
            line-height: 150%; /* 30px */
            letter-spacing: -0.2px;       """
        )


        # Line
        ## Design Line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: #ccc;")

        # Center it using a layout
        line_layout = QHBoxLayout()
        line_layout.addStretch()
        line_layout.addWidget(line)
        line_layout.addStretch()

        # menu Button
        menu_button = QPushButton(" ...")
        menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        menu_button.setFixedSize(56, 40)
        menu_button.setStyleSheet("""
                                    QPushButton {
                                        border-radius: 8px;
                                        background: #EEE;
                                        color: black;
                                        border: none;
                                        border-radius: 8px;
                                        font-weight: bold;
                                        font-size: 11pt;
                                        
                                    }
                                    QPushButton:hover {
                                        background-color: #b0aeab;
                                    }""")
        # Create the dropdown menu for extra stuff
        menu = QMenu()
        profiles_button = menu.addAction("Profiles")
        profiles_button.triggered.connect(self.profile_window)
        log_out_button = menu.addAction("Log out")
        log_out_button.triggered.connect(self.log_out)
        about_button = menu.addAction("About")
        about_button.triggered.connect(lambda: ui_controller.show_popup(
            "PennyPilot — Track your income, expenses, and spending habits.\n© 2025 Mohammed & Alex. All rights reserved."
        ))


        menu.setStyleSheet("""
                    QMenu {
                        background-color: white;
                        border: 1px solid #ccc;
                        border-radius: 10px;
                        padding: 5px;
                        color: black;
                    }
                    QMenu::item {
                        padding: 8px 20px;
                        border-radius: 5px;
                    }
                    QMenu::item:selected {
                        background-color: #0078d7;
                        color: white;
                    }""")

        menu_button.clicked.connect(lambda: menu.exec_(menu_button.mapToGlobal(menu_button.rect().bottomLeft())))


        # import button
        import_button = QPushButton("Import")
        import_button.setCursor(QCursor(Qt.PointingHandCursor))
        import_button.setFixedSize(83, 40)
        import_button.setStyleSheet("""
                                    QPushButton {
                                        border-radius: 8px;
                                        background: black;
                                        color: white;
                                        border: none;
                                        border-radius: 8px;
                                        font-weight: bold;
                                        font-size: 11pt;
                                        
                                    }
                                    QPushButton:hover {
                                        background-color: #333;
                                    }""")

        # Create the dropdown menu
        import_menu = QMenu()
        import_menu_action =import_menu.addAction("Import CSV")
        import_pdf_button = import_menu.addAction("Import PDF")
        import_menu_action.triggered.connect(lambda: self.import_data(True))
        import_pdf_button.triggered.connect(lambda: self.import_data(False))
        import_menu.setStyleSheet("""
                            QMenu {
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                padding: 5px;
                                color: black;
                            }
                            QMenu::item {
                                padding: 8px 20px;
                                border-radius: 5px;
                            }
                            QMenu::item:selected {
                                background-color: #0078d7;
                                color: white;
                            }""")

        import_button.clicked.connect(lambda: import_menu.exec_(import_button.mapToGlobal(import_button.rect().bottomLeft())))


        # Adding everything to the header_layout
        header_layout.addWidget(logo_label)
        header_layout.addWidget(menu_button)
        header_layout.addWidget(import_button)


#=======================================================================================================================
        # panel 2 with view change buttons and search bar

        view_change_layout = QHBoxLayout()
        view_change_layout.setAlignment(Qt.AlignLeft)

        self.dashboard_view_button = QPushButton("Dashboard")
        self.dashboard_view_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_view_button.setFixedSize(84,24)
        self.dashboard_view_button.setStyleSheet("""
                                QPushButton {
                                        border-radius: 12px;
                                        background: black;
                                        color: white;
                                        border: none;
                                        font-weight: bold;
                                        font-size: 11pt;
                                        
                                    }
                                    QPushButton:hover {
                                        background-color: #333;
                                    }
        
                            """)

        self.dashboard_view_button.clicked.connect(self.switch_panel)



        self.transaction_view_button = QPushButton("Transaction")
        self.transaction_view_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.transaction_view_button.setFixedSize(84, 24)
        self.transaction_view_button.setStyleSheet("""
                                       QPushButton {
                                               border-radius: 12px;
                                               background: #EEE;
                                               color: black;
                                               border: none;
                                               font-weight: bold;
                                               font-size: 11pt;

                                           }
                                           QPushButton:hover {
                                               background-color: #333;
                                           }

                                   """)

        self.transaction_view_button.clicked.connect(self.switch_panel)



        # Search Bar
        self.search_transaction = QLineEdit(self)
        self.search_transaction.setPlaceholderText("Search Transaction")
        self.search_transaction.setFixedSize(250, 40)
        self.search_transaction.setStyleSheet("""
                           QLineEdit {
                               border: 1px solid #ccc;
                               border-radius: 8px;
                               padding: 8px;
                               font-size: 12pt;
                               color: black;
                           }
                       """)

        # Add icon using QAction
        search_icon = QIcon("assets/search.png")
        search_action = QAction(search_icon, "", self)  # fixed: include empty string for text
        self.search_transaction.addAction(search_action, QLineEdit.LeadingPosition)
        self.search_transaction.textChanged.connect(self.filter_table)



        # Adding all the widgets to the  view_change_layout(Panel 2)
        view_change_layout.addWidget(self.dashboard_view_button)
        view_change_layout.addWidget(self.transaction_view_button)
        view_change_layout.addStretch()
        view_change_layout.addWidget(self.search_transaction)


# =======================================================================================================================
        # Panel three: display balance, money spent, etc
        money_tracking_layout = QHBoxLayout()

        # Floating Box Wrapper ---
        current_balance_widget = QWidget()
        current_balance_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                padding: 16px;
            }
        """)

        # Adds subtle drop shadow for floating effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 80))
        current_balance_widget.setGraphicsEffect(shadow)

        # Inner Layout
        current_balance_layout = QVBoxLayout()

        current_balance_heading_label = QLabel("Current Balance")
        current_balance_heading_label.setAlignment(Qt.AlignLeft)
        current_balance_heading_label.setStyleSheet("""
            color: #000;
            font-family: Inter;
            font-size: 16px;
            font-style: normal;
            font-weight: 600;
        """)

        self.has_imported_once = False
        # Turn off dev
        import_data.import_file(dev=False)  # Load the sample.csv when the app starts

        self.current_balance_label = QLabel(f"$ {dashboard_controller.current_balance(): 0.2f}")
        self.current_balance_label.setAlignment(Qt.AlignLeft)
        self.current_balance_label.setStyleSheet("""
            color: #000;
            font-family: Inter;
            font-size: 40px;
            font-style: normal;
            font-weight: 600;
            letter-spacing: -0.8px;
        """)

        self.current_balance_desc_label = QLabel(dashboard_controller.balance_compared_last_month())
        self.current_balance_desc_label.setAlignment(Qt.AlignLeft)
        self.current_balance_desc_label.setStyleSheet("""
            color: #666;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 400;
     
        """)

        # Adding all the widgets to the inner layout
        current_balance_layout.addWidget(current_balance_heading_label)
        current_balance_layout.addWidget(self.current_balance_label)
        current_balance_layout.addWidget(self.current_balance_desc_label)

        # Apply the layout to the floating widget
        current_balance_widget.setLayout(current_balance_layout)

        money_tracking_layout.addWidget(current_balance_widget)
        money_tracking_layout.setSpacing(20)

    #===========================================================================
        # Second box - monthly spending info
        # --- Floating Box Wrapper ---
        monthly_spending_widget = QWidget()
        monthly_spending_widget.setStyleSheet("""
                   QWidget {
                       background-color: #ffffff;
                       padding: 16px;
                   }
               """)

        # Adds subtle drop shadow for floating effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 80))
        monthly_spending_widget.setGraphicsEffect(shadow)

        # Inner Layout
        monthly_spending_layout = QVBoxLayout()

        metadata = dashboard_controller.get_monthly_total_by_type("debit")

        self.monthly_spending_heading_label = QLabel(f"Money Spent in {metadata[0].title()}")
        self.monthly_spending_heading_label.setAlignment(Qt.AlignLeft)
        self.monthly_spending_heading_label.setStyleSheet("""
                   color: #000;
                   font-family: Inter;
                   font-size: 16px;
                   font-style: normal;
                   font-weight: 600;
               """)

        self.monthly_spending_label = QLabel(f"$ {metadata[1]: 0.2f}")
        self.monthly_spending_label.setAlignment(Qt.AlignLeft)
        self.monthly_spending_label.setStyleSheet("""
                   color: #000;
                   font-family: Inter;
                   font-size: 40px;
                   font-style: normal;
                   font-weight: 600;
                   letter-spacing: -0.8px;
               """)

        self.monthly_spending_desc_label = QLabel(dashboard_controller.money_spent_compared_last_month())
        self.monthly_spending_desc_label.setAlignment(Qt.AlignLeft)
        self.monthly_spending_desc_label.setStyleSheet("""
                   color: #666;
                   font-family: Inter;
                   font-size: 14px;
                   font-style: normal;
                   font-weight: 400;

               """)
        # Adding all the widgets to the inner layout
        monthly_spending_layout.addWidget(self.monthly_spending_heading_label)
        monthly_spending_layout.addWidget(self.monthly_spending_label)
        monthly_spending_layout.addWidget(self.monthly_spending_desc_label)

        # Apply the layout to the floating widget
        monthly_spending_widget.setLayout(monthly_spending_layout)

        # Adding the spending box into money_tracking layout
        money_tracking_layout.addWidget(monthly_spending_widget)
        money_tracking_layout.setSpacing(20)


#=============================================
        # Floating Box Wrapper
        income_widget = QWidget()
        income_widget.setStyleSheet("""
                           QWidget {
                               background-color: #ffffff;
                               padding: 16px;
                           }
                       """)

        # Adds subtle drop shadow for floating effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 80))
        income_widget.setGraphicsEffect(shadow)


        # Inner Layout
        monthly_income_layout = QVBoxLayout()

        income_heading_label = QLabel("Income Current Month")
        income_heading_label.setAlignment(Qt.AlignLeft)
        income_heading_label.setStyleSheet("""
                           color: #000;
                           font-family: Inter;
                           font-size: 16px;
                           font-style: normal;
                           font-weight: 600;
                       """)

        income_data = dashboard_controller.get_monthly_total_by_type("credit")
        self.income_label = QLabel(f"$ {income_data[1]: 0.2f}")
        self.income_label.setAlignment(Qt.AlignLeft)
        self.income_label.setStyleSheet("""
                           color: #000;
                           font-family: Inter;
                           font-size: 40px;
                           font-style: normal;
                           font-weight: 600;
                           letter-spacing: -0.8px;
                       """)

        self.income_desc_label = QLabel(dashboard_controller.money_made_compared_last_month())
        self.income_desc_label.setAlignment(Qt.AlignLeft)
        self.income_desc_label.setStyleSheet("""
                           color: #666;
                           font-family: Inter;
                           font-size: 14px;
                           font-style: normal;
                           font-weight: 400;

                       """)

        # Adding all the widgets to the inner layout
        monthly_income_layout.addWidget(income_heading_label)
        monthly_income_layout.addWidget(self.income_label)
        monthly_income_layout.addWidget(self.income_desc_label)

        # Apply the layout to the floating widget
        income_widget.setLayout(monthly_income_layout)

        # Adding the income box into money_tracking layout
        money_tracking_layout.addWidget(income_widget)

#=======================================================================================================================
        # Panel 4
        # Subtitle box for Data Visualization
        subtitle = QLabel("Historical Data Visualization ")
        subtitle.setAlignment(Qt.AlignLeft)
        subtitle.setStyleSheet("""
        color: #000;
        /* Small text */
        font-family: Inter;
        font-size: 16px;
        font-style: normal;
        font-weight: 500;
        line-height: 150%; /* 24px */
        """)

        # Stack container
        self.stack = QStackedWidget(self)

        # =================================================================
        # Dashboard View
        self.dashboard_layout = QVBoxLayout()
        dashboard_subtitle = QLabel("Main View")
        dashboard_subtitle.setAlignment(Qt.AlignLeft)
        dashboard_subtitle.setStyleSheet("""
            color: #000;
            font-family: Inter;
            font-size: 16px;
            font-style: normal;
            font-weight: 500;
            line-height: 150%;
        """)
        self.dashboard_layout.addWidget(subtitle)

        # Generate histogram for total income by week
        self.dashboard_layout.addWidget(visualization.histogram_income_by_week())
        # Generate histogram for total expenses by week
        self.dashboard_layout.addWidget(visualization.histogram_expenses_by_week())



        self.dashboard_layout.addWidget(dashboard_subtitle)


        dashboard_widget = QWidget()
        dashboard_widget.setLayout(self.dashboard_layout)

        # ======================================================================
        # Transaction View
        self.transaction_layout = QVBoxLayout()
        transaction_subtitle = QLabel("Account Records")
        transaction_subtitle.setAlignment(Qt.AlignLeft)
        transaction_subtitle.setStyleSheet("""
            color: #000;
            font-family: Inter;
            font-size: 16px;
            font-style: normal;
            font-weight: 500;
            line-height: 150%;
        """)

        self.transaction_layout.addWidget(transaction_subtitle)
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)

        self.transaction_layout.addWidget(self.table)

        transaction_widget = QWidget()
        transaction_widget.setLayout(self.transaction_layout)

        # ===============================================================
        # Add views to stack
        self.stack.addWidget(dashboard_widget)
        self.stack.addWidget(transaction_widget)

#=======================================================================================================================
        main_layout.addLayout(header_layout)
        main_layout.addWidget(line)
        main_layout.addLayout(view_change_layout)
        main_layout.addLayout(money_tracking_layout)
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

# =======================================================================================================================
# Method Logic

    def switch_panel(self):
        # Switch colors of dashboard and transaction button
        temp_transaction_style = self.transaction_view_button.styleSheet()
        self.transaction_view_button.setStyleSheet(self.dashboard_view_button.styleSheet())
        self.dashboard_view_button.setStyleSheet(temp_transaction_style)

        current_index = self.stack.currentIndex()
        next_index = 1 if current_index == 0 else 0
        data = import_data.get_all_records_view()
        self.original_df = data

        self.show_table(data)
        self.stack.setCurrentIndex(next_index)

    # Review This
    def show_table(self, df):
        self.table.clear()
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        columns = ["Date", "Description", "Category", "Credit", "Debit","Balance"]

        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)
        self.table.setHorizontalHeaderLabels(columns)

        self.table.resizeColumnsToContents()
        self.table.setStyleSheet("""
            QTableWidget {
                color: black;
            }
            QHeaderView::section {
                color: black;
                background-color: white;
            }
        """)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iat[i, j]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)

    # Review this
    def filter_table(self, text):
        if not hasattr(self, 'original_df'):
            return

        df = self.original_df
        if text:
            df = df[df.apply(lambda row: row.astype(str).str.contains(text, case=False).any(), axis=1)]
        self.show_table(df)


    def refresh_dashboard(self):
        self.current_balance_label.setText(f"$ {dashboard_controller.current_balance(): 0.2f}")
        self.current_balance_desc_label.setText(dashboard_controller.balance_compared_last_month())

        metadata = dashboard_controller.get_monthly_total_by_type("debit")
        self.monthly_spending_label.setText(f"$ {metadata[1]: 0.2f}")
        self.monthly_spending_desc_label.setText(dashboard_controller.money_spent_compared_last_month())

        income_data = dashboard_controller.get_monthly_total_by_type("credit")
        self.income_label.setText(f"$ {income_data[1]: 0.2f}")
        self.income_desc_label.setText(dashboard_controller.money_made_compared_last_month())


    def import_data(self, isCSV = True ):
        loading = ui_controller.show_loading_message()
        QApplication.processEvents()
        # Clear DB only on first import
        clear_existing = not self.has_imported_once
        if isCSV:
            import_data.import_file(clear_existing=clear_existing)
        else:
            import_data.import_bank_statement(clear_existing=clear_existing)
        self.has_imported_once = True
        loading.close()

        # Refresh table
        data = import_data.get_all_records_view()
        self.original_df = data
        self.show_table(data)
        self.refresh_dashboard()

    def clean_all(self):
        from dao.bankrecords_dao import BankRecordsDAO
        from dao.balance_dao import BalanceDAO
        from dao.expense_dao import ExpenseDAO
        from dao.income_dao import IncomeDAO
        from dao.category_dao import CategoryDAO

        BankRecordsDAO().delete_all()
        BalanceDAO().delete_all()
        ExpenseDAO().delete_all()
        IncomeDAO().delete_all()
        CategoryDAO().delete_all()

    def profile_window(self):
        from View.profile_view import ProfileWindow
        self.profile_window = ProfileWindow(email=self.email)
        self.profile_window.show()
        self.close()

    def log_out(self):
        from login_view import LoginWindow
        self.create_window = LoginWindow()
        self.create_window.show()
        self.close()


# Run the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    #window.showFullScreen()
    window.show()
    sys.exit(app.exec_())
