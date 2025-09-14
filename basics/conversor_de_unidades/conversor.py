"""
Unit Converter
Author: [Your Name]
Date: [Date]
Description: A simple unit converter that handles length, temperature, and weight conversions.
"""

class UnitConverter:
    def __init__(self):
        self.conversion_history = []
    
    # Length conversions
    def length_convert(self, value, from_unit, to_unit):
        conversions = {
            'm': 1.0,
            'km': 0.001,
            'cm': 100.0,
            'mm': 1000.0,
            'inch': 39.3701,
            'foot': 3.28084,
            'yard': 1.09361,
            'mile': 0.000621371
        }
        
        try:
            value_in_meters = value / conversions[from_unit]
            result = value_in_meters * conversions[to_unit]
            self._add_to_history(f"{value} {from_unit} → {result:.4f} {to_unit}")
            
            return round(result, 4)
        except KeyError:
            raise ValueError("Unidad no válida")
    
    # Temperature conversions
    def temperature_convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == 'f':
            celsius = (value - 32) * 5/9
        elif from_unit == 'k':
            celsius = value - 273.15
        else:  # already celsius
            celsius = value
        
        # Convert from Celsius to target unit
        if to_unit == 'f':
            result = (celsius * 9/5) + 32
        elif to_unit == 'k':
            result = celsius + 273.15
        else:  # to celsius
            result = celsius
        
        # Add to history
        self._add_to_history(f"{value}°{from_unit.upper()} → {result:.2f}°{to_unit.upper()}")
        
        return round(result, 2)
    
    # Weight conversions
    def weight_convert(self, value, from_unit, to_unit):
        conversions = {
            'kg': 1.0,
            'g': 1000.0,
            'mg': 1000000.0,
            'lb': 2.20462,
            'oz': 35.274
        }
        
        try:
            # Convert to kg first, then to target unit
            value_in_kg = value / conversions[from_unit]
            result = value_in_kg * conversions[to_unit]
            
            # Add to history
            self._add_to_history(f"{value} {from_unit} → {result:.4f} {to_unit}")
            
            return round(result, 4)
        except KeyError:
            raise ValueError("Unidad no válida")
    
    def _add_to_history(self, conversion):
        self.conversion_history.append(conversion)
        # Keep only last 10 conversions
        if len(self.conversion_history) > 10:
            self.conversion_history.pop(0)
    
    def show_history(self):
        print("\n--- Historial de Conversiones ---")
        for i, conversion in enumerate(self.conversion_history, 1):
            print(f"{i}. {conversion}")
        print("--------------------------------\n")

def main():
    converter = UnitConverter()
    
    # Unit abbreviations
    length_units = ['m', 'km', 'cm', 'mm', 'inch', 'foot', 'yard', 'mile']
    temp_units = ['c', 'f', 'k']  # c=celsius, f=fahrenheit, k=kelvin
    weight_units = ['kg', 'g', 'mg', 'lb', 'oz']
    
    while True:
        print("\nConversor de Unidades")
        print("1. Longitud")
        print("2. Temperatura")
        print("3. Peso")
        print("4. Ver historial")
        print("5. Salir")
        
        choice = input("Selecciona una opción (1-5): ")
        
        if choice == '5':
            print("Chau")
            break
        
        if choice == '4':
            converter.show_history()
            continue
        
        try:
            if choice == '1':
                print("\nConversión de Longitud")
                print("Unidades disponibles: m, km, cm, mm, inch, foot, yard, mile")
                value = float(input("Valor a convertir: "))
                from_unit = input("De unidad: ").lower()
                to_unit = input("A unidad: ").lower()
                
                if from_unit not in length_units or to_unit not in length_units:
                    print("Error: Unidad no válida")
                    continue
                
                result = converter.length_convert(value, from_unit, to_unit)
                print(f"Resultado: {result} {to_unit}")
            
            elif choice == '2':
                print("\nConversión de Temperatura")
                print("Unidades disponibles: c (Celsius), f (Fahrenheit), k (Kelvin)")
                value = float(input("Valor a convertir: "))
                from_unit = input("De unidad (c/f/k): ").lower()
                to_unit = input("A unidad (c/f/k): ").lower()
                
                if from_unit not in temp_units or to_unit not in temp_units:
                    print("Error: Unidad no válida")
                    continue
                
                result = converter.temperature_convert(value, from_unit, to_unit)
                print(f"Resultado: {result}°{to_unit.upper()}")
            
            elif choice == '3':
                print("\nConversión de Peso")
                print("Unidades disponibles: kg, g, mg, lb, oz")
                value = float(input("Valor a convertir: "))
                from_unit = input("De unidad: ").lower()
                to_unit = input("A unidad: ").lower()
                
                if from_unit not in weight_units or to_unit not in weight_units:
                    print("Error: Unidad no válida")
                    continue
                
                result = converter.weight_convert(value, from_unit, to_unit)
                print(f"Resultado: {result} {to_unit}")
            
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
