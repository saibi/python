import json
import re

REGEXP_VERSION_NUMBERS = r"\d+\.\d+\.\d+"
REGEXP_GUI_VER = r"GUI_V\d+\.\d+\.\d+"
REGEXP_MOTOR_VER = r"MOTOR_V\d+\.\d+\.\d+"


with open('8bca82e0.json', 'r') as f:
    json_data = json.load(f)

gui = json_data['gui']
motor = json_data['motor']


SW_UPDATE_BIN = "HPE910XD_GUI_V1.16.4_MOTOR_V2.3.3.zip"


def extract_version_str_from_full_version_string(str):
    match = re.findall(REGEXP_VERSION_NUMBERS, str)
    if len(match) > 0:
        return match[0]
    else:
        return None


gui_ver = extract_version_str_from_full_version_string(gui)
motor_ver = extract_version_str_from_full_version_string(motor)

print(f"GUI: {gui_ver}, Motor: {motor_ver}")


def extract_version_str_from_update_binary(ptn, filename):
    match = re.findall(ptn, filename)
    if len(match) > 0:
        return re.findall(REGEXP_VERSION_NUMBERS, match[0])[0]
    else:
        return None


latest_gui_ver = extract_version_str_from_update_binary(
    REGEXP_GUI_VER, SW_UPDATE_BIN)
latest_motor_ver = extract_version_str_from_update_binary(
    REGEXP_MOTOR_VER, SW_UPDATE_BIN)

print(f"latest GUI: {latest_gui_ver}, latest Motor: {latest_motor_ver}")


def compare_versions(ver1, ver2):
    """compare version number
    if ver1 > ver2, return 1
    if ver1 < ver2, return -1
    if ver1 == ver2, return 0
    """
    if ver1 is None or ver2 is None:
        return None
    ver1 = ver1.split('.')
    ver2 = ver2.split('.')
    if len(ver1) != len(ver2):
        return None

    for i in range(len(ver1)):
        if int(ver1[i]) > int(ver2[i]):
            return 1
        elif int(ver1[i]) < int(ver2[i]):
            return -1
    return 0


check_gui = compare_versions(gui_ver, latest_gui_ver)
check_motor = compare_versions(motor_ver, latest_motor_ver)

print(f"result: GUI: {check_gui}, Motor: {check_motor}")


class SWUpdateVersionChecker:

    def __init__(self, device_info_path, sw_update_bin_name):
        with open(device_info_path, 'r') as f:
            json_data = json.load(f)

        self.device_version = {"gui": self.__extract_version_str_from_full_version_string(
            json_data["gui"]), "motor": self.__extract_version_str_from_full_version_string(json_data["motor"])}
        self.update_version = {"gui": self.__extract_version_str_from_update_binary(
            REGEXP_GUI_VER, sw_update_bin_name), "motor": self.__extract_version_str_from_update_binary(REGEXP_MOTOR_VER, sw_update_bin_name)}

    def check_for_update(self):
        self.gui_update_available = self.__compare_versions(
            self.device_version["gui"], self.update_version["gui"]) < 0
        self.motor_update_available = self.__compare_versions(
            self.device_version["motor"], self.update_version["motor"]) < 0
        return self.gui_update_available or self.motor_update_available

    def __extract_version_str_from_full_version_string(self, str):
        match = re.findall(REGEXP_VERSION_NUMBERS, str)
        if len(match) > 0:
            return match[0]
        else:
            return None

    def __extract_version_str_from_update_binary(self, ptn, filename):
        match = re.findall(ptn, filename)
        if len(match) > 0:
            return re.findall(REGEXP_VERSION_NUMBERS, match[0])[0]
        else:
            return None

    def __compare_versions(self, ver1, ver2):
        if ver1 is None or ver2 is None:
            return None
        ver1 = ver1.split('.')
        ver2 = ver2.split('.')
        if len(ver1) != len(ver2):
            return None

        for i in range(len(ver1)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver1[i]) < int(ver2[i]):
                return -1
        return 0


checker = SWUpdateVersionChecker(
    "8bca82e0.json", "HPE910XD_GUI_V1.16.18_MOTOR_V2.3.2.zip")
print(checker.check_for_update())
