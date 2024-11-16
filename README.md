# SQL Stored Procedure Comparator

A Python tool to compare SQL stored procedures across two folders and generate a detailed Excel report. This script identifies differences between stored procedures, normalizes SQL content for comparison, and highlights discrepancies for further analysis.

## Features

- **Folder Comparison**: 
  - Compares stored procedures (`.sql` files) in two directories.
  - Identifies whether a stored procedure exists in one folder, both folders, or is missing.
- **Normalization**:
  - Ignores comments and formatting differences while comparing SQL files.
- **Excel Report**:
  - Generates an Excel file with details such as:
    - Stored procedure name.
    - Existence in Folder 1 and Folder 2.
    - Whether the files are identical or different.
    - Developer name and timestamp.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/use_git_url.git
   cd sql-sp-comparator
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required library:
   ```bash
   pip install openpyxl
   ```

3. **Run the Script**:
   Edit the `folder1`, `folder2`, and `output_excel_file` variables in the script to match your directory structure and desired output location. Then execute the script:
   ```bash
   python compare_sps.py
   ```

## Usage

1. Place the stored procedure files in two separate folders (e.g., `folder1` and `folder2`).
2. Update the following variables in the script:
   - `folder1`: Path to the first folder.
   - `folder2`: Path to the second folder.
   - `output_excel_file`: Path to save the generated Excel report.
   - `developer_name`: Your name for tracking changes in the report.
3. Run the script to generate the comparison report.

### Example

```python
folder1 = r'C:\Projects\Folder1'
folder2 = r'C:\Projects\Folder2'
output_excel_file = r'C:\Projects\SP_Comparison_Report.xlsx'
developer_name = "Anuj Gupta"
```

### Generated Report

The script produces an Excel file with the following columns:

| SP NAME       | Folder1 | Folder2 | Is Different | Developer Name | Date Time           |
|---------------|---------|---------|--------------|----------------|---------------------|
| example.sql   | Yes     | Yes     | No           | Anuj Gupta     | 2024-11-16 14:30:00 |
| missing1.sql  | Yes     | NA      | NA           | Anuj Gupta     | 2024-11-16 14:30:00 |
| different.sql | Yes     | Yes     | Yes          | Anuj Gupta     | 2024-11-16 14:30:00 |

## How It Works

1. **File Reading**:
   - Reads `.sql` files from both folders.
   - Removes comments and normalizes SQL to ensure accurate comparisons.
2. **Comparison**:
   - Checks if a file exists in both folders.
   - Compares the normalized SQL content for equality.
3. **Excel Report Generation**:
   - Writes a summary of findings to an Excel file with headers and details.

## Requirements

- **Python**: Version 3.6 or higher.
- **Libraries**:
  - `openpyxl`: For Excel file generation.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with a clear explanation of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements

- `openpyxl` for Excel file creation.
- Python's `re` module for SQL normalization.
- Developers and testers for feedback on refining the tool.
