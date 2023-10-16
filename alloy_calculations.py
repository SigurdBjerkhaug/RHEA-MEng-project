from matplotlib import pyplot as plt
import numpy as np
import ElementProperties
import pandas as pd

# deals with weight percent and atomic percent conversion


def atomic_percent_to_weight_percent(
    alloy_composition_atomic_percent, atomic_masses=ElementProperties.atomic_masses
):
    """alloy_composition_atomic is a dictionary with Element being Key and atomic percent being Value"""
    # calculate total mass
    elements = list(alloy_composition_atomic_percent.keys())
    total_mass = 0.0
    for element in elements:
        total_mass += alloy_composition_atomic_percent[element] * atomic_masses[element]

    alloy_composition_weight_percent = {}
    for element in elements:
        alloy_composition_weight_percent[element] = (
            alloy_composition_atomic_percent[element]
            * atomic_masses[element]
            * 100
            / total_mass
        )

    return alloy_composition_weight_percent


def weight_percent_to_atomic_percent(
    alloy_composition_weight_percent, atomic_masses=ElementProperties.atomic_masses
):
    """alloy_composition_weight_percent is a dictionary with Element being Key and atomic percent being Value"""
    # calculate total mass
    elements = list(alloy_composition_weight_percent.keys())
    total_atomic_mass = 0.0
    for element in elements:
        total_atomic_mass += (
            alloy_composition_weight_percent[element] / atomic_masses[element]
        )

    alloy_composition_atomic_percent = {}
    for element in elements:
        alloy_composition_atomic_percent[element] = (
            alloy_composition_weight_percent[element]
            * 100
            / (total_atomic_mass * atomic_masses[element])
        )

    return alloy_composition_atomic_percent


def measured_weight_to_weight_percent(
    measured_weight, atomic_masses=ElementProperties.atomic_masses
):
    """Calculates weight percent composition based on raw material of element composition you have measured for the sample"""
    elements = list(measured_weight.keys())
    total_mass = 0.0

    for element in elements:
        total_mass += measured_weight[element]

    alloy_composition_weight_percent = {}
    for element in elements:
        alloy_composition_weight_percent[element] = (
            measured_weight[element] / total_mass * 100
        )

    return alloy_composition_weight_percent


# estimates properties


def alloy_average_atomic_radii(
    alloy_composition_atomic_percent, atomic_radii_pm=ElementProperties.atomic_radii_pm
):
    """returns average alloy particle radius in picometre"""
    # This uses a weighted average
    weighted_alloy_radii = []
    for element in alloy_composition_atomic_percent:
        weighted_alloy_radii.append(
            alloy_composition_atomic_percent[element] * atomic_radii_pm[element] / 100
        )
    weighted_alloy_radii = np.array(weighted_alloy_radii)

    alloyAverageAtomicRadius = np.sum(weighted_alloy_radii)
    return alloyAverageAtomicRadius


def alloy_average_atomic_mass(
    alloy_composition_atomic, atomic_masses=ElementProperties.atomic_masses
):
    """returns average alloy particle mass in g/Mol"""
    # This uses a weighted average
    weighted_alloy_molar_mass = []
    for element in alloy_composition_atomic:
        weighted_alloy_molar_mass.append(
            alloy_composition_atomic[element] * atomic_masses[element] / 100
        )
    weighted_alloy_molar_mass = np.array(weighted_alloy_molar_mass)
    #     alloyAverageAtomicRadius = np.sum(weightedAlloyRadii)/len(weightedAlloyRadii)
    alloy_average_atom_molar_mass = np.sum(weighted_alloy_molar_mass)
    return alloy_average_atom_molar_mass


def estimate_alloy_density(
    alloy_composition_atomic_percent,
    metallic_densities_g_per_cm3=ElementProperties.metallic_densities_g_per_cm3,
):
    """returns estimated alloy density in g/cm^3"""

    estimated_alloy_density = 0
    for element in alloy_composition_atomic_percent:
        estimated_alloy_density += (
            alloy_composition_atomic_percent[element]
            * metallic_densities_g_per_cm3[element]
            / 100
        )
    return estimated_alloy_density


def estimate_alloy_price(
    alloy_composition_weight_percent,
    element_prices_per_kg=ElementProperties.element_prices_per_kg,
):
    "Calculate the price of an alloy based on rough raw material price in USD (not accounting for processing). 1st principles model"
    estimated_alloy_price = 0
    elements = list(alloy_composition_weight_percent.keys())

    for element in elements:
        estimated_alloy_price += (
            alloy_composition_weight_percent[element]
            / 100
            * element_prices_per_kg[element]
        )

    return estimated_alloy_price


# deals with formatting of datastructures


def dictionary_to_alloy_shorthand(alloy_dictionary):
    alloy_dictionary_keys = list(alloy_dictionary.keys())

    shorthand = ""
    for key in alloy_dictionary_keys:
        shorthand += f"{key}({float(alloy_dictionary[key]):.3})"

    return shorthand


def dictionary_to_alloy_latex_shorthand(alloy_dictionary):
    alloy_dictionary_keys = list(alloy_dictionary.keys())

    shorthand = "$"
    for key in alloy_dictionary_keys:
        if str(alloy_dictionary[key]).endswith("0") == True:
            shorthand += f"{key}_"
            shorthand += "{"
            shorthand += f"{alloy_dictionary[key]:.0f}"
            shorthand += "}"

        else:
            shorthand += f"{key}_"
            shorthand += "{"
            shorthand += f"{alloy_dictionary[key]:.3}"
            shorthand += "}"

    shorthand += "$"

    return shorthand


# Deals with Thermo-Calc


def npy_to_dataframe(npy_file, header_row=[]):
    dummy_array = np.load(npy_file)
    dummy_array = np.transpose(dummy_array)
    dummy_data_frame = pd.DataFrame(dummy_array)
    if header_row != []:
        dummy_data_frame.columns = header_row
    return dummy_data_frame


# making tables under below


def alloy_preparation_latex_table(
    alloys, batch_number, sample_target_weight=10, folder="Latex\\"
):
    """Generate a latex table for alloy preparation"""
    pd.set_option("display.max_colwidth", None)

    sample_target_weight = sample_target_weight  # target weight in grams

    target_component_weights = []
    weight_percent = []

    component_weights = []
    measured_component_weights = []

    # Latex formatted strings
    atomic_percent_shorthand = []
    weight_percent_shorthand = []
    alloy_index = []

    for alloy in alloys:
        alloy_weight_percent = atomic_percent_to_weight_percent(alloy)
        weight_percent.append(alloy_weight_percent)
        atomic_percent_shorthand.append(dictionary_to_alloy_latex_shorthand(alloy))
        weight_percent_shorthand.append(
            dictionary_to_alloy_latex_shorthand(alloy_weight_percent)
        )

        target_component_weight = "\makecell[l]{"
        measured_component_weight = "\makecell[l]{"

        for element in alloy:
            target_component_weight += rf" {element} : { alloy_weight_percent[element]*sample_target_weight/100:.2f} g \\"
            measured_component_weight += rf" {element} :\\"

        target_component_weight += "}"
        measured_component_weight += "}"

        component_weights.append(target_component_weight)
        measured_component_weights.append(measured_component_weight)
        target_component_weights.append(rf"{sample_target_weight} g")

    for i in range(len(alloys)):
        alloy_index.append(f"B{batch_number}-{i+1}")

    alloy_dictionary = {
        "\thead{index}": alloy_index,
        "\thead{Composition \\\ At\%}": atomic_percent_shorthand,
        "\thead{Composition \\\ Wt\%}": weight_percent_shorthand,
        "\thead{Total target weight \\\ sample}": target_component_weights,
        "\thead{Target weight \\\ per element}": component_weights,
        "\thead{Measure weight \\\ per element}": measured_component_weights,
    }

    alloy_data = pd.DataFrame(alloy_dictionary)
    alloy_data.to_latex(
        f"{folder}Batch {batch_number}_Preparatory calculations.tex",
        escape=False,
        index=False,
    )

    return alloy_data


def alloy_mesured_weight_input_sheet(alloys, batch_number):
    """Creates excel sheet for easy data entry after preparing sample"""
    alloys_components = []

    alloys_shorthand = []
    # alloys_component_entry = []

    for alloy in alloys:
        for element in alloy.keys():
            if element in alloys_components:
                continue
            alloys_components.append(element)

        alloys_shorthand.append(dictionary_to_alloy_shorthand(alloy))

    alloys_components = pd.DataFrame(alloys_components, columns=["Alloying element"])
    alloy_entry = []

    for i in range(len(alloys_components)):
        dummy = []
        for j in range(len(alloys)):
            dummy.append("")
        alloy_entry.append(dummy)

    alloys_component_entry = pd.concat(
        [alloys_components, pd.DataFrame(alloy_entry, columns=alloys_shorthand)]
    )

    alloys_component_entry.to_excel(
        f"Batch {batch_number}_Measured alloy component entry.xlsx", index=False
    )

    return alloys_component_entry
