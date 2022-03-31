#En pyhton las variables pueden cambiar de tipo
#Como en la mayoria de los lenguajes dinamicos

var_one = 42
var_one = "Karen"

print(var_one)

#Cambiar tipos de variables
var_two = 50.34
var_two_str = str(var_two)
var_two_float = float(var_two)
var_two_int = int(var_two)

print(var_two_str)
print(var_two_float)
print(var_two_int)

#obteniendo el tipo de la variable
print(type(var_two))
print(type(var_two_str))
print(type(var_two_float))
print(type(var_two_int))

#los nombres de las variables no pueden tener espacios
#ni operaciones matematicas y tampoco partir con un numero

# 2var = 42, esta variable esta mala,  no puede empezar con numero
# my-var = 42, esta variable esta mala, no puede tener el signo guin medio -
# my var = 42, esta variable esta mala, no puede tener espacios en las variables

