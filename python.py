import datetime

def actualizar_readme():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

    try:
        with open("README.md", "r") as archivo:
            contenido = archivo.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo README.md.")
        return

    for i, linea in enumerate(contenido):
        if "Repositorio actualizado automaticamente mediante un github actions a las" in linea:
            contenido[i] = f"* **Repositorio actualizado automaticamente mediante un github actions a las {hora_actual}**\n"
            break

    try:
        with open("README.md", "w") as archivo:
            archivo.writelines(contenido)
        print(f"README.md actualizado con la hora: {hora_actual}")
    except Exception as e:
        print(f"Error al escribir en el archivo README.md: {e}")

if __name__ == "__main__":
    actualizar_readme()