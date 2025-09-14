class CalculadoraBasica:
    def __init__(self):
        self.historial = []
    
    def suma(self, a, b):
        resultado = a + b
        self._agregar_al_historial(f"{a} + {b} = {resultado}")
        return resultado
    
    def resta(self, a, b):
        resultado = a - b
        self._agregar_al_historial(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicacion(self, a, b):
        resultado = a * b
        self._agregar_al_historial(f"{a} * {b} = {resultado}")
        return resultado
    
    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        resultado = a / b
        self._agregar_al_historial(f"{a} / {b} = {resultado}")
        return resultado
    
    def _agregar_al_historial(self, operacion):
        self.historial.append(operacion)
        # Mantener solo las últimas 10 operaciones
        if len(self.historial) > 10:
            self.historial.pop(0)
    
    def mostrar_historial(self):
        print("\n--- Historial de Operaciones ---")
        for operacion in self.historial:
            print(operacion)
        print("-------------------------------\n")

def main():
    calc = CalculadoraBasica()
    
    while True:
        print("\nCalculadora Básica")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Ver historial")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "6":
            print("Chau")
            break
        
        if opcion == "5":
            calc.mostrar_historial()
            continue
        
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == "1":
                    resultado = calc.suma(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcion == "2":
                    resultado = calc.resta(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcion == "3":
                    resultado = calc.multiplicacion(num1, num2)
                    print(f"Resultado: {resultado}")
                elif opcion == "4":
                    resultado = calc.division(num1, num2)
                    print(f"Resultado: {resultado}")
                    
            except ValueError:
                print("Error: Por favor ingresa números válidos.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Opción no válida. Por favor selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()
