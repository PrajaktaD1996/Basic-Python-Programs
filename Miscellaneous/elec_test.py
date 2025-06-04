#script trigger to when a button is pressed
from frappe_client import client_util as c
from frappe_client.frappeclient import FrappeClient
from frappe_client import auth
from templates import Device
def detect_start_press():
    #use gpio check when enter is pressed
    return True
def detect_device(ser):
    return Device()
def get_device_template(device):
    #get item qualiyt inspection template from ERPNext
    template_name = client.get_value("Item", "quality_inspection_template",device.item_code)
    template = None
    if template_name :
        template = client.get_doc("Quality Inspection Template", template_name['quality_inspection_template'])

    return template
def create_serial_comm():
    return True
def validate_results(device, param):
    return True
def test_paramter(device, param):
    return


if __name__ == "__main__":
    client = c.create_client(auth.url, auth.user, auth.passwd)
    while True:
        if  detect_start_press():
            if  client ==  None:
                break;
            ser = create_serial_comm()
            device = detect_device(ser)
            print(device.item_code)
            if device:
                template = device.get_device_template(device)
                for param in template.item_quality_inspection_parameter










