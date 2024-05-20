from openpyxl import load_workbook


def get_merged_ranges(column, file_path_):
    workbook = load_workbook(file_path_)
    worksheet = workbook.active
    merged_ranges_in_column_a = [merged_cell_range for merged_cell_range in worksheet.merged_cells.ranges
                                 if merged_cell_range.min_col == column]
    return merged_ranges_in_column_a


file_path = r'../../data/raw/input.xlsx'
merged_ranges_in_column_A = get_merged_ranges(1, file_path)
print("merged_ranges_in_column_A: ", merged_ranges_in_column_A)
