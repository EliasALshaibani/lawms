# Copyright (c) 2024, elias Alshaibani and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    # ????? ??????? ???? ????? ?? ???????
    columns = [
        {"fieldname": "case_id", "label": "Case ID", "fieldtype": "Data", "width": 70},
        {"fieldname": "case_name", "label": "Case Name", "fieldtype": "Data", "width": 70},
        {"fieldname": "case_status", "label": "Case Status", "fieldtype": "Select", "width": 70},
        {"fieldname": "case_subject", "label": "Case Subject", "fieldtype": "Data", "width": 70},
    ]
    
    session_columns = [
        {"fieldname": "num_session", "label": "Num Session", "fieldtype": "Data", "width": 70},
        {"fieldname": "gregorian_date", "label": "Session Date", "fieldtype": "Date", "width": 70},
        {"fieldname": "session_content", "label": "Session Content", "fieldtype": "Data", "width": 70},
    ]
    
    transaction_columns = [
        {"fieldname": "num_transaction", "label": "Num Transaction", "fieldtype": "Data", "width": 70},
        {"fieldname": "transaction_date", "label": "Transaction Date", "fieldtype": "Date", "width": 70},
        {"fieldname": "transaction_decision", "label": "Transaction Decision", "fieldtype": "Data", "width": 70},
    ]
    
    data = []

    # ????? ??????? ?????????? ?? ???????????
    case_filter = {
        "case_status": filters.get("case_status"),
        "client": filters.get("client"),
        
    }

    # ??? ?????? ??????? ????? ??? ??????? (?? ???? ?????? ??????? ???????? session_date)
    cases = frappe.get_all("Casee", filters=case_filter, fields=["name", "case_id", "case_name", "case_status", "case_subject", "client"])

    for case in cases:
        # ????? ?????? ??????
        case_data = {
            "case_id": case.name,
            "case_name": case.case_name,
            "case_status": case.case_status,
            "case_subject": case.case_subject,
        }
        data.append(case_data)

        # 1. ??? ??????? ???????? ??????? ?????? ??????? ???????? session_date
        sessions_filter = {"case_subject": case.name}

        # ????? ??????? ???????? ??????? ???????
        #if filters.get("session_date_from"):
           # sessions_filter["gregorian_date"] = [">=", filters.get("session_date_from")]

       # if filters.get("session_date_to"):
           # if "gregorian_date" not in sessions_filter:
            #    sessions_filter["gregorian_date"] = []
            #sessions_filter["gregorian_date"].append(["<=", filters.get("session_date_to")])

        sessions = frappe.get_all(
            "Sessionss", 
            filters={"case_subject": case.name}, 
            fields=["num_session", "gregorian_date", "session_content"]
        )

        if sessions:
            session_header = {"case_id": "Sessions for " + case.case_name}
            data.append(session_header)
            for session in sessions:
                data.append({
                    "num_session": session.get("num_session"),
                    "gregorian_date": session.get("gregorian_date"),
                    "session_content": session.get("session_content"),
                })
        else:
            data.append({"case_id": "No sessions available"})

        # 2. ??? ????????? ???????? ???????
        transactions = frappe.get_all(
            "Transactions", 
            filters={"case_subject": case.name}, 
            fields=["num_transaction", "transaction_date", "transaction_decision"]
        )

        if transactions:
            transaction_header = {"case_id": "Transactions for " + case.case_name}
            data.append(transaction_header)
            for transaction in transactions:
                data.append({
                    "num_transaction": transaction.get("num_transaction"),
                    "transaction_date": transaction.get("transaction_date"),
                    "transaction_decision": transaction.get("transaction_decision"),
                })
        else:
            data.append({"case_id": "No transactions available"})

    # ????? ??????? ????????? ?????? ???????
    return columns + session_columns + transaction_columns, data





