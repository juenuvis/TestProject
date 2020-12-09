Rivers = {'nile': 'egypt', 'huanghe': 'china', 'Dahe': 'world'}
rivers = []
countrys = []
for river, country in Rivers.items():
    print("The " + river + " runs through " + country )
    rivers.append(river)   
    countrys.append(country)
    print(country)
    