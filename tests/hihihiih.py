import pandas as pd

# Ví dụ DataFrame
data = {
    'CADICS ID': [' 123 ', '456', ' 789', '123 ', ' 456', '000', '789', '123']
}
df = pd.DataFrame(data)

# Xóa khoảng trắng ở đầu và cuối của cột 'CADICS ID'
df['CADICS ID'] = df['CADICS ID'].str.strip()

# Tạo danh sách các phần tử trùng lặp
duplicated_elements = df[df.duplicated('CADICS ID', keep=False)]['CADICS ID'].unique().tolist()

# Hiển thị DataFrame sau khi xóa khoảng trắng
print("DataFrame sau khi xóa khoảng trắng:")
print(df)

# Hiển thị danh sách các phần tử trùng lặp
print("\nDanh sách các phần tử trùng lặp:")
print(duplicated_elements)
