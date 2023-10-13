from tc_python import *

with TCPython() as session:
    system = (session.select_database_and_elements("FEDEM", ["Fe", "Cr", "C"])
              .get_system())
    calc = system.with_single_equilibrium_calculation()

    (calc
        .set_condition("T", 700 + 273.15)
        .set_condition(ThermodynamicQuantity.mole_fraction_of_a_component("Cr"), 0.1)
        .set_condition(ThermodynamicQuantity.mole_fraction_of_a_component("C"), 0.01))
    
    result = calc.calculate()

    carbide_volume_frac = result.get_value_of(ThermodynamicQuantity.volume_fraction_of_a_phase("M23C6"))

    print(carbide_volume_frac)
