

def my_sum(x, y):
    '''
    Takes in two numbers (x and y) and returns
    it's sum.

    '''
    if type(x) == str or type(y) == str:
    	raise TypeError
    else:
    	return x + y
