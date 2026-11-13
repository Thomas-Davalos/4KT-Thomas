#crear un programa que me permita ver si un usuario es niño, adolescente, un adulto 
#o un adulto mayor

usuario_edad = 26

print("=== SECCION 2: Control de flujo con condicionales ===")

if usuario_edad < 5:
    print("El usuario es de primera infancia.")
elif usuario_edad < 11:
    print("El usuario es un niño.")          
elif usuario_edad < 18:
    print("El usuario es un adolecente.")
elif usuario_edad <=26:
    print("El usuario es de juventud.")    
elif usuario_edad <= 60:
    print("El usuario es un adulto.")
elif usuario_edad > 60:
    print("El usuario es un adulto mayor.")
    
print(f"El usuario tiene {usuario_edad} años.")
    