import pandas as panda
import numpy as np 

def slice_data_frame():
    
    aa = panda.DataFrame({'id':[1,2,3,4,5,6]})
    print(aa['id'][2:]) # selection from 3rd value onwards 

    a = panda.DataFrame({'id1':[1,2,3],'id2':[11,22,33]})

    # returns data frame
    print(a[['id1','id2']][1:], type(a[['id1','id2']][1:]) ,a[1:3])

    # returns data frame
    print(aa[1:4], ) ## fro 1st row till 3rd

def selection_data_frame_ilocation_based():
    '''

    we will look at the following : loc, iloc, conditional selection

    .iloc[<row_selection],<column_selection>] : returns dataframe(NOT ALWAYS)
        - just row selection is sufficient eg a.iloc[0], or a.iloc[[0,1,2]]
        - can also add column selection eg a.iloc[[0],[0,1]] or a.iloc[0,[1,2]]
        - can also support slicing eg a.iloc[:2], a.iloc[1:2,1:3]
        - when using single value it returns Series eg a.iloc[1]..all columns shown in transposed format
        - however when using list syntax returns eg a.iloc[[1]]..show in tabular format
        - if only one column is selected even in that case returns series eg a.iloc[:,3]
        - however this returns DataFrame a.iloc[:[3]]
        - we can pass a callable to apply condition selection

    '''
    a = panda.DataFrame( data = \
    
        {
            'id' : list(range(1,6)),
            'sex': ['M','M','F','F','M'], #np.random.choice(['M','F'], 5),
            'age' : np.random.randint(22,45,(5)),
            'salary': [2344.12, 2000,33,44555,1000],
            'name' : ['name1', 'name2', 'name3', 'name4', 'name5']

        }
    
    )
    print(a)

    ## select the top row 
    print(a.loc[0], type(a.loc[0]), type(a.loc[[0]])) ## returns a series, secnd syntax returns data frame
    print(a.iloc[0], type(a.iloc[0]), type(a.iloc[[0]])) ## returns a series, secnd syntax returns data frame
    print(type(a.iloc[:,3])) ## returns series since only one column selected
    print(type(a.iloc[:,[3]])) ## returns DataFrae even though only one column selected due to list syntax
    # print(a.iloc[0], type(a.iloc[0]), a.iloc[[1,2,3]], a.iloc[1,[2,3]])
    # print(a.iloc[:2], a.iloc[:,1:3])
    print('iloc selection: \n',a.iloc[lambda x : (x.sex=='M').values])

    # print(a[a.sex=='M'])





def selection_data_frame_label_based():
    '''

    loc is mainly used as a label selector. how it differs from iloc???

    so anytime a integer is passed in loc, it is essentially pointing to an index

    if i say a.iloc[5] - gives me 5th row
    if i say a.loc[5] - gives me the row with index as 5

    cool example below:

    >>> import pandas as panda
    >>> a = panda.Series( data = [1,2,3,4,5], index = [1,2,3,4,5])
    >>> p = panda.DataFrame({'id':a})
    >>> p
    id
    1   1
    2   2
    3   3
    4   4
    5   5
    >>> p.iloc[4]
    id    5
    Name: 5, dtype: int64
    >>> p.loc[4]
    id    4
    Name: 4, dtype: int64

    if not found , throws KeyError

    .loc[<row_selection],<column_selection>] : returns dataframe(NOT ALWAYS)
        - just row selection is sufficient eg a.loc[0](0th index), or a.loc[[0,1,2]]
        - can also add column selection eg a.loc[[0],['col_name','col_name']] ..HAS to be names
        - can also support slicing eg a.loc[:2] : all rows till index 2
        - can also support slicing in columns eg a.loc[:, 'col1':'col4'].. again if 1 series, if >1 dataframe
        - when using single value it returns Series eg a.iloc[1]..all columns shown in transposed format
        - however when using list syntax returns eg a.iloc[[1]]..show in tabular format
        - if only one row is selected even in that case returns series eg a.loc[3]
        - however this returns DataFrame a.loc[[3]]
        - conditional selection is possible. eg a.loc[a.sex=='M','id':'salary']
            - diff between a[a.sex==''M] is that in this syntax all columns are returned
             with a.loc[a.sex=='M',...] we have possibility of selecting columns

        - conditional selection with and condition a.loc[a.sex=='M' & a.salary >2500]

            IMP: The operators are: | for or, & for and, and ~ for not. 
                 These must be grouped by using parentheses

        - conditional selection: if you want to use string functions such as endswith you
        have to do a.loc[a.sex.str.endswith] cause a.sex is a series, a.sex.str is a string
        - we can pass a callable to apply condition selection

    '''
    a = panda.DataFrame( data = \
    
        {
            'id' : list(range(1,6)),
            'sex': ['M','M','F','F','M'], #np.random.choice(['M','F'], 5),
            'age' : np.random.randint(22,45,(5)),
            'salary': [2344.12, 2000,33,44555,1000],
            'name' : ['name1', 'name2', 'name3', 'name4', 'name5']

        }
    
    )
    print(a)

    ## select the top row 
    print(a.loc[1], '\n', a.loc[[1]],type(a.loc[1]), type(a.loc[[1]])) ## returns a series, secnd syntax returns data frame
    
    print(a.loc[:,'id':'salary']) ## returns dataframe since more than one column selected
    print(a.loc[:,'id'], type(a.loc[:,'id'])) ## returns series since more than one column selected

    ## VVIMP: without brackets & doest work
    print(a.loc[a.sex=='M'], '\n', a.loc[(a.sex=='M') & (a.name=='name1')])
    print(a.loc[(a.sex=='F') & (a.salary >2500)])
    print(a.loc[a.sex.str.startswith('M')])

    ## it is possible to take the selector out for easier code read

    selector = a.sex.str.startswith('M')
    print(a.loc[selector])

def selection_based_on_iat_or_at():
    '''

    selections using [] or loc or iloc needs to handle a lot of cases
    such as row evaluation, slice evaluation etc etc. if you need to have
    exact scalar value, what might be faster is iat or at

    '''

    a = panda.DataFrame( data = \
    
        {
            'id' : list(range(1,6)),
            'sex': ['M','M','F','F','M'], #np.random.choice(['M','F'], 5),
            'age' : np.random.randint(22,45,(5)),
            'salary': [2344.12, 2000,33,44555,1000],
            'name' : ['name1', 'name2', 'name3', 'name4', 'name5']

        }
    
    )
    
    print(a)

    print(a.iat[4,2]) ## returns the 3rd col of 5th row(since indices start from 0)

    print(a.at[4,'sex']) ## returns sex value of the row with index 4
    print(a.at[2,'salary'])
    a.at[2,'salary'] = 1 ##value can be set..similar to loc
    print(a)

def selection_where_clause():
    '''

    a = id:[1,2,3,4,1,1,.4]

    if we do a[a.id<=1] we get [1,1,1,.4] all rows which validates the condition.
    the size of the returned dataframe/series may or may nt be same

    where clause returns with the same size. the values which are not matched are 
    returned as NaN

    so a.where[a.id <=1] = [1,NaN,NaN,NaN,NaN,1,1,0.4]


    '''

    a = panda.DataFrame( data = \
    
        {
            'id' : list(range(1,6)),
            'sex': ['M','M','F','F','M'], #np.random.choice(['M','F'], 5),
            'age' : np.random.randint(22,45,(5)),
            'salary': [2344.12, 2000,33,44555,1000],
            'name' : ['name1', 'name2', 'name3', 'name4', 'name5']

        }
    
    )
    
    print(a)
    print(a.where(a.sex=='M'), type(a.where(a.sex=='M')))

    ##you can also replae NaN with smething else
    print(a.where(a.sex=='M', 'blablaaablaaa'))

def selection_using_query_expression():

    a = panda.DataFrame( data = \
    
        {
            'id' : list(range(1,6)),
            'sex': ['M','M','F','F','M'], #np.random.choice(['M','F'], 5),
            'age' : np.random.randint(22,45,(5)),
            'salary': [2344.12, 2000,33,44555,1000],
            'name' : ['name1', 'name2', 'name3', 'name4', 'name5']

        }
    
    )
    
    print(a)
    sex_i_want = 'F'
    age_i_want =30
    print(a.query("sex == @sex_i_want & age <@age_i_want"))    

selection_using_query_expression()
# selection_where_clause()
# selection_based_on_iat_or_at()
# selection_data_frame_label_based()
# selection_data_frame_ilocation_based()
# slice_data_frame()

