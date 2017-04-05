import random, os, logging

from cassiopeia import riotapi

region = 'NA'
key = 'DEV_KEY'

riotapi.set_region(region)
keyExists = os.environ.get(key)

if keyExists == 'None':
    raise ValueError('Environment variable ' + key + ' does not exist on the system.')

riotapi.set_api_key(os.environ[key])
# Load from environment variable. Source:
# http://cassiopeia.readthedocs.io/en/latest/setup.html#setting-additional-environment-variables

summoner = riotapi.get_summoner_by_name("Verciau")
print("{name} is a level {level} summoner on the NA server. He rocks on these champs:".format(name=summoner.name,
                                                                                              level=summoner.level))

ranked = summoner.ranked_stats()

print("{name} has played {numChamps} champions this season.".format(name=summoner.name, numChamps=len(ranked)))

for entry in ranked.items():
    winRate = entry[1].wins / entry[1].games_played
    if winRate > 0.5:
        print("Champ: {champ} | Wins: {wins} | Games Played: {played}".format(champ=entry[0].name, wins=entry[1].wins,
                                                                              played=entry[1].games_played))

champions = riotapi.get_champions()
random_champion = random.choice(champions)
print("He enjoys playing LoL on all different champions, like {name}.".format(name=random_champion.name))

challenger_league = riotapi.get_challenger()
best_na = challenger_league[0].summoner
print("He's much better at writing Python code than he is at LoL. He'll never be as good as {name}.".format(
    name=best_na.name))
