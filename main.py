from infi.devicemanager import DeviceManager
import time

def scanUSB ():
    start_time = time.time()
    dm = DeviceManager()
    dm.root.rescan()
    all_devices = dm.all_devices

    usb_devices = [device for device in all_devices if "USB" in device.description
                and "концентратор" not in device.description.lower()
                and "host controller" not in device.description.lower()]

    for usb_device in usb_devices:
        print(f"Device: {usb_device}")
        print(f"Instance ID: {usb_device.instance_id}")
        print(f"Description: {usb_device.description}")
        print(f"Class GUID: {usb_device.class_guid}")
        print(f"Hardware IDs: {usb_device.hardware_ids}")
        try:
            location_info = usb_device.location
            print(f"Location: {location_info}")
        except KeyError:
            print("Location information not available")
        print("---")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения функции scanUSB() : {execution_time} секунд")

if __name__ == "__main__":
   scanUSB()
