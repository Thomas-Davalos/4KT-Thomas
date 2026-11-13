print("=== SECCIÓN 1: Evaluando Expresiones Lógicas ===")

edad_estudiante = 26
tiene_carnet = True
promedio_notas = 15


es_mayor_de_edad = edad_estudiante >= 26

if(es_mayor_de_edad):{
    print(f"El estudiante sí es mayor de edad y tiene({edad_estudiante} años)")
}
else:{
    print(f"El estudiante no es mayor de edad y tiene({edad_estudiante} años)")
}

elegible_beca = (es_mayor_de_edad) and (promedio_notas >= 9.5) and tiene_carnet
print(f"¿Es elegible para la beca de liderazgo?: {elegible_beca}")

necesita_refuerzo = not (promedio_notas >= 9.5)
print(f"¿Necesita refuerzo académico?: {necesita_refuerzo}\n")

print("El estudiante cumple con los siguientes criterios:")
if(es_mayor_de_edad):
    print("- Es mayor de edad")
if(promedio_notas >= 9.5):
    print("- Tiene un buen promedio académico")
if(tiene_carnet):
    print("- Tiene carnet de estudiante")

print("Por lo tanto, el estudiante es alegible para la beca.\n")