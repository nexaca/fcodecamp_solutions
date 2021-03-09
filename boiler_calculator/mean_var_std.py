import numpy as np

def calculate(anylist):
    while True:

        my_array = np.array(anylist)
        
        if my_array.size != (3,3):
            raise ValueError( "List must contain nine numbers." )

        else:
            my_array = my_array.reshape((3,3))  
    

        #stds
        std_1 = my_array.std()
        std_2 = my_array.std(axis = 0)
        std_3 = my_array.std(axis = 1)      

        #mean 
        mean_1 = my_array.mean()
        mean_2 = my_array.mean(axis = 0)
        mean_3= my_array.mean(axis = 1)     

        #max
        max_1 = my_array.max()
        max_2 = my_array.max(axis = 0)
        max_3 = my_array.max(axis = 1)      

        #min
        min_1 = my_array.min()
        min_2 = my_array.min(axis = 0)
        min_3 = my_array.min(axis = 1)      

        #sum
        sum_1 = my_array.sum()
        sum_2 = my_array.sum(axis = 0)
        sum_3 = my_array.sum(axis = 1)      
    

        calculations = {
        "mean" :[mean_1,mean_2,mean_3], 
        'standart': [std_1, std_2, std_3],
        "max" : [max_1, max_2,max_3],
        "min" : [min_1, min_2,min_3],
        'sum' : [sum_1,sum_2,sum_3]
        }


        return calculations
        break

