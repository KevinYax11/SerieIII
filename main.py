import json
from components.hash_fnv1 import calcular_hash_fnv1, mostrar_hash
from components.compression import comprimir, descomprimir, mostrar_tamanios
from components.rsa_digital_signature import generar_claves, firmar_hash, verificar_firma, mostrar_claves_y_firma

datos = {
    "mensaje": None,
    "hash_fnv1": None,
    "msg_comprimido": None,
    "tamanio_original": None,
    "tamanio_comprimido": None,
    "clave_privada": None,
    "clave_publica": None,
    "firma": None,
    "paquete_enviado": None
}

def paso_1_ingresar_mensaje():
    global datos
    datos["mensaje"] = input("Ingrese el mensaje de texto: ")
    print(f"Mensaje ingresado: '{datos['mensaje']}'")

def paso_2_calcular_hash():
    global datos
    if not datos["mensaje"]:
        print("Primero debe ingresar un mensaje (Opción 1).")
        return
    datos["hash_fnv1"] = calcular_hash_fnv1(datos["mensaje"])
    mostrar_hash(datos["hash_fnv1"])

def paso_3_comprimir():
    global datos
    if not datos["mensaje"]:
        print("Primero debe ingresar un mensaje (Opción 1).")
        return
        
    datos["msg_comprimido"], datos["tamanio_original"], datos["tamanio_comprimido"] = \
        comprimir(datos["mensaje"])
        
    mostrar_tamanios(datos["tamanio_original"], datos["tamanio_comprimido"])

def paso_4_firmar_rsa():
    global datos
    if not datos["hash_fnv1"]:
        print("Primero debe calcular el hash (Opción 2).")
        return
        
    if not datos["clave_privada"]:
        datos["clave_privada"], datos["clave_publica"] = generar_claves()
        
    datos["firma"] = firmar_hash(datos["hash_fnv1"], datos["clave_privada"])
    mostrar_claves_y_firma(datos["clave_publica"], datos["firma"])

def paso_5_simular_envio():
    global datos
    if not all([datos.get("msg_comprimido"), datos.get("firma"), datos.get("clave_publica")]):
        print("Asegúrese de haber comprimido (3) y firmado (4) el mensaje.")
        return

    datos["paquete_enviado"] = {
        "mensaje_comprimido": datos["msg_comprimido"],
        "firma_digital": datos["firma"],
        "clave_publica_emisor": datos["clave_publica"]
    }
    
    if input("¿Desea simular una alteración del mensaje COMPRIMIDO durante el envío? (s/n): ").lower() == 's':
         datos["paquete_enviado"]["mensaje_comprimido"] += "ALTERADO"
         print("Mensaje COMPRIMIDO alterado intencionalmente para la prueba.")
    
    print("Simulación de envío completada. Paquete listo para recepción.")
    
def paso_6_descomprimir_verificar():
    global datos
    if not datos["paquete_enviado"]:
        print("Primero debe simular el envío (Opción 5).")
        return
        
    paquete = datos["paquete_enviado"]
    print("\nReceptor simula la recepción y verificación.")
    
    mensaje_descomprimido_recibido = descomprimir(paquete["mensaje_comprimido"])
    
    if "[ERROR" in mensaje_descomprimido_recibido:
         print(f"Error al descomprimir. El mensaje comprimido parece estar dañado.")
         datos["es_autentico"] = False
         return

    print(f"Mensaje descomprimido: '{mensaje_descomprimido_recibido[:30]}...'")

    hash_recibido_calculado = calcular_hash_fnv1(mensaje_descomprimido_recibido)
    print(f"Hash FNV-1 calculado por el receptor: **{hash_recibido_calculado}**")
    
    firma_valida = verificar_firma(
        hash_recibido_calculado, 
        paquete["firma_digital"], 
        paquete["clave_publica_emisor"]
    )
    
    datos["es_autentico"] = firma_valida and (hash_recibido_calculado == datos["hash_fnv1"])

def paso_7_mostrar_resultado():
    global datos
    if "es_autentico" not in datos:
        print("Primero debe completar la verificación de la firma (Opción 6).")
        return
        
    print("\n--- RESULTADO DE AUTENTICIDAD ---")
    if datos["es_autentico"]:
        print("   **MENSAJE AUTÉNTICO Y NO MODIFICADO**")
    else:
        print("   **MENSAJE ALTERADO o FIRMA NO VÁLIDA**")
    print("-----------------------------------")


def iniciar_programa():
    
    menu_opciones = {
        1: ("Ingresar mensaje", paso_1_ingresar_mensaje),
        2: ("Calcular hash FNV-1", paso_2_calcular_hash),
        3: ("Comprimir mensaje (Huffman o RLE)", paso_3_comprimir),
        4: ("Firmar el hash con la clave privada RSA", paso_4_firmar_rsa),
        5: ("Simular envío (mensaje comprimido + firma + clave pública)", paso_5_simular_envio),
        6: ("Descomprimir y verificar firma (clave pública)", paso_6_descomprimir_verificar),
        7: ("Mostrar si el mensaje es auténtico o alterado", paso_7_mostrar_resultado),
        0: ("Salir", None)
    }
    
    while True:
        print("\n" + "="*70)
        print("           SISTEMA DE MENSAJERÍA SEGURA (Emisor -> Receptor)")
        print("="*70)
        for num, (desc, _) in menu_opciones.items():
            print(f"{num}. {desc}")
        print("-" * 70)
        
        opcion = input("Ingrese una opción: ")

        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. Adiós!")
                break
            
            if opcion in menu_opciones:
                print("\n" + "*"*70)
                print(f"EJECUTANDO PASO {opcion}: {menu_opciones[opcion][0]}")
                menu_opciones[opcion][1]()
                print("*"*70)
            else:
                print("Opción fuera de rango.")
                
        except ValueError:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    iniciar_programa()