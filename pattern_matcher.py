#solve pattern matching problem

# pattern - xxyxx
# sentence - sosolionsoso 
# This sentence follows the pattern


def fix_pattern(pattern):
    #This makes sure that the pattern starts from 'x'
    if(pattern[0] == 'x'):
        return pattern
    else:
        pattern = ''.join(['x' if pattern[i] == 'y' else 'y' for i in range(len(pattern))])

    return pattern

def x_and_y_lengths(length_sentence, dic_xy, x):
    #this finds the possible values of x and y lengths
    x_part = x*dic_xy['x']
    y_part = length_sentence - x_part
    if(y_part/dic_xy['y'] == y_part//dic_xy['y']):
        return len(y_part)
    else:
        return False




    
