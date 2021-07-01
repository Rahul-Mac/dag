# Author: Rahul Mac
# Directed Acyclic Graph (DAG)

def build_graph(code):
    graph = {}
    order = []
    for c in code:
        lhs = True
        chk = False
        exp = ""
        idn = ""
        for i in c:
            if chk:
                idn += i 
            if lhs:
                exp = i
                lhs = False
            if i == "=":
                chk = True
        order.append(exp)
        graph[exp] = idn
    return graph, order

def display_graph(graph, order):
    operators =  ["+", "-", "*", "/", "^"]
    for key in order:
        c = True
        l = ""
        r = ""
        o = ""
        val = graph[key]
        for i in val:
            if c and i not in operators:
                l = i
            if i in operators:
                o = i
                c = False
            if not c:
                r = i
        if c:
            print(key+" = "+l)
        else:
            print(l+"->"+o+"<-"+r+"\tExpression = "+key)
            

code = ["x=a+b", "y=x+c", "z=x+y", "q=z"]
graph, order = build_graph(code)
display_graph(graph, order)
