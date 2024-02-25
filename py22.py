melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}


oxides = {key: value for key, value in melt.items() if 'O' in key}
melting_temperatures = ' '.join(str(value) for value in oxides.values())

print(melting_temperatures)
