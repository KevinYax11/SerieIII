## Estructura De Datos II
## Kevin Miguel Yax Puác - 1529422

-----

# 🛡️ Proyecto: Sistema de Mensajería Segura (Serie III)

Este proyecto simula el proceso de **envío y verificación de un mensaje seguro** utilizando mecanismos de Hashing (FNV-1), Compresión (RLE) y Firma Digital (RSA).

## Contenido de la Serie III

El sistema implementa el siguiente flujo de seguridad simulado:

1.  **Hashing (FNV-1a):** Generación de un resumen único del mensaje.
2.  **Compresión (RLE):** Reducción del tamaño del mensaje para optimizar el envío.
3.  **Firma Digital (RSA):** Autenticación del emisor y garantía de integridad.

El programa está organizado modularmente y utiliza un menú de consola para guiar al usuario paso a paso.

-----

## Instalación y Requisitos

Este proyecto requiere únicamente el intérprete estándar de **Python 3**.

### Ejecución Inicial

1.  Abre tu terminal o Símbolo del Sistema.
2.  Navega hasta la carpeta raíz del proyecto (`SerieIII`).
3.  Ejecuta el archivo principal:

<!-- end list -->

```bash
python main.py
```

-----

##  Guía de Uso (Flujo Secuencial)

El programa funciona a través de un **menú numerado**. Es crucial seguir los pasos secuencialmente del **1 al 7** para que el proceso de seguridad se complete correctamente.

### 1\. Flujo de Verificación Exitosa (Mensaje Auténtico)

Este flujo demuestra la **compresión exitosa** y la **integridad** del mensaje de principio a fin.

1.  **Paso 1 (Ingresar mensaje):** Inicia el proceso. Asegúrate de ingresar un mensaje con repeticiones, como **`TESTTTEST`**, para ver una reducción positiva en la compresión RLE.
2.  **Paso 2 (Calcular hash FNV-1):** Genera el hash del mensaje original.
3.  **Paso 3 (Comprimir mensaje):** Comprime el mensaje usando RLE. La salida debe mostrar una **Reducción Positiva**.
4.  **Paso 4 (Firmar el hash):** Genera las claves RSA y firma digitalmente el hash con la clave privada.
5.  **Paso 5 (Simular envío):** Cuando se pregunte si deseas alterar el mensaje, escribe **`n`** (No) para enviar el paquete intacto.
6.  **Paso 6 (Descomprimir y verificar):** El receptor descomprime, calcula un nuevo hash y verifica que la firma sea válida.
7.  **Paso 7 (Mostrar resultado):** El resultado final debe ser: **`MENSAJE AUTÉNTICO Y NO MODIFICADO`**.

-----

### 2\. Flujo de Prueba de Integridad (Mensaje Alterado)

Este flujo demuestra que el sistema **detecta cualquier alteración** ocurrida durante el envío.

1.  **Paso 1 (Ingresar mensaje):** Ingresa cualquier mensaje, por ejemplo: **`prueba`**.
2.  **Paso 2 (Calcular hash FNV-1):** Calcula el hash.
3.  **Paso 3 (Comprimir mensaje):** Comprime el mensaje.
4.  **Paso 4 (Firmar el hash):** Firma digitalmente el hash.
5.  **Paso 5 (Simular envío):** Cuando se pregunte si deseas alterar el mensaje, escribe **`s`** (Sí). Esto simula un ataque o corrupción en el canal de comunicación.
6.  **Paso 6 (Descomprimir y verificar):** El receptor intentará procesar el mensaje dañado. La descompresión fallará debido a que el formato RLE se rompió.
7.  **Paso 7 (Mostrar resultado):** El resultado final debe ser: **`MENSAJE ALTERADO o FIRMA NO VÁLIDA`**.
