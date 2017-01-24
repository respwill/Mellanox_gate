#Job 8:7
#Though your beginning was small, yet your latter end would greatly increase.

import sys
sys.path.append("D:\Python")
from HI_tool.schedule_check import sch_check


# try:
# creating Dataframe
EL = sch_check("Mellanox(497) Package CES v1.2.xlsm","Turnkey schedule","Main Lot#/DCC", device_column="Main Tdevice",po_column="PO#",datecode_column="Date Code", current_fg_column="Main EL FG/PV", pre_split_fg_column = "Split EL FG/PV" )
BE = sch_check("Mellanox(497) Package CES v1.2.xlsm","Normal BE schedule","Lot#/DCC", device_column="Tdevice",po_column="PO#", custInfo_column="Cust Info",tracecode_column="Trace Code(Date code in PO)", current_fg_column="FG",marking_spec_column="Spec#<MK#>")
Return_BE = sch_check("Mellanox(497) Package CES v1.2.xlsm","Return BE schedule","Lot#/DCC", device_column="Main Tdevice",po_column="PO#", custInfo_column="Cust Info", tracecode_column="Trace Code(Date code in PO)", current_fg_column="FG", marking_spec_column="Spec#<MK#>")

# import target lot# list from turnkey sheet.
EL.set_target(497, "P/D/L", "PO Qty")
EL.parser(EL.target_lots, EL.EMES_df,EL.result_df)
EL.get_info(['test_device', 'test_po', 'date_code', 'current_fg', 'pre_split_fg'])
EL.comparing('EL')

BE.set_target(497, "P/D/L", "PO Qty")
BE.parser(BE.target_lots, BE.EMES_df,BE.result_df)
BE.get_info(['test_device', 'test_po', 'cust_info', 'trace_code', 'current_fg', 'current_fg_marking'])
BE.comparing('BE')

Return_BE.set_target(497, "P/D/L", "PO Qty")
Return_BE.parser(Return_BE.target_lots, Return_BE.EMES_df,Return_BE.result_df)
Return_BE.get_info(['test_device', 'test_po', 'cust_info', 'trace_code', 'current_fg', 'current_fg_marking'])
Return_BE.comparing('Return_BE')

print("Inspection complete")

# except PermissionError:
#     input("Please close result files. Proram needs to overwrite them.")
#
# except:
#     input("Unexpected error caused, please run it in pycharm to check error")
