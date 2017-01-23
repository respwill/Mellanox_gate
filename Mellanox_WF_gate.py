#Job 8:7
#Though your beginning was small, yet your latter end would greatly increase.

import sys
sys.path.append("D:\Python")
from HI_tool.schedule_check import sch_check


# creating Dataframe
EL = sch_check("Mellanox(497) Wafer CES v1.0.xlsm","Probe schedule","Bank Lot#(Job#)", dcc_column="dcc", device_column="Test device", po_column="T PO#", ship_column="선적지", current_fg_column="FG / PV" )
EL.set_target(497, "wafer", "Wfr")
EL.parser(EL.target_lots, EL.EMES_df, EL.result_df)
EL.get_info(['test_device', 'test_po', 'ship_code', 'current_fg', ])
EL.comparing("Wafer")

print("Inspection complete")
