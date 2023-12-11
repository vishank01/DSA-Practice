def permute(ip,op=""):
    if len(ip)==0:
        print(op)
    else:
        permute(ip[1:],str(op)+str(ip[0]).lower())
        permute(ip[1:],str(op)+str(ip[0]).upper())

permute("Ad")