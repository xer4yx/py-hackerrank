if __name__ == '__main__':
    """x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    '''
    Instead of using nested loops to append the x,y,z values in the list,
    we used a nested list for a more concise result. 
    '''

    theList = [[i, j, k] for i in range(x + 1)
               for j in range(y + 1)
               for k in range(z + 1)
               if sum([i, j, k]) != n]

    print(theList)"""
    
    
    
    names = [
        'Angelo M. Bicomong',
        'Chris B. Brown',
        'Maria A. Ozawa'
    ]

    last = [n.split(' ')[-1] for n in names]
    print(last)