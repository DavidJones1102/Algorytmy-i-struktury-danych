class Node:
    def __init__(self, v = None):
        self.v = v
        self.p = None
        self.g = None # r
        self.a = None # m
        self.c = None # l
        self.counter = 0

# inserts one char
def insert( root, v ):
    if v == 'G':
        if root.g == None:
            to_add = Node( v )
            root.g = to_add
            to_add.p = root
            
        return root.g
    elif v == 'A':
        if root.a == None:
            to_add = Node( v )
            root.a = to_add
            to_add.p = root
            
        return root.a
    elif v == 'C':
        if root.c == None:
            to_add = Node( v )
            root.c = to_add
            to_add.p = root
            
        return root.c

# adds string
def add( root, s):
    n = len( s )
    for i in range( n ):
        root = insert( root, s[i] )
    root.counter += 1



def DNA( T ):
    n = len( T )
    root = Node( None )
    for i in range( n ):
        add( root, T[i] )
    c = 0
    c = count( root, c)
    return c

def count( root, c ):
    if root.a:
        c = count( root.a, c)
    if root.c:
        c = count( root.c, c)
    if root.g:
        c = count( root.g, c)

    if root.counter == 2:
        c+=1
    
    return c




T = [ 'GGAC','GGA','CGA','CGA','GGA']

print( DNA( T ) )


