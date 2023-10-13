atomic_masses = { 
    'H': 1.008,
    'He': 4.0026,
    'Li': 6.94,
    'Be': 9.0122,
    'B': 10.81,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'F': 18.998,
    'Ne': 20.180,
    'Na': 22.990,
    'Mg': 24.305,
    'Al': 26.982,
    'Si': 28.085,
    'P': 30.974,
    'S': 32.06,
    'Cl': 35.45,
    'K': 39.098,
    'Ar': 39.948,
    'Ca': 40.078,
    'Sc': 44.956,
    'Ti': 47.867,
    'V': 50.942,
    'Cr': 51.996,
    'Mn': 54.938,
    'Fe': 55.845,
    'Ni': 58.693,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.922,
    'Se': 78.971,
    'Br': 79.904,
    'Kr': 83.798,
    'Rb': 85.468,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.95,
    'Tc': 98.0,
    'Ru': 101.07,
    'Rh': 102.91,
    'Pd': 106.42,
    'Ag': 107.87,
    'Cd': 112.41,
    'In': 114.82,
    'Sn': 118.71,
    'Sb': 121.76,
    'Te': 127.60,
    'I': 126.90,
    'Xe': 131.29,
    'Cs': 132.91,
    'Ba': 137.33,
    'La': 138.90,
    'Ce': 140.12,
    'Pr': 140.91,
    'Nd': 144.24,
    'Pm': 145.0,
    'Sm': 150.36,
    'Eu': 152.00,
    'Gd': 157.25,
    'Tb': 158.93,
    'Dy': 162.50,
    'Ho': 164.93,
    'Er': 167.26,
    'Tm': 168.93,
    'Yb': 173.05,
    'Lu': 175.00,
    'Hf': 178.49,
    'Ta': 180.95,
    'W': 183.84,
    'Re': 186.21,
    'Os': 190.23,
    'Ir': 192.22,
    'Pt': 195.08,
    'Au': 196.97,
    'Hg': 200.59,
    'Tl': 204.38,
    'Pb': 207.2,
    'Bi': 208.98,
    'Th': 232.04,
    'Pa': 231.04,
    'U': 238.03,
    'Np': 237.0,
    'Pu': 244.0,
    'Am': 243.0,
    'Cm': 247.0,
    'Bk': 247.0,
    'Cf': 251.0,
    'Es': 252.0,
    'Fm': 257.0,
    'Md': 258.0,
    'No': 259.0,
    'Lr': 266.0,
    'Rf': 267.0,
    'Db': 270.0,
    'Sg': 271.0,
    'Bh': 270.0,
    'Hs': 277.0,
    'Mt': 276.0,
    'Ds': 281.0,
    'Rg': 280.0,
    'Cn': 285.0,
    'Nh': 284.0,
    'Fl': 289.0,
    'Mc': 288.0,
    'Lv': 293.0,
    'Ts': 294.0,
    'Og': 294.0,
}

element_prices_per_kg = {
    'H': 0.01,      # Approximate price for hydrogen
    'He': 5.00,     # Approximate price for helium
    'Li': 30.00,    # Approximate price for lithium
    'Be': 200.00,   # Approximate price for beryllium
    'B': 20.00,     # Approximate price for boron
    'C': 0.50,      # Approximate price for carbon (varies with form)
    'N': 1.50,      # Approximate price for nitrogen
    'O': 0.20,      # Approximate price for oxygen
    'F': 1.00,      # Approximate price for fluorine
    'Ne': 20.00,    # Approximate price for neon
    'Na': 2.00,     # Approximate price for sodium
    'Mg': 3.00,     # Approximate price for magnesium
    'Al': 1.50,     # Approximate price for aluminum
    'Si': 1.50,     # Approximate price for silicon
    'P': 2.00,      # Approximate price for phosphorus
    'S': 0.20,      # Approximate price for sulfur
    'Cl': 1.50,     # Approximate price for chlorine
    'K': 25.00,     # Approximate price for potassium
    'Ar': 20.00,    # Approximate price for argon
    'Ca': 2.50,     # Approximate price for calcium
    'Sc': 20.00,    # Approximate price for scandium
    'Ti': 6.00,     # Approximate price for titanium
    'V': 31.0,      # Updated with prices from google
    'Cr': 7.00,     # Approximate price for chromium
    'Mn': 2.00,     # Approximate price for manganese
    'Fe': 0.80,     # Approximate price for iron
    'Ni': 8.00,     # Approximate price for nickel
    'Co': 45.00,    # Approximate price for cobalt
    'Cu': 8.00,     # Approximate price for copper
    'Zn': 3.00,     # Approximate price for zinc
    'Ga': 150.00,   # Approximate price for gallium
    'Ge': 1000.00,  # Approximate price for germanium
    'As': 6.00,     # Approximate price for arsenic
    'Se': 50.00,    # Approximate price for selenium
    'Br': 3.00,     # Approximate price for bromine
    'Kr': 20.00,    # Approximate price for krypton
    'Rb': 15.00,    # Approximate price for rubidium
    'Sr': 300.00,   # Approximate price for strontium
    'Y': 300.00,    # Approximate price for yttrium
    'Zr': 100.00,   # Approximate price for zirconium
    'Nb': 45.00,   # Approximate price for niobium
    'Mo': 35.00,    # Approximate price for molybdenum
    'Tc': None,     # Technetium is not commonly traded
    'Ru': 80.00,    # Approximate price for ruthenium
    'Rh': 100.00,   # Approximate price for rhodium
    'Pd': 300.00,   # Approximate price for palladium
    'Ag': 600.00,   # Approximate price for silver
    'Cd': 8.00,     # Approximate price for cadmium
    'In': 300.00,   # Approximate price for indium
    'Sn': 15.00,    # Approximate price for tin
    'Sb': 10.00,    # Approximate price for antimony
    'Te': 50.00,    # Approximate price for tellurium
    'I': 100.00,    # Approximate price for iodine
    'Xe': 50.00,    # Approximate price for xenon
    'Cs': 600.00,   # Approximate price for cesium
    'Ba': 300.00,   # Approximate price for barium
    'La': 5.00,     # Approximate price for lanthanum
    'Ce': 3.00,     # Approximate price for cerium
    'Pr': 250.00,   # Approximate price for praseodymium
    'Nd': 250.00,   # Approximate price for neodymium
    'Pm': None,     # Promethium is not commonly traded
    'Sm': 100.00,   # Approximate price for samarium
    'Eu': 200.00,   # Approximate price for europium
    'Gd': 300.00,   # Approximate price for gadolinium
    'Tb': 600.00,   # Approximate price for terbium
    'Dy': 300.00,   # Approximate price for dysprosium
    'Ho': 300.00,   # Approximate price for holmium
    'Er': 600.00,   # Approximate price for erbium
    'Tm': 700.00,   # Approximate price for thulium
    'Yb': 400.00,   # Approximate price for ytterbium
    'Lu': 600.00,   # Approximate price for lutetium
    'Hf': 5400.00,   # Updated with prices from google
    'Ta': 150.00,    # Googled 16.09.2023
    'W': 35.00,     # Approximate price for tungsten
    'Re': 200.00,   # Approximate price for rhenium
    'Os': 400.00,   # Approximate price for osmium
    'Ir': 800.00,   # Approximate price for iridium
    'Pt': 30000.00, # Approximate price for platinum
    'Au': 50000.00, # Approximate price for gold
    'Hg': 100.00,   # Approximate price for mercury
    'Tl': 30.00,    # Approximate price for thallium
    'Pb': 2.00,     # Approximate price for lead
    'Bi': 15.00,    # Approximate price for bismuth
    'Th': 600.00,   # Approximate price for thorium
    'Pa': None,     # Protactinium is not commonly traded
    'U': 50.00,     # Approximate price for uranium
}

# Note: Some elements have a price of 'None' as they are not commonly traded in pure form.

# Approximate atomic radii in picometers (pm) based on the Pauling scale or metallic radii
# Source: Data from various references, including the CRC Handbook of Chemistry and Physics.

atomic_radii_pm = {
    'H': 53,     'He': 31,
    'Li': 167,   'Be': 112,
    'B': 87,     'C': 67,
    'N': 56,     'O': 48,
    'F': 42,     'Ne': 38,
    'Na': 190,   'Mg': 145,
    'Al': 118,   'Si': 111,
    'P': 98,     'S': 88,
    'Cl': 79,    'K': 243,
    'Ar': 71,    'Ca': 194,
    'Sc': 184,   'Ti': 147,
    'V': 134,    'Cr': 166,
    'Mn': 161,   'Fe': 156,
    'Ni': 149,   'Co': 152,
    'Cu': 145,   'Zn': 142,
    'Ga': 136,   'Ge': 125,
    'As': 114,   'Se': 103,
    'Br': 94,    'Kr': 88,
    'Rb': 265,   'Sr': 219,
    'Y': 212,    'Zr': 206,
    'Nb': 146,   'Mo': 190,
    'Tc': 183,   'Ru': 178,
    'Rh': 173,   'Pd': 169,
    'Ag': 165,   'Cd': 161,
    'In': 156,   'Sn': 145,
    'Sb': 133,   'Te': 123,
    'I': 115,    'Xe': 108,
    'Cs': 298,   'Ba': 253,
    'La': 195,   'Ce': 186,
    'Pr': 185,   'Nd': 185,
    'Pm': 185,   'Sm': 185,
    'Eu': 185,   'Gd': 185,
    'Tb': 185,   'Dy': 185,
    'Ho': 185,   'Er': 185,
    'Tm': 185,   'Yb': 185,
    'Lu': 175,   'Hf': 225, 
    'Ta': 146,   'W': 139,
    'Re': 136,   'Os': 135,
    'Ir': 136,   'Pt': 139,
    'Au': 144,   'Hg': 149,
    'Tl': 148,   'Pb': 147,
    'Bi': 146,   'Th': 180,
    'Pa': 169,   'U': 160,
    'Np': 155,   'Pu': 159,
    'Am': 173,   'Cm': 174,
    'Bk': 170,   'Cf': 186,
    'Es': 186,   'Fm': 186,
    'Md': 186,   'No': 186,
    'Lr': 186,   'Rf': None,
    'Db': None,  'Sg': None,
    'Bh': None,  'Hs': None,
    'Mt': None,  'Ds': None,
    'Rg': None,  'Cn': None,
    'Nh': None,  'Fl': None,
    'Mc': None,  'Lv': None,
    'Ts': None,  'Og': None
}
#Hf, Ti, V, Nb updated by googling, most seem wrong

# Approximate densities of some common metallic elements in g/cm^3
# Source: Data from various references, including the CRC Handbook of Chemistry and Physics.

metallic_densities_g_per_cm3 = {
    'Li': 0.53,
    'Be': 1.85,
    'Na': 0.97,
    'Mg': 1.74,
    'Al': 2.70,
    'Si': 2.33,
    'K': 0.86,
    'Ca': 1.54,
    'Sc': 2.99,
    'Ti': 4.50,
    'V': 6.11,
    'Cr': 7.19,
    'Mn': 7.21,
    'Fe': 7.87,
    'Co': 8.90,
    'Ni': 8.91,
    'Cu': 8.96,
    'Zn': 7.13,
    'Ga': 5.91,
    'Ge': 5.32,
    'As': 5.73,
    'Se': 4.82,
    'Rb': 1.53,
    'Sr': 2.63,
    'Y': 4.47,
    'Zr': 6.51,
    'Nb': 8.57,
    'Mo': 10.22,
    'Tc': None,  # Technetium is not commonly encountered in pure form.
    'Ru': 12.41,
    'Rh': 12.41,
    'Pd': 12.02,
    'Ag': 10.49,
    'Cd': 8.65,
    'In': 7.31,
    'Sn': 7.29,
    'Sb': 6.68,
    'Te': 6.24,
    'I': 4.93,
    'Cs': 1.93,
    'Ba': 3.51,
    'La': 6.15,
    'Ce': 6.77,
    'Pr': 6.77,
    'Nd': 7.00,
    'Pm': None,  # Promethium is not commonly encountered in pure form.
    'Sm': 7.52,
    'Eu': 5.24,
    'Gd': 7.89,
    'Tb': 8.23,
    'Dy': 8.55,
    'Ho': 8.80,
    'Er': 9.07,
    'Tm': 9.32,
    'Yb': 6.90,
    'Lu': 9.84,
    'Hf': 13.31,
    'Ta': 16.65,
    'W': 19.25,
    'Re': 21.02,
    'Os': 22.57,
    'Ir': 22.42,
    'Pt': 21.45,
    'Au': 19.32,
    'Hg': 13.53,
    'Tl': 11.85,
    'Pb': 11.34,
    'Bi': 9.75,
    'Th': 11.72,
    'Pa': 15.37,
    'U': 19.05,
}

