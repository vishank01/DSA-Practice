def solve(ip):
    solveHelper(ip[1:],ip[0])


def solveHelper(ip,op):
    if len(ip)==0:
        print(op)
    else:
        solveHelper(ip[1:],op+f" {ip[0]}")
        solveHelper(ip[1:],op+ip[0])
solve("abc")
