top_10_population = {
  'Hungary': {
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
  },
  'Germany': {
      'Berlin': 3520031,
      'Hamburg': 1787408,
      'Munich': 1450381,
      'Cologne': 1060582,
      'Frankfurt am Main': 732688,
      'Stuttgart': 623738,
      'Düsseldorf': 612178,
      'Dortmund': 586181,
      'Essen': 582624,
      'Leipzig': 560472
  },
  'France': {
      'Paris': 2187526,
      'Marseille': 863310,
      'Lyon': 516092,
      'Toulouse': 479553,
      'Nice': 340017,
      'Nantes': 309346,
      'Montpellier': 285121,
      'Strasbourg': 280966,
      'Bordeaux': 254436,
      'Lille': 232787
  }
}

print('Is Cologne in top 10?')
if 'Cologne' in top_10_population['Germany']:
    print('Yes, it is.')
else:
    print('No, it is not.')

def print_country_population(top_10_population, Hungary):
    print(top_10_population['Hungary'])

print_country_population(top_10_population, 'Hungary')

print(top_10_population.items())

print(top_10_population['Germany'].items())










