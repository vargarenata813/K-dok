population = {
'Budapest': 1750216,
'Debrecen': 201112,
'Szeged': 160258,
'Miskolc': 167754,
'Pécs': 141843,
'Győr': 133946,
'Nyíregyháza': 116814,
'Kecskemét': 110373,
'Székesfehérvár': 96529,
'Szombathely': 78591
}

def print_city_population(population_dict, city):
    print(city + ' népessége a legutóbbi népszámlálás szerint: ' + str(population_dict['Pécs']))

print_city_population(population, 'Pécs')



print(population.get('Debrecen'))


population['Debrecen'] = 220000
print(population)

population['Szolnok'] = 70554
population['Érd'] = 69431
print(population)

population.update({'Budapest': 1749812, 'Érd': 69431})
print(population)

del population['Debrecen']
del population['Kecskemét']
print(population)

overpopulated_cities = population.pop('Budapest')
print(population)