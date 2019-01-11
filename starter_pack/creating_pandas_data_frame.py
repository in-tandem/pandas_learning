import pandas as panda 
import numpy as np 

def create_panda_data_frame():
    '''
        there are two primary data structure in pandas
        
        1. panda series : container for scalar values. NOT SIZE MUTABLE
        2. panda data frame : container for series. COLUMNS CAN BE ADDED,MUTABLE
    

        panda dataframe: General 2D labeled, size-mutable tabular \
                         structure with potentially heterogeneously-typed column
                         pandas.core.frame.DataFrame
        how to create a pandas data series??
        pandas.DataFrame(data=None, index=None, dtype=None, columns=None, copy=False)

        data: can be 2d ndarray, another dataframe, dict, panda.Series values
        dtype: is a python dtype. can be provided. if provided will be forced on all
        index: needs to be hashable,doesnt need to be unique. if not provided will be rangeindex(0,n)
        columns: will default to rangeinedx(0,n)if not provided.


    '''
    
    ## from 2d ndarrays / list
    print(panda.DataFrame(np.random.randint(1,14,(2,4))))
    print(panda.DataFrame([[1,2],[3,4]]))
    print(panda.DataFrame([[1,2],[3,4]], dtype = np.float32)) #forcing to a particular dtype
    print(panda.DataFrame(data = [[1,2],[3,4]], columns = ['a','b'])) ##column needs to be arraylike..so list/tuple/etc
    print(panda.DataFrame(data = [[1,2],[3,4]], columns = ['a','b'], \
                            index = [11,22])) ##passing index


    ## from panda.Series
    print(panda.DataFrame(data = panda.Series(data = np.random.randint(1,22,(4)))))

    ##this creates a 2*4 array. and even boolean gets converted to int ie 1/0
    ## however the same will not be the case if we pass it as a dict 
    print(panda.DataFrame(data = \
        [
            panda.Series(np.random.randint(1,33,(4))),
            panda.Series(np.random.choice([True,False], 4))

        ],
        )
    )

    ## this will be 4*2 with each column gettings its own
    print(panda.DataFrame(data = \
        {
            'id'    :   panda.Series(np.random.randint(1,33,(4))),
            'val'   :   panda.Series(np.random.choice([True,False], 4))

        },
        )
    )

    ## lets see what happens when individual indices are diff
    ## this will result in 8*2 table structure. with 4 nan against 1,2,3,4
    ## and 4 NaN againt 11,22,33,44
    print(panda.DataFrame(data = \
        {
            'id'    :   panda.Series(np.random.randint(1,33,(4)), index = [1,2,3,4]),
            'val'   :   panda.Series(np.random.choice([True,False], 4), index = [11,22,33,44])

        },
        )
    )

    ## this will result in entire table having NaN values
    print(panda.DataFrame(data = \
        {
            'id'    :   panda.Series(np.random.randint(1,33,(4)), index = [1,2,3,4]),
            'val'   :   panda.Series(np.random.choice([True,False], 4), index = [11,22,33,44])

        },\
        index = ['aa','bb','cc','dd']
        )
    )

def create_panda_data_series():
    '''
        there are two primary data structure in pandas
        
        1. panda series : container for scalar values. NOT SIZE MUTABLE
        2. panda data frame : container for series. COLUMNS CAN BE ADDED,MUTABLE
    
        panda series: 1D labeled homogeneously-typed(means only singular datatype in one series) array.\
                      Its essentially a 1d ndarray with axis labels(index). labels must be hashable.
                      Since its stored as a ndarray , it has methods like dtype/shape attributes. 
                      Also it can be passed to most numpy functions that expects ndarray as well
                      Meaning vectorixation is possible 
                      pandas.core.series.Series

        panda dataframe: General 2D labeled, size-mutable tabular \
                         structure with potentially heterogeneously-typed column


        how to create a pandas data series??
        pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

        data: can be ndarray,list, dict,scalar values
        dtype: is a python dtype. can be provided. if not provided will be inferred
        index: needs to be hashable,doesnt need to be unique. if not provided will be rangeindex(0,n)

    '''
    
    ##creation from a list
    print(panda.Series(data = [1,2,3,3,45,5])) #dtype has been inferred.inde auto assigned
    print(panda.Series(data = [1,2,3,3], dtype=np.float32))


    ##creation from a scalar value
    print(panda.Series(5))
    print(panda.Series(5, index = ['a','a','aa','aaa'])) # will be repeated based on index

    ##creation from ndarray values
    print(panda.Series(np.random.randint(1,3,(6))))
    # print(panda.Series(np.random.randint(1,3,(6,1))))#will give error since series expects 1d
    print(panda.Series(np.random.randint(1,5,(4)), index = [11,22,33,44,]))

    ## will fail..if index passed it needs to be same size
    # print(panda.Series(np.random.randint(1,5,(4)), index = [11,22,33,]))
    print(panda.Series(np.random.choice([True,False],6)))

    ##from dict
    print(panda.Series(dict(a=1,b=2,c=33,d=44))) ##order will be maintained, keys will be index

    ## you will see that index has certain values which are not keys in the dict
    ## for those particular rows,index will be set but value will be NaN
    ## like in below eg, index 1,22,33 will have value NaN
    ## whereas index c will have value True
    print(panda.Series(dict(a=True,b=False,c=True) , index= [1,22,33,'c'])) #index will override dict keys


    ##lets try slicing series : as expected returns ndarray

    a = panda.Series(np.random.randint(1,6,(6)))
    print('slicing :', a , a[1], type(a[1]), a[:4]) 


    ## can be used in most np functions
    b = panda.Series(np.random.randint(1,4,(6)))

    print('additiona of twp panda series: ',np.add(a,b))

    ## lets see what happens when see add up two series
    ## this works off index..same indices will be added
    ## what happens when a index is not present, will result in NaN
    print('addition of a:', a ,'\n with b : ', b , '\n reslt: ', a+b)

    a = panda.Series({'a':1,'b':2})
    b = panda.Series({'a':10, 'c':30,'b':20})

    print(a+b) ##c will be present but will be NaN



create_panda_data_frame()
# create_panda_data_series()