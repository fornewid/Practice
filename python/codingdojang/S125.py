class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data


def make_tree(s):
    S = []
    prev = None
    for c in s:
        if c == ')':
            if prev == ',':
                S.append(None)
            # print([str(item) for item in S])
            r = S.pop(-1)
            l = S.pop(-1)
            S[-1].right = r
            S[-1].left = l
        elif c == ',':
            if prev == '(':
                S.append(None)
        elif c != '(':
            S.append(Tree(c))
        prev = c
    return S[0]


def inorder(node, h=1, L=[]):
    if node is not None:
        inorder(node.left,  h + 1, L)
        L.append((node.data, h))
        inorder(node.right, h + 1, L)
        return L
    return None

L = inorder(make_tree('n(k(c(a,h(g(e,),)),m),u(p(,s(q,)),))'))
for i in range(len(L)):
    print("%s %d %d" % (L[i][0], i+1, L[i][1]))
