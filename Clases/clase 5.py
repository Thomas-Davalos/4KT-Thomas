try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("fallo matematico")
else:
    print("No se ha producido ningun error. El calculo es correcto.")
finally:
    print("El programa finaliza sin detenerse. Entorno limpio.")