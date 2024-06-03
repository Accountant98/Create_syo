import pandas as pd

results_querry_region_6 = [('WZ1J', 'ROOM MIRROR', 'XX4EMC,XQ4実車', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'ROOM MIRROR / REAR VISIBILITY', 'XX4EMC,XQ4車体', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'ROOM MIRROR－SMART REAR VIEW MIRROR', 'XX4GN1ラジオノイズ', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'SMART REAR VIEW MIRROR', 'XX4WH', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'SRVM', 'XR6視界,XX4SC,XM6camera,XM6アンテナ', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'VOICE VEHICLE CONTROL', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'COMBINATION SWITCH', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'POWER STEERING', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'STEERING', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'STEERING WHEEL', 'XQ4実車', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'STEERING SWITCH', 'null', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'STEERING SWITCHES', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'USB AND POWER SUPPLY FR', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'TIRE', 'XJBVDC,XX4ALARM,XQ2操安', 'comment_1', 'DWHL2'),
                           ('WZ1J', 'TIRE SIZE', 'XQ5保安防災', 'comment_1', 'DWHL2'),
                           ('WZ1J', 'Wheelサイズ', 'XR2シャシー,XQ4車体', 'comment_1', 'DWHL2'),
                           ('WZ1J', 'WHEEL TYPE,SIZE', 'XQ4実車', 'comment_1', 'DWHL2'),
                           ('WZ1J', 'AD', 'XR6視界,XP4EVシステム', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'AD(AUTONOMOUS DRIVING)', 'XX4WH', 'comment_1', 'ACCS3'), (
                               'WZ1J', 'AUTONOMOUS DRIVING',
                               'XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT',
                               'comment_1', 'ACCS3'), ('WZ1J', 'AUTONOMOUS DRIVING SF', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'XX4EMC', 'comment_1', 'CLAS2'),
                           ('WZ1J', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'XQ3AD', 'comment_1', 'CLAS2'), (
                               'WZ1J', 'AROUND VIEW MONITOR', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera', 'comment_1',
                               'ACCS3'), ('WZ1J', 'AROUND VIEW MONITOR\n（AVM）', 'XR6視界', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'AUTO PARKING REMOTE CONTROL', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'AUTO PARKING REMOTE CONTROL ', 'XX4GN1ラジオノイズ', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'FAP（フルオートパーク）', 'UI6EV', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'OUTSIDE CAMERA', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'PARK ASSIST', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'PARKING ALERTS', 'XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'PARKING ASSIST SYSTEM', 'XQ3AD,XX4EMC', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'Full FlanK Protection(FKP)', 'XX4SONAR', 'comment_1', 'ACCS3'),
                           ('WZ1J', 'プロパイロットパーク', 'XQA商品性', 'comment_1', 'ACCS3'), (
                               'WZ1J', 'DYNAMIC TURN INDICATOR', 'XX4TurnLamp', 'comment_2',
                               'FR LED ✚ RR LED ✚ 3-BLINK TURN SIGNAL ✚ LED ON SIDE MIRRORS'), (
                               'WZ1J', 'SUSPENSION TYPE', 'XQ5車両信頼性,XJBVDC', 'comment_2',
                               'A: 電制SUSP無し、B: 電制SUSPあり'), (
                               'WZ1J', '3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP', 'XX4EMC', 'comment_2',
                               'S:LED 3RD BRAKE LAMP'), ('WZ1J', 'ALS(Auto Light Sensor)', 'XX4レインセンサ', 'comment_2',
                                                         'LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'AUTO LIGHT (ALS)', 'XX4オートライト', 'comment_2',
                            'LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'Auto light', 'XX4BCM', 'comment_2',
                            'S：LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'Brake lamp', 'XX4BCM', 'comment_2', 'S:LED REAR LAMP ✚ LED BRAKE LAMP'),
                           ('WZ1J', 'DAYTIME RUNNING LIGHTS', 'XX4EMC,XX4WH', 'comment_2', 'LED DRL'), (
                               'WZ1J', 'FRONT LIGHT', 'XX4EMC', 'comment_2',
                               'S：LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'FRONT LIGHT\nヘッドランプ', 'XR6視界', 'comment_2',
                            'S：LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'FRONT LIGHT/HEAD LAMP', 'XX4WH', 'comment_2',
                            'S：LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'GROUND ILLUMINATION', 'XX4EMC', 'comment_2', 'GROUND ILLUMINATION'), (
                               'WZ1J', 'LED HEADLAMP', 'XX4GN1ラジオノイズ', 'comment_2',
                               'S：LED LB ✚ LED HB ✚ AUTO LIGHT (ALS) ✚ LED SIGNATURE ✚ DELAY TIMER ✚ HIGH BEAM ASSIST (HBA)'),
                           ('WZ1J', 'LED REAR LAMP ', 'XX4GN1ラジオノイズ', 'comment_2', 'S:LED REAR LAMP ✚ LED BRAKE LAMP'),
                           ('WZ1J', 'REAR LIGHT', 'XX4EMC', 'comment_2', 'S:LED REAR LAMP ✚ LED BRAKE LAMP'), (
                               'WZ1J', 'REAR LIGHT\nリアライト\nリアコンビランプ', 'XR6視界', 'comment_2',
                               'S:LED REAR LAMP ✚ LED BRAKE LAMP'), ('WZ1J', 'TURN SIGNAL', 'XX4EMC', 'comment_2',
                                                                     'S:FR LED ✚ RR LED ✚ 3-BLINK TURN SIGNAL ✚ LED ON SIDE MIRRORS'),
                           ('WZ1J', '外装イルミランプ', 'XX4BCM', 'comment_2', 'GROUND ILLUMINATION'),
                           ('WZ1J', '足元ランプ（ミラー付け）', 'XR6視界', 'comment_2', 'GROUND ILLUMINATIONは該当しない？'), (
                               'WZ1J', 'FRONT WINDSCREEN WIPER SP', 'XX4EMC', 'comment_2',
                               'S1:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE'), (
                               'WZ1J', 'RAIN SENSITIVE', 'XX4オートライト,レインセンサ', 'comment_2',
                               'S1:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE'),
                           ('WZ1J', 'REAR WIPERS\nリアワイパー', 'XR6視界', 'comment_2', 'なし？'), (
                               'WZ1J', 'WINDSCREEN WIPERS', 'XX4EMC', 'comment_2',
                               'S1:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE'), (
                               'WZ1J', 'WINDSCREEN WIPERS\nフロントワイパー', 'XR6視界', 'comment_2',
                               'S1:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE'), (
                               'WZ1J', 'EXTERIOR REAR VIEW MIRROR', 'XX4EMC', 'comment_2',
                               'S1:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED'), (
                               'WZ1J', 'OUTSIDE MIRROR', 'XX4EMC,XX4スイッチ', 'comment_2',
                               'S1:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED'), (
                               'WZ1J', 'OUTSIDE MIRROR ADJUST', 'XX4EMC', 'comment_2',
                               'S1:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED'), (
                               'WZ1J', 'OUTSIDE MIRROR\nアウトサイドミラー', 'XR6視界', 'comment_2',
                               'S1:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED'), (
                               'WZ1J', 'OUTSIDE MIRROR MEMORY', 'XX4PMU', 'comment_2',
                               'S1:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED'),
                           ('WZ1J', 'ROOM MIRROR', 'XX4EMC,XQ4実車', 'comment_2', 'S1:AUTO DIMMING'),
                           ('WZ1J', 'ROOM MIRROR / REAR VISIBILITY', 'XX4EMC,XQ4車体', 'comment_2', 'S1:AUTO DIMMING'),
                           ('WZ1J', 'ROOM MIRROR－AUTO DIMMING', 'XX4GN1ラジオノイズ', 'comment_2', 'AUTO DIMMING'),
                           ('WZ1J', 'COMBI METER', 'XX4CANGateway', 'comment_2', 'FULL TFT'),
                           ('WZ1J', 'METER UNIT', 'XX4EMC', 'comment_2', 'FULL TFT'), (
                               'WZ1J', 'SETTINGS OF COMBI METER', 'XX4EMC,XR6シートベルト', 'comment_2',
                               'S1:CONTROL OF BRIGHTNESS'), (
                               'WZ1J', 'SIZE OF COMBI METER SCREEN', 'XX4EMC,XM6メータ,XR6シートベルト', 'comment_2',
                               '14.3" DISPLAY'), ('WZ1J', 'SPEED METER UNIT', 'XX4EMC', 'comment_2', 'FULL TFT'),
                           ('WZ1J', 'TYPE OF COMBI METER', 'XX4EMC,XR6シートベルト', 'comment_2', 'FULL TFT'),
                           ('WZ1J', 'IN-CAR COMMUNICATION', 'XX4EMC', 'comment_2', 'VISUAL COMMUNICATION'),
                           ('WZ1J', 'VOICE VEHICLE CONTROL', 'XX4EMC', 'comment_2', 'S1:BASIC '),
                           ('WZ1J', 'ENGINE START / POWER ON', 'XX4EMC', 'comment_2', 'PUSH START ENGINE / POWER ON'),
                           ('WZ1J', 'ENGINE START TYPE', 'XX7USM,XX4EMC', 'comment_2', 'PUSH START ENGINE / POWER ON'),
                           ('WZ1J', 'COMBINATION SWITCH', 'XX4EMC', 'comment_2',
                            'S1:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD1 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'PADDLE Shift', 'XX4BCM', 'comment_2', 'PADDLE SHIFT LEVER'),
                           ('WZ1J', 'POWER STEERING', 'XX4EMC', 'comment_2', 'S1:POWER STEERING'),
                           ('WZ1J', 'STEERING', 'XX4EMC', 'comment_2', 'S1:POWER STEERING'),
                           ('WZ1J', 'STEERING WHEEL', 'XQ4実車', 'comment_2', 'S1:POWER STEERING'), (
                               'WZ1J', 'STEERING SWITCH', 'null', 'comment_2',
                               'S1:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD1 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'STEERING SWITCHES', 'XX4EMC', 'comment_2',
                            'S1:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD1 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'STEERING WHEEL ADJUSTMENT', 'XX4EMC,XQ4車体', 'comment_2',
                            'S1:MANUAL TILT / HEIGHT ADJUSTMENT ✚ MANUAL TELESCOPIC / IN-DEPTH ADJUSTMENT'),
                           ('WZ1J', 'ＳＴＲＧ固定式パドル', 'XR2コントロール', 'comment_2', 'PADDLE SHIFT LEVER'), (
                               'WZ1J', 'FRONT DOOR WINDOW OPENING', 'XX4EMC', 'comment_2',
                               'S:POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER & ASSIST ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'),
                           ('WZ1J', 'FRONT DOOR WINDOW OPENING2', 'XX4スイッチ', 'comment_2',
                            'S:POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER & ASSIST ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL'),
                           ('WZ1J', 'REAR DOOR WINDOW OPENING', 'XX4EMC', 'comment_2',
                            'S:POWERED REAR WINDOW LIFT ✚ REAR ONE TOUCH ✚ AUTO REVERSE ✚ TIMER'), (
                               'WZ1J', 'REAR DOOR WINDOW OPENING2', 'XX4スイッチ', 'comment_2',
                               'S:POWERED REAR WINDOW LIFT ✚ REAR ONE TOUCH ✚ AUTO REVERSE ✚ TIMER'), (
                               'WZ1J', 'SUN VISOR LED LIGHT', 'XR6内外装', 'comment_2',
                               'S:MIRROR + TICKET HOLDER ✚ LED LIGHT ✚ EXTENSION'),
                           ('WZ1J', 'DR SEAT COMFORT FEATURE', 'XX4EMC', 'comment_2', 'S1:POWER 4 WAY LUMBAR'),
                           ('WZ1J', 'DR SEAT HEATER AND COOLER', 'XX4EMC', 'comment_2', 'S1:HEATED SEAT'), (
                               'WZ1J', 'DR SEAT TYPE AND ADJUSTMENT', 'XX4EMC', 'comment_2',
                               'S1:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'FRONT SEATS TYPE', 'XX4EMC,XR2車体信頼', 'comment_2',
                               'S1:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'MASSAGE STANDARD\n(FR seat)', 'XX4SPCU', 'comment_2',
                               'MASSAGE STANDARD ✚ POWER 4 WAY LUMBAR'),
                           ('WZ1J', 'POWER SEAT', 'XX4GN1ラジオノイズ', 'comment_2',
                            'STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'SEAT HEATING', 'XX4EMC', 'comment_2', 'S1:HEATED SEAT'), (
                               'WZ1J', 'SEAT TYPE', 'XQ5保安防災', 'comment_2',
                               'STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'TYPE OF DRIVER SEAT ADJUS', 'XX4EMC', 'comment_2',
                               'S1:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'AS SEAT COMFORT FEATURE', 'XX4EMC', 'comment_2',
                               'S:POWER 4 WAY LUMBAR ✚ MASSAGE STANDARD'),
                           ('WZ1J', 'AS SEAT HEATER AND COOLER', 'XX4EMC', 'comment_2', 'S1:HEATED SEAT'), (
                               'WZ1J', 'AS SEAT TYPE AND ADJUSTMENT', 'XX4EMC', 'comment_2',
                               'S1:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'FRONT PASSENGER SEAT(S)', 'XX4EMC', 'comment_2',
                               'S1:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT'), (
                               'WZ1J', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT', 'XR6乗員判別',
                               'comment_2', 'OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT'),
                           ('WZ1J', '2nd row armrest', 'XD2材料', 'comment_2', 'CENTER ARMREST'),
                           ('WZ1J', '2ND ROW SEAT COMFORT FEATURE', 'XX4EMC', 'comment_2', 'S:CENTER ARMREST'),
                           ('WZ1J', '2ND ROW SEAT HEATER AND COOLER', 'XX4EMC', 'comment_2', 'S:HEATED SEAT'), (
                               'WZ1J', '2ND ROW SEAT TYPE AND ADJUSTMENT', 'XX4EMC', 'comment_2',
                               'S:BENCH FIXED / NO ADJUSTMENT ✚ MANUAL 40:60 & RECLINING ✚ SINGLE FOLDING'), (
                               'WZ1J', 'REAR SEAT', 'XR2車体信頼', 'comment_2',
                               'S:BENCH FIXED / NO ADJUSTMENT ✚ MANUAL 40:60 & RECLINING ✚ SINGLE FOLDING'),
                           ('WZ1J', 'Rr 空調シート(Heater ＋ Cooler Seat)', 'XR5空調', 'comment_2', 'S:HEATED SEAT'), (
                               'WZ1J', 'ZONES OF AMBIENT LIGHTING', 'XX4EMC', 'comment_2',
                               'S1:WHITE COLOR ILLUMINATION ✚ ILLUMINATION CONTROL'), (
                               'WZ1J', 'USB AND POWER SUPPLY 2ND ROW', 'XX4EMC', 'comment_2',
                               'S:TYPE C FOR POWER CHARGE *2'),
                           ('WZ1J', 'USB AND POWER SUPPLY FR', 'XX4EMC', 'comment_2',
                            'S1:12V SOCKET *1 ✚ TYPE C FOR DATA & CHARGE *2 ✚ WIRELESS CHARGE FOR SMARTPHONE *2'),
                           ('WZ1J', 'AIR CONDITIONING AND HEATING TYPE', 'XX4NH電動車,XX4EMC,XX4WH', 'comment_2',
                            'S:DUAL ZONE AUTO A/C'), (
                               'WZ1J', 'AIR CONDITIONING AND HEATING SYSTEM', 'XX4EMC,XQE電動車', 'comment_2',
                               'S:DUAL ZONE AUTO A/C'),
                           ('WZ1J', 'AIR CONTIONING AND HEATIN', 'XX4EMC', 'comment_2', 'S:DUAL ZONE AUTO A/C'),
                           ('WZ1J', 'HEATER FOR EV', 'XX4NH電動車', 'comment_2', 'PTC HEATER ✚ HEAT PUMP'), (
                               'WZ1J', 'HEATER FOR EV / ADDITIONAL HEATER', 'XX4EMC', 'comment_2',
                               'S:PTC HEATER ✚ HEAT PUMP'),
                           ('WZ1J', 'PTC Heater', 'XX4BCM', 'comment_2', 'PTC HEATER ✚ HEAT PUMP'),
                           ('WZ1J', 'HEAT PUMP', 'XR5空調', 'comment_2', 'PTC HEATER ✚ HEAT PUMP'),
                           ('WZ1J', 'AIR TREATMENT', 'XX4EMC', 'comment_2', 'S:POLLEN/PARTICLE FILTER'),
                           ('WZ1J', 'ANTENNA', 'XM6アンテナ', 'comment_2', 'SHARK FIN'), (
                               'WZ1J', 'AUDIO', 'XM6音質,XX4AD', 'comment_2',
                               'S:AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'), (
                               'WZ1J', 'AUDIO & NAVIGATION', 'XX4WH', 'comment_2',
                               'S:AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'), (
                               'WZ1J', 'AUDIO & NAVIGATION / TYPES OF RADIOS', 'XM6アンテナ', 'comment_2',
                               'S:AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'),
                           ('WZ1J', 'CCS2', 'XM6E2E', 'comment_2', 'AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'),
                           ('WZ1J', 'SHARK FIN ANTENNA', 'XX4GN1ラジオノイズ', 'comment_2', 'SHARK FIN'), (
                               'WZ1J', 'TYPE OF HEAD UNIT HARDWARE & CCS SF', 'XX4EMC', 'comment_2',
                               'S:AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'), (
                               'WZ1J', 'HEAD UNIT', 'XM6アンテナ', 'comment_2',
                               'S:AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'), (
                               'WZ1J', 'TYPES OF RADIOS', 'XX4CANGateway,XX4EMC', 'comment_2',
                               'AIVI2 EVO GAS NAVI 14.3”\u200b ✚ CCS2 EVO 5G'),
                           ('WZ1J', 'SPEAKER', 'XM6音質', 'comment_2', 'S:CLASSIC / STANDARD SOUND ✚ 7 SPEAKERS'),
                           ('WZ1J', 'sound bubble', 'XM6音質', 'comment_2', 'STANDARD'),
                           ('WZ1J', 'ANC (ACTIVE NOISE CANCELLATION)', 'XX4EMC', 'comment_2', 'S:ANC - ROAD'),
                           ('WZ1J', 'ANC', 'XQ4実車', 'comment_2', 'S:ANC - ROAD'), (
                               'WZ1J', 'Central door locking', 'XX4スイッチ', 'comment_2',
                               'S:CENTRAL DOOR LOCKING ✚ SPEED SENSING LOCK = AUTO LOCK WITH SPEED ✚ REAR DOOR CHILD LOCK (MANUAL/MECHANICAL)'),
                           ('WZ1J', 'DOOR SAFETY', 'XX4EMC', 'comment_2',
                            'S:CENTRAL DOOR LOCKING ✚ SPEED SENSING LOCK = AUTO LOCK WITH SPEED ✚ REAR DOOR CHILD LOCK (MANUAL/MECHANICAL)'),
                           ('WZ1J', 'FLUSH DOOR HANDLE', 'XX4メカトロS45', 'comment_2',
                            'New : MANUAL PUSH BUTTON FOR LOCK/UNLOCK ON DRIVER DOOR ONLY   \nDeleted : TOUCH SENSOR FOR LOCK/UNLOCK ON 2 FRONT DOORS   \nNot modified : FLUSH DOOR HANDLE ✚ E-LATCH ✚ EXTERNAL TAILGATE / TRUNK ELECTRIC OPENER'),
                           ('WZ1J', 'Flush handle', 'XX4BCM', 'comment_2',
                            'New : MANUAL PUSH BUTTON FOR LOCK/UNLOCK ON DRIVER DOOR ONLY   \nDeleted : TOUCH SENSOR FOR LOCK/UNLOCK ON 2 FRONT DOORS   \nNot modified : FLUSH DOOR HANDLE ✚ E-LATCH ✚ EXTERNAL TAILGATE / TRUNK ELECTRIC OPENER'),
                           ('WZ1J', 'I-KEY ', 'XX4EMC', 'comment_2',
                            'S:2 I-KEYS STANDARD FINISH ✚ APPROACH UNLOCK ALL DIRECTION ✚ WALK AWAY LOCK ✚ PANIC ALARM'),
                           ('WZ1J', 'I-KEY (BADGE)', 'XX4EMC', 'comment_2',
                            'S:2 I-KEYS STANDARD FINISH ✚ APPROACH UNLOCK ALL DIRECTION ✚ WALK AWAY LOCK ✚ PANIC ALARM'),
                           ('WZ1J', 'Panic Alarm', 'XX4BCM', 'comment_2',
                            '2 I-KEYS STANDARD FINISH ✚ APPROACH UNLOCK ALL DIRECTION ✚ WALK AWAY LOCK ✚ PANIC ALARM'),
                           ('WZ1J', 'SAFETY ACCESS FUNCTIONS', 'XX4EMC', 'comment_2',
                            'S:CENTRAL DOOR LOCKING ✚ SPEED SENSING LOCK = AUTO LOCK WITH SPEED ✚ REAR DOOR CHILD LOCK (MANUAL/MECHANICAL)'),
                           ('WZ1J', 'Speed sensing lock', 'XX4BCM', 'comment_2',
                            'CENTRAL DOOR LOCKING ✚ SPEED SENSING LOCK = AUTO LOCK WITH SPEED ✚ REAR DOOR CHILD LOCK (MANUAL/MECHANICAL)'),
                           ('WZ1J', 'Touch Sensor  (I-key)', 'XX4BCM', 'comment_2',
                            '2 I-KEYS STANDARD FINISH ✚ APPROACH UNLOCK ALL DIRECTION ✚ WALK AWAY LOCK ✚ PANIC ALARM'),
                           ('WZ1J', '電動格納式フラッシュアウトサイドハンドル付', 'XX4Flush', 'comment_2',
                            'New : MANUAL PUSH BUTTON FOR LOCK/UNLOCK ON DRIVER DOOR ONLY   \nDeleted : TOUCH SENSOR FOR LOCK/UNLOCK ON 2 FRONT DOORS   \nNot modified : FLUSH DOOR HANDLE ✚ E-LATCH ✚ EXTERNAL TAILGATE / TRUNK ELECTRIC OPENER'),
                           ('WZ1J', 'HAND FREE', 'XX4KickSensor', 'comment_2',
                            'POWER OPEN/CLOSE ✚ HANDS FREE ✚ AUTO CLOSER'), (
                               'WZ1J', 'Kick Sensor', 'XX4BCM', 'comment_2',
                               'POWER OPEN/CLOSE ✚ HANDS FREE ✚ AUTO CLOSER'),
                           ('WZ1J', 'PBD', 'XX4BCM', 'comment_2', 'POWER OPEN/CLOSE ✚ AUTO CLOSER'), (
                               'WZ1J', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE', 'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
                               'comment_2',
                               'POWER OPEN/CLOSE ✚ AUTO CLOSER'), (
                               'WZ1J', 'TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE',
                               'XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ',
                               'comment_2', 'POWER OPEN/CLOSE ✚ HANDS FREE ✚ AUTO CLOSER'), (
                               'WZ1J', 'Power Back Door(PBD)', 'XX4メカトロS46', 'comment_2',
                               'POWER OPEN/CLOSE ✚ AUTO CLOSER'),
                           ('WZ1J', 'REAR DOOR OPENING', 'XX4EMC', 'comment_2', 'S1:POWER OPEN/CLOSE ✚ AUTO CLOSER'),
                           ('WZ1J', 'REAR GATE OPENING', 'XX4EMC', 'comment_2', 'S1:POWER OPEN/CLOSE ✚ AUTO CLOSER'),
                           ('WZ1J', 'ROOF', 'XQ4実車', 'comment_2', 'S:FIXED ✚ PANORAMIC'),
                           ('WZ1J', 'ROOF OPENING', 'XR2車体信頼', 'comment_2', 'S:FIXED ✚ PANORAMIC'),
                           ('WZ1J', 'Sunshade', 'XX4BCM', 'comment_2', 'FIXED ✚ PANORAMIC'), (
                               'WZ1J', 'TAILGATE/TRUNK OPENING', 'XX4EMC', 'comment_2',
                               'S1:POWER OPEN/CLOSE ✚ AUTO CLOSER'), ('WZ1J', 'Illumination BI', 'XL7外装', 'comment_2',
                                                                      'FR:BRAND EMBLEM / LOGO ✚ INFINITI ✚ ILLUMINATED LOGO'),
                           ('WZ1J', 'ANTI-LOCK BRAKING SYSTEM', 'XX4EMC', 'comment_2',
                            'S:ANTI-LOCK BRAKING SYSTEM (ABS) ✚ HILL START ASSIST (HSA) ✚ VEHICLE DYNAMICS CONTROL (VDC)'),
                           ('WZ1J', 'BRAKING ASSISTANCE', 'XX4EMC', 'comment_2', 'S:EMERGENCY BRAKE ASSIST (EBA / BA)'),
                           ('WZ1J', 'EMERGENCY BRAKE ASSIST (EBA / BA)', 'XX4EMC', 'comment_2',
                            'S:EMERGENCY BRAKE ASSIST (EBA / BA)'), ('WZ1J', 'VDC', 'XX4EMC', 'comment_2',
                                                                     'S:ANTI-LOCK BRAKING SYSTEM (ABS) ✚ HILL START ASSIST (HSA) ✚ VEHICLE DYNAMICS CONTROL (VDC)'),
                           ('WZ1J', 'Driving mode', 'XX4BCM', 'comment_2', 'NEUTRAL / ECO / SPORT / CUSTOM'),
                           ('WZ1J', 'DRIVING MODE 2WD', 'XX4EMC', 'comment_2', 'S:NEUTRAL / ECO / SPORT / CUSTOM'), (
                               'WZ1J', 'DRIVING MODE 4WD', 'XX4EMC', 'comment_2',
                               'S:NEUTRAL / ECO / SPORT / SNOW / CUSTOM'),
                           ('WZ1J', 'DRIVING MODE CONTROL', 'XX4EMC', 'comment_2', 'S1:NEUTRAL / ECO / SPORT / CUSTOM'),
                           ('WZ1J', 'TIRE PRESSURE MONITOR', 'XX4EMC', 'comment_2',
                            'S:TIRE PRESSURE MONITORING SYSTEM (DIRECT) ✚ EASY FILL ALERT'), (
                               'WZ1J', 'TIRE PRESSURE MONITORING SYSTEM (TPMS)', 'XX4EMC', 'comment_2',
                               'S:TIRE PRESSURE MONITORING SYSTEM (DIRECT) ✚ EASY FILL ALERT'),
                           ('WZ1J', 'Wheelサイズ', 'XR2シャシー,XQ4車体', 'comment_2', 'S:19" ✚ ALLOY'),
                           ('WZ1J', 'WHEEL TYPE,SIZE', 'XQ4実車', 'comment_2', 'S:19" ✚ ALLOY'),
                           ('WZ1J', 'SPARE WHEEL', 'XR2車体信頼', 'comment_2', 'REPAIR KIT / INFLATION KIT'), (
                               'WZ1J', 'AUTONOMOUS DRIVING SF', 'XX4EMC', 'comment_2',
                               'AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK'), (
                               'WZ1J', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'XX4EMC', 'comment_2',
                               'S1:AEB ALL SPEED ✚ PEDESTRIAN + CYCLIST + POWERED 2 WHEELS ✚ REAR AEB WITH RCTA'), (
                               'WZ1J', 'AUTONOMOUS EMERGENCY STEERING', 'XX4EMC', 'comment_2',
                               'S:EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)'), (
                               'WZ1J', 'AUTONOMOUS EMERGENCY STEERING (AES)', 'XX4EMC', 'comment_2',
                               'S:EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)'), (
                               'WZ1J', 'BLIND SPOT DETECTION', 'XX4EMC', 'comment_2',
                               'S:BLIND SPOT WARNING (BSW) ✚ BLIND SPOT INTERVENTION (BSI) ✚ LANE DEPARTURE WARNING (LDW) ✚ LANE DEPARTURE PREVENTION (LDP) ✚ LANE KEEPING ASSIST (LKA) ✚ EMERGENCY LANE KEEPING ASSIST (E-LKA) ROAD EDGE + ONCOMING'),
                           ('WZ1J', 'CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)', 'XQ3AD', 'comment_2',
                            'AEB ALL SPEED ✚ PEDESTRIAN + CYCLIST + POWERED 2 WHEELS ✚ JUNCTION ASSIST ✚ REAR AEB WITH RCTA'),
                           ('WZ1J', 'DRIVE EVENT RECORDER', 'XX4EMC', 'comment_2',
                            'S:FRONT SCENE RECORDER DIGITAL ✚ REAR SCENE RECORDER DIGITAL'), (
                               'WZ1J', 'DRIVER MONITORING', 'XX4EMC', 'comment_2',
                               'S1:DRIVER MONITORING BY STEERING (UTA / WDA / DAA)'), (
                               'WZ1J', 'emergency steering assist/support (esa/ess)', 'XQ3AD', 'comment_2',
                               'EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)'), (
                               'WZ1J', 'FORWARD COLLISION WARNING', 'XX4EMC', 'comment_2',
                               'S:PREDICTIVE FORWARD COLLISION WARNING (PFCW)'), (
                               'WZ1J', 'FORWARD EMERGENCY BRAKING', 'XQ3AD,XX4EMC,XX4AD', 'comment_2',
                               'AEB ALL SPEED ✚ PEDESTRIAN + CYCLIST + POWERED 2 WHEELS ✚ REAR AEB WITH RCTA'), (
                               'WZ1J', 'FRONT COLLISION WARNING', 'XQ3AD', 'comment_2',
                               'PREDICTIVE FORWARD COLLISION WARNING (PFCW)'), (
                               'WZ1J', 'LANE KEEP', 'XQ3AD,XX4EMC', 'comment_2',
                               'S:BLIND SPOT WARNING (BSW) ✚ BLIND SPOT INTERVENTION (BSI) ✚ LANE DEPARTURE WARNING (LDW) ✚ LANE DEPARTURE PREVENTION (LDP) ✚ LANE KEEPING ASSIST (LKA) ✚ EMERGENCY LANE KEEPING ASSIST (E-LKA) ROAD EDGE + ONCOMING'),
                           ('WZ1J', 'LATERAL SUPPORT SYSTEM', 'XX4EMC', 'comment_2',
                            'S:BLIND SPOT WARNING (BSW) ✚ BLIND SPOT INTERVENTION (BSI) ✚ LANE DEPARTURE WARNING (LDW) ✚ LANE DEPARTURE PREVENTION (LDP) ✚ LANE KEEPING ASSIST (LKA) ✚ EMERGENCY LANE KEEPING ASSIST (E-LKA) ROAD EDGE + ONCOMING'),
                           ('WZ1J', 'OCCUPANT MONITORING', 'XX4EMC', 'comment_2',
                            'S:OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT'), (
                               'WZ1J', 'OCCUPANTS SAFE EXIT', 'XX4EMC', 'comment_2',
                               'S:OCCUPANT SAFE EXIT WARNING (OSE) ✚ OCCUPANT SAFE EXIT INTERVENTION (A-OSE)'), (
                               'WZ1J', 'SCENE RECORDER', 'XX4EMC', 'comment_2',
                               'S:FRONT SCENE RECORDER DIGITAL ✚ REAR SCENE RECORDER DIGITAL'), (
                               'WZ1J', 'TRAFFIC SIGN RECOGNITION', 'XX4EMC', 'comment_2',
                               'S:TRAFFIC SIGN RECOGNITION (TSR)'), (
                               'WZ1J', 'AROUND VIEW MONITOR', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera', 'comment_2',
                               'S:3D FIXED VIEW AROUND VIEW MONITOR DIGITAL (AVM)'), (
                               'WZ1J', 'AROUND VIEW MONITOR\n（AVM）', 'XR6視界', 'comment_2',
                               'S:3D FIXED VIEW AROUND VIEW MONITOR DIGITAL (AVM)'), (
                               'WZ1J', 'AUTO PARKING REMOTE CONTROL', 'XX4EMC', 'comment_2',
                               'S:FULL AUTO PARK SYSTEM (FAPK) / PRO PILOT PARKING'), (
                               'WZ1J', 'FAP（フルオートパーク）', 'UI6EV', 'comment_2',
                               'S:FULL AUTO PARK SYSTEM (FAPK) / PRO PILOT PARKING'),
                           ('WZ1J', 'OUTSIDE CAMERA', 'XX4EMC', 'comment_2', 'S1:REAR VIEW CAMERA (DIGITAL)'), (
                               'WZ1J', 'PARK ASSIST', 'XX4EMC', 'comment_2',
                               'S:FULL AUTO PARK SYSTEM (FAPK) / PRO PILOT PARKING'),
                           ('WZ1J', 'PARKING ALERTS', 'XX4EMC', 'comment_2', 'S1:FRONT & REAR PARKING AID'), (
                               'WZ1J', 'PARKING ASSIST SYSTEM', 'XQ3AD,XX4EMC', 'comment_2',
                               'FULL AUTO PARK SYSTEM (FAPK) / PRO PILOT PARKING'), (
                               'WZ1J', 'Full FlanK Protection(FKP)', 'XX4SONAR', 'comment_2',
                               'S1:FRONT & REAR PARKING AID'), ('WZ1J', 'プロパイロットパーク', 'XQA商品性', 'comment_2',
                                                                'FULL AUTO PARK SYSTEM (FAPK) / PRO PILOT PARKING'), (
                               'WZ1J', 'Alarm type', 'XX4BCM', 'comment_2',
                               'IMMOBILIZER BY TRANSPONDER ✚ SECURITY ALARM / PERIMETRIC ALARM'), (
                               'WZ1J', 'ANTI-THEFT DEVICES', 'XX7USM,XX4EMC', 'comment_2',
                               'IMMOBILIZER BY TRANSPONDER ✚ SECURITY ALARM / PERIMETRIC ALARM'), (
                               'WZ1J', 'EMERGENCY CALL AND BREAKDOWN', 'XX4EMC', 'comment_2',
                               'S:Deleted : BREAKDOWN   \nNot modified : EMERGENCY CALL (E-CALL) ✚ AUTO HAZARD AFTER COLLISION'),
                           ('WZ1J', 'LEAD CAR DEPARTURE NOTIFICATION', 'XX4EMC', 'comment_2',
                            'S:LEAD CAR DEPARTURE NOTIFICATION (LCDN)'), (
                               'WZ1J', 'LEAD CAR DEPARTURE NOTIFICATION (LCDN)', 'XX4EMC', 'comment_2',
                               'S:LEAD CAR DEPARTURE NOTIFICATION (LCDN)'), (
                               'WZ1J', 'POST COLLISION AND BREAKDOWN', 'XX4EMC', 'comment_2',
                               'S:Deleted : BREAKDOWN   \nNot modified : EMERGENCY CALL (E-CALL) ✚ AUTO HAZARD AFTER COLLISION'),
                           ('WZ1J', 'AIRBAG CANCEL', 'XX4EMC', 'comment_2', 'S:AUTOMATIC ASSIST AIRBAG DEACTIVATION'),
                           ('WZ1J', "DRIVER'S AIRBAG", 'XX4EMC', 'comment_2', 'S:DR AIRBAG ✚ AS AIRBAG'),
                           ('WZ1J', 'FAR SIDE AIRBAG', 'XX4EMC', 'comment_2', 'S:FRONT FAR SIDE AIRBAG'),
                           ('WZ1J', 'FRONT AIRBAG', 'XX4EMC', 'comment_2', 'S:DR AIRBAG ✚ AS AIRBAG'),
                           ('WZ1J', 'FRONT KNEE AIRBAGS', 'XX4EMC', 'comment_2', 'S:DRIVER + ASSIST KNEE AIRBAG'),
                           ('WZ1J', 'FRONT SIDE AIRBAG', 'XX4EMC', 'comment_2', 'S:ROW 1 + 2 CURTAIN AIRBAG'),
                           ('WZ1J', 'PASSENGER AIRBAG', 'XX4EMC', 'comment_2', 'S:DR AIRBAG ✚ AS AIRBAG'), (
                               'WZ1J', 'SIDE AIRBAG', 'XX4EMC', 'comment_2',
                               'S:DRIVER + ASSISTANT THORAX AIRBAG ✚ RR SIDE THORAX AIRBAG'),
                           ('WZ1J', 'SIDE CURTAIN AIRBAG', 'XX4EMC', 'comment_2', 'S:ROW 1 + 2 CURTAIN AIRBAG'), (
                               'WZ1J', 'FRONT SEAT BELT', 'XX4EMC,XR6シートベルト', 'comment_2',
                               'S:HEIGHT ADJUSTABLE ✚ LOAD LIMITER ✚ PRE-TENSIONER ✚ AUTOMATIC LOCKING RETRACTOR (ALR) FOR AS'),
                           ('WZ1J', 'FRONT SEAT BELT REMINDER', 'XX4EMC,XR6シートベルト', 'comment_2',
                            'S:DRIVER AND ASSIST SEAT BELT REMINDER'), (
                               'WZ1J', 'FRONT SEAT BELT PRETENSIONER', 'XX4EMC', 'comment_2',
                               'S:HEIGHT ADJUSTABLE ✚ LOAD LIMITER ✚ PRE-TENSIONER ✚ AUTOMATIC LOCKING RETRACTOR (ALR) FOR AS'),
                           ('WZ1J', 'FRONT SEAT BELT PRE-TENSIONER', 'XX4EMC', 'comment_2',
                            'S:HEIGHT ADJUSTABLE ✚ LOAD LIMITER ✚ PRE-TENSIONER ✚ AUTOMATIC LOCKING RETRACTOR (ALR) FOR AS'),
                           ('WZ1J', 'FRONT SEAT BELT ADJUSTMEN', 'XX4EMC', 'comment_2',
                            'S:HEIGHT ADJUSTABLE ✚ LOAD LIMITER ✚ PRE-TENSIONER ✚ AUTOMATIC LOCKING RETRACTOR (ALR) FOR AS'),
                           ('WZ1J', 'SEAT BELT REMINDER', 'XX4EMC', 'comment_2',
                            'S:DRIVER AND ASSIST SEAT BELT REMINDER'), (
                               'WZ1J', '2ND ROW SEAT BELT', 'XX4EMC,XR6シートベルト', 'comment_2',
                               'S:LOAD LIMITER ✚ PRE-TENSIONER ✚ REAR CENTER 3 POINTS ✚ LATERAL 3 POINTS ✚ EMERGENCY LOCKING RETRACTOR (ELR)'),
                           ('WZ1J', '2ND ROW SEAT BELT REMINDER', 'XX4EMC,XR6シートベルト', 'comment_2',
                            'S:2ND ROW SEAT BELT REMINDER'), ('WZ1J', 'REAR SEATS BELT', 'XX4EMC', 'comment_2',
                                                              'S:LOAD LIMITER ✚ PRE-TENSIONER ✚ REAR CENTER 3 POINTS ✚ LATERAL 3 POINTS ✚ EMERGENCY LOCKING RETRACTOR (ELR)'),
                           ('WZ1J', 'REAR SEAT BELT PRETENSIONER', 'XX4EMC', 'comment_2',
                            'S:LOAD LIMITER ✚ PRE-TENSIONER ✚ REAR CENTER 3 POINTS ✚ LATERAL 3 POINTS ✚ EMERGENCY LOCKING RETRACTOR (ELR)'),
                           ('WZ1J', 'ASSISTANT SEAT BELT', 'XX4EMC', 'comment_2',
                            'S:HEIGHT ADJUSTABLE ✚ LOAD LIMITER ✚ PRE-TENSIONER ✚ AUTOMATIC LOCKING RETRACTOR (ALR) FOR AS'),
                           ('WZ1J', 'UNIVERSAL GARAGE DOOR OPENER', 'XX4GN1ラジオノイズ', 'comment_2',
                            'UNIVERSAL GARAGE DOOR OPENER'),
                           ('WZ1J', 'UNIVERSAL GARAGE DOOR OPE', 'XX4EMC', 'comment_2', 'UNIVERSAL GARAGE DOOR OPENER'),
                           ('WZ1J', 'AC 120V or 240V 1500W OUTLET', 'XX4WH', 'comment_2',
                            'VEHICLE TO LOAD (V2L) OUTSIDE ✚ VEHICLE POWER CONNECTOR (VPC)'),
                           ('WZ1J', 'AC CHARGER', 'XX4EMC', 'comment_2', 'S:SINGLE PHASE POWER B'), (
                               'WZ1J', 'AC PLUG STANDARD', 'XX4EMC,XX4NH電動車', 'comment_2',
                               'MODE 2 CABLE STANDARD (10 A)'),
                           ('WZ1J', 'Battery Charger For ELEC. VEH', 'UE2燃費', 'comment_2', 'S:SINGLE PHASE POWER B'),
                           ('WZ1J', 'CHARGER', 'XX4NH電動車', 'comment_2', 'SINGLE PHASE POWER B'),
                           ('WZ1J', 'DC CHARGER', 'XX4EMC', 'comment_2', 'DC CHARGER'), (
                               'WZ1J', 'REVERSIBLE CHARGER', 'XX4NH電動車,XX4EMC', 'comment_2',
                               'S:VEHICLE TO LOAD (V2L) OUTSIDE ✚ VEHICLE POWER CONNECTOR (VPC)'), (
                               'WZ1J', 'VEHICLE TO LOAD (V2L) OUTSIDE', 'XP4充電', 'comment_2',
                               'S:VEHICLE TO LOAD (V2L) OUTSIDE ✚ VEHICLE POWER CONNECTOR (VPC)'),
                           ('WZ1J', '単相(AC1)', 'XX4HF-VR-ETC', 'comment_2', 'SINGLE PHASE POWER B'), (
                               'WZ1J', 'ONE PEDAL FUNCTION WITH STOP', 'XX4EMC', 'comment_2',
                               'S:MULTI-LEVEL REGEN BRAKING BY SHIFTER + ONE PEDAL WITH CREEPING'),
                           ('WZ1J', 'VEHICLE SOUND FOR PEDESTRIANS ', 'XX7USM', 'comment_2', 'BASIC'), (
                               'WZ1J', 'FRONT WINDSCREEN WIPER SP', 'XX4EMC', 'comment_3',
                               'S2:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE ✚ HEATED WASHER'), (
                               'WZ1J', 'RAIN SENSITIVE', 'XX4オートライト,レインセンサ', 'comment_3',
                               'S2:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE ✚ HEATED WASHER'), (
                               'WZ1J', 'WINDSCREEN WIPERS', 'XX4EMC', 'comment_3',
                               'S2:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE ✚ HEATED WASHER'), (
                               'WZ1J', 'WINDSCREEN WIPERS\nフロントワイパー', 'XR6視界', 'comment_3',
                               'S2:VARIABLE INTERMITTENT ✚ SPEED SENSITIVE ✚ RAIN SENSITIVE ✚ HEATED WASHER'), (
                               'WZ1J', 'EXTERIOR REAR VIEW MIRROR', 'XX4EMC', 'comment_3',
                               'S2:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR', 'XX4EMC,XX4スイッチ', 'comment_3',
                            'S2:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR ADJUST', 'XX4EMC', 'comment_3',
                            'S2:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR\nアウトサイドミラー', 'XR6視界', 'comment_3',
                            'S2:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR MEMORY', 'XX4PMU', 'comment_3',
                            'S2:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'ROOM MIRROR', 'XX4EMC,XQ4実車', 'comment_3',
                            'S2:SMART REAR VIEW MIRROR DIGITAL (SRVM)'), (
                               'WZ1J', 'ROOM MIRROR / REAR VISIBILITY', 'XX4EMC,XQ4車体', 'comment_3',
                               'S2:SMART REAR VIEW MIRROR DIGITAL (SRVM)'),
                           ('WZ1J', 'VOICE VEHICLE CONTROL', 'XX4EMC', 'comment_3', 'S2:BASIC + SEAT'), (
                               'WZ1J', 'COMBINATION SWITCH', 'XX4EMC', 'comment_3',
                               'S2:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD2 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'POWER STEERING', 'XX4EMC', 'comment_3', 'S2:STEER BY WIRE'),
                           ('WZ1J', 'STEERING', 'XX4EMC', 'comment_3', 'S2:STEER BY WIRE'),
                           ('WZ1J', 'STEERING WHEEL', 'XQ4実車', 'comment_3', 'S2:STEER BY WIRE'), (
                               'WZ1J', 'STEERING SWITCH', 'null', 'comment_3',
                               'S2:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD2 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'STEERING SWITCHES', 'XX4EMC', 'comment_3',
                            'S2:VOICE RECOGNITION (VR) SWITCH ✚ ADAPTIVE CRUISE CONTROL (ACC/ICC) SWITCH ✚ PHONE SWITCH ✚ AUDIO SWITCH ✚ AUTONOMOUS DRIVING SWITCH FOR AD2 ✚ SCROLLING OF COMBI METER SCREEN SWITCH ✚ SCROLLING OF CENTRAL SCREEN SWITCH ✚ CAPACITIVE TYPE WITH TOUCH PAD'),
                           ('WZ1J', 'STEERING WHEEL ADJUSTMENT', 'XX4EMC,XQ4車体', 'comment_3',
                            'S2:ELECTRIC TILT / HEIGHT ADJUSTMENT ✚ ELECTRIC TELESCOPIC / IN-DEPTH ADJUSTMENT ✚ MEMORY'),
                           ('WZ1J', 'DR SEAT COMFORT FEATURE', 'XX4EMC', 'comment_3',
                            'S2:MASSAGE STANDARD ✚ POWER 4 WAY LUMBAR'), (
                               'WZ1J', 'DR SEAT HEATER AND COOLER', 'XX4EMC', 'comment_3',
                               'S2:HEATED SEAT ✚ VENTILATED SEAT'), (
                               'WZ1J', 'DR SEAT TYPE AND ADJUSTMENT', 'XX4EMC', 'comment_3',
                               'S2:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'FRONT SEATS TYPE', 'XX4EMC,XR2車体信頼', 'comment_3',
                            'S2:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'POWER SEAT', 'XX4GN1ラジオノイズ', 'comment_3', 'HEATED SEAT'), (
                               'WZ1J', 'SEAT HEATER', 'XX4GN1ラジオノイズ,XR6乗員判別', 'comment_3',
                               'HEATED SEAT ✚ VENTILATED SEAT'),
                           ('WZ1J', 'SEAT HEATING', 'XX4EMC', 'comment_3', 'S2:HEATED SEAT ✚ VENTILATED SEAT'), (
                               'WZ1J', 'TYPE OF DRIVER SEAT ADJUS', 'XX4EMC', 'comment_3',
                               'S2:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'AS SEAT HEATER AND COOLER', 'XX4EMC', 'comment_3',
                            'S2:HEATED SEAT ✚ VENTILATED SEAT'), (
                               'WZ1J', 'AS SEAT TYPE AND ADJUSTMENT', 'XX4EMC', 'comment_3',
                               'S2:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'FRONT PASSENGER SEAT(S)', 'XX4EMC', 'comment_3',
                            'S2:STANDARD SEAT ✚ POWER 8 WAY: SLIDING & RECLINING & HEIGHT & TILT ✚ SEAT MEMORY ON DOOR'),
                           ('WZ1J', 'ZONES OF AMBIENT LIGHTING', 'XX4EMC', 'comment_3',
                            'S2:MULTI COLOR ILLUMINATION ✚ ILLUMINATION CONTROL'), (
                               'WZ1J', 'USB AND POWER SUPPLY FR', 'XX4EMC', 'comment_3',
                               'S2:12V SOCKET *1 ✚ TYPE C FOR DATA & CHARGE *2 ✚ WIRELESS CHARGE FOR SMARTPHONE *2 ✚ A/C 120V OR 240V *1'),
                           ('WZ1J', 'SPEAKER', 'XM6音質', 'comment_3', 'S2:PREMIUM SOUND ✚ 18 SPEAKERS'), (
                               'WZ1J', 'REAR DOOR OPENING', 'XX4EMC', 'comment_3',
                               'S2POWER OPEN/CLOSE ✚ HANDS FREE ✚ AUTO CLOSER'),
                           ('WZ1J', 'Illumination BI', 'XL7外装', 'comment_3', 'RR:ALPHABETICAL BRAND NAME ✚ INFINITI'),
                           ('WZ1J', 'Driving mode', 'XX4BCM', 'comment_3', 'NEUTRAL / ECO / SPORT / SNOW / CUSTOM'), (
                               'WZ1J', 'DRIVING MODE CONTROL', 'XX4EMC', 'comment_3',
                               'S2:NEUTRAL / ECO / SPORT / SNOW / CUSTOM'),
                           ('WZ1J', 'Wheelサイズ', 'XR2シャシー,XQ4車体', 'comment_3', 'D:21" ✚ ALLOY'),
                           ('WZ1J', 'WHEEL TYPE,SIZE', 'XQ4実車', 'comment_3', 'D:21" ✚ ALLOY'), (
                               'WZ1J', 'AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)', 'XX4EMC', 'comment_3',
                               'S2:AEB ALL SPEED ✚ PEDESTRIAN + CYCLIST + POWERED 2 WHEELS ✚ JUNCTION ASSIST ✚ REAR AEB WITH RCTA'),
                           ('WZ1J', 'DRIVER MONITORING', 'XX4EMC', 'comment_3',
                            'S2:DRIVER MONITORING BY STEERING (UTA / WDA / DAA) ✚ DRIVER MONITORING BY CAMERA'), (
                               'WZ1J', 'AROUND VIEW MONITOR', 'XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera', 'comment_3',
                               'D:3D VIEW ROTATION AROUND VIEW MONITOR DIGITAL (AVM)'), (
                               'WZ1J', 'AROUND VIEW MONITOR\n（AVM）', 'XR6視界', 'comment_3',
                               'D:3D VIEW ROTATION AROUND VIEW MONITOR DIGITAL (AVM)'), (
                               'WZ1J', 'OUTSIDE CAMERA', 'XX4EMC', 'comment_3',
                               'S2:3D FIXED VIEW AROUND VIEW MONITOR DIGITAL (AVM) ✚ MOVING OBJECT DETECTION (MOD)'), (
                               'WZ1J', 'PARKING ALERTS', 'XX4EMC', 'comment_3',
                               'S2:FRONT & REAR PARKING AID & FLANK PROTECTION (FKP)'), (
                               'WZ1J', 'Full FlanK Protection(FKP)', 'XX4SONAR', 'comment_3',
                               'S2:FRONT & REAR PARKING AID & FLANK PROTECTION (FKP)'),
                           ('WZ1J', '単相(AC1)', 'XX4HF-VR-ETC', 'comment_3', 'AC1 11kW'),
                           ('WZ1J', 'WINDSCREEN WIPERS\nフロントワイパー', 'XR6視界', 'comment_4', 'WASHER違い？'), (
                               'WZ1J', 'EXTERIOR REAR VIEW MIRROR', 'XX4EMC', 'comment_4',
                               'S3:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ AUTO DIMMING DRIVER & ASSIST SIDE ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR', 'XX4EMC,XX4スイッチ', 'comment_4',
                            'S3:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ AUTO DIMMING DRIVER & ASSIST SIDE ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR ADJUST', 'XX4EMC', 'comment_4',
                            'S3:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ AUTO DIMMING DRIVER & ASSIST SIDE ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR\nアウトサイドミラー', 'XR6視界', 'comment_4',
                            'S3:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ AUTO DIMMING DRIVER & ASSIST SIDE ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'OUTSIDE MIRROR MEMORY', 'XX4PMU', 'comment_4',
                            'S3:ELEC ADJUSTMENT ✚ ELEC FOLDING ✚ AUTOMATICALLY FOLDING ✚ HEATED ✚ MEMORY ✚ AUTO DIMMING DRIVER & ASSIST SIDE ✚ REVERSE DRIVER & ASSIST SIDE'),
                           ('WZ1J', 'VOICE VEHICLE CONTROL', 'XX4EMC', 'comment_4', 'S3:BASIC + SEAT+ AD'), (
                               'WZ1J', 'OUTSIDE CAMERA', 'XX4EMC', 'comment_4',
                               'S3:3D VIEW ROTATION AROUND VIEW MONITOR DIGITAL (AVM) ✚ MOVING OBJECT DETECTION (MOD)')]


def region_6(result_querry_region6):
    df_6_begin = pd.DataFrame(result_querry_region6,
                              columns=['Project', 'CADICS ID', 'gr', 'Comment_column', 'Value'])
    df_6_version2 = df_6_begin[['CADICS ID', 'gr', 'Comment_column', 'Value']]
    df_6 = df_6_version2.pivot(index=['CADICS ID', 'gr'], columns='Comment_column', values='Value')
    df_6.reset_index(inplace=True)
    return df_6


df_6 = region_6(results_querry_region_6)
df_6.to_excel('df6.xlsx')
print(df_6)
