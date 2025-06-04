#!/usr/bin/python3
#changes done according to GETT_2V1
#
####################################
import sys
from PyHT6022.LibUsbScope import Oscilloscope

def fun():
    scope = Oscilloscope()
    scope.setup()
    if not scope.open_handle():
        sys.exit( -1 )
    if (not scope.is_device_firmware_present):
        print( 'upload firmware...' )
        scope.flash_firmware()
    product = scope.get_product_string()
    if product:
        print( 'product name:', product )
    serial = scope.get_serial_number_string()
    if serial:
        print( 'serial number:', serial )
    version = scope.get_fw_version()
    if version:
        print( 'FW version:', hex( version ) )
    scope.close_handle()
