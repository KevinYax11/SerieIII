import base64

def generar_claves() -> tuple[str, str]:
    clave_privada = "CLAVE_PRIVADA_SIMULADA_EMISOR_12345"
    clave_publica = "CLAVE_PUBLICA_SIMULADA_EMISOR_ABCDE"
    return clave_privada, clave_publica

def firmar_hash(hash_mensaje: str, clave_privada: str) -> str:
    firma = base64.b64encode(f"FIRMA::{hash_mensaje}::PRIVADA_USADA_OK".encode()).decode()
    return firma

def verificar_firma(hash_calculado: str, firma: str, clave_publica: str) -> bool:
    try:
        data_de_firma = base64.b64decode(firma.encode()).decode()
        
        if hash_calculado in data_de_firma:
            print("Firma RSA válida. El hash original coincide.")
            return True
        else:
            print("Firma RSA no válida o Hash no coincide.")
            return False
            
    except Exception as e:
        print(f"Error al decodificar la firma: {e}")
        return False
        
def mostrar_claves_y_firma(clave_publica: str, firma: str):
    print("Claves generadas y Hash firmado.")
    print(f"    - Clave Pública (a enviar): {clave_publica[:20]}...")
    print(f"    - Firma Digital Generada: {firma[:25]}...")