import csv
import form_editing
import add_column
import del_column
import datatype_fix



def prep(source, output, new_category, extra):
    '''does complete preparations on new data'''
    form_editing.editing(source, output)
    add_column.add_column(output, source, new_category, extra)
    del_column.del_column(source, output, new_category)
    datatype_fix.Datatype_fix(output, source, new_category)



#prep('Action.csv', 'Action-.csv', 'Genre', 'action')
#prep('RPG.csv', 'RPG-.csv', 'Genre', 'RPG')
#prep('Adventure.csv', 'Adventure-.csv', 'Genre', 'adventure')
#prep('MMO.csv', 'MMO-.csv', 'Genre', 'MMO')
#prep('Indie.csv', 'Indie-.csv', 'Genre', 'indie')
#prep('Simulation.csv', 'Simulation-.csv', 'Genre', 'simulation')
#prep('Sports.csv', 'Sports-.csv', 'Genre', 'sports')
#prep('Strategy.csv', 'Strategy-.csv', 'Genre', 'strategy')
