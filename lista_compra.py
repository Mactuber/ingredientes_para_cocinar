import csv
import os

# Base de datos de ingredientes por plato
INGREDIENTES_PLATOS = {
    "Ensalada mixta": ["lechuga", "tomate", "cebolla", "aceite de oliva", "vinagre", "sal"],
    "Gazpacho andaluz": ["tomate", "pepino", "pimiento", "cebolla", "ajo", "aceite de oliva", "vinagre", "pan", "sal"],
    "Paella de marisco": ["arroz", "gambas", "mejillones", "calamares", "pimiento rojo", "ajo", "aceite de oliva", "azafrán", "caldo de pescado"],
    "Lentejas estofadas": ["lentejas", "cebolla", "zanahoria", "ajo", "tomate", "pimiento", "aceite de oliva", "laurel", "pimentón"],
    "Cocido madrileño": ["garbanzos", "carne de ternera", "chorizo", "morcilla", "tocino", "hueso de jamón", "patata", "col", "zanahoria"],
    "Fabada asturiana": ["fabes", "chorizo", "morcilla", "lacón", "ajo", "cebolla", "aceite de oliva", "pimentón"],
    "Pasta boloñesa": ["pasta", "carne picada", "tomate", "cebolla", "zanahoria", "apio", "vino tinto", "aceite de oliva", "queso parmesano"],
    "Pizza margarita": ["masa de pizza", "tomate triturado", "mozzarella", "albahaca", "aceite de oliva"],
    "Tortilla de patata": ["huevos", "patatas", "cebolla", "aceite de oliva", "sal"],
    "Pollo al horno con verduras": ["pollo", "patatas", "cebolla", "pimiento", "zanahoria", "aceite de oliva", "romero", "ajo"],
    "Salmón a la plancha": ["salmón", "limón", "aceite de oliva", "sal", "pimienta"],
    "Bacalao al pil pil": ["bacalao", "ajo", "aceite de oliva", "guindilla"],
    "Albóndigas en salsa de tomate": ["carne picada", "huevo", "pan rallado", "ajo", "perejil", "tomate", "cebolla", "aceite de oliva"],
    "Empanada gallega": ["masa de empanada", "atún", "cebolla", "pimiento", "tomate", "huevo duro", "aceite de oliva"],
    "Bocadillo de jamón serrano": ["pan", "jamón serrano", "tomate", "aceite de oliva"],
    "Jamón serrano": ["jamón serrano"],
    "Queso manchego": ["queso manchego"],
    "Gazpachuelo malagueño": ["patatas", "huevos", "mayonesa", "limón", "aceite de oliva", "sal"],
    "Pulpo a la gallega": ["pulpo", "patatas", "pimentón", "aceite de oliva", "sal gorda"],
    "Mejillones al vapor": ["mejillones", "vino blanco", "cebolla", "perejil", "ajo"],
    "Gambas a la plancha": ["gambas", "ajo", "aceite de oliva", "sal", "limón"],
    "Sardinas asadas": ["sardinas", "aceite de oliva", "sal", "limón"],
    "Sepia a la plancha": ["sepia", "ajo", "perejil", "aceite de oliva", "limón"],
    "Huevos rotos con jamón": ["huevos", "patatas", "jamón serrano", "aceite de oliva"],
    "Arroz a la cubana": ["arroz", "huevos", "tomate frito", "plátano", "aceite de oliva"],
    "Croquetas de pollo": ["pollo", "leche", "harina", "mantequilla", "huevo", "pan rallado", "aceite de oliva"],
    "Calamares a la romana": ["calamares", "harina", "huevo", "aceite de oliva", "limón"],
    "Ensaladilla rusa": ["patatas", "zanahoria", "guisantes", "huevos", "atún", "mayonesa"],
    "Sopas de ajo": ["ajo", "pan", "huevos", "pimentón", "aceite de oliva", "caldo"],
    "Pisto manchego": ["calabacín", "berenjena", "pimiento", "tomate", "cebolla", "aceite de oliva"],
    "Ratatouille": ["berenjena", "calabacín", "pimiento", "tomate", "cebolla", "ajo", "hierbas provenzales"],
    "Pollo tikka masala": ["pollo", "yogur", "tomate", "nata", "cebolla", "ajo", "jengibre", "especias curry"],
    "Sushi variado": ["arroz", "pescado crudo", "alga nori", "wasabi", "jengibre", "salsa de soja"],
    "Shawarma de pollo": ["pollo", "pan pita", "yogur", "pepino", "tomate", "cebolla", "especias"],
    "Hummus": ["garbanzos", "tahini", "limón", "ajo", "aceite de oliva"],
    "Falafel": ["garbanzos", "cebolla", "ajo", "perejil", "comino", "aceite de oliva"],
    "Couscous con verduras": ["couscous", "calabacín", "zanahoria", "cebolla", "garbanzos", "caldo"],
    "Tabulé": ["bulgur", "tomate", "pepino", "cebolla", "perejil", "menta", "limón", "aceite de oliva"],
    "Burrito de pollo": ["tortilla de trigo", "pollo", "frijoles", "arroz", "queso", "tomate", "lechuga"],
    "Chili con carne": ["carne picada", "frijoles rojos", "tomate", "cebolla", "pimiento", "especias"],
    "Hamburguesa casera": ["carne picada", "pan de hamburguesa", "lechuga", "tomate", "cebolla", "queso"],
    "Hot dog": ["salchicha", "pan de hot dog", "mostaza", "ketchup", "cebolla"],
    "Sopa de verduras": ["zanahoria", "apio", "cebolla", "patata", "judías verdes", "caldo"],
    "Crema de calabaza": ["calabaza", "cebolla", "patata", "nata", "caldo", "aceite de oliva"],
    "Minestrone": ["tomate", "cebolla", "apio", "zanahoria", "judías", "pasta", "caldo"],
    "Spaghetti carbonara": ["spaghetti", "huevos", "bacon", "queso parmesano", "pimienta"],
    "Ravioli rellenos": ["ravioli", "ricotta", "espinacas", "tomate", "queso parmesano"],
    "Lasagna casera": ["pasta lasagna", "carne picada", "tomate", "bechamel", "queso", "cebolla"],
    "Kebab mixto": ["carne de cordero", "pollo", "pan pita", "tomate", "cebolla", "yogur"],
    "Tacos de carne": ["tortillas de maíz", "carne", "cebolla", "cilantro", "limón", "salsa"]
}

def cargar_platos_csv(archivo):
    """Carga los platos desde el archivo CSV"""
    platos = []
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la cabecera
            for row in reader:
                if row and row[0]:  
                    platos.append(row[0])
        return platos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("    GENERADOR DE LISTA DE LA COMPRA")
    print("="*50)
    print("1. Ver todos los platos disponibles")
    print("2. Seleccionar platos para la lista de compra")
    print("3. Ver ingredientes de un plato específico")
    print("4. Salir")
    print("="*50)

def mostrar_platos(platos):
    print("\n--- PLATOS DISPONIBLES ---")
    for i, plato in enumerate(platos, 1):
        print(f"{i:2d}. {plato}")

def mostrar_ingredientes_plato(plato):
    if plato in INGREDIENTES_PLATOS:
        print(f"\n--- INGREDIENTES DE '{plato}' ---")
        for ingrediente in INGREDIENTES_PLATOS[plato]:
            print(f"• {ingrediente}")
    else:
        print(f"No se encontraron ingredientes para '{plato}'")

def seleccionar_platos(platos):
    platos_seleccionados = []
    
    while True:
        print(f"\n--- SELECCIÓN DE PLATOS ---")
        print("Platos seleccionados:", len(platos_seleccionados))
        
        mostrar_platos(platos)
        print(f"\n{len(platos)+1}. Finalizar selección")
        
        try:
            opcion = input("\nSelecciona un plato (número): ").strip()
            
            if opcion == str(len(platos)+1):
                break
            
            numero = int(opcion)
            if 1 <= numero <= len(platos):
                plato_elegido = platos[numero-1]
                if plato_elegido not in platos_seleccionados:
                    platos_seleccionados.append(plato_elegido)
                    print(f"✓ '{plato_elegido}' añadido a la lista")
                else:
                    print(f"'{plato_elegido}' ya está en tu lista")
            else:
                print("Número inválido. Intenta de nuevo.")
                
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    return platos_seleccionados

def generar_lista_compra(platos_seleccionados):
    if not platos_seleccionados:
        print("No has seleccionado ningún plato.")
        return
    
    ingredientes_contador = {}
    
    print(f"\n--- PLATOS SELECCIONADOS ---")
    for plato in platos_seleccionados:
        print(f"• {plato}")
        if plato in INGREDIENTES_PLATOS:
            for ingrediente in INGREDIENTES_PLATOS[plato]:
                ingredientes_contador[ingrediente] = ingredientes_contador.get(ingrediente, 0) + 1
    
    print(f"\n" + "="*50)
    print("           LISTA DE LA COMPRA")
    print("="*50)
    
    ingredientes_ordenados = sorted(ingredientes_contador.keys())
    for ingrediente in ingredientes_ordenados:
        cantidad = ingredientes_contador[ingrediente]
        if cantidad > 1:
            print(f"• {ingrediente} (necesario para {cantidad} platos)")
        else:
            print(f"• {ingrediente}")
    
    print("="*50)
    print(f"Total de ingredientes únicos: {len(ingredientes_ordenados)}")
    
    # Guardar en CSV
    archivo_csv = "lista_compra.csv"
    try:
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Ingrediente", "Cantidad (nº de platos)"])
            for ingrediente, cantidad in ingredientes_contador.items():
                writer.writerow([ingrediente, cantidad])
        print(f"\nLista de la compra guardada en '{archivo_csv}' ✅")
    except Exception as e:
        print(f"Error al generar la lista de la compra: {e}")

def main():
    archivo_csv = "platos_50.csv"
    
    if not os.path.exists(archivo_csv):
        print(f"Error: No se encontró el archivo '{archivo_csv}' en el directorio actual.")
        return
    
    platos = cargar_platos_csv(archivo_csv)
    if not platos:
        print("No se pudieron cargar los platos del archivo CSV.")
        return
    
    print(f"Se cargaron {len(platos)} platos del archivo CSV.")
    
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("\nSelecciona una opción (1-4): ").strip()
            
            if opcion == "1":
                mostrar_platos(platos)
                
            elif opcion == "2":
                platos_seleccionados = seleccionar_platos(platos)
                generar_lista_compra(platos_seleccionados)
                
            elif opcion == "3":
                mostrar_platos(platos)
                try:
                    numero = int(input("\n¿De qué plato quieres ver los ingredientes? (número): "))
                    if 1 <= numero <= len(platos):
                        mostrar_ingredientes_plato(platos[numero-1])
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, introduce un número válido.")
                    
            elif opcion == "4":
                print("\n¡Gracias por usar el generador de lista de compra! 🛒")
                break
                
            else:
                print("Opción inválida. Por favor, selecciona 1, 2, 3 o 4.")
                
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
