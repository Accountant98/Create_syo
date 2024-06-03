import pandas as pd

data = [('WZ1J', 'conf-001', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', ' LANE DEPARTURE PREVENTION (LDP)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', ' POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4PSD', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-002', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', '2nd row armrest', 'w', 'null', 'XD2材料', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', '2ND ROW HEATED SEAT', 'w,w/o', 'null', 'XX4SC', '2ND ROW SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-001', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
                   'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT BELT REMINDER OCS', 'w.w/o', 'null', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-002', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-003', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-004', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-005', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-006', '2ND ROW SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-001', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
         'w/o'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-001', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', '2ND ROW SEAT', 'X03_SEAT',
            'S'), (
            'WZ1J', 'conf-001', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'), (
            'WZ1J', 'conf-002', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'), (
            'WZ1J', 'conf-003', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'), (
            'WZ1J', 'conf-004', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'), (
            'WZ1J', 'conf-005', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'), (
            'WZ1J', 'conf-006', '2ND ROW SEAT TYPE AND ADJUSTMENT.', 'BENCH,SPRIT', 'null', 'XR6シートベルト', '2ND ROW SEAT',
            'X03_SEAT', 'BENCH'),
        ('WZ1J', 'conf-001', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', '2nd Seat\n3rd Seat', 'w/o', 'null', 'XQ2乗心地性能', 'DRIVER SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-002', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-003', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-004', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-005', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-006', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'S'), (
            'WZ1J', 'conf-001', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-002', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-003', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-004', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-005', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-006', '3RD ROW SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-001', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-002', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-003', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-004', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-005', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-006', '3RD ROW SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), ('WZ1J', 'conf-001', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
                   'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', '3RD ROW SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        (
            'WZ1J', 'conf-002', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        (
            'WZ1J', 'conf-003', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        (
            'WZ1J', 'conf-004', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        (
            'WZ1J', 'conf-005', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        (
            'WZ1J', 'conf-006', '3rd Seat', 'w,w/o', 'null', 'XR3シート,XQ2乗心地性能,XL4シート', 'DRIVER SEAT', 'X03_SEAT',
            '-'),
        ('WZ1J', 'conf-001', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-002', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-003', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-004', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-005', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-006', 'AC 120V or 240V 1500W OUTLET', 'Ｗ', 'null', 'XX4WH', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-001', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-002', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-003', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-004', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-005', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-006', 'AC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-001', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'AC INV\n(V2L_inside)', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-002', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-003', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-004', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-005', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-006', 'AC PLUG STANDARD',
            'MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE ',
            'null', 'XX4EMC,XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-001', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'AC-INV', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'Accel Pedal KD(キックダウン)', 'null', 'null', 'XR2コントロール', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-003', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-004', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-006', 'ACTIVE SOUND CONTROL', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-001', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1 NEXT'),
        ('WZ1J', 'conf-002', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
         'AD1 NEXT WITH NAVI-LINK +'),
        ('WZ1J', 'conf-003', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD2'),
        ('WZ1J', 'conf-004', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1 NEXT'),
        ('WZ1J', 'conf-005', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
         'AD1 NEXT WITH NAVI-LINK +'), (
            'WZ1J', 'conf-006', 'AD', 'w', 'null', 'XR6視界,XP4EVシステム', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1 NEXT WITH NAVI-LINK +'), (
            'WZ1J', 'conf-001', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1'), (
            'WZ1J', 'conf-002', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1'), (
            'WZ1J', 'conf-003', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD2'), (
            'WZ1J', 'conf-004', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1'), (
            'WZ1J', 'conf-005', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1'), (
            'WZ1J', 'conf-006', 'AD(AUTONOMOUS DRIVING)', 'ALL', 'null', 'XX4WH', 'ADAS COMFORT', 'X11_SAFETY_SECURITY',
            'AD1'),
        ('WZ1J', 'conf-001', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-004', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'AD1', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-001', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'AD2', 'w,w/o', 'null', 'XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'ADAPTIVE CRUISE CONTROL (ACC)', 'ALL,w', 'null', 'XX4EMC,XX4WH', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', 'ADAPTIVE DRIVING BEAM (ADB)', 'w,w/o', 'null', 'XR6視界,XX4LEDHead', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-002', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-003', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-004', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-005', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-006', 'ADAPTIVE FRONT LIGHTING SYSTE(AFS)', 'w', 'null', 'XX4AFS', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), ('WZ1J', 'conf-001', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
                   'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'ADB(ADAPTIVE DRIVING BEAM)', 'ｗ,w/o', 'null', 'XX4HBA,XX4ADB', 'LIGHTING',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-001', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'ADDITIONAL HEATER FOR PASSENGERS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'ADDITIONAL REAR AIR CONDITIONING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'ADJUSTMENT OF HEADLIGHTS ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-002', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-003', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-004', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-005', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-006', 'AFS', 'null', 'アダプティブフロントライティングシステム', 'XR6視界', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-001', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-002', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-003', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-004', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-005', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-006', 'AIR CONDITIONER', 'AUTO A/C,ALL', 'null', 'XR5空調,XX4SC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'AUTO A/C'), (
            'WZ1J', 'conf-001', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-002', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-003', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-004', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-005', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-006', 'AIR CONDITIONING AND HEATING SYSTEM', 'ALL', 'null', 'XX4EMC,XQE電動車',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-001', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-002', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-003', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-004', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-005', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-006', 'AIR CONDITIONING AND HEATING TYPE', 'ALL', 'null', 'XX4NH電動車,XX4EMC,XX4WH',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-001', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-002', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-003', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-004', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-005', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-006', 'AIR CONTIONING AND HEATIN', 'ALL', 'null', 'XX4EMC', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-001', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), (
            'WZ1J', 'conf-002', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), (
            'WZ1J', 'conf-003', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), (
            'WZ1J', 'conf-004', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), (
            'WZ1J', 'conf-005', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), (
            'WZ1J', 'conf-006', 'AIR TREATMENT', 'ALL', 'null', 'XX4EMC', 'AIR QUALITY MANAGEMENT',
            'X06_AIR_CONDITIONER',
            'S'), ('WZ1J', 'conf-001', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'AIRBAG CANCEL', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'), (
            'WZ1J', 'conf-002', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'), (
            'WZ1J', 'conf-003', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'), (
            'WZ1J', 'conf-004', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'), (
            'WZ1J', 'conf-005', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'), (
            'WZ1J', 'conf-006', 'Alarm type', 'Perimeric,Volmatric', 'null', 'XX4BCM', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'Perimeric'),
        ('WZ1J', 'conf-001', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'ALS(Auto Light Sensor)', 'w,w/o', 'null', 'XX4レインセンサ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49', 'AMBIENT LIGHTING',
         'X04_INTERIOR_TRIM_&_STORAGE', 'Mono color ambient'), (
            'WZ1J', 'conf-002', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49',
            'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'Multi color'), (
            'WZ1J', 'conf-003', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49',
            'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'Multi color'), (
            'WZ1J', 'conf-004', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49',
            'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'Mono color ambient'), (
            'WZ1J', 'conf-005', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49',
            'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'Multi color'), (
            'WZ1J', 'conf-006', 'Ambient light', 'Mono color ambient,Multi color', 'null', 'XX4ESS49',
            'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'Multi color'), (
            'WZ1J', 'conf-001', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'モノかラー'), (
            'WZ1J', 'conf-002', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'マルチカラー'), (
            'WZ1J', 'conf-003', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'マルチカラー'), (
            'WZ1J', 'conf-004', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'モノかラー'), (
            'WZ1J', 'conf-005', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'マルチカラー'), (
            'WZ1J', 'conf-006', 'Ambient lighting', 'マルチカラー,モノかラー', 'null', 'XX4BCM', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'マルチカラー'),
        ('WZ1J', 'conf-001', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-002', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-003', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-004', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-005', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-006', 'ANC', 'ALL', 'null', 'XQ4実車', 'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-001', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-003', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-004', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-006', 'ANC (ACTIVE NOISE CANCELLATION)', 'ALL', 'null', 'XX4EMC', 'NVH MANAGEMENT',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-001', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-003', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-004', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-006', 'ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL', 'ALL', 'null', 'XM6音質',
            'NVH MANAGEMENT', 'X07_AUDIO_NAVIGATION_CCS', 'S'), ('WZ1J', 'conf-001', 'ANTENNA',
                                                                 '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
                                                                 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
                                                                 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'), (
            'WZ1J', 'conf-002', 'ANTENNA',
            '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
            'null', 'XM6アンテナ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'), (
            'WZ1J', 'conf-003', 'ANTENNA',
            '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
            'null', 'XM6アンテナ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'), (
            'WZ1J', 'conf-004', 'ANTENNA',
            '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
            'null', 'XM6アンテナ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'), (
            'WZ1J', 'conf-005', 'ANTENNA',
            '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
            'null', 'XM6アンテナ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'), (
            'WZ1J', 'conf-006', 'ANTENNA',
            '200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',
            'null', 'XM6アンテナ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'SHARK FIN'),
        ('WZ1J', 'conf-001', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-002', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-003', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-004', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-005', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-006', 'ANTI-LOCK BRAKING SYSTEM', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'), (
            'WZ1J', 'conf-001', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'ANTI-THEFT DEVICES', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'D'), (
            'WZ1J', 'conf-004', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'AROUND VIEW MONITOR\n（AVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'D'), (
            'WZ1J', 'conf-004', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'AROUND VIEW MONITOR', 'ALL,w', 'null', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera',
            'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'AS HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-004', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'AS SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-001', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'AS SEAT HEATER ', 'w,w/o', 'null', 'XR6乗員判別', 'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-003', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-006', 'AS SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-001', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-002', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-003', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-006', 'AS SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'), (
            'WZ1J', 'conf-001', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-002', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-003', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-004', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-005', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-006', 'AS SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-001', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'ASCD', 'w', 'オートスピードコントロール', 'UE2動力運転性,XP4EVシステム', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'ASL', 'w', 'null', 'UE2動力運転性,XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'ASSISTANT SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'ATシフトデバイス', 'null', 'アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）', 'XR2コントロール',
            'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-002', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-003', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-004', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-005', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-006', 'AUDIO', 'IVI,DA,レス', 'null', 'XM6音質,XX4AD', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'IVI'), (
            'WZ1J', 'conf-001', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-002', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-003', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-004', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-005', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-006', 'AUDIO & NAVIGATION', 'ALL', 'null', 'XX4WH', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-001', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-002', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-003', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-004', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-005', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-006', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'ALL', 'null', 'XM6アンテナ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-001', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-002', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-003', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-004', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-005', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-006', 'AUDIO LESS', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), ('WZ1J', 'conf-001', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
                   'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-002', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-003', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-004', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-005', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-006', 'Audio Navigation', 'GAS NAVI,DA', 'null', 'XX4SV', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), ('WZ1J', 'conf-001', 'AUDIO SYSTEM',
                                                      'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
                                                      'null', 'XX4HF-VR-ETC', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS',
                                                      'non-BOSE'), ('WZ1J', 'conf-002', 'AUDIO SYSTEM',
                                                                    'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
                                                                    'null', 'XX4HF-VR-ETC', 'SPEAKERS',
                                                                    'X07_AUDIO_NAVIGATION_CCS', 'non-BOSE'), (
            'WZ1J', 'conf-003', 'AUDIO SYSTEM',
            'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
            'null', 'XX4HF-VR-ETC', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'BOSE'),
        ('WZ1J', 'conf-004', 'AUDIO SYSTEM',
         'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
         'null', 'XX4HF-VR-ETC', 'SPEAKERS',
         'X07_AUDIO_NAVIGATION_CCS',
         'non-BOSE'), (
            'WZ1J', 'conf-005', 'AUDIO SYSTEM',
            'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
            'null', 'XX4HF-VR-ETC', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'non-BOSE'), (
            'WZ1J', 'conf-006', 'AUDIO SYSTEM',
            'BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',
            'null', 'XX4HF-VR-ETC', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'BOSE'),
        ('WZ1J', 'conf-001', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'AUDIO VISUAL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'AUTO CLOSER', 'ｗ', 'null', 'XX4バックドアクロージャ―', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'AUTO COMPASS', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'AUTO EXTENTION LIGHT ', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'AUTO HAZARD', 'null', 'null', 'XR6視界', 'WARNING & ALERT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'AUTO LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
         'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
            'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
            'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
            'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
            'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'Auto light', 'w/o,LINタイプ,ハードウェアタイプ', '自動車のボディ制御に使われる通信プロトコル「LIN」', 'XX4BCM',
            'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'AUTO LIGHT (ALS)', 'w,w/o', 'null', 'XX4オートライト', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'AUTO LIGHT SYSTEM', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'Auto Wiper', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'AUTO WIPER AND AUTO LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-002', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-003', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S2'), (
            'WZ1J', 'conf-004', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-005', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-006', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-001', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-002', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-005', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'Automatically folding mirror', 'w,w/o', 'null', 'XX4BCM', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), ('WZ1J', 'conf-001', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
                                     'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT',
                                     'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1'), (
            'WZ1J', 'conf-002', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
            'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'AD1'), ('WZ1J', 'conf-003', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
                                            'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT',
                                            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD2'), (
            'WZ1J', 'conf-004', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
            'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'AD1'), ('WZ1J', 'conf-005', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
                                            'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT',
                                            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1'), (
            'WZ1J', 'conf-006', 'AUTONOMOUS DRIVING', 'ALL,w/o,AD1,AD2', 'null',
            'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'AD1'), (
            'WZ1J', 'conf-001', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', 'AUTONOMOUS DRIVING SF', 'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK', 'null', 'XX4EMC',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'AUTONOMOUS EMERGENCY STEERING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-002', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-003', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-004', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-005', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-006', 'BACKWARD COLLISION PREVEN', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-001', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), (
            'WZ1J', 'conf-002', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), (
            'WZ1J', 'conf-003', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), (
            'WZ1J', 'conf-004', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), (
            'WZ1J', 'conf-005', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), (
            'WZ1J', 'conf-006', 'Battery Charger For ELEC. VEH', 'ALL', 'null', 'UE2燃費', 'CHARGER', 'X14_EV_PHEV_HEV',
            'S'), ('WZ1J', 'conf-001', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
                   'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-002', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-003', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-004', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-005', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-006', 'BATTERY HEATING', '(Water PTC),w', 'null', 'XX4NH電動車,XQ5保安防災',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-001', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'BD-EPS(ベルトドライブEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
                   'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'BLACK BOX', 'W/ EVENT DATA RECORDER', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-002', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-003', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-004', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-005', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-006', 'BLIND SPOT DETECTION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        ('WZ1J', 'conf-001', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
         'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'BLIND SPOT INTERVENTION (BSI)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-002', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-005', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', 'BLIND SPOT WARNING (BSW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'),
        ('WZ1J', 'conf-001', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-002', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-003', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-004', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-005', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-006', 'BOSE', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-001', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-002', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-003', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-004', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-005', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-006', 'BOSE SPEAKER', 'Ｗ', 'null', 'XX4WH', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-001', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-002', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-003', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-004', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-005', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-006', 'Brake lamp', 'LED,Bulb', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'LED'), (
            'WZ1J', 'conf-001', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'Brake type', 'null', 'null', 'XJBVDC,XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-002', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-003', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-004', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-005', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-006', 'BRAKING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-001', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'BULB REAR LAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'CAB違い', 'null', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-002', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-003', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-004', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-005', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-006', 'CCS2', 'w', 'null', 'XM6E2E', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-001', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', 'CENTER CONSOLE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-002', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-003', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-004', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-005', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-006', 'CENTER CONSOLE 2ND ROW', '2ND SUPER MULTI CONSOLE with RCP', 'null', 'XX4EMC',
            '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-002', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-003', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-004', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-005', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-006', 'Central door locking', 'central door lock SW (DR)', 'null', 'XX4スイッチ', 'ACCESS',
            'X08_EXTERIOR', 'central door lock SW (DR)'), (
            'WZ1J', 'conf-001', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'CHARGE WARNING LAMP', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-002', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-003', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-004', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-005', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-006', 'CHARGER', 'SINGLE,3PHASE', 'null', 'XX4NH電動車', 'CHARGER', 'X14_EV_PHEV_HEV', 'SINGLE'),
        ('WZ1J', 'conf-001', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
         'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'CLUTCH CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'CLUTCH_UNIT', 'null', 'null', 'XR2コントロール', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'COLD STARTING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
                   'COMBI METER', 'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-002', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
            'COMBI METER', 'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-003', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
            'COMBI METER', 'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-004', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
            'COMBI METER', 'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-005', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
            'COMBI METER', 'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-006', 'COMBI METER', 'FULL TFT,ANALOG SPEED+TACHO + TFT,ALL', 'null', 'XX4CANGateway',
            'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-001', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'COMBINATION SWITCH', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-001', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Cross bar', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-002', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-005', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', 'CRUISE CONTROL/SPEED LIMI', 'null', 'null', 'XQ3AD', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY',
            'w'), ('WZ1J', 'conf-001', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
                   'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'CRUISE CONTROL/SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'DAS', 'w,w/o', 'DAS(ダイレクトアダプティブステアリング)', 'XQ5Failsafe', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'DAS(ダイレクトアダプティブステアリング)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'DAYTIME HEADLIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'DAYTIME RUNNING LIGHT', 'with', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-002', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-005', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'DAYTIME RUNNING LIGHT (DRL)', 'w,ALL', 'null', 'XR6視界,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        (
            'WZ1J', 'conf-002', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        (
            'WZ1J', 'conf-003', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        (
            'WZ1J', 'conf-004', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        (
            'WZ1J', 'conf-005', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        (
            'WZ1J', 'conf-006', 'DAYTIME RUNNING LIGHTS', 'ALL', 'null', 'XX4EMC,XX4WH', 'LIGHTING', 'X01_VISIBILITY',
            'w'),
        ('WZ1J', 'conf-001', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-002', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-003', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-004', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-005', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-006', 'DC CHARGER', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-001', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'DCDC', 'ALL', 'null', 'XX4NH電動車', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'Delay Timer', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'DIRECT ADAPTIVE STEERING', 'ｗ', 'null', 'XX4PT', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
                   'X07_AUDIO_NAVIGATION_CCS', 'w/o'), (
            'WZ1J', 'conf-002', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w/o'), (
            'WZ1J', 'conf-003', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w/o'), (
            'WZ1J', 'conf-004', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w/o'), (
            'WZ1J', 'conf-005', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w/o'), (
            'WZ1J', 'conf-006', 'DISPLAY AUDIO', 'w', 'null', 'XX4GN1ラジオノイズ,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w/o'),
        ('WZ1J', 'conf-001', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-002', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-003', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-004', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-005', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-006', 'DOOR SAFETY', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'), (
            'WZ1J', 'conf-001', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'DP-EPS(デュアルピニオンEPS)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'DR HEATED SEAT', 'w,w/o', 'null', 'XX4SC', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-003', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-006', 'DR SEAT COMFORT FEATURE', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-001', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-003', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-006', 'DR SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-001', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-002', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-003', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-006', 'DR SEAT TYPE AND ADJUSTMENT', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'), (
            'WZ1J', 'conf-001', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-002', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-003', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-004', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-005', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-006', 'DR SEAT TYPE AND ADJUSTMENT.', 'POWER,MANUAL', 'null', 'XR6シートベルト', 'DRIVER SEAT',
            'X03_SEAT', 'POWER'), (
            'WZ1J', 'conf-001', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-002', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-003', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        (
            'WZ1J', 'conf-004', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-005', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-006', 'DRIVE EVENT RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'),
        ('WZ1J', 'conf-001', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
         'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'DRIVE RECORDER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4CANGateway', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', 'DRIVER ATTENTION ALERT', 'ALL', 'null', 'XX4EMC,XQ3AD', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-002', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-003', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-004', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-005', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-006', 'DRIVER MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-001', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
         'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-002', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S2'), (
            'WZ1J', 'conf-003', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S2'), (
            'WZ1J', 'conf-004', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-005', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S2'), (
            'WZ1J', 'conf-006', 'driver monitoring by steering', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-001', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', "DRIVER'S AIRBAG", 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'DRIVING ASSISTANCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'DRIVING ASSITANCE', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        (
            'WZ1J', 'conf-001', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'), (
            'WZ1J', 'conf-002', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'), (
            'WZ1J', 'conf-003', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'), (
            'WZ1J', 'conf-004', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'), (
            'WZ1J', 'conf-005', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'), (
            'WZ1J', 'conf-006', 'Driving mode', 'LINタイプ,ハードウェアタイプ', 'どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」',
            'XX4BCM',
            'DRIVING MODE', 'X09_MECHANISM', 'ハードウェアタイプ'),
        ('WZ1J', 'conf-001', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-002', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-003', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-004', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-005', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-006', 'DRIVING MODE 2WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-001', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-002', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-003', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-004', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-005', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-006', 'DRIVING MODE 4WD', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-001', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S1'),
        ('WZ1J', 'conf-002', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S2'),
        ('WZ1J', 'conf-003', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S2'),
        ('WZ1J', 'conf-004', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S1'),
        ('WZ1J', 'conf-005', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S2'),
        ('WZ1J', 'conf-006', 'DRIVING MODE CONTROL', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'S2'),
        ('WZ1J', 'conf-001', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'DRL', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-002', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-003', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-005', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-006', 'DVR', 'null', 'ドライブレコーダー', 'XR6視界,XX4DVR', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'DYNAMIC TURN INDICATOR', 'w', 'null', 'XX4TurnLamp', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-002', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-003', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-004', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-005', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-006', 'E-DIMMING', 'null', 'null', 'XX4Sunroof', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-001', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'e-releace', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'ECO DRIVING COACHING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-002', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-003', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-004', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-005', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-006', 'ECONOMIC DRIVING', 'ALL', 'null', 'XX4EMC', 'DRIVING MODE', 'X09_MECHANISM', 'w'), (
            'WZ1J', 'conf-001', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'ECU付電動センサーストレージボックス', 'ALL', 'null', 'XX4MCS', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-002', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-003', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-004', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-005', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-006', 'ELECTRIC PARKING BRAKE', 'null', 'null', 'XQ5保安防災', 'PARKING BRAKE', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-001', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'ELECTRIC TOLL COLLECTION', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
                   'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-002', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
            'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-003', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
            'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-004', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
            'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-005', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
            'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-006', 'ELECTRICAL SIDE DOOR OPENING AND CLOSING', 'ALL', 'null', 'XX4EMC', 'OPENING',
            'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-001', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', 'EMERGENCY ASSIST FOR PEDAL MISAPPLICATION', 'ALL', 'null', 'XQ3AD,XX4EMC',
            'ADAS SAFETY',
            'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), (
            'WZ1J', 'conf-002', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), (
            'WZ1J', 'conf-003', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), (
            'WZ1J', 'conf-004', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), (
            'WZ1J', 'conf-005', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), (
            'WZ1J', 'conf-006', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'ALL', 'null', 'XX4EMC', 'BRAKING',
            'X09_MECHANISM',
            'S'), ('WZ1J', 'conf-001', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
                   'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'EMERGENCY CALL AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-002', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-003', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-004', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-005', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        (
            'WZ1J', 'conf-006', 'EMERGENCY SIGNAL', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT', 'X11_SAFETY_SECURITY',
            '-'),
        ('WZ1J', 'conf-001', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
         'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'emergency steering assist/support (esa/ess)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'EMERGENCY STOP SIGNAL ', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'ENERGY SMART MANAGEMENT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'ENG', 'Gasoline,Diesel', 'null', 'XR2燃料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        (
            'WZ1J', 'conf-001', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'ENGINE REV COUNTER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
         'w'), (
            'WZ1J', 'conf-002', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-003', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-004', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-005', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-006', 'ENGINE START / POWER ON', 'ALL', 'null', 'XX4EMC', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'w'), ('WZ1J', 'conf-001', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
                   'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-002', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-003', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-004', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-005', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-006', 'ENGINE START TYPE', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'PHYSICAL SWITCHES',
            'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-001', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'EPKB', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'ESCL', 'w,w/o', '電子ステアリング コラム ロック', 'XX4BCM', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'ESS', 'null', 'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)', 'XR6視界', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'ETC 2.0(ELECTRIC TOLL COLLECTION)', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'EV CHARGE CONN TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
                   'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-002', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-003', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-004', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-005', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-006', 'EV SOUND FOR PEDESTRIANS', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-001', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'EVSE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Exh.仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'EXTERIOR MIRRORS RETRACTI', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-002', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-003', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'), (
            'WZ1J', 'conf-004', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-005', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-006', 'EXTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'),
        ('WZ1J', 'conf-001', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'FAP（フルオートパーク）', 'w', 'null', 'UI6EV', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'FAR SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'FLUSH DOOR HANDLE', 'w', 'null', 'XX4メカトロS45', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Flush handle', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'FOG LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'FORWARD COLLISION WARNING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
                   'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'FORWARD EMERGENCY BRAKING', 'ALL', 'null', 'XQ3AD,XX4EMC,XX4AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), (
            'WZ1J', 'conf-002', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), (
            'WZ1J', 'conf-005', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', 'FR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), ('WZ1J', 'conf-001', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'FR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'FR FOG LAMP(HAROGEN)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'FR FOG LAMP(LED)', 'W', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR Grill-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'Fr Heater Seat', 'with', 'null', 'XR5空調', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'FR RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'FR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'FR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'FR SIDE CAMERA', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'FR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'FR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-002', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-003', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'B'), (
            'WZ1J', 'conf-004', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-005', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-006', 'FR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            'B'), (
            'WZ1J', 'conf-001', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-002', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-003', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w'), (
            'WZ1J', 'conf-004', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-005', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-006', 'Fr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', 'DRIVER SEAT',
            'X03_SEAT',
            'w'),
        ('WZ1J', 'conf-001', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:Multi\nRR:5link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:Multi\nRR:LEAF', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:Multi\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:STRUT\nRR:3Link', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
         '-'), (
            'WZ1J', 'conf-002', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'FR:STRUT\nRR:HT Beam', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'FR:STRUT\nRR:Prarell', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:STRUT\nRR:QI2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:STRUT\nRR:RM2', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'FR:STRUT\nRR:TC', 'w', 'null', 'XR2シャシー', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-002', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-003', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-004', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-005', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-006', 'FRONT  WINDOW OPENING SYS', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        ('WZ1J', 'conf-001', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-002', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-005', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', 'FRONT COLLISION WARNING', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-001', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-002', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-003', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-004', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-005', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-006', 'FRONT DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        ('WZ1J', 'conf-001', 'FRONT DOOR WINDOW OPENING2',
         'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
         'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
         'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'), (
            'WZ1J', 'conf-002', 'FRONT DOOR WINDOW OPENING2',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
            'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'), (
            'WZ1J', 'conf-003', 'FRONT DOOR WINDOW OPENING2',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
            'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'), (
            'WZ1J', 'conf-004', 'FRONT DOOR WINDOW OPENING2',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
            'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'), (
            'WZ1J', 'conf-005', 'FRONT DOOR WINDOW OPENING2',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
            'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'), (
            'WZ1J', 'conf-006', 'FRONT DOOR WINDOW OPENING2',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL', 'null',
            'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT',
            'POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'),
        ('WZ1J', 'conf-001', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-002', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-003', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-004', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-005', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-006', 'Front Fog', 'w,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-001', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-002', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-003', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-004', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-005', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-006', 'FRONT FOG LAMP\nフロントフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        ('WZ1J', 'conf-001', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
         'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'FRONT FOG LAMP', 'LED,HALOGEN,w,all', 'null', 'XX7USM,XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'FRONT ILLUMINATION LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT KNEE AIRBAGS', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT LIGHT\nヘッドランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-001', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-001', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT LIGHT/HEAD LAMP', 'ALL', 'null', 'XX4WH', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-001', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-002', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-003', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-006', 'FRONT PASSENGER SEAT(S)', 'ALL', 'null', 'XX4EMC', 'ASSIST SEAT', 'X03_SEAT', 'S2'), (
            'WZ1J', 'conf-001', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'FRONT SEAT BELT', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-001', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'FRONT SEAT BELT ADJUSTMEN', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
                   'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'FRONT SEAT BELT PRE-TENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'FRONT SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
                   'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'FRONT SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-002', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-003', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-006', 'FRONT SEATS TYPE', 'ALL', 'null', 'XX4EMC,XR2車体信頼', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-001', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'FRONT SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-002', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-003', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-004', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-005', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-006', 'FRONT WINDSCREEN HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'GLASSES', 'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-001', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN', 'w,w/o', 'null', 'XM6アンテナ', 'GLASSES',
            'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-002', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-003', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-004', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'),
        ('WZ1J', 'conf-005', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'),
        ('WZ1J', 'conf-006', 'FRONT WINDSCREEN WIPER SP', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-001', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-002', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-003', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-004', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-005', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-006', 'FULL AUTO A/C (TOUCH PANEL TYPE)', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '-'), (
            'WZ1J', 'conf-001', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'Full FlanK Protection(FKP)', 'w', 'null', 'XX4SONAR', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-001', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-003', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-004', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-006', 'GALASS ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-001', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'),
        ('WZ1J', 'conf-002', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'),
        ('WZ1J', 'conf-003', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'),
        ('WZ1J', 'conf-004', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'),
        ('WZ1J', 'conf-005', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'),
        ('WZ1J', 'conf-006', 'GEAR SHIFT AT', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT', 'Shift by wire'), (
            'WZ1J', 'conf-001', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-002', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-003', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-004', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-005', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-006', 'GEAR SPEED CONTROL TYPE', 'ALL', 'null', 'XX4EMC', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-001', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)', 'w/o', 'null', 'XX4AFS',
            'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-002', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-003', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-005', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-006', 'GROUND ILLUMINATION', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-002', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-003', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-004', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-005', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-006', 'HALOGEN HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-002', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-003', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-005', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-006', 'HAND FREE', 'w', 'Kick Sensor', 'XX4KickSensor', 'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'HANDS FREE POWER DOOR', 'w', 'null', 'XX4PSD', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-002', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-003', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-004', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-005', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-006', 'HBA(HIGH BEAM ASSIST)', 'w/o,w', 'null', 'XX4ADB,XX4HBA', 'LIGHTING', 'X01_VISIBILITY',
            'w'), ('WZ1J', 'conf-001', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'HDC', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'HEAD LAMP LEVELIZER', 'Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',
            'null',
            'XX7USM', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-002', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-003', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-004', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-005', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-006', 'HEAD LAMPS TYPE', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'LED'), (
            'WZ1J', 'conf-001', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-002', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-003', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-004', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-005', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-006', 'HEAD UNIT', 'NAVI,AUDIO,AUDIO LESS,NAVI READY', 'null', 'XM6アンテナ',
            'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'),
        ('WZ1J', 'conf-001', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-002', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-003', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-005', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-006', 'Head Up Display', 'w,w/o', 'null', 'XX4SV', 'COMBI METER', 'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w/o'), (
            'WZ1J', 'conf-002', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w/o'), (
            'WZ1J', 'conf-003', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-004', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w/o'), (
            'WZ1J', 'conf-005', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w/o'), (
            'WZ1J', 'conf-006', 'HEAD UP DISPLAY (HUD)', 'ALL', 'null', 'XX4EMC,XX4WH,XX4CANGateway', 'COMBI METER',
            'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-002', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-003', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-004', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-005', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-006', 'HEADLAMP CLEANER', 'with,ALL', 'null', 'XX7USM,XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'),
        ('WZ1J', 'conf-001', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-002', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-003', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-004', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-005', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-006', 'HEADLAMP TYPE', 'LED ,HALOGEN ', 'null', 'XX7USM', 'LIGHTING', 'X01_VISIBILITY', 'LED'),
        ('WZ1J', 'conf-001', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'HEADLIGHT WASHER', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'HEADLIGHT WIPERS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-002', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-003', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-004', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-005', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-006', 'HEAT PUMP', 'w,w/o', 'null', 'XR5空調', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'),
        ('WZ1J', 'conf-001', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'HEATED SCREEN', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-002', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-003', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-004', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-005', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-006', 'HEATER FOR EV', '(AIR PTC)', 'null', 'XX4NH電動車', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', '(AIR PTC)'), (
            'WZ1J', 'conf-001', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-002', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-003', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-004', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-005', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'), (
            'WZ1J', 'conf-006', 'HEATER FOR EV / ADDITIONAL HEATER', 'ALL', 'null', 'XX4EMC',
            'AIR CONDITIONING AND HEATING', 'X06_AIR_CONDITIONER', 'S'),
        ('WZ1J', 'conf-001', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-002', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-003', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-004', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-005', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-006', 'Heating windscreen', 'w,w/o', 'null', 'XX4BCM', 'GLASSES', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-001', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'HEPS(油圧電動パワステ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'HEV/PHEV ENERGY MODE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-002', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-003', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-004', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-005', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'), (
            'WZ1J', 'conf-006', 'HIGH BEAM ASSIST', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            'w'),
        ('WZ1J', 'conf-001', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'HIGH BEAM ASSIST (HBA)', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'HIGH MOUNTED STOP LAMP', 'null', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Hood visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'),
        ('WZ1J', 'conf-002', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'),
        ('WZ1J', 'conf-003', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'),
        ('WZ1J', 'conf-004', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'),
        ('WZ1J', 'conf-005', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'),
        ('WZ1J', 'conf-006', 'HORN', 'null', 'null', 'XR6視界', 'OTHER', 'X12_OTHER', 'DOUBLE'), (
            'WZ1J', 'conf-001', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-002', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-003', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-004', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-005', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-006', 'HUD', 'w,w/o', 'null', 'XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'w'), ('WZ1J', 'conf-001', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-002', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-003', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-004', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-005', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-006', 'I-KEY ', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-001', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-002', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-003', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-004', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-005', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-006', 'I-KEY (BADGE)', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-001', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'ICC', 'w,w/o', 'null', 'XJBVDC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'ADAS COMFORT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)', 'null', 'null', 'XQ4機構', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Illumination BI', 'null', 'null', 'XL7外装', 'LOGO & EMBLEM', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'IN-CAR COMMUNICATION', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-002', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-005', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'INSIDE MIRROR\nインサイドミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-002', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-005', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'INTERIOR REAR VIEW MIRROR', 'ALL', 'null', 'XX4EMC', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'IONIZER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'IVC', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-002', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-003', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-004', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-005', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-006', 'IVI', 'w,w/o', 'null', 'XX4BCM,XM6IVI,XR4HMI', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-001', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-002', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-003', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-004', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-005', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'), (
            'WZ1J', 'conf-006', 'IVI（NAVI/DA）', 'NAVI,DA,Less', 'null', 'XM6メータ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'NAVI'),
        ('WZ1J', 'conf-001', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'KEY SET', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-002', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-003', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-005', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-006', 'Kick Sensor', 'w,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'LANE DEPARTURE WARNING (LDW)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'LANE KEEP', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'Lapプリテン装備', 'with,without', '運転席プリテンショナ', 'XR6シートベルト', 'SEAT BELT',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'LATERAL SUPPORT SYSTEM', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
                   'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'LEAD CAR DEPARTURE NOTIFICATION', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'LED HEADLAMP', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'LED LB', 'w', 'null', 'XX4LEDHead', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'LED REAR LAMP ', 'w', 'null', 'XX4GN1ラジオノイズ', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'LIGHTS-ON WARNING', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        (
            'WZ1J', 'conf-001', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-002', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-003', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-004', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-005', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-006', 'LOCAL NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'),
        ('WZ1J', 'conf-001', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'LUGGAGE HOOK', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'MANUAL LEVELIZER', 'null', 'null', 'XR6視界', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'MAP LAMP', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-004', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'MASSAGE STANDARD\n(2nd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-001', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-004', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'MASSAGE STANDARD\n(3rd seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-001', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'MASSAGE STANDARD\n(FR seat)', 'w', 'null', 'XX4SPCU', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Max C.W.\nFR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Max C.W.\nRR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'Max C.W.\nTotal', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
         '-'), (
            'WZ1J', 'conf-002', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'MEDIA', 'AM/FM,DTV,SXM,DAS', 'null', 'XM6アンテナ', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-002', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-003', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-004', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-005', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-006', 'Meter', 'Full TFT,Display,Segment', 'null', 'XX4BCM,XX4AD', 'COMBI METER',
            'X02_COCKPIT',
            'Full TFT'), (
            'WZ1J', 'conf-001', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'), (
            'WZ1J', 'conf-002', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'), (
            'WZ1J', 'conf-003', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'), (
            'WZ1J', 'conf-004', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'), (
            'WZ1J', 'conf-005', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'), (
            'WZ1J', 'conf-006', 'Meter Display Size', '7inch,12.3inch,14inch', 'null', 'XX4SV,XX4AD', 'COMBI METER',
            'X02_COCKPIT', '14inch'),
        ('WZ1J', 'conf-001', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-002', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-003', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-004', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-005', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-006', 'METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-001', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'MICROPHONE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'MOVING OBJECT DETECTION (MOD)', 'null', 'null', 'XQ3AD', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'MUD GUARD', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        (
            'WZ1J', 'conf-002', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        (
            'WZ1J', 'conf-003', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        (
            'WZ1J', 'conf-004', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        (
            'WZ1J', 'conf-005', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        (
            'WZ1J', 'conf-006', 'NAVI', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
            'w'),
        ('WZ1J', 'conf-001', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS',
         '14.3”\u200b'), (
            'WZ1J', 'conf-002', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '14.3”\u200b'), (
            'WZ1J', 'conf-003', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '14.3”\u200b'), (
            'WZ1J', 'conf-004', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '14.3”\u200b'), (
            'WZ1J', 'conf-005', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '14.3”\u200b'), (
            'WZ1J', 'conf-006', 'Navi-size', 'ALL', 'null', 'XR6内外装', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '14.3”\u200b'),
        ('WZ1J', 'conf-001', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'OCCUPANT MONITORING', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
         'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-002', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-003', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-004', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-005', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-006', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT', 'null', 'null', 'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-002', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-003', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-004', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-005', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-006', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'null', 'null',
            'XR6乗員判別',
            'ASSIST SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'OCCUPANTS SAFE EXIT', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'OFF ROAD', 'ALL', 'null', 'XX4EMC,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
         'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-002', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-003', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-004', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-005', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'S'), (
            'WZ1J', 'conf-006', 'ONE PEDAL FUNCTION WITH STOP', 'ALL', 'null', 'XX4EMC', 'EV DEDICATED FEATURES',
            'X14_EV_PHEV_HEV', 'S'),
        ('WZ1J', 'conf-001', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-002', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-003', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S3'),
        ('WZ1J', 'conf-004', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-005', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-006', 'OUTSIDE CAMERA', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S2'), (
            'WZ1J', 'conf-001', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-002', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-003', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'), (
            'WZ1J', 'conf-004', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-005', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-006', 'OUTSIDE MIRROR\nアウトサイドミラー', 'null', 'null', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'), ('WZ1J', 'conf-001', 'OUTSIDE MIRROR',
                                      'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
                                      'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
                                      'Electrrical Adjustment + Automatically Folding'), (
            'WZ1J', 'conf-002', 'OUTSIDE MIRROR',
            'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
            'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            'Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side'), (
            'WZ1J', 'conf-003', 'OUTSIDE MIRROR',
            'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
            'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            'Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side'), (
            'WZ1J', 'conf-004', 'OUTSIDE MIRROR',
            'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
            'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            'Electrrical Adjustment + Automatically Folding'), ('WZ1J', 'conf-005', 'OUTSIDE MIRROR',
                                                                'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
                                                                'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA',
                                                                'X01_VISIBILITY',
                                                                'Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side'),
        ('WZ1J', 'conf-006', 'OUTSIDE MIRROR',
         'Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',
         'null', 'XX4EMC,XX4スイッチ', 'SIDE VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
         'Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side'), (
            'WZ1J', 'conf-001', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-002', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-003', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'), (
            'WZ1J', 'conf-004', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-005', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-006', 'OUTSIDE MIRROR ADJUST', 'ALL', 'null', 'XX4EMC', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S3'), (
            'WZ1J', 'conf-001', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'OUTSIDE MIRROR MEMORY', 'w', 'null', 'XX4PMU', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'OUTSIDE TEMPERATURE METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-001', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'OUTSIDE THERMO METER', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-001', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-002', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-003', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-005', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-006', 'PADDLE Shift', 'w,w/o', 'null', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-002', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-003', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w'), (
            'WZ1J', 'conf-004', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-005', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w/o'), (
            'WZ1J', 'conf-006', 'PADDLE SHIFT LEVER', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4EMC', 'STEERING', 'X02_COCKPIT',
            'w'), ('WZ1J', 'conf-001', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Panic Alarm', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'PARK ASSIST', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-002', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-003', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S2'),
        ('WZ1J', 'conf-004', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-005', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'),
        ('WZ1J', 'conf-006', 'PARKING ALERTS', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'S1'), (
            'WZ1J', 'conf-001', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'PARKING ASSIST SYSTEM', 'ALL', 'null', 'XQ3AD,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-001', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-002', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-003', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-004', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-005', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-006', 'PARKING BRAKE TYPE', 'null', 'mechanical, electric両方', 'XJBVDC', 'PARKING BRAKE',
            'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-001', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'), (
            'WZ1J', 'conf-002', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'), (
            'WZ1J', 'conf-003', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'), (
            'WZ1J', 'conf-004', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'), (
            'WZ1J', 'conf-005', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'), (
            'WZ1J', 'conf-006', 'PARKING BRAKE TYPE AND ASSIST', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE',
            'X02_COCKPIT',
            'EPKB'),
        ('WZ1J', 'conf-001', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'PASSENGER AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'PATH CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'PBD', 'w,w/o', 'Power Back Door', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'PCU', 'null', 'null', 'XX4リモート', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-002', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-003', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-004', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-005', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-006', 'PKB hand,foot', 'null', 'null', 'XR2コントロール', 'PARKING BRAKE', 'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-001', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-002', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-003', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-004', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-005', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'),
        ('WZ1J', 'conf-006', 'PLUG AND CHARGE', 'null', 'null', 'XX4EMC', 'CHARGER', 'X14_EV_PHEV_HEV', 'w'), (
            'WZ1J', 'conf-001', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'POST COLLISION AND BREAKDOWN', 'ALL', 'null', 'XX4EMC', 'WARNING & ALERT',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'), (
            'WZ1J', 'conf-002', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'), (
            'WZ1J', 'conf-003', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'), (
            'WZ1J', 'conf-004', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'), (
            'WZ1J', 'conf-005', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'), (
            'WZ1J', 'conf-006', 'POWER BACK DOOR', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING',
            'X08_EXTERIOR',
            'w'),
        ('WZ1J', 'conf-001', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Power Back Door(PBD)', 'w', 'null', 'XX4メカトロS46', 'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'POWER OPEN/CLOSE SLIDE', 'w', 'null', 'XX4メカトロS45', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-002', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'POWER SEAT', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-002', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-003', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-004', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-005', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-006', 'Power Slide Door', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-001', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'POWER STEERING', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-001', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-002', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-003', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-004', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-005', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'),
        ('WZ1J', 'conf-006', 'Power Trunk', 'null', 'null', 'XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', '-'), (
            'WZ1J', 'conf-001', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'), (
            'WZ1J', 'conf-002', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'), (
            'WZ1J', 'conf-003', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'), (
            'WZ1J', 'conf-004', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'), (
            'WZ1J', 'conf-005', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'), (
            'WZ1J', 'conf-006', 'Powerwindow', '4席アンチピンチあり, 4席アンチピンチなし', 'SPに4APと記載', 'XX4BCM', 'WINDOW OPENING',
            'X02_COCKPIT', '-'),
        ('WZ1J', 'conf-001', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'PRE CRASH', 'w', 'null', 'XX4プリクラッシュ', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-002', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-003', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-004', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-005', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-006', 'predictive forward collision warning (pfcw)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'PROXIMITY RADAR', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'PS', 'With', 'null', 'XQ2操安', 'STEERING', 'X02_COCKPIT', 'w/o'), (
            'WZ1J', 'conf-001', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-002', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-003', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-004', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-005', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'), (
            'WZ1J', 'conf-006', 'PTC Heater', 'w,w/o', 'null', 'XX4BCM', 'AIR CONDITIONING AND HEATING',
            'X06_AIR_CONDITIONER', 'w'),
        ('WZ1J', 'conf-001', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'PUDDLE LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'RAIN SENSITIVE', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'GLASSES', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'RAISED BRAKE LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'REAR  LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'REAR AEB', 'null', 'null', 'XQ3AD', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'REAR CAMERA', 'w', 'null', 'XX4GN1ラジオノイズ', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'REAR CNTER SEAT BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-002', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-003', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'),
        ('WZ1J', 'conf-004', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-005', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-006', 'REAR DOOR OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'),
        ('WZ1J', 'conf-001', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-002', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-003', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-004', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-005', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-006', 'REAR DOOR WINDOW OPENING', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-001', 'REAR DOOR WINDOW OPENING2', 'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
         'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'), (
            'WZ1J', 'conf-002', 'REAR DOOR WINDOW OPENING2',
            'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
            'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'), (
            'WZ1J', 'conf-003', 'REAR DOOR WINDOW OPENING2',
            'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
            'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'), (
            'WZ1J', 'conf-004', 'REAR DOOR WINDOW OPENING2',
            'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
            'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'), (
            'WZ1J', 'conf-005', 'REAR DOOR WINDOW OPENING2',
            'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
            'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'), (
            'WZ1J', 'conf-006', 'REAR DOOR WINDOW OPENING2',
            'POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',
            'null', 'XX4スイッチ', 'WINDOW OPENING', 'X02_COCKPIT', 'POWERED REAR WINDOW LIFT ✚ TIMER'),
        ('WZ1J', 'conf-001', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-002', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-003', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-004', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-005', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-006', 'Rear Fog', 'LED,Bulb,w/o', 'null', 'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR FOG LAMP\nリアフォグランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-002', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-003', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-004', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-005', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-006', 'REAR FOG LAMP', 'w,ALL', 'null', 'XX4GN1ラジオノイズ,XX4WH,XX4EMC', 'LIGHTING',
            'X01_VISIBILITY',
            '-'), ('WZ1J', 'conf-001', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-002', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-003', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'),
        ('WZ1J', 'conf-004', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-005', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-006', 'REAR GATE OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'), (
            'WZ1J', 'conf-001', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), (
            'WZ1J', 'conf-002', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), (
            'WZ1J', 'conf-003', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), (
            'WZ1J', 'conf-004', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), (
            'WZ1J', 'conf-005', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), (
            'WZ1J', 'conf-006', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY',
            'S'), ('WZ1J', 'conf-001', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-002', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-003', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-004', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-005', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-006', 'REAR LIGHT', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-001', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR SCREEN', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR SCREEN SF', 'DEFOGGER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR SCREEN WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-002', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-003', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-004', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-005', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-006', 'REAR SEAT', 'ALL', 'null', 'XR2車体信頼', '2ND ROW SEAT', 'X03_SEAT', 'S'),
        ('WZ1J', 'conf-001', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', 'REAR SEAT ALERT', 'ALL', 'null', 'XR6乗員判別,XX4EMC', '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'REAR SEAT BELT PRETENSIONER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            'S'),
        ('WZ1J', 'conf-001', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'REAR SEATS BELT', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'REAR SPOILER', 'w,w/o', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device', 'UNKNOW_device_group',
         '-'), (
            'WZ1J', 'conf-002', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'REAR TOWING DEVICE', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
                   'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-003', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-004', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-006', 'REAR VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-001', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'REAR VIEW CAMERA', 'ALL', 'null', 'XX4EMC,XM6camera', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'REAR VIEW CAMERA (DIGITAL)'), (
            'WZ1J', 'conf-002', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), (
            'WZ1J', 'conf-003', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), (
            'WZ1J', 'conf-004', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'REAR VIEW CAMERA (DIGITAL)'), (
            'WZ1J', 'conf-005', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), (
            'WZ1J', 'conf-006', 'REAR VIEW MONITOR\n（RVM）', 'ALL', 'null', 'XR6視界', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w/o'), ('WZ1J', 'conf-001', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR WINDOW', 'W/ TIMER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-002', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-003', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-004', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-005', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        (
            'WZ1J', 'conf-006', 'REAR WINDOW OPENING SYSTE', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            'S'),
        ('WZ1J', 'conf-001', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR WINDOW WIPER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'REAR WIPERS\nリアワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'REGENERATIVE BRAKE FOR EV', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'REGENERATIVE BRAKING TYPE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'REMOTE ENGINE STARTER', 'w,w/o', 'null', 'XX4BCM,XX4GN1ラジオノイズ', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'REMOTE ENGINE STARTER (STAND ALONE)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'REMOTE ENGINE STARTER WITH KEY', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-002', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-003', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-004', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-005', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'), (
            'WZ1J', 'conf-006', 'REMOTE PARKING', 'w,w/o,ALL', 'null', 'XX4BCM,XX4EMC', 'ADAS PARKING',
            'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-001', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'RES', 'ｗ', 'null', 'XP4EVシステム', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-002', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-003', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-004', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-005', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-006', 'REVERSIBLE CHARGER', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'null', 'XX4NH電動車,XX4EMC',
            'CHARGER', 'X14_EV_PHEV_HEV', 'VEHICLE TO LOAD (V2L) OUTSIDE'), (
            'WZ1J', 'conf-001', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-002', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-003', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-004', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-005', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), (
            'WZ1J', 'conf-006', 'RLS(Rain Light Sensor)', 'w,w/o', 'null', 'XX4オートライト,レインセンサ', 'LIGHTING',
            'X01_VISIBILITY',
            'w/o'), ('WZ1J', 'conf-001', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
                     'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-002', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-003', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-004', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-005', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'), (
            'WZ1J', 'conf-006', 'ROD ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-001', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-002', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-003', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-004', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-005', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-006', 'ROOF', 'ALL', 'null', 'XQ4実車', 'OPENING', 'X08_EXTERIOR', 'S'), (
            'WZ1J', 'conf-001', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-002', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-003', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-004', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-005', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-006', 'ROOF / SUNROOF', 'ALL,Sun Roof,Glass Roof,Normal Roof', 'null', 'XX4EMC,XR6乗員判定',
            'OPENING', 'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-001', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-002', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-003', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-004', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-005', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'), (
            'WZ1J', 'conf-006', 'ROOF OPENING', 'Sun Roof,Glass Roof,Normal Roof', 'null', 'XR2車体信頼', 'OPENING',
            'X08_EXTERIOR', 'Glass Roof'),
        ('WZ1J', 'conf-001', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Roof rack', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'Roof rail', 'w,w/o', 'null', 'XR5風音,XR6内外装', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
                   'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'ROOF RAIL AND CROSS BAR', 'ｗ', 'null', 'XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-002', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-003', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-004', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-005', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-006', 'ROOM MIRROR', 'ALL', 'null', 'XX4EMC,XQ4実車', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-001', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
         'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-002', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-003', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S2'), (
            'WZ1J', 'conf-004', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-005', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-006', 'ROOM MIRROR / REAR VISIBILITY', 'ALL', 'null', 'XX4EMC,XQ4車体',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'S1'), (
            'WZ1J', 'conf-001', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-002', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-003', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-004', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-005', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-006', 'ROOM MIRROR－AUTO DIMMING', 'w', 'null', 'XX4GN1ラジオノイズ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
         'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'w', 'null', 'XX4GN1ラジオノイズ',
            'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'RR BMPR-type', 'ALL', 'null', 'XR6内外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-002', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-003', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-004', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-005', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'),
        ('WZ1J', 'conf-006', 'RR BRAKE UNIT', 'null', 'null', 'XR2コントロール', 'BRAKING', 'X09_MECHANISM', '-'), (
            'WZ1J', 'conf-001', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-002', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-005', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', 'RR CAMERA', 'w,w/o', 'null', 'XL7外装,XR6内外装', 'ADAS PARKING',
            'X11_SAFETY_SECURITY',
            'w'), ('WZ1J', 'conf-001', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'RR FOG LAMP', 'W', 'null', 'XL7外装', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'Rr Heater Seat', 'with', 'null', 'XR5空調', '2ND ROW SEAT', 'X03_SEAT', 'w'), (
            'WZ1J', 'conf-001', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'RR POWER SLIDE  DOOR ', 'Ｗ', 'null', 'XX4WH', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'RR SEAT HEATER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-004', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', 'RR SEAT HEATER AND COOLER', 'Ｗ', 'null', 'XX4WH', '2ND ROW SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-001', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'RR SIDE RADAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'RR SONAR', 'null', 'null', 'XL7外装', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'RR SPOILER', 'null', 'null', 'XL7外装', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'RR SUSP形式違い', 'ALL', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-002', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-003', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-004', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-005', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-006', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'with', 'null', 'XR5空調', '2ND ROW SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-001', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'RVI CRUISE CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-002', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-003', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-004', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-005', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'),
        ('WZ1J', 'conf-006', 'SAFETY ACCESS FUNCTIONS', 'ALL', 'null', 'XX4EMC', 'ACCESS', 'X08_EXTERIOR', 'S'), (
            'WZ1J', 'conf-001', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1e'), (
            'WZ1J', 'conf-002', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1e+Navilink'), (
            'WZ1J', 'conf-003', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD2'), (
            'WZ1J', 'conf-004', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1e'), (
            'WZ1J', 'conf-005', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1e+Navilink'), (
            'WZ1J', 'conf-006', 'Safety Driving', 'ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink', 'null', 'XX4AD',
            'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'AD1e+Navilink'),
        ('WZ1J', 'conf-001', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'SCENE RECORDER', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーなし'),
        ('WZ1J', 'conf-002', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーあり'),
        ('WZ1J', 'conf-003', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーあり'),
        ('WZ1J', 'conf-004', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーなし'),
        ('WZ1J', 'conf-005', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーあり'),
        ('WZ1J', 'conf-006', 'Seat adjustment', 'メモリーあり,メモリーなし', 'null', 'XX4BCM', 'DRIVER SEAT', 'X03_SEAT', 'メモリーあり'),
        ('WZ1J', 'conf-001', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY',
         '-'), (
            'WZ1J', 'conf-002', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-003', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-004', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-005', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'), (
            'WZ1J', 'conf-006', 'SEAT BELT NOT SECURED WAR', 'ALL', 'null', 'XX4EMC', 'SEAT BELT',
            'X11_SAFETY_SECURITY',
            '-'),
        ('WZ1J', 'conf-001', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'SEAT BELT REMINDER', 'ALL', 'null', 'XX4EMC', 'SEAT BELT', 'X11_SAFETY_SECURITY', 'S'), (
            'WZ1J', 'conf-001', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-002', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w'),
        (
            'WZ1J', 'conf-003', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w'),
        (
            'WZ1J', 'conf-004', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w'),
        (
            'WZ1J', 'conf-005', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w'),
        (
            'WZ1J', 'conf-006', 'SEAT HEATER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ,XR6乗員判別', 'DRIVER SEAT', 'X03_SEAT',
            'w'),
        ('WZ1J', 'conf-001', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
         '-'), (
            'WZ1J', 'conf-002', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'SEAT HEATER AND COOLER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-003', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-006', 'SEAT HEATING', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'), (
            'WZ1J', 'conf-001', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER A'), (
            'WZ1J', 'conf-002', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER B'), (
            'WZ1J', 'conf-003', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER C'), (
            'WZ1J', 'conf-004', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER A'), (
            'WZ1J', 'conf-005', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER B'), (
            'WZ1J', 'conf-006', 'SEAT LINING', 'ALL', 'null', 'XR6乗員判別,XQ4実車', 'TRIM', 'X03_SEAT',
            'SYNTHETIC LEATHER C'), (
            'WZ1J', 'conf-001', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER A'), (
            'WZ1J', 'conf-002', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER B'), (
            'WZ1J', 'conf-003', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER C'), (
            'WZ1J', 'conf-004', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER A'), (
            'WZ1J', 'conf-005', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER B'), (
            'WZ1J', 'conf-006', 'SEAT LINING.', 'PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',
            'null', 'XR6シートベルト', 'TRIM', 'X03_SEAT', 'SYNTHETIC LEATHER C'),
        ('WZ1J', 'conf-001', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'),
        ('WZ1J', 'conf-002', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'),
        ('WZ1J', 'conf-003', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'),
        ('WZ1J', 'conf-004', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'),
        ('WZ1J', 'conf-005', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'),
        ('WZ1J', 'conf-006', 'SEAT TYPE', '手動、自動', 'null', 'XQ5保安防災', 'DRIVER SEAT', 'X03_SEAT', '自動'), (
            'WZ1J', 'conf-001', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-002', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-003', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-004', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-005', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-006', 'SETTINGS OF COMBI METER', 'ALL', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT',
            'S1'), ('WZ1J', 'conf-001', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
                    'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-002', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-003', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-004', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-005', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'), (
            'WZ1J', 'conf-006', 'SHARK FIN ANTENNA', 'w', 'null', 'XX4GN1ラジオノイズ', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'w'),
        ('WZ1J', 'conf-001', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'SIDE AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-002', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-003', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-004', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-005', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-006', 'SIDE CURTAIN AIRBAG', 'ALL', 'null', 'XX4EMC', 'AIRBAGS', 'X11_SAFETY_SECURITY', 'S'),
        ('WZ1J', 'conf-001', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'SIDE LIGHTS', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-002', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-003', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-004', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-005', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-006', 'SIDE MARKER LAMP', 'ALL', '前後フェンダーの標識ランプ', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY',
            '-'), ('WZ1J', 'conf-001', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'SIDE TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-001', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Side visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-002', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-003', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-004', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-005', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-006', 'SIZE OF COMBI METER SCREEN', 'ALL,14.3" DISPLAY', 'null', 'XX4EMC,XM6メータ,XR6シートベルト',
            'COMBI METER', 'X02_COCKPIT', '14.3" DISPLAY'), (
            'WZ1J', 'conf-001', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'SMART REAR VIEW MIRROR', 'ALL', 'null', 'XX4WH', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'),
        ('WZ1J', 'conf-001', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-002', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-003', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-004', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-005', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-006', 'SOCKET ACCESSORY', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-001', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'SONER', 'ALL', 'null', 'XX4EMC', 'ADAS PARKING', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-002', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-003', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-004', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-005', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', '-'),
        ('WZ1J', 'conf-006', 'sound bubble', 'ALL', 'null', 'XM6音質', 'SOUND BUBBLE', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-001', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'SP1', '2phm,4ohm', 'null', 'XM6音質', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'SP2', 'Bose,Klipsch,Panasonic,6SP,4SP,2SP', 'null', 'XM6音質', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-002', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-003', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-004', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-005', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-006', 'SPARE WHEEL', 'w', 'null', 'XR2車体信頼', 'SPARE WHEEL', 'X10_WHEELS_&_TIRES', 'w/o'),
        ('WZ1J', 'conf-001', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-002', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-003', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S2'),
        ('WZ1J', 'conf-004', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-005', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-006', 'SPEAKER', 'ALL', 'null', 'XM6音質', 'SPEAKERS', 'X07_AUDIO_NAVIGATION_CCS', 'S2'),
        ('WZ1J', 'conf-001', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'SPEED CUT', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-002', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-003', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-004', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-005', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-006', 'SPEED LIMITER', 'ALL', 'null', 'XX4EMC', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', '-'),
        ('WZ1J', 'conf-001', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-002', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-003', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-004', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-005', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-006', 'SPEED METER UNIT', 'ALL', 'null', 'XX4EMC', 'COMBI METER', 'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-001', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Speed sensing lock', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-004', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', 'SRVM', 'null', 'null', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'REAR VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-001', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'), (
            'WZ1J', 'conf-002', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'), (
            'WZ1J', 'conf-003', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'), (
            'WZ1J', 'conf-004', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'), (
            'WZ1J', 'conf-005', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'), (
            'WZ1J', 'conf-006', 'Start Engine  type', 'I-key,CKC', 'null', 'XX4BCM', 'PHYSICAL SWITCHES', 'X02_COCKPIT',
            'I-key'),
        ('WZ1J', 'conf-001', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'STATIONARY HEATER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'STEERING', 'ELECTRIC POWERED', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-001', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'STEERING SWITCH', 'ALL', 'null', 'null', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-001', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'STEERING SWITCHES', 'ALL', 'null', 'XX4EMC', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-001', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-004', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'STEERING WHEEL', 'ALL', 'null', 'XQ4実車', 'STEERING', 'X02_COCKPIT', 'S1'), (
            'WZ1J', 'conf-001', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-002', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S2'), (
            'WZ1J', 'conf-003', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S2'), (
            'WZ1J', 'conf-004', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S1'), (
            'WZ1J', 'conf-005', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S2'), (
            'WZ1J', 'conf-006', 'STEERING WHEEL ADJUSTMENT', 'ALL', 'null', 'XX4EMC,XQ4車体', 'STEERING', 'X02_COCKPIT',
            'S2'),
        ('WZ1J', 'conf-001', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-002', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'STEERING WHEEL HEATER', 'ALL', 'null', 'XX4EMC,XX4WH', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-001', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-002', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'STRG Heater', 'w,w/o', 'null', 'XR5空調,XX4AD', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-001', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-002', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-003', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-004', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-005', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'),
        ('WZ1J', 'conf-006', 'SUN VISOR LED LIGHT', 'w,w/o', 'null', 'XR6内外装', 'SUN VISOR', 'X02_COCKPIT', 'S'), (
            'WZ1J', 'conf-001', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-002', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-003', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-004', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-005', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-006', 'SUNROOF', 'null', 'null',
            'XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別',
            'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-001', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'Sunroof visor', 'null', 'null', 'XR5風音', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-002', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-003', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-004', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-005', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-006', 'Sunshade', 'E-sunshade,basic,w/o', 'null', 'XX4BCM', 'OPENING', 'X08_EXTERIOR', 'basic'),
        ('WZ1J', 'conf-001', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
         'A'), (
            'WZ1J', 'conf-002', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-003', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
            'B'), (
            'WZ1J', 'conf-004', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-005', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'), (
            'WZ1J', 'conf-006', 'SUSPENSION CONTROL', 'null', 'null', 'XJBVDC', 'UNKNOW_device', 'UNKNOW_device_group',
            'B'), (
            'WZ1J', 'conf-001', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-002', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-003', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'B'), (
            'WZ1J', 'conf-004', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-005', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-006', 'SUSPENSION CONTROL VARIABLE DAMPING', 'w,w/o', 'null', 'XX4PT,XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', 'B'), (
            'WZ1J', 'conf-001', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-002', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-003', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'B'), (
            'WZ1J', 'conf-004', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-005', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-006', 'SUSPENSION TYPE', 'ALL', 'null', 'XQ5車両信頼性,XJBVDC', 'UNKNOW_device',
            'UNKNOW_device_group', 'B'), (
            'WZ1J', 'conf-001', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-002', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-003', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-004', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-005', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-006', 'TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE', 'w', 'null', 'XX4PBD', 'OPENING',
            'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-002', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-003', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'),
        ('WZ1J', 'conf-004', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-005', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S1'),
        ('WZ1J', 'conf-006', 'TAILGATE/TRUNK OPENING', 'ALL', 'null', 'XX4EMC', 'OPENING', 'X08_EXTERIOR', 'S2'), (
            'WZ1J', 'conf-001', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-002', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-003', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-004', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-005', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-006', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
            'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-002', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-003', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-004', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-005', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w/o'), (
            'WZ1J', 'conf-006', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE', 'w,w/o', 'null',
            'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ', 'OPENING', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'TELEMATIC', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
         '-'), (
            'WZ1J', 'conf-002', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'TELEMATIC DOORS LOCK', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
                   'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'TELEMATIC SYSTEM HYPOTHES', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'TELEMATICS\n(EMERGENCY CALL SW)', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-002', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-003', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-004', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-005', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-006', 'TIRE', 'null', 'null', 'XJBVDC,XX4ALARM,XQ2操安', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'),
        ('WZ1J', 'conf-001', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'),
        ('WZ1J', 'conf-002', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'),
        ('WZ1J', 'conf-003', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'),
        ('WZ1J', 'conf-004', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'),
        ('WZ1J', 'conf-005', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'),
        ('WZ1J', 'conf-006', 'TIRE PRESSURE MONITOR', 'ALL', 'null', 'XX4EMC', 'TIRES', 'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-001', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-002', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-003', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-004', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-005', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-006', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'ALL', 'null', 'XX4EMC', 'TIRES',
            'X10_WHEELS_&_TIRES', 'S'), (
            'WZ1J', 'conf-001', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-002', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-003', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-004', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-005', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-006', 'TIRE SIZE', 'null', 'null', 'XQ5保安防災', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'),
        ('WZ1J', 'conf-001', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-002', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-003', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-004', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-005', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-006', 'TIRE TYPE', 'null', 'null', 'null', 'TIRES', 'X10_WHEELS_&_TIRES', '-'),
        ('WZ1J', 'conf-001', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', 'Touch Sensor  (I-key)', 'w,w/o', 'null', 'XX4BCM', 'ACCESS', 'X08_EXTERIOR', 'w'), (
            'WZ1J', 'conf-001', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'TOWING CAPACITY', '最大仕様', 'null', 'XQE電動車,XR2車体信頼', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'TRACTION CONTROL SYSTEM', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-002', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-003', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-004', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-005', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), (
            'WZ1J', 'conf-006', 'TRAFFIC SIGN RECOGNITION', 'ALL', 'null', 'XX4EMC', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY',
            'S'), ('WZ1J', 'conf-001', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
                   'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-002', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-003', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-004', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-005', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-006', 'TRAFFIC SIGN RECOGNITION (TSR)', 'null', 'null', 'XQ3AD', 'ADAS SAFETY',
            'X11_SAFETY_SECURITY', 'w'), (
            'WZ1J', 'conf-001', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', 'TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION', 'ALL', 'null', 'XX4EMC',
            'ADAS SAFETY', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'TRUNK', 'POWER OPEN/CLOSE', 'null', 'XX4PTL', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'TSA', 'w', 'null', 'XQ2VDC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-002', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-003', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-004', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-005', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-006', 'TURN SIGNAL', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'S'),
        ('WZ1J', 'conf-001', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-002', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-003', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-004', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-005', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'),
        ('WZ1J', 'conf-006', 'TURN SIGNAL LAMP', 'ALL', 'null', 'XX4EMC', 'LIGHTING', 'X01_VISIBILITY', 'w'), (
            'WZ1J', 'conf-001', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-002', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-003', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-004', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-005', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'), (
            'WZ1J', 'conf-006', 'TYPE OF COMBI METER', 'ALL,FULL TFT', 'null', 'XX4EMC,XR6シートベルト', 'COMBI METER',
            'X02_COCKPIT', 'FULL TFT'),
        ('WZ1J', 'conf-001', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'TYPE OF CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        (
            'WZ1J', 'conf-002', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        (
            'WZ1J', 'conf-003', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        (
            'WZ1J', 'conf-004', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        (
            'WZ1J', 'conf-005', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        (
            'WZ1J', 'conf-006', 'TYPE OF DOOR-OPENER REMOT', 'ALL', 'null', 'XX4EMC', 'WINDOW OPENING', 'X02_COCKPIT',
            '-'),
        ('WZ1J', 'conf-001', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-002', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-003', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-004', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S1'),
        ('WZ1J', 'conf-005', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'),
        ('WZ1J', 'conf-006', 'TYPE OF DRIVER SEAT ADJUS', 'ALL', 'null', 'XX4EMC', 'DRIVER SEAT', 'X03_SEAT', 'S2'), (
            'WZ1J', 'conf-001', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-002', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-003', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-004', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-005', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'), (
            'WZ1J', 'conf-006', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS', 'S'),
        ('WZ1J', 'conf-001', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'),
        ('WZ1J', 'conf-002', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'),
        ('WZ1J', 'conf-003', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'),
        ('WZ1J', 'conf-004', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'),
        ('WZ1J', 'conf-005', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'),
        ('WZ1J', 'conf-006', 'TYPE OF PARK BRAKE', 'ALL', 'null', 'XX4EMC', 'PARKING BRAKE', 'X02_COCKPIT', 'EPKB'), (
            'WZ1J', 'conf-001', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-002', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-003', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-004', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-005', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-006', 'TYPE OF TIRES FR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-001', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-002', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-003', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-004', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-005', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '235 ✚ 55 ✚ R19'), (
            'WZ1J', 'conf-006', 'TYPE OF TIRES RR', 'ALL', 'null', 'XR2車体信頼', 'TIRES', 'X10_WHEELS_&_TIRES',
            '255 ✚ 40 ✚ R21'), (
            'WZ1J', 'conf-001', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-002', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-003', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-004', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-005', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'), (
            'WZ1J', 'conf-006', 'TYPES OF RADIOS', 'DA,NAVI,GAS NAVI,ALL', 'null', 'XX4CANGateway,XX4EMC',
            'AUDIO & NAVIGATION', 'X07_AUDIO_NAVIGATION_CCS', 'GAS NAVI'),
        ('WZ1J', 'conf-001', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'),
        ('WZ1J', 'conf-002', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'),
        ('WZ1J', 'conf-003', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'),
        ('WZ1J', 'conf-004', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'),
        ('WZ1J', 'conf-005', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'),
        ('WZ1J', 'conf-006', 'UNIVERSAL GARAGE DOOR OPE', 'ALL', 'null', 'XX4EMC', 'OTHER', 'X12_OTHER', 'w'), (
            'WZ1J', 'conf-001', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-002', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-003', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-004', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-005', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-006', 'UNIVERSAL GARAGE DOOR OPENER', 'w,w/o', 'null', 'XX4GN1ラジオノイズ', 'OTHER', 'X12_OTHER',
            'w'),
        (
            'WZ1J', 'conf-001', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'), (
            'WZ1J', 'conf-002', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'), (
            'WZ1J', 'conf-003', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'), (
            'WZ1J', 'conf-004', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'), (
            'WZ1J', 'conf-005', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'), (
            'WZ1J', 'conf-006', 'USB AND POWER SUPPLY', 'w_1500W,wo_1500W', 'null', 'XX4NH電動車BATTERY HEATING',
            'AMENITY',
            'X05_AMENITY', '-'),
        ('WZ1J', 'conf-001', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-002', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-003', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-004', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-005', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-006', 'USB AND POWER SUPPLY 2ND ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S'),
        ('WZ1J', 'conf-001', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-002', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-003', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-004', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-005', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-006', 'USB AND POWER SUPPLY 3RD ROW', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-001', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S1'),
        ('WZ1J', 'conf-002', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S1'),
        ('WZ1J', 'conf-003', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S2'),
        ('WZ1J', 'conf-004', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S1'),
        ('WZ1J', 'conf-005', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S1'),
        ('WZ1J', 'conf-006', 'USB AND POWER SUPPLY FR', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'S1'),
        ('WZ1J', 'conf-001', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-002', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-003', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-004', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-005', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-006', 'USB AND POWER SUPPLY LUGGAGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', '-'),
        ('WZ1J', 'conf-001', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-002', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-003', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-004', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-005', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-006', 'VDC', 'ALL', 'null', 'XX4EMC', 'BRAKING', 'X09_MECHANISM', 'S'),
        ('WZ1J', 'conf-001', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-002', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-003', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-004', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-005', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'),
        ('WZ1J', 'conf-006', 'VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)', 'null', 'null', 'XQ4機構', 'BRAKING', 'X09_MECHANISM', 'w'), (
            'WZ1J', 'conf-001', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'VEHICLE DYNAMICS CONTROL', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-002', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-003', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-004', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-005', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-006', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'w', 'null', 'XP4充電', 'CHARGER', 'X14_EV_PHEV_HEV',
            'w'),
        (
            'WZ1J', 'conf-001', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-002', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-003', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w'), (
            'WZ1J', 'conf-004', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-005', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w/o'), (
            'WZ1J', 'conf-006', 'Ventilated(Heater&Cooler) Seat', 'w,w/o', 'null', 'XR6乗員判別', 'DRIVER SEAT',
            'X03_SEAT',
            'w'), (
            'WZ1J', 'conf-001', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-002', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-003', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-004', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-005', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), (
            'WZ1J', 'conf-006', 'VIDEO SCREENS', 'ALL', 'null', 'XX4EMC', 'AUDIO & NAVIGATION',
            'X07_AUDIO_NAVIGATION_CCS',
            '-'), ('WZ1J', 'conf-001', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-002', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-003', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S3'),
        ('WZ1J', 'conf-004', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-005', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S1'),
        ('WZ1J', 'conf-006', 'VOICE VEHICLE CONTROL', 'ALL', 'null', 'XX4EMC', 'HMI', 'X02_COCKPIT', 'S2'),
        ('WZ1J', 'conf-001', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', 'VR', 'w,w/o', 'VOICE RECOGNITION ', 'XX4BCM', 'STEERING', 'X02_COCKPIT', 'w'), (
            'WZ1J', 'conf-001', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', 'WELCOME & GOODBYE SEQUENCE', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-002', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-003', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-004', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-005', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-006', 'Wheel Cover', 'with & 全種類', 'null', 'XR2シャシー', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-001', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-002', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-003', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-004', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-005', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-006', 'WHEEL COVERS-size', 'ALL', 'null', 'XR6内外装', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', '-'), (
            'WZ1J', 'conf-001', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-002', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-003', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'D'), (
            'WZ1J', 'conf-004', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-005', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-006', 'WHEEL TYPE,SIZE', 'ALL', 'null', 'XQ4実車', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'D'), (
            'WZ1J', 'conf-001', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-002', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-003', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'D'), (
            'WZ1J', 'conf-004', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-005', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'S'), (
            'WZ1J', 'conf-006', 'Wheelサイズ', 'ALL', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES',
            'D'), (
            'WZ1J', 'conf-001', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'), (
            'WZ1J', 'conf-002', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'), (
            'WZ1J', 'conf-003', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'), (
            'WZ1J', 'conf-004', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'), (
            'WZ1J', 'conf-005', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'), (
            'WZ1J', 'conf-006', 'Wheel材質', 'AL Wheel,Steel Wheel', 'null', 'XR2シャシー,XQ4車体', 'WHEELS & WHEEL COVERS',
            'X10_WHEELS_&_TIRES', 'AL Wheel'),
        ('WZ1J', 'conf-001', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'WINDOWS COLOUR', ' WIPER DE-ICER', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'WINDSCREEN', ' WIPER DE-ICER,HEATING WINDSCREEN', 'null', 'XX4EMC', 'GLASSES',
            'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'WINDSCREEN HEATER', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S1'), (
            'WZ1J', 'conf-002', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S1'), (
            'WZ1J', 'conf-003', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S1'), (
            'WZ1J', 'conf-004', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S2'), (
            'WZ1J', 'conf-005', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S2'), (
            'WZ1J', 'conf-006', 'WINDSCREEN WIPERS\nフロントワイパー', 'null', 'null', 'XR6視界', 'GLASSES', 'X01_VISIBILITY',
            'S2'),
        ('WZ1J', 'conf-001', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-002', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-003', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S1'),
        ('WZ1J', 'conf-004', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'),
        ('WZ1J', 'conf-005', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'),
        ('WZ1J', 'conf-006', 'WINDSCREEN WIPERS', 'ALL', 'null', 'XX4EMC', 'GLASSES', 'X01_VISIBILITY', 'S2'),
        ('WZ1J', 'conf-001', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'WIPER DEICER', 'Ｗ', 'null', 'XX4WH', 'GLASSES', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-002', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-003', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-004', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-005', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'),
        ('WZ1J', 'conf-006', 'WIRELESS PHONE CHARGE', 'ALL', 'null', 'XX4EMC', 'AMENITY', 'X05_AMENITY', 'w'), (
            'WZ1J', 'conf-001', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'WITH TIMER CHARGER', 'ALL', 'null', 'XX4EMC', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
         'X04_INTERIOR_TRIM_&_STORAGE', 'S1'), (
            'WZ1J', 'conf-002', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'S2'), (
            'WZ1J', 'conf-003', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'S2'), (
            'WZ1J', 'conf-004', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'S1'), (
            'WZ1J', 'conf-005', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'S2'), (
            'WZ1J', 'conf-006', 'ZONES OF AMBIENT LIGHTING', 'ALL', 'null', 'XX4EMC', 'AMBIENT LIGHTING',
            'X04_INTERIOR_TRIM_&_STORAGE', 'S2'),
        ('WZ1J', 'conf-001', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'アンダーカバー', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'ウィンドシールド取付構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'ウィンドシールド形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'ウインチ', 'null', 'winch', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'エアバッグシステム', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-001', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        (
            'WZ1J', 'conf-002', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        (
            'WZ1J', 'conf-003', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        (
            'WZ1J', 'conf-004', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        (
            'WZ1J', 'conf-005', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        (
            'WZ1J', 'conf-006', 'エネルギー\n吸収材仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'A'),
        ('WZ1J', 'conf-001', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'エンジンフード形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', 'オットマン', 'ｗ', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'キャニスタ ORVR 追加', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
                   'Shift by wire'), (
            'WZ1J', 'conf-002', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-003', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-004', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-005', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'), (
            'WZ1J', 'conf-006', 'ギアシフト', 'Shift by wire,コラムシフト', 'null', 'XX4BCM', 'GEAR SHIFT', 'X02_COCKPIT',
            'Shift by wire'),
        ('WZ1J', 'conf-001', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'グリルシャッター', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'コラムEPS', 'null', 'null', 'XQ4機構', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'コーナリングランプ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'B'),
        ('WZ1J', 'conf-004', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'サスペンション', 'ALL', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', 'B'),
        ('WZ1J', 'conf-001', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-002', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-003', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-004', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-005', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-006', 'サンルーフ', 'w', 'null', 'XD2材料', 'OPENING', 'X08_EXTERIOR', 'w/o'),
        ('WZ1J', 'conf-001', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'シル構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'シートベルトアンカ位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-001', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'), (
            'WZ1J', 'conf-002', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'), (
            'WZ1J', 'conf-003', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'), (
            'WZ1J', 'conf-004', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'), (
            'WZ1J', 'conf-005', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'), (
            'WZ1J', 'conf-006', 'シート材質', 'Cloth,Leather', 'null', 'XR3シート,XX4ALARM,XD2材料', 'TRIM', 'X03_SEAT',
            'Leather'),
        ('WZ1J', 'conf-001', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', 'シート機構', '8WP,6WM,4WP,4WM', 'null', 'XL4シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-001', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', 'スポーツシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-001', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-002', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-003', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-005', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-006', 'スライドシート', 'null', 'null', 'XR3シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'センターピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-001', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', 'トーイング', 'null', 'towing', 'XQA商品性,XQ2操安', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'), ('WZ1J', 'conf-001', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'バッテリクーラ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'バッテリヒータ', 'w', 'null', 'XP4充電', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', 'バッテリー', 'AFD,HE', 'null', 'XX4ALARM', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'バンパ仕様', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', 'フィラーチューブ', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'), (
            'WZ1J', 'conf-001', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-002', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-003', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-004', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-005', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-006', 'フューエルタンクの取り付け方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group',
            'ー'),
        ('WZ1J', 'conf-001', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', 'フューエルタンクの材質', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-001', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', 'フューエルタンク形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-001', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', 'フューエルタンク搭載位置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-001', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'フロントサイドマーカ', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'フロントサイドメンバ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'フロントピラー構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'フロントフェンダ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'フードヒンジ構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-002', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-003', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-005', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-006', 'プロパイロット', 'null', 'AD1,AD2', 'XQA商品性', 'ADAS COMFORT', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-001', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-002', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-003', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w'),
        ('WZ1J', 'conf-004', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-005', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-006', 'プロパイロットパーク', 'null', 'null', 'XQA商品性', 'ADAS PARKING', 'X11_SAFETY_SECURITY', 'w/o'),
        ('WZ1J', 'conf-001', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'ヘッドランプウオッシャー\n（HLC)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'ヘッドランプ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-001', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-002', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-003', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-004', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-005', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-006', 'マニュアルトランスミッション', 'null', 'null', 'XQA商品性', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        (
            'WZ1J', 'conf-001', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-002', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-003', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-004', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-005', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        (
            'WZ1J', 'conf-006', 'リアアンダーミラー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'),
        ('WZ1J', 'conf-001', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
         '-'), (
            'WZ1J', 'conf-002', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-003', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-004', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-005', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'), (
            'WZ1J', 'conf-006', 'リアカメラウオッシャー', 'null', 'null', 'XR6視界', 'REAR VIEW MIRROR / CAMERA', 'X01_VISIBILITY',
            '-'), ('WZ1J', 'conf-001', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
                   'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-002', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-003', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-004', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-005', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-006', 'リア・サイド・メンバー / リア・サイド・フレームの形状', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', 'リヤサイドマーカー', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'ルーフサイド構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'), (
            'WZ1J', 'conf-001', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', 'ワイパーデアイサー', 'null', 'ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる', 'XR6視界', 'GLASSES',
            'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', 'ワイパ外形', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-002', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-003', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-004', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-005', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-006', '三相(AC3)', 'AC3', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', '-'),
        ('WZ1J', 'conf-001', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', '乗員H.P.', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', '内装違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', '冷却仕様', 'ALL', 'null', 'XR5冷熱', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-002', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-003', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-004', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-005', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-006', '前席ELR仕様', 'LLA,LLD,PSB', 'Emergency Locking Retractorチャイルドシート用', 'XR6シートベルト',
            'SEAT BELT', 'X11_SAFETY_SECURITY', '-'), (
            'WZ1J', 'conf-001', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'), (
            'WZ1J', 'conf-002', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'), (
            'WZ1J', 'conf-003', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'), (
            'WZ1J', 'conf-004', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'), (
            'WZ1J', 'conf-005', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'), (
            'WZ1J', 'conf-006', '助手席SEN仕様', '歪み式,静電容量式,簡易マット式', 'null', 'XR6シートベルト', 'ASSIST SEAT',
            'X03_SEAT', '-'),
        ('WZ1J', 'conf-001', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'),
        ('WZ1J', 'conf-002', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'),
        ('WZ1J', 'conf-003', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'),
        ('WZ1J', 'conf-004', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'),
        ('WZ1J', 'conf-005', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'),
        ('WZ1J', 'conf-006', '単相(AC1)', 'AC1', 'null', 'XX4HF-VR-ETC', 'CHARGER', 'X14_EV_PHEV_HEV', 'AC1'), (
            'WZ1J', 'conf-001', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-002', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-003', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'Coutesy lamp'), (
            'WZ1J', 'conf-004', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-005', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'w/o'), (
            'WZ1J', 'conf-006', '外装イルミランプ', 'Coutesy lamp,Puddle lamp,w/o', 'ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす',
            'XX4BCM', 'LIGHTING', 'X01_VISIBILITY', 'Coutesy lamp'), (
            'WZ1J', 'conf-001', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', '外装違い\nナロー/ワイド、2/3ROW', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', '姿勢違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device', 'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-001', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', '強電BAT MD/Cell違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-001', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-002', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-003', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-004', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-005', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'), (
            'WZ1J', 'conf-006', '強電BAT 容量違い', 'null', 'null', 'XQ5保安防災', 'UNKNOW_device',
            'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', '後席ODS仕様', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-001', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', '後席シートスライド', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-001', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-002', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-003', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-004', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-005', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'),
        ('WZ1J', 'conf-006', '後席シートリクライニング', 'with,without', 'null', 'XR6シートベルト', '2ND ROW SEAT', 'X03_SEAT', '-'), (
            'WZ1J', 'conf-001', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-002', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-003', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-004', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-005', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'), (
            'WZ1J', 'conf-006', '後席プリテン装備', 'with,without', 'null', 'XR6シートベルト', 'SEAT BELT', 'X11_SAFETY_SECURITY',
            'w'),
        ('WZ1J', 'conf-001', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-002', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-003', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-004', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-005', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-006', '後輪懸架装置', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'A'),
        ('WZ1J', 'conf-001', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-002', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-003', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-004', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-005', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-006', '油圧PS(パワステ)', 'w', 'null', 'XQ4機構,XR5冷熱', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-001', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', '燃料供給方式', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'), (
            'WZ1J', 'conf-001', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-002', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-003', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-004', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-005', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'), (
            'WZ1J', 'conf-006', '燃料系部品取り付け構造', 'null', 'null', 'XR8XTF', 'UNKNOW_device',
            'UNKNOW_device_group',
            'ー'),
        ('WZ1J', 'conf-001', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-002', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-003', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-004', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-005', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'),
        ('WZ1J', 'conf-006', '燃料配管', 'null', 'null', 'XR8XTF', 'UNKNOW_device', 'UNKNOW_device_group', 'ー'), (
            'WZ1J', 'conf-001', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-002', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-003', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-004', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-005', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-006', '直前直左鏡', 'null', 'サイドアンダーミラー', 'XR6視界', 'SIDE VIEW MIRROR / CAMERA',
            'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-001', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-002', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-003', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-004', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-005', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w/o'),
        ('WZ1J', 'conf-006', '空調シート', 'w', 'null', 'XR3シート,XL4シート', 'DRIVER SEAT', 'X03_SEAT', 'w'),
        ('WZ1J', 'conf-001', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-002', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-003', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-004', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-005', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'),
        ('WZ1J', 'conf-006', '足元ランプ（ミラー付け）', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', '-'), (
            'WZ1J', 'conf-001', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-002', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-003', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-004', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-005', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'), (
            'WZ1J', 'conf-006', '跳ね上げフード', 'with,without', 'null', 'XR6歩行者保護', 'UNKNOW_device',
            'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-001', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-002', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-003', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-004', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-005', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        ('WZ1J', 'conf-006', '車体色', '黒若しくはダーク色', 'null', 'XD2材料', 'UNKNOW_device', 'UNKNOW_device_group', '-'),
        (
            'WZ1J', 'conf-001', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'), (
            'WZ1J', 'conf-002', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'), (
            'WZ1J', 'conf-003', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'), (
            'WZ1J', 'conf-004', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'), (
            'WZ1J', 'conf-005', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'), (
            'WZ1J', 'conf-006', '通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル', 'null', 'null', 'XX4Flush', 'ACCESS',
            'X08_EXTERIOR',
            '-'),
        ('WZ1J', 'conf-001', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
         'STANDARD'), (
            'WZ1J', 'conf-002', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
            'STANDARD'), (
            'WZ1J', 'conf-003', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
            'STANDARD'), (
            'WZ1J', 'conf-004', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
            'STANDARD'), (
            'WZ1J', 'conf-005', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
            'STANDARD'), (
            'WZ1J', 'conf-006', '金属製フットレスト', 'null', 'null', 'XR2コントロール', 'PEDALS AND FOOT-REST', 'X02_COCKPIT',
            'STANDARD'),
        ('WZ1J', 'conf-001', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-002', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-003', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-004', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-005', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-006', '電動格納式フラッシュアウトサイドハンドル付', 'null', 'null', 'XX4Flush', 'ACCESS', 'X08_EXTERIOR', 'w'),
        ('WZ1J', 'conf-001', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
         'OPT無し'), (
            'WZ1J', 'conf-002', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
            'OPT無し'), (
            'WZ1J', 'conf-003', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
            'Full OPT'), (
            'WZ1J', 'conf-004', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
            'OPT無し'), (
            'WZ1J', 'conf-005', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
            'OPT無し'),
        (
            'WZ1J', 'conf-006', '電装OPT', 'Full OPT,OPT無し', 'null', 'XX4AIO', 'UNKNOW_device', 'UNKNOW_device_group',
            '-'),
        ('WZ1J', 'conf-001', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-002', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-003', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w'),
        ('WZ1J', 'conf-004', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-005', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w/o'),
        ('WZ1J', 'conf-006', 'ＳＴＲＧ固定式パドル', 'null', 'null', 'XR2コントロール', 'STEERING', 'X02_COCKPIT', 'w')]

# Chuyển đổi list các tuple thành DataFrame tạm thời
"""
device_details_name = colD
option_detail = colC
auto = colA
group_detail = colB
device_name = sub_max
device_group = max
('WZ1J', 'conf-001', ' HIGH BEAM ASSIST (HBA)', 'null', 'null', 'XR6視界', 'LIGHTING', 'X01_VISIBILITY', 'w')
'col1', 'colE','colD','colC','colA','colB','sub_max','max','col9'
"""
#
df = pd.DataFrame(data, columns=['col1', 'colE', 'colD', 'colC', 'colA', 'colB', 'sub_max', 'max', 'col9'])
df = df[['max', 'sub_max', 'colA', 'colB', 'colC', 'colD', 'colE', 'col9']]
df_sorted = df.sort_values(by=['max', 'sub_max'])
# print(df_sorted)
#
result_tuple = [tuple(row) for row in df_sorted.to_records(index=False)]
# print(result_tuple)
# Danh sách để lưu trữ các giá trị của từng cột
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []

# Xử lý dữ liệu để điền vào các danh sách
for row in result_tuple:
    col1.extend([row[0], row[1], row[2]])
    col2.extend(['', '', row[3]])
    col3.extend(['', '', row[4]])
    col4.extend(['', '', row[5]])
    col5.extend(['', '', row[6]])
    col6.extend(['', '', row[7]])

# Tạo DataFrame từ các danh sách
result_df = pd.DataFrame({
    'col1': col1,
    'col2': col2,
    'col3': col3,
    'col4': col4,
    'col5': col5,
    'col6': col6
})

# Tách các hàng có giá trị 'null' trong cột 'col1'
null_rows = result_df[result_df['col1'] == 'null']

non_null_rows = result_df[result_df['col1'] != 'null']
# print("non_null_rows:")
# print(non_null_rows)
# Loại bỏ các hàng trùng lặp từ phần không chứa 'null'
non_null_deduplicated = non_null_rows.drop_duplicates(subset=['col1'], keep='first')
# print("non_null_deduplicated: ")
# print(non_null_deduplicated)
# Kết hợp lại hai phần này
# result_df = pd.concat([null_rows, non_null_deduplicated]).reset_index(drop=True)
result_df = pd.concat([null_rows, non_null_deduplicated])
result_df = result_df.sort_index()
result_df = result_df.replace('null', None)
print(result_df)
# result_df.to_excel(r'C:\Users\KNT21617\Downloads\newken\project\data\processed\abc.xlsx')
df_lot_optioncode = result_df.pivot(index=['col1','col2', 'col3', 'col4'], columns='col5', values='col6')
print(df_lot_optioncode)
# df_x = result_df.drop_duplicates(subset=['col1'], keep='first')
# result_df.to_excel(r'C:\Users\KNT21617\Downloads\newken\project\data\processed\abc.xlsx', index=None)
# Đặt lại chỉ số (index)
# df_lot_optioncode.to_excel(r'C:\Users\KNT21617\Downloads\newken\project\data\processed\abcdxxx.xlsx', index=None, header=None)
# df_lot_optioncode.to_excel(r'C:\Users\KNT21617\Downloads\newken\project\data\processed\abcd.xlsx')