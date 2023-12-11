def permute(ip,op=""):
    if len(ip)==0:
        print(op)
    else:
        if str(ip).isdigit():
            permute(ip[1:],op+ip[0])
        else:
            permute(ip[1:],op+ip[0].lower())
            permute(ip[1:],op+ip[0].upper())
        
permute("a1b2")