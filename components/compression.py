import base64

def comprimir(mensaje: str) -> tuple[str, int, int]:
    if not mensaje:
        return "", 0, 0
        
    tamanio_original = len(mensaje.encode('utf-8'))
    mensaje_comprimido_rle = ""
    
    count = 1
    for i in range(1, len(mensaje)):
        if mensaje[i] == mensaje[i-1]:
            count += 1
        else:
            mensaje_comprimido_rle += str(count) + mensaje[i-1]
            count = 1
    
    mensaje_comprimido_rle += str(count) + mensaje[-1]
    
    tamanio_comprimido = len(mensaje_comprimido_rle.encode('utf-8'))
    
    return mensaje_comprimido_rle, tamanio_original, tamanio_comprimido

def descomprimir(mensaje_comprimido: str) -> str:
    mensaje_original = ""
    count_str = ""
    
    for char in mensaje_comprimido:
        if char.isdigit():
            count_str += char
        else:
            if count_str:
                count = int(count_str)
                mensaje_original += char * count
                count_str = ""
            else:
                return "[ERROR: Fallo al descomprimir o formato RLE inválido]"

    if "[ERROR" in mensaje_original:
        return "[ERROR: Fallo al descomprimir o formato RLE inválido]"
        
    return mensaje_original

def mostrar_tamanios(original: int, comprimido: int):
    print("Compresión RLE finalizada.")
    print(f"    - Tamaño Original: {original} bytes")
    print(f"    - Tamaño Comprimido: {comprimido} bytes")
    
    if original > 0:
        reduccion = ((original - comprimido) / original) * 100
        print(f"    - Reducción: {reduccion:.2f}%")