import base64

def comprimir(mensaje: str) -> tuple[str, int, int]:
    mensaje_comprimido = base64.b64encode(mensaje.encode()).decode()
    tamanio_original = len(mensaje.encode())
    tamanio_comprimido = len(mensaje_comprimido.encode())
    
    return mensaje_comprimido, tamanio_original, tamanio_comprimido

def descomprimir(mensaje_comprimido: str) -> str:
    try:
        mensaje_original = base64.b64decode(mensaje_comprimido.encode()).decode()
        return mensaje_original
    except:
        return "[ERROR: Fallo al descomprimir]"

def mostrar_tamanios(original: int, comprimido: int):
    print("Compresión finalizada.")
    print(f"    - Tamaño Original: {original} bytes")
    print(f"    - Tamaño Comprimido: {comprimido} bytes")
    
    if original > 0:
        reduccion = ((original - comprimido) / original) * 100
        print(f"    - Reducción (Simulada): {reduccion:.2f}%")