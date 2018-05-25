country = {'usa': ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7'],
      'ukraine': ['20.20.20.1','20.20.20.2','20.20.20.3','20.20.20.4','20.20.20.5','20.20.20.6','20.20.20.7'],
      'europe': ['30.30.30.1','30.30.30.2','30.30.30.3','30.30.30.4','30.30.30.5','30.30.30.6','30.30.30.7'],
      'asia': ['40.40.40.1','40.40.40.2','40.40.40.3','40.40.40.4','40.40.40.5','40.40.40.6','40.40.40.7']
}

def identity(ip, country):
    res = None
    for k, v in country.items():
        if ip in v:
            res =  k
    if res == None:
        res = ("IP %r not found" %ip)
    return res

test_ip = raw_input("Input ip: ")
print identity(test_ip,country)

