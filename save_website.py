import tools
import re

for year in range(2000,2017):
    base = 'http://www.metacritic.com/browse/games/score'
    showscore = 'metascore'
    sort_by = 'discussed'
    filters = 'sort=desc&year_selected='

    adress = '{}/{}/{}/pc/filtered?{}{}'.format(base, showscore, sort_by, filters, year)
    file = 'metacritic_{}.html'.format(year)

    tools.shrani(adress, file)
