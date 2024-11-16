import os
import re
import openpyxl
from datetime import datetime

def normalize_sql(sql):
    sql = re.sub(r'\s+', ' ', sql).strip()
    return sql.lower()

def remove_sql_comments(sql):
    sql = re.sub(r'--.*', '', sql)
    sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
    return sql.lower()

# Function to read the contents of a stored procedure file
def read_sp_file(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return remove_sql_comments(file.read())
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try a fallback encoding
            with open(file_path, 'r', encoding='ISO-8859-1') as file:
                return remove_sql_comments(file.read())
    return None

def compare_stored_procedures(sp1_content, sp2_content):
    return normalize_sql(sp1_content) == normalize_sql(sp2_content)

def create_excel_report(data, output_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    headers = ['SP NAME', 'Folder1', 'Folder2', 'Is Different', 'Developer Name', 'Date Time']
    sheet.append(headers)

    # Append data rows
    for row in data:
        sheet.append(row)

    if not output_file.endswith('.xlsx'):
        output_file += '.xlsx'

    workbook.save(output_file)
    print(f"Excel report saved as {output_file}")

def compare_sps_in_folders(folder1, folder2, output_excel_file, developer_name):
    sp_files_folder1 = set(f for f in os.listdir(folder1) if f.endswith('.sql'))
    sp_files_folder2 = set(f for f in os.listdir(folder2) if f.endswith('.sql'))

    all_sp_files = sp_files_folder1.union(sp_files_folder2)

    # Store the result data
    result_data = []

    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Iterate through all SP files
    for sp_file in all_sp_files:
        sp1_path = os.path.join(folder1, sp_file)
        sp2_path = os.path.join(folder2, sp_file)

        sp1_exists = sp_file in sp_files_folder1
        sp2_exists = sp_file in sp_files_folder2

        sp1_content = read_sp_file(sp1_path) if sp1_exists else None
        sp2_content = read_sp_file(sp2_path) if sp2_exists else None

        # Determine comparison result using normalized contents
        if sp1_exists and sp2_exists:
            if sp1_content and sp2_content:
                is_different = 'Yes' if not compare_stored_procedures(sp1_content, sp2_content) else 'No'
            else:
                is_different = 'Yes'  # One of the SP contents couldn't be read, so treat it as different
        else:
            is_different = 'NA'

        # Append the row for this SP with additional columns
        result_data.append([
            sp_file,  # SP Name
            'Yes' if sp1_exists else 'NA',  # Folder1
            'Yes' if sp2_exists else 'NA',  # Folder2
            is_different,  # Is Different
            developer_name,  # Developer Name
            current_datetime  # Date Time
        ])

    create_excel_report(result_data, output_excel_file)

folder1 = r'A:\Python\t1'
folder2 = r'A:\Python\t2'
output_excel_file = r'A:\testing'
developer_name = "Anuj Gupta"

compare_sps_in_folders(folder1, folder2, output_excel_file, developer_name)
