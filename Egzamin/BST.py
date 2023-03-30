class Node:
    def __init__(self, v = None):
        self.v = v
        self.p = None
        self.r = None
        self.l = None

def insert( root, v ):
    to_add = Node( v )
    prev = None
    while root != None:
        if root.v > to_add.v:
            prev = root
            root = root.l
        else:
            prev = root
            root = root.r

    if prev.v > to_add.v:
        prev.l = to_add
        to_add.p = prev
    else:
        prev.r = to_add
        to_add.p = prev

def maximum( root ):
    prev = None
    while root!=None:
        prev = root
        root = root.r
    return prev

def minimum( root ):
    prev = None
    while root!=None:
        prev = root
        root = root.l
    return prev

def prev( p ):
    if p.l:
        return maximum(p.l)
    
    while p == p.p.l:
        p=p.p
        if p.p == None:
            return None
    return p.p

def next( p ):
    if p.r:
        return minimum(p.r)

    while p == p.p.r:
        p=p.p
        if p.p == None:
            return None
    return p.p

def find( root, v ):
    
    while root != None and root.v !=v:
        if v > root.v:
            root = root.r
        else:
            root = root.l
    
    return root

def remove( to_del ):
    if to_del.l == to_del.r == None:
        if to_del.p.l == to_del:
            to_del.p.l = None
            to_del.p = None
        else:
            to_del.p.r = None
            to_del.p = None
    elif to_del.r == None:
        if to_del.p.r == to_del:
            to_del.p.r = to_del.l
            to_del.p = None
            to_del.l = None
        else:
            to_del.p.l = to_del.r
            to_del.p = None
            to_del.r = None
    elif to_del.l == None:
        if to_del.p.l == to_del:
            to_del.p.l = to_del.r
            to_del.p = None
            to_del.r = None
        else:
            to_del.p.r = to_del.l
            to_del.p = None
            to_del.l = None
    else:
        n = next( to_del )
        if n == n.p.l:
            n.p.l = None
        else:
            n.p.r = None
        
        n.p = to_del.p
        n.r = to_del.r
        n.l = to_del.l
        if to_del.p.l == to_del:
            to_del.p.l = n
        else:
            to_del.p.r = n
        to_del.p = None
        to_del.r = None
        to_del.l = None 



if __name__ == "__main__":
    root = Node( 10 )
    insert( root, 15 )
    insert( root, 8 )
    insert( root, 11 )
    insert( root, 9 )
    insert( root, 16 )

    remove(root.r)
    print(root.r.v)

