# Danh sách A và B
A = [
    ('UNKNOW_device_group', 'UNKNOW_device', 'XQA商品性', 'CCM'),
    ('UNKNOW_device_group', 'UNKNOW_device', None, 'ZONE'),
    ('UNKNOW_device_group', 'UNKNOW_device', None, 'BODY')
]

B = [
    ('UNKNOW_device_group', 'UNKNOW_device', 'XX4PT', 'ENGINE'),
    ('UNKNOW_device_group', 'UNKNOW_device', 'XQA商品性', 'CCM'),
    ('UNKNOW_device_group', 'UNKNOW_device', None, 'ZONE'),
    ('UNKNOW_device_group', 'UNKNOW_device', None, 'AXLE'),
    ('UNKNOW_device_group', 'UNKNOW_device', None, 'BODY')
]

set_A = set(A)

only_in_B = [item for item in B if item not in set_A]

print(only_in_B)
