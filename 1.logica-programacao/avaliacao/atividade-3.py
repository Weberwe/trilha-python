# escala = 
# escalas_convertidas =
# #Celsius-> kelvin
# c = k - 273
# #Celsius-> Fahrenheit

#Fahrenheit->Celsius

#Fahrenheit->kelvin

#kelvin

#kelvin
#qual tipo de conversão deseja fazer tem que ser do tipo float
print("utilize c para celsius /n k para kelvin /n f para fahrenheit :")
conversao = input ('Escolha qual conversão de temperatura para converter utilizando "_" EX: k_c_f :')
numero = float(input('Digite a temperatura :'))

k_c = (numero - 273)
k_f= (numero -273) *1.8+32
c_k= (numero + 273)
c_f= (numero * 1.8 + 32) 
f_c= c =(numero -32)/1.8
f_k=(numero -32)*(5/9) + 273


#escala = input(' :')


# float(escala_convertidas)
# conversao_final = input ('Escolha qual conversão de temperatura quer fazer :')
if conversao == k_c:
    print (k_c)
elif conversao == k_f:
    print (k_f)
elif conversao == c_k:
    print (c_k)
elif conversao == f_c:
    print(f_c)    
elif conversao == c_f:
    print(c_f)
elif conversao == f_k:
    print(f_k)



#convck = input('digite a c')




