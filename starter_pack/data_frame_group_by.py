import pandas as panda 
import numpy as np 

a = panda.DataFrame(
    {
        'animal': ['horse','cat','dog','tiger','whale','dog','tiger','horse','cat','rat'],
        'weight': [245,12,15,200,780,17,176,234,12,9],
        'age' : [14,15,4,17,34,2,21,21,2,5],
        # 'color' : ['']

    }
)

def perform_simple_groupby():
    '''
    if you group by a single columns - series
    if you group by returns multiple columns - dataframe
    '''
    print(a)

    ## group by animal type
    g_by_animal = a.groupby(by =['animal']) # dis is a DataFrameGroupBy object
    
    print(g_by_animal) ##returns a groupby object on which we can run agg functions
    print(g_by_animal.groups) ##returns a dict stating the group names and the index where they are
    print(g_by_animal['weight']) # this is SeriesGroupBy object

    # how to select a single grooup
    print(g_by_animal.get_group('dog'))

    #IMP to note: the group names becomes the new index
    print(g_by_animal.sum(), g_by_animal.agg(np.sum))
    print(g_by_animal.max(),'\n', g_by_animal.agg(np.max))
    
    # say group by animal and give sum of weights of each group
    print(g_by_animal['weight'].sum())

    # say give me sum of weights/mean of weights as well
    print(g_by_animal['weight'].agg([np.sum, np.mean]))
    print(g_by_animal['weight'].agg([np.sum, np.mean]).reset_index())#in case you dont want the group names to be index

    # how do we rename these new columns? we use method chaining

    r = g_by_animal['weight'].agg([
            np.sum,
            np.mean
    ])\
    .rename(
        columns = {
            'sum':'sum_weight',
            'mean' :'average_weight'
        }
    )
    print(r)

    # print()
    # grpuby max weight
    # print(g_by_animal['weight'].max(), type(g_by_animal['weight'].max())

    # #give me the count of each animal
    # print(g_by_animal['animal'].count())

    # # give me total weight of all animals by their type
    # print(g_by_animal['weight'].sum())

    # def ends_with_at(animal_type):
    
    #     if animal_type.endswith('at'):
    #         return 'ends_with_at' # the group key
    #     else:
    #         return 'does_not_end_with_at'

    # a.index = a.animal

    # ## groupby can be used with callable..however function is applied on the index
    # g_by_ends_with_at = a.groupby(by = ends_with_at)

    # print(g_by_ends_with_at.groups.keys())
    # print(g_by_ends_with_at['weight'].max())
    # print(list(g_by_ends_with_at))

    # a.index = list(range(0, len(a)))
    # print(a)


perform_simple_groupby()