# Manual de Usuario
## Sistema de Gestión de Inventario y Bodega

UNIVERSIDAD AGRARIA DEL ECUADOR

FACULTAD DE CIENCIAS AGRARIAS

CIENCIAS DE LA COMPUTACIÓN — MODALIDAD EN LÍNEA

LENGUAJE DE PROGRAMACIÓN 2

**Grupo N.º:** 7

**Integrantes:**
- Rodolfo Javier Jhayya
- Madeline Núñez
- Rubén Noboa
- Elizabeth Buñay

---

## Índice

1. Introducción
2. Requisitos del Sistema
3. Instalación
4. Descripción de la Interfaz
5. Guía de Uso
   5.1. Registrar un producto
   5.2. Listar productos
   5.3. Eliminar un producto
   5.4. Buscar producto por código
   5.5. Registrar un proveedor
   5.6. Listar proveedores
   5.7. Eliminar un proveedor
   5.8. Registrar entrada o salida de mercancía
   5.9. Deshacer un movimiento
   5.10. Ver historial de movimientos
   5.11. Crear un pedido
   5.12. Procesar un pedido
   5.13. Reporte de bajo stock
   5.14. Rotar inventario
   5.15. Ordenar productos (Burbuja)
   5.16. Ordenar productos (Merge Sort)
   5.17. Búsqueda lineal por nombre
   5.18. Búsqueda binaria por código
6. Preguntas Frecuentes

---

## 1. Introducción

El Sistema de Gestión de Inventario y Bodega es un programa de computadora que ayuda a llevar el control de los productos, proveedores y movimientos de mercancía de una bodega o almacén. Permite registrar qué productos hay, cuántos hay de cada uno, quiénes son los proveedores, y llevar un historial de las entradas y salidas de mercancía.

Este manual está dirigido a cualquier persona que vaya a usar el sistema, sin necesidad de conocimientos técnicos de programación.

---

## 2. Requisitos del Sistema

Para ejecutar el sistema, su computadora debe cumplir con los siguientes requisitos:

**Hardware:**
- Computadora con sistema operativo Windows 10 o superior
- Procesador de 1.5 GHz o superior
- 2 GB de memoria RAM o más
- 50 MB de espacio disponible en disco

**Software:**
- Python 3.10 o superior instalado
- No se requiere conexión a internet para su funcionamiento

---

## 3. Instalación

Siga estos pasos para instalar y ejecutar el sistema:

1. **Descargue la carpeta del proyecto** desde el repositorio de GitHub o desde el archivo comprimido que le entregaron.

2. **Abra una terminal** (Símbolo del sistema o PowerShell) en la carpeta `02-Programa`.

3. **Ejecute el siguiente comando:**
   ```
   python main.py
   ```

4. **La ventana del sistema se abrirá automáticamente.** Ya puede empezar a usarlo.

Si al ejecutar el comando aparece un error, asegúrese de tener Python instalado correctamente. Puede verificarlo abriendo una terminal y escribiendo:
```
python --version
```
Si ve un número de versión (por ejemplo, Python 3.14.0), está listo.

---

## 4. Descripción de la Interfaz

Al abrir el sistema, verá una ventana con los siguientes elementos:

- **Botones de funcionalidad:** en la parte superior hay botones organizados en filas. Cada botón realiza una tarea específica (registrar productos, hacer movimientos, ordenar, etc.).
- **Área de texto:** ocupa la mayor parte de la ventana. Allí se muestran los resultados de cada operación: listados de productos, confirmaciones, mensajes de error, etc.
- **Botón Salir:** en la parte inferior, cierra el programa.

No se necesitan comandos ni códigos: todo se maneja haciendo clic en los botones y llenando los cuadros de diálogo que aparecen.

---

## 5. Guía de Uso

### 5.1. Registrar un producto

1. Haga clic en el botón **Registrar Producto**.
2. Aparecerá una ventana pidiendo el **Código** del producto (por ejemplo, A001).
3. Escriba el código y haga clic en **Aceptar**.
4. Aparecerá una ventana pidiendo el **Nombre** del producto.
5. Continúe llenando los datos solicitados: categoría, precio, stock actual, stock mínimo y stock máximo.
6. Al terminar, el programa mostrará un mensaje de confirmación en el área de texto: *"✓ Producto registrado: A001 - Laptop"*.

### 5.2. Listar productos

1. Haga clic en el botón **Listar Productos**.
2. En el área de texto se mostrarán todos los productos registrados, con su código, nombre, precio y stock.

### 5.3. Eliminar un producto

1. Haga clic en el botón **Eliminar Producto**.
2. Escriba el código del producto que desea eliminar.
3. Haga clic en **Aceptar**.
4. El producto se eliminará del sistema y de la base de datos.

### 5.4. Buscar producto por código

1. Haga clic en el botón **Buscar por código**.
2. Escriba el código del producto.
3. El sistema mostrará la información del producto si existe, o un mensaje de "Producto no encontrado" si no.

### 5.5. Registrar un proveedor

1. Haga clic en el botón **Registrar Proveedor**.
2. Llene los datos solicitados: RUC, nombre, teléfono, email y dirección.
3. El sistema mostrará un mensaje de confirmación.

### 5.6. Listar proveedores

1. Haga clic en el botón **Listar Proveedores**.
2. En el área de texto se mostrarán todos los proveedores registrados.

### 5.7. Eliminar un proveedor

1. Haga clic en el botón **Eliminar Proveedor**.
2. Escriba el RUC del proveedor que desea eliminar.
3. El proveedor se eliminará del sistema.

### 5.8. Registrar entrada o salida de mercancía

1. Haga clic en el botón **Entrada/Salida**.
2. Escriba el código del producto.
3. Escriba la cantidad.
4. Escriba "entrada" o "salida" según el tipo de movimiento.
5. El sistema actualizará el stock del producto y mostrará un resumen del movimiento.

### 5.9. Deshacer un movimiento

1. Haga clic en el botón **Deshacer**.
2. El último movimiento registrado (entrada o salida) se revertirá automáticamente.
3. El stock del producto volverá al valor anterior al movimiento.

### 5.10. Ver historial de movimientos

1. Haga clic en el botón **Ver Movimientos**.
2. En el área de texto se mostrará la lista de todos los movimientos registrados, con fecha, tipo, producto y cantidad.

### 5.11. Crear un pedido

1. Haga clic en el botón **Nuevo Pedido**.
2. Escriba el nombre del cliente.
3. Agregue productos al pedido: escriba el código del producto y la cantidad deseada.
4. Para terminar, deje el código vacío y haga clic en **Aceptar**.
5. El sistema mostrará el total del pedido.

### 5.12. Procesar un pedido

1. Haga clic en el botón **Procesar Pedido**.
2. El sistema tomará el pedido más antiguo de la cola y lo mostrará en pantalla.
3. Si no hay pedidos pendientes, mostrará un mensaje indicándolo.

### 5.13. Reporte de bajo stock

1. Haga clic en el botón **Bajo Stock**.
2. El sistema mostrará todos los productos cuyo stock actual está por debajo del stock mínimo configurado.

### 5.14. Rotar inventario

1. Haga clic en el botón **Rotar Inventario**.
2. El sistema rotará la lista de productos: el primer producto pasará al último lugar.
3. Esto es útil para simular la rotación física de productos en bodega.

### 5.15. Ordenar productos (Burbuja)

1. Haga clic en el botón **Ord. Burbuja**.
2. Escriba el criterio de ordenamiento: `codigo`, `nombre`, `precio` o `stock`.
3. El sistema mostrará los productos ordenados según el criterio elegido, usando el algoritmo de burbuja.

### 5.16. Ordenar productos (Merge Sort)

1. Haga clic en el botón **Ord. Merge Sort**.
2. Escriba el criterio de ordenamiento (igual que en burbuja).
3. El sistema mostrará los productos ordenados usando merge sort, que es más rápido que burbuja para listas grandes.

### 5.17. Búsqueda lineal por nombre

1. Haga clic en el botón **Búsq. Lineal**.
2. Escriba el nombre del producto que busca.
3. El sistema buscará el producto recorriendo la lista uno por uno y mostrará su información si lo encuentra.

### 5.18. Búsqueda binaria por código

1. Haga clic en el botón **Búsq. Binaria**.
2. Escriba el código del producto.
3. El sistema ordenará la lista y buscará el producto usando búsqueda binaria, que es más rápida que la búsqueda lineal.

---

## 6. Preguntas Frecuentes

**1. ¿El sistema guarda los datos al cerrarlo?**
Sí. Todos los productos, proveedores y movimientos se guardan automáticamente en el archivo `inventario.db`. Al volver a abrir el programa, los datos estarán ahí.

**2. ¿Puedo recuperar un producto que eliminé por error?**
No, la eliminación es permanente. Antes de eliminar, asegúrese de que es el producto correcto.

**3. ¿Qué hago si el programa no abre?**
Verifique que tiene Python instalado. Abra una terminal y escriba `python --version`. Si no reconoce el comando, descargue Python desde https://www.python.org/downloads/ e instálelo.

**4. ¿Puedo usar el sistema en otro idioma?**
No, la interfaz está en español y no tiene opción de cambio de idioma.

**5. ¿Qué significa O(n²) y O(n log n)?**
Son notaciones que indican qué tan rápido es cada algoritmo de ordenamiento. Para uso diario, no necesita entenderlas: el programa funciona igual. Si tiene curiosidad, O(n log n) es más rápido que O(n²) cuando hay muchos productos.

**6. ¿Cuántos productos puedo registrar?**
No hay límite. El programa puede manejar cientos o miles de productos sin problemas.

**7. ¿El sistema funciona sin internet?**
Sí, completamente. No necesita conexión para funcionar.

**8. ¿Cómo sé qué versión del programa tengo?**
Revise el título de la ventana principal, que dice "Inventario y Bodega - Grupo 7". La versión corresponde a la entrega final de la semana 14.
