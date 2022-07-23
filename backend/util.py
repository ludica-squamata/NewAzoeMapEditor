from winreg import OpenKey, EnumValue, HKEY_LOCAL_MACHINE
from os import path, getcwd
from pygame import quit
from sys import exit
import json


def salir():
    quit()
    exit()


def read_registry_data():
    """This function retrieves the a key from the Windows Registry"""
    key = OpenKey(HKEY_LOCAL_MACHINE, 'SOFTWARE\\Ludica Squamata\\ManoGift\\')
    base = EnumValue(key, 0)[1]
    return base


def abrir_json(ruta):
    route = path.join(getcwd(), *ruta.split('/'))
    with open(route, 'rt', encoding='utf-8') as file:
        return json.load(file)


def guardar_json(ruta, data):
    route = path.join(getcwd(), *ruta.split('/'))
    with open(route, 'wt', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, separators=(',', ': '))
