""" import os
print(os.getcwd())
os.chdir('c:\\Users\\sigur\\OneDrive - Imperial College London\\[01] MEng project\\[03] Computer calculators')
print(os.getcwd())
import numpy as np

testArray = np.array([[2, 1], [3, 4]])


import os
print(os.getcwd())





np.savetxt("test.txt", testArray) """

from tc_python import *
import numpy as np
from matplotlib import pyplot as plt

alloys = [
    {"Ti": 38.0, "V": 15.0, "Nb": 23.0, "Hf": 24.0},
    {"Ti": 25.0, "V": 25.0, "Nb": 25.0, "Hf": 25.0},
    {"Ti": 12.0, "V": 13.0, "Nb": 16.0, "Mo": 24.0, "Ta": 20.0, "W": 15.0},
    {"Ti": 16.7, "V": 16.7, "Nb": 16.7, "Mo": 16.7, "Ta": 16.7, "W": 16.7},
    {"V": 23.0, "Cr": 31.0, "Mo": 17.0, "Hf": 29.0},
    {"V": 25.0, "Cr": 25.0, "Mo": 25.0, "Hf": 25.0},
    {"Ti": 11.0, "Zr": 40.0, "Hf": 49.0},
    {"Ti": 33.0, "Zr": 33.0, "Hf": 33.0},
    {"Ti": 50.0, "V": 20.0, "Nb": 30.0},
    {"Ti": 33.0, "V": 33.0, "Nb": 33.0},
    {"Ti": 49.0, "V": 19.0, "Hf": 32.0},
    {"Ti": 33.0, "V": 33.0, "Hf": 33.0},
]


def DictionaryToAlloyShorthand(AlloyDict):
    AlloyDictKeys = list(AlloyDict.keys())

    shorthand = ""
    for key in AlloyDictKeys:
        shorthand += str(key) + str(AlloyDict[key])

    return shorthand


def estimate_liquidus_solidus(alloys, Databases=["TCHEA2"]):
    alloysShorthand = []

    LiquidusTempK = []
    SolidusTempK = []
    deltaT = []

    with TCPython() as session:
        for Database in Databases:
            for alloy in alloys:
                alloyKeys = list(alloy.keys())
                print(alloyKeys)
                system = session.select_database_and_elements(
                    Database, alloyKeys
                ).get_system()

                calc = system.with_property_model_calculation(
                    "Liquidus and Solidus Temperature"
                )

                for i in range(len(alloyKeys) - 1):
                    calc.set_composition(alloyKeys[i], alloy[alloyKeys[i]])

                result = calc.calculate()

                LiquidusTempK.append(result.get_value_of("Liquidus temperature"))
                SolidusTempK.append(result.get_value_of("Solidus temperature"))
                alloysShorthand.append(DictionaryToAlloyShorthand(alloy))

            LiquidusTempC = np.array(LiquidusTempK) - 273.14
            SolidusTempC = np.array(SolidusTempK) - 273.14
            deltaT = LiquidusTempC - SolidusTempC

            solidus_liquidus_array = np.array(
                [
                    alloysShorthand,
                    LiquidusTempK,
                    LiquidusTempC,
                    SolidusTempK,
                    SolidusTempC,
                    deltaT,
                ]
            )

    return solidus_liquidus_array


print(estimate_liquidus_solidus(alloys))
