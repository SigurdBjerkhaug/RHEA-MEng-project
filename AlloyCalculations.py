from matplotlib import pyplot as plt
import numpy as np
import ElementProperties
import pandas as pd
import datetime

# deals with weight percent and atomic percent conversion


def atomicPercentToWegihtPercent(
    AlloyCompositionAtomic, atomic_masses=ElementProperties.atomic_masses
):
    """AlloyCompositionAtomic is a dictionary with Element being Key and atomic percent being Value"""
    # calculate total mass
    elements = list(AlloyCompositionAtomic.keys())
    totalMass = 0.0
    for element in elements:
        totalMass += AlloyCompositionAtomic[element] * atomic_masses[element]

    AlloyCompositionWeight = {}
    for element in elements:
        AlloyCompositionWeight[element] = (
            AlloyCompositionAtomic[element] * atomic_masses[element] * 100 / totalMass
        )

    return AlloyCompositionWeight


def WeightPercent_To_AtomicPercent(
    AlloyCompositionWeight, atomic_masses=ElementProperties.atomic_masses
):
    """AlloyCompositionWeight is a dictionary with Element being Key and atomic percent being Value"""
    # calculate total mass
    elements = list(AlloyCompositionWeight.keys())
    totalAtomicMass = 0.0
    for element in elements:
        totalAtomicMass += AlloyCompositionWeight[element] / atomic_masses[element]

    AlloyCompositionAtomic = {}
    for element in elements:
        # AlloyCompositionWeight[element] = AlloyCompositionAtomic[element]*atomic_masses[element]*100 / totalMass
        AlloyCompositionAtomic[element] = (
            AlloyCompositionWeight[element]
            * 100
            / (totalAtomicMass * atomic_masses[element])
        )

    return AlloyCompositionAtomic


def measured_weight_to_WtPercent(
    MeasuredWeight, atomic_masses=ElementProperties.atomic_masses
):
    """Calculates weight percent composition based on raw material of element composition you have measured for the sample"""
    elements = list(MeasuredWeight.keys())
    totalMass = 0.0

    for element in elements:
        totalMass += MeasuredWeight[element]

    AlloyCompositionWeightPercent = {}
    for element in elements:
        AlloyCompositionWeightPercent[element] = (
            MeasuredWeight[element] / totalMass * 100
        )

    return AlloyCompositionWeightPercent


# estimates properties


def alloyAverageAtomicRadii(
    alloyCompositionAtomic, atomic_radii_pm=ElementProperties.atomic_radii_pm
):
    """returns average alloy particle radius in picometre"""
    # this uses a weighted average
    WeightedAlloyRadii = []
    for element in alloyCompositionAtomic:
        WeightedAlloyRadii.append(
            alloyCompositionAtomic[element] * atomic_radii_pm[element] / 100
        )
    weightedAlloyRadii = np.array(WeightedAlloyRadii)
    #     alloyAverageAtomicRadius = np.sum(weightedAlloyRadii)/len(weightedAlloyRadii)
    alloyAverageAtomicRadius = np.sum(weightedAlloyRadii)
    return alloyAverageAtomicRadius


def alloyAverageAtomicMass(
    alloyCompositionAtomic, atomic_masses=ElementProperties.atomic_masses
):
    """returns average alloy particle mass in g/Mol"""
    # this uses a weighted average
    WeightedAlloyMolarMass = []
    for element in alloyCompositionAtomic:
        WeightedAlloyMolarMass.append(
            alloyCompositionAtomic[element] * atomic_masses[element] / 100
        )
    WeightedAlloyMolarMass = np.array(WeightedAlloyMolarMass)
    #     alloyAverageAtomicRadius = np.sum(weightedAlloyRadii)/len(weightedAlloyRadii)
    alloyAverageAtomMolarMass = np.sum(WeightedAlloyMolarMass)
    return alloyAverageAtomMolarMass


def estimateAlloyDensity(
    alloyCompositionAtomic,
    metallic_densities_g_per_cm3=ElementProperties.metallic_densities_g_per_cm3,
):
    """returns estimated alloy density in g/cm^3"""
    #     a = a*10**(-10) #to convert from pm to cm
    #     N_a = 6.02*10**23
    #     estimatedAlloyDensity = Z*M_m/(N_a*(a*16/3)**3)
    estimatedAlloyDensity = 0
    for element in alloyCompositionAtomic:
        estimatedAlloyDensity += (
            alloyCompositionAtomic[element]
            * metallic_densities_g_per_cm3[element]
            / 100
        )
    return estimatedAlloyDensity


def alloyPrice(
    AlloyCompositionWeight,
    element_prices_per_kg=ElementProperties.element_prices_per_kg,
):
    "Calculate the price of an alloy based on rough raw material price in USD (not accounting for processing). 1st principles model"
    AlloyPrice = 0
    elements = list(AlloyCompositionWeight.keys())

    for element in elements:
        AlloyPrice += (
            AlloyCompositionWeight[element] / 100 * element_prices_per_kg[element]
        )

    return AlloyPrice


# deals with formatting of datastructures


def DictionaryToAlloyShorthand(AlloyDict):
    AlloyDictKeys = list(AlloyDict.keys())

    shorthand = ""
    for key in AlloyDictKeys:
        shorthand += f"{key}({float(AlloyDict[key]):.3})"

    return shorthand


def dictionary_to_alloy_latex_shorthand(AlloyDict):
    AlloyDictKeys = list(AlloyDict.keys())

    shorthand = ""
    for key in AlloyDictKeys:
        shorthand += rf"{key}_{'{'}{float(AlloyDict[key]):.3}{'}'}"

    return shorthand


# Deals with Thermo-Calc


def npyToDataframe(npyFile, headerRow=[]):
    DummyArray = np.load(npyFile)
    DummyArray = np.transpose(DummyArray)
    Dataframe = pd.DataFrame(DummyArray)
    if headerRow != []:
        Dataframe.columns = headerRow
    return Dataframe
