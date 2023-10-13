from tc_python import *
import numpy as np
from matplotlib import pyplot as plt

with TCPython() as session:
    system = (session.select_database_and_elements("FEDEM", ["Fe", "Cr", "C"])
              .get_system())
    
    cr_contents = np.arange(8.5, 9.5, 0.005)

    calc = system()

    (calc
        .set_condition("T", 700 + 273.15)
        .set_condition(ThermodynamicQuantity.mole_fraction_of_a_component("C"), 0.01))

    carbide_volume_fracs = []

    for cr_content in cr_contents:
        calc.set_condition(ThermodynamicQuantity.mole_fraction_of_a_component("Cr"), cr_content/100)
    
        result = calc.calculate()

        carbide_volume_frac = result.get_value_of(ThermodynamicQuantity.volume_fraction_of_a_phase("M23C6"))
        carbide_volume_fracs.append(carbide_volume_frac)
        print(carbide_volume_fracs[-1])

    plt.plot(cr_contents, carbide_volume_fracs)
    plt.xlabel("Cr-content / Wt%")
    plt.ylabel("M23C6 - content / vol-fraction")
    plt.show()
