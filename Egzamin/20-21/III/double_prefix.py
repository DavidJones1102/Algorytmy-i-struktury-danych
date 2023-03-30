from zad2testy import runtests

class Node:
    def __init__(self):
        self.p = None
        self.z = None
        self.j = None
        self.counter = 1
def add( root, s ):
    for i in range( len(s) ):
        if s[i] == '1':
            if root.j == None:
                to_add = Node()
                to_add.p = root
                root.j = to_add
                root = root.j
            else:
                root=root.j
                root.counter+=1
        else:
            if root.z == None:
                to_add = Node()
                to_add.p = root
                root.z = to_add
                root = root.z
            else:
                root=root.z
                root.counter+=1
 

def double_prefix( L ):
    root = Node()
    for s in L:
        add( root, s)
    
    s = ''
    ans = []
    def _search_ans( root, s ):
        nonlocal ans
        if (root.j and root.j.counter >= 2) or (root.z and root.z.counter >= 2):
            if (root.j and root.j.counter >= 2):
                _search_ans( root.j, s+'1' )
            if (root.z and root.z.counter >= 2):
                _search_ans( root.z, s+'0' )
        elif root.counter >= 2:
            ans.append(s)
        
    _search_ans( root, '')

    
    return ans


runtests( double_prefix )
