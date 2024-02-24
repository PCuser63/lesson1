 #melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni':
#1455,'Si': 1415, 'Be': 1287}
Sn = 232
Zn = 420
Be = 1287
Si = 1415
Ni = 1455
Fe = 1539
b = input()
if b == "Fe Sn":
    print(int(Fe-Sn))
elif b == "Fe Zn":
    print(int(Fe - Zn))
elif b == "Fe Be":
    print(int(Fe-Be))
elif b == "Fe Si":
    print(int(Fe-Si))
elif b == "Fe Ni":
    print(int(Fe-Ni))
elif b == "Ni Sn":
    print(int(Ni-Sn))
elif b == "Ni Zn":
    print(Ni-Zn)
elif b == "Ni Be":
    print(int(Ni-Be))
elif b == "Ni Si":
    print(int(Ni-Si))
elif b == "Si Sn":
    print(int(Si-Sn))
elif b == "Si Zn":
    print(int(Si-Zn))
elif b == "Si Be":
    print(int(Si-Be))
elif b == "Be Sn":
    print(int(Be-Sn))
elif b == "Be Zn":
    print(int(Be - Zn))
elif b == "Zn Sn":
    print(int(Zn - Sn))