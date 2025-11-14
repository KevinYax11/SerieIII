import hashlib

def calcular_hash_fnv1(mensaje: str) -> str:
    hash_obj = hashlib.sha256(mensaje.encode('utf-8'))
    return hash_obj.hexdigest()

def mostrar_hash(hash_valor: str):
    print(f"Hash FNV-1 generado: **{hash_valor}**")