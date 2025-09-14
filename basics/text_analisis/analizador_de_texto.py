import re
from collections import Counter

class TextAnalyzer:
    def __init__(self):
        self.analysis_history = []
    
    def analyze_text(self, text):
        """Main analysis function that returns all statistics"""
        if not text.strip():
            raise ValueError("El texto no puede estar vacío")
        
        analysis = {
            'character_count': self._count_characters(text),
            'word_count': self._count_words(text),
            'sentence_count': self._count_sentences(text),
            'line_count': self._count_lines(text),
            'word_frequency': self._word_frequency(text),
            'most_common_words': self._most_common_words(text),
            'text_length': len(text),
            'average_word_length': self._average_word_length(text),
            'reading_time': self._estimate_reading_time(text)
        }
        
        # Add to history
        self._add_to_history(analysis)
        
        return analysis
    
    def _count_characters(self, text):
        """Count characters excluding spaces"""
        return len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    
    def _count_words(self, text):
        """Count words using regex to handle various word boundaries"""
        words = re.findall(r'\b\w+\b', text.lower())
        return len(words)
    
    def _count_sentences(self, text):
        """Count sentences using punctuation marks"""
        sentences = re.split(r'[.!?]+', text)
        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    
    def _count_lines(self, text):
        """Count lines in the text"""
        return text.count('\n') + 1 if text else 0
    
    def _word_frequency(self, text):
        """Calculate word frequency"""
        words = re.findall(r'\b\w+\b', text.lower())
        return dict(Counter(words))
    
    def _most_common_words(self, text, n=5):
        """Get n most common words"""
        words = re.findall(r'\b\w+\b', text.lower())
        return Counter(words).most_common(n)
    
    def _average_word_length(self, text):
        """Calculate average word length"""
        words = re.findall(r'\b\w+\b', text)
        if not words:
            return 0
        total_length = sum(len(word) for word in words)
        return round(total_length / len(words), 2)
    
    def _estimate_reading_time(self, text, words_per_minute=200):
        """Estimate reading time in minutes"""
        word_count = self._count_words(text)
        minutes = word_count / words_per_minute
        return round(max(0.1, minutes), 1)  # At least 0.1 minutes
    
    def _add_to_history(self, analysis):
        """Add analysis to history"""
        summary = f"Text: {analysis['text_length']} chars, {analysis['word_count']} words"
        self.analysis_history.append({
            'summary': summary,
            'analysis': analysis
        })
        # Keep only last 5 analyses
        if len(self.analysis_history) > 5:
            self.analysis_history.pop(0)
    
    def show_history(self):
        """Display analysis history"""
        print("\n--- Historial de Análisis ---")
        for i, item in enumerate(self.analysis_history, 1):
            print(f"{i}. {item['summary']}")
        print("-----------------------------\n")
    
    def display_analysis(self, analysis):
        """Display analysis results in a formatted way"""
        print("\n" + "="*50)
        print("ANÁLISIS DE TEXTO")
        print("="*50)
        
        print(f"Longitud del texto: {analysis['text_length']} caracteres")
        print(f"Caracteres (sin espacios): {analysis['character_count']}")
        print(f"Palabras: {analysis['word_count']}")
        print(f"Oraciones: {analysis['sentence_count']}")
        print(f"Líneas: {analysis['line_count']}")
        print(f"Longitud promedio de palabras: {analysis['average_word_length']} caracteres")
        print(f"Tiempo estimado de lectura: {analysis['reading_time']} minutos")
        
        print(f"\n🗣️ Palabras más comunes:")
        for word, count in analysis['most_common_words']:
            print(f"   '{word}': {count} veces")
        
        print("="*50)

def get_text_input():
    """Get text input from user with multiple options"""
    print("\n¿Cómo quieres ingresar el texto?")
    print("1. Escribir texto directamente")
    print("2. Ingresar texto multilínea (terminar con 'END' en una línea)")
    print("3. Volver al menú principal")
    
    choice = input("Selecciona una opción (1-3): ")
    
    if choice == '3':
        return None
    
    if choice == '1':
        print("\nEscribe tu texto (presiona Enter cuando termines):")
        text = input()
        return text
    
    elif choice == '2':
        print("\nEscribe tu texto (escribe 'END' en una línea separada para terminar):")
        lines = []
        while True:
            line = input()
            if line.upper() == 'END':
                break
            lines.append(line)
        return '\n'.join(lines)
    
    else:
        print("Opción no válida")
        return None

def main():
    analyzer = TextAnalyzer()
    
    while True:
        print("\nAnalizador de Texto")
        print("1. Analizar texto")
        print("2. Ver historial de análisis")
        print("3. Salir")
        
        choice = input("Selecciona una opción (1-3): ")
        
        if choice == '3':
            print("Chau")
            break
        
        if choice == '2':
            analyzer.show_history()
            continue
        
        if choice == '1':
            text = get_text_input()
            if text is None:
                continue
            
            try:
                analysis = analyzer.analyze_text(text)
                analyzer.display_analysis(analysis)
                
                # Ask if user wants to see full word frequency
                see_full = input("\n¿Ver frecuencia completa de palabras? (s/n): ").lower()
                if see_full == 's':
                    print("\nFrecuencia de todas las palabras:")
                    for word, count in analysis['word_frequency'].items():
                        print(f"   '{word}': {count}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
