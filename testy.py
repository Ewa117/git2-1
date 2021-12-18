continent = input('[U]SA czy [E]UROPA ?:')
if continent == 'U':
    print('mozesz uzywac aplikacje USA')
if continent == 'E' :
    print('mozesz uzywac aplikacji EUROPA')
    wiek = input("Podaj wiek: ")
    # Sprawdzamy, czy wiek jest złożony z cyfr
    if wiek.isdigit() == False:
        exit("Wiek musi być liczbą")
    wiek = int(wiek)
    if wiek >= 21 and wiek <= 65:
        print("Witamy w aplikacji i smacznej degustacji!")
    elif wiek > 65:
        print("Jesteś już za stary/a na alkohol")
    else:
        exit('jesteś za młody/a!, w USA wymagamy 21 lat')
elif continent =='m':
    print('Ta aplikacja nie jest dla facetow, sorry!')

else:
    print('Wybrano nieoslugiwana wartosci. Aplikacja jest tylko dla pelnoletnich kobiet. Sprobuj ponownie')
