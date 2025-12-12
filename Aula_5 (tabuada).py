
# TABUADA 
multiplicador = int(input('='))
v  =  [0,1,2,3,4,5,6,7,8,9,10]
v2  =  list(range(11))

for valores in v:
    ca =  multiplicador * valores
    print( multiplicador, 'X', valores, '=', ca)