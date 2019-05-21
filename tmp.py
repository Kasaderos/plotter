import matplotlib

TNUMBER = 0
TOP1 = 1
TOP2 = 2
TVAR = 3
TFUNCALL = 4

def check(expr, values = {}):
    values = values or {}
    nstack = []
    L = len(expr.tokens)
    for item in expr.tokens:
        type_ = item.type_
        if type_ == TNUMBER:
            nstack.append(item.number_)
        elif type_ == TOP2:
            n2 = nstack.pop()
            n1 = nstack.pop()
            f = expr.ops2[item.index_]
            nstack.append(f(n1, n2))
        elif type_ == TVAR:
            if item.index_ in values:
                nstack.append(values[item.index_])
            elif item.index_ in expr.functions:
                nstack.append(expr.functions[item.index_])
            else:
                return False # undefined variable:  item.index_
        elif type_ == TOP1:
            n1 = nstack.pop()
            f = expr.ops1[item.index_]
            nstack.append(f(n1))
        elif type_ == TFUNCALL:
            n1 = nstack.pop()
            f = nstack.pop()
            if callable(f):
                if type(n1) is list:
                    nstack.append(f(*n1))
                else:
                    nstack.append(f(n1))
            else:
                return False #f  is not a function
        else:
            return False # invalid Expression
    if len(nstack) > 1:
        return False # invalid Expression (parity)
    return True



def f(a, b):
    return a + b

fs = []
#parser = matplotlib.mathtext.Parser()

exec("f(1,2)")
