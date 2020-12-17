első = int(input('Mi az egyik szám? '))
második = int(input('Mi a másik szám? '))
if első > második:
    szám = 'Az ' + str(első) + ' a nagyobb.'
elif első == második:
    szám = 'Egyenlőek.'
else:
    kiírandó = 'A ' + str(második) + ' a nagyobb.'
print(szám)