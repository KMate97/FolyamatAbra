eletkor=17
diak=True


if eletkor<6:
    print("ingyenes")
elif eletkor<18:
    print("Diákjegy: 1800 Ft")
elif eletkor>65:
    print("Nyugdijas jegy: 2000 Ft")
else:
    print("Teljesárú jegy: 3000 Ft")