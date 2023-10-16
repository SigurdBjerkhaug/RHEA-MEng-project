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
            shorthand += rf"{key}_{float(alloy_dictionary[key]):.0f}"

        else:
            shorthand += rf"\{key}_{float(alloy_dictionary[key]):.3}"

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
