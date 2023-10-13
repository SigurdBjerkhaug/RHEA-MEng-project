import os
print(os.getcwd())
os.chdir('c:\\Users\\sigur\\OneDrive - Imperial College London\\[01] MEng project\\[03] Computer calculators')
print(os.getcwd())
import numpy as np


from tc_python import *
import numpy as np
from matplotlib import pyplot as plt

alloy = {"Ti":38.0, "V":15.0, "Nb":23.0, "Hf":24.0, "Al": 0.0}
          

SiCompositions = np.arange(0, 20, 1)
print(SiCompositions)

def DictionaryToAlloyShorthand(AlloyDict):
    AlloyDictKeys = list(AlloyDict.keys())
    
    shorthand = ""
    for key in AlloyDictKeys:
            shorthand += str(key) + str(AlloyDict[key])

    return shorthand

alloysShorthand = []


LiquidusTempK = []
SolidusTempK = []
deltaT = []

""" for alloy in alloys:
    print(alloy)
    alloyKeys = list(alloy.keys())
    print(alloyKeys)
    for i in range(len(alloyKeys)-1):
        print(alloyKeys[i], alloy[alloyKeys[i]])

testArray = np.array([[1, 1, 1], [2, 2, 2]])


np.save("test3", testArray)
np.savetxt("test3.txt", testArray) """

Database = "TCNI11"

with TCPython() as session:  

        alloyKeys = list(alloy.keys())
        print(alloyKeys)
        print(alloy)
        system = (session.select_database_and_elements(Database, alloyKeys)
                .get_system())

        calc = system.with_property_model_calculation("Liquidus and Solidus Temperature")

        for composition in SiCompositions:
            alloy["Al"] = composition
            alloy["Hf"] = 24.0 - composition

            for i in range(len(alloyKeys)-1):
                calc.set_composition(alloyKeys[i], alloy[alloyKeys[i]])

            result = calc.calculate()

            LiquidusTempK.append(result.get_value_of('Liquidus temperature'))
            SolidusTempK.append(result.get_value_of('Solidus temperature'))
            alloysShorthand.append(DictionaryToAlloyShorthand(alloy))

        LiquidusTempC = np.array(LiquidusTempK) - 273.14
        SolidusTempC = np.array(SolidusTempK) - 273.14    
        deltaT = LiquidusTempC - SolidusTempC

        solidusLiquidusArray = np.array([SiCompositions, LiquidusTempK, LiquidusTempC, SolidusTempK, SolidusTempC, deltaT])
        print(solidusLiquidusArray)
        np.save(f"SolidusLiquidusData_Al variation_TiVNbHf_{Database}_09oct23", solidusLiquidusArray)
        np.savetxt("SolidusLiquidusData_09oct23.txt", solidusLiquidusArray, fmt='%s')
