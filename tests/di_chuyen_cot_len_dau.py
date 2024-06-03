# import pandas as pd
#
# # Giả sử đây là DataFrame ban đầu
# data = {
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'abc': ['A', 'B', 'C']
# }
# df = pd.DataFrame(data)
#
# # Hiển thị DataFrame ban đầu
# print("DataFrame ban đầu:")
# print(df)
#
# # Đặt cột 'abc' vào vị trí thứ 3
# position = 1  # Vị trí thứ 3 (0-indexed)
# columns = [col for col in df.columns if col != 'abc']
# columns.insert(position, 'abc')
# df = df[columns]
#
# # Hiển thị DataFrame sau khi di chuyển cột 'abc' lên vị trí thứ 3
# print("\nDataFrame sau khi di chuyển cột 'abc' lên vị trí thứ 3:")
# print(df)
import pandas as pd

# Tạo DataFrame ví dụ
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'xxx': ['X', 'Y', 'Z'],
    'gender': ['F', 'M', 'M']
}
df = pd.DataFrame(data)

# Hiển thị DataFrame ban đầu
print("DataFrame ban đầu:")
print(df)

# Đặt cột 'xxx' vào vị trí thứ 2
position = 1  # Vị trí thứ 2 (0-indexed)
columns = [col for col in df.columns if col != 'xxx']
columns.insert(position, 'xxx')
df = df[columns]

# Hiển thị DataFrame sau khi di chuyển cột 'xxx' lên vị trí thứ 2
print("\nDataFrame sau khi di chuyển cột 'xxx' lên vị trí thứ 2:")
print(df)
