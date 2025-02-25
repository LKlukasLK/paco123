import os
import csv

def main():
    csv_file = os.path.join(os.path.dirname(__file__),"datos.csv")
    write_csv(csv_file)
    read_csv(csv_file)

def comprobaciones(file_name):
    if os.path.exists(file_name):
        while True:
            print("El archivo ya existe. ¿Qué desea hacer? (s/e/n/a/v): ")
            print("s = sobreescribir el archivo")
            print("e = eliminar el contenido del archivo (manteniendo encabezado)")
            print("n = no hacer nada")
            print("a = añadir datos al archivo")
            print("v = visualizar contenido del archivo")
            
            respuesta = input().strip().lower()
            
            if respuesta == "s":
                with open(file_name, "w", newline="") as file:
                    print("El archivo se ha sobrescrito.")
                return False
            elif respuesta == "e":
                with open(file_name, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Nombre", "Edad", "Ciudad"])  # Mantener encabezado
                print("El contenido del archivo se ha eliminado, pero el encabezado se ha mantenido.")
                return False
            elif respuesta == "n":
                print("No se realizarán cambios en el archivo.")
                return True
            elif respuesta == "a":
                print("Se añadirán datos al archivo.")
                return False
            elif respuesta == "v":
                visualizar_csv(file_name)
            else:
                print("Respuesta no válida. Inténtelo de nuevo.")
    else:
        print("El archivo no existe. Se creará un nuevo archivo.")
        return False

def visualizar_csv(file_name):
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            print("Contenido del archivo CSV::")
            for row in reader:
                print(",".join(row))
    except Exception as e:
        print(f"Error leyendo el archivo CSV: {e}")

def write_csv(file_name):
    archivo_existe = os.path.exists(file_name)
    tiene_contenido = archivo_existe and os.path.getsize(file_name) > 0
    
    if comprobaciones(file_name):
        return
    
    data = []
    print("Introduce los datos para el archivo CSV.")
    while True:
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        ciudad = input("Ciudad: ")
        data.append([nombre, edad, ciudad])
        
        respuesta = input("¿Desea introducir otro registro? (s/n): ").strip().lower()
        if respuesta != "s":
            break
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        if not archivo_existe or not tiene_contenido:
            writer.writerow(["Nombre", "Edad", "Ciudad"])  # Escribir encabezado si el archivo está vacío
        writer.writerows(data)
    
    print("Datos añadidos al archivo CSV correctamente.")

def read_csv(file_name):
    try:
        with open(file_name, "r", newline="") as file:
            reader = csv.reader(file)
            print("Contenido del archivo CSV:")
            for row in reader:
                print(",".join(row))
    except Exception as e:
        print(f"Error leyendo el archivo CSV: {e}")

if __name__ == "__main__":
    main()
