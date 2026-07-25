# Sistema de Gestión de Inventario y Bodega

UNIVERSIDAD AGRARIA DEL ECUADOR

FACULTAD DE CIENCIAS AGRARIAS

CIENCIAS DE LA COMPUTACIÓN — MODALIDAD EN LÍNEA

LENGUAJE DE PROGRAMACIÓN 2

**Título del Proyecto:** Sistema de Gestión de Inventario y Bodega

**Grupo N.º:** 7

**Integrantes:**
- Rodolfo Javier Jhayya
- Madeline Núñez
- Rubén Noboa
- Elizabeth Buñay

**Docente:** Ing. Bryan Vélez, MSc.

**Curso:** Tercer Semestre

**Período Académico:** 2026

## Índice de Contenidos

1. Introducción
2. Justificación
3. Objetivos
   3.1. Objetivo General
   3.2. Objetivos Específicos
4. Alcance del Proyecto
   4.1. Funcionalidades Incluidas
   4.2. Funcionalidades No Incluidas
5. Marco Teórico
   5.1. Programación Orientada a Objetos (POO)
   5.2. Estructura de Datos: Lista Circular
   5.3. Estructura de Datos: Cola (Queue)
   5.4. Estructura de Datos: Pila (Stack)
   5.5. Algoritmos de Búsqueda y Ordenamiento
   5.6. Gestión de Inventarios
6. Diseño Preliminar del Sistema
   6.1. Diagrama de Clases UML
   6.2. Modelo Entidad-Relación (MER)
7. Metodología
8. Implementación
9. Pruebas
10. Análisis de Complejidad Big-O
11. Conclusiones
12. Recomendaciones
13. Referencias Bibliográficas
14. Anexos

---

## 1. Introducción

Controlar el inventario y los movimientos de bodega es hoy una de esas tareas que separa a las empresas que crecen de las que sobreviven apenas. Sin un registro ordenado de lo que entra y sale, sin saber a quién se le compra ni cuánto stock hay en cada momento, cualquier negocio opera a ciegas (Mauleón, 2018). Reducir costos, evitar desabastecimientos y tomar decisiones con un mínimo de información —todo eso depende de tener los datos al día. Sin embargo, muchas empresas comerciales siguen llevando cuentas en papel o usando sistemas genéricos que les quedan grandes o chicos.

El proyecto propone construir un sistema de gestión de inventario y bodega en Python (Python Software Foundation, 2024), apoyado en programación orientada a objetos y en estructuras de datos que no se eligen al azar. Una lista circular modela la rotación de productos; una cola procesa los pedidos pendientes en orden de llegada; una pila permite deshacer el último movimiento registrado (Cormen et al., 2009). La idea es que cada estructura resuelva un problema concreto del almacén, no que estén ahí porque toca.

Este documento sigue la estructura oficial de la asignatura Lenguaje de Programación 2. En esta entrega de la semana 12 se cubren introducción, justificación, objetivos, alcance, marco teórico y diseño preliminar. La versión final, con metodología, implementación, pruebas y conclusiones, se entregará en la semana 14.

---

## 2. Justificación

Visto desde la carrera, el proyecto obliga a juntar en un solo lugar los conceptos de POO (Joyanes, 2018), estructuras de datos y algoritmos que han ido apareciendo por separado en clase (Cormen et al., 2009). Implementar una lista circular, una cola y una pila dentro de un sistema que sí sirve para algo —no un ejercicio de pizarrón— obliga a entender cómo funcionan realmente y por qué se usan así (Weiss, 2013). Eso, en sí mismo, ya justifica el trabajo.

En la práctica, los beneficios son más o menos directos. La lista circular permite que la rotación de productos sea equitativa y ayuda a detectar cuáles llevan mucho tiempo quietos. La cola evita que los pedidos se salteen o se atiendan fuera de turno. Y la pila de movimientos —un deshacer de cada entrada o salida— reduce el riesgo de que un error de registro deje el inventario inconsistente (Summerfield, 2010).

Ni todo esto es nuevo ni estamos inventando nada, pero juntarlo en un sistema funcional que una empresa real pudiera usar es lo que le da sentido al proyecto.

---

## 3. Objetivos

### 3.1. Objetivo General

Desarrollar un sistema de gestión de inventario y bodega en Python que permita controlar los productos, las entradas y salidas de mercancía y los proveedores, aplicando estructuras de datos como lista circular, cola y pila para optimizar los procesos de rotación, despacho y seguridad de la información.

### 3.2. Objetivos Específicos

- Implementar un módulo de registro y consulta de productos, proveedores y movimientos de bodega utilizando los principios de la programación orientada a objetos (Joyanes, 2018).
- Aplicar una lista circular para modelar la rotación de productos en bodega, permitiendo identificar el orden de reposición y los productos con menor rotación (Cormen et al., 2009).
- Implementar una cola (FIFO) para gestionar los pedidos pendientes de despacho, garantizando su procesamiento en orden de llegada (Weiss, 2013).
- Implementar una pila (LIFO) para registrar los movimientos de inventario y permitir deshacer el último movimiento registrado (Deitel & Deitel, 2019).
- Diseñar una interfaz de usuario funcional que permita la interacción con el sistema de forma clara e intuitiva (Summerfield, 2010).

---

## 4. Alcance del Proyecto

### 4.1. Funcionalidades Incluidas

El sistema contempla las siguientes funcionalidades:

- Registro, modificación, eliminación y consulta de productos con código, nombre, descripción, categoría, precio, stock mínimo y stock máximo.
- Registro y consulta de proveedores con nombre, RUC, teléfono, correo electrónico y dirección.
- Gestión de entradas de mercancía a bodega con registro de fecha, cantidad y proveedor.
- Gestión de salidas de mercancía con registro de fecha, cantidad y destino.
- Rotación automática de productos en bodega mediante una lista circular (Cormen et al., 2009).
- Cola de pedidos pendientes de despacho procesados en orden FIFO (Weiss, 2013).
- Pila de movimientos para deshacer el último registro de entrada o salida (Deitel & Deitel, 2019).
- Consulta del historial de movimientos de un producto específico.
- Reporte de productos con bajo stock (Mauleón, 2018).

### 4.2. Funcionalidades No Incluidas

El sistema no incluye las siguientes funcionalidades:

- Facturación electrónica o generación de comprobantes fiscales.
- Integración con sistemas contables o ERP externos.
- Módulo de ventas al por menor (punto de venta).
- Conexión con bases de datos relacionales (el almacenamiento será en memoria durante la ejecución con persistencia opcional en archivos).
- Interfaz web o aplicación móvil (la interacción será mediante consola o interfaz gráfica básica).
- Módulo de usuarios con roles y permisos avanzados.
- Notificaciones automáticas por correo electrónico.

---

## 5. Marco Teórico

### 5.1. Programación Orientada a Objetos (POO)

La POO organiza el código alrededor de clases y objetos: una clase describe la estructura y el comportamiento de un tipo de cosas, y un objeto es una de esas cosas, con valores concretos (Joyanes, 2018). En lugar de tener funciones sueltas operando sobre datos separados, los datos y las operaciones vienen juntos.

Hay cuatro pilares que aparecen en cualquier implementación seria:

- **Encapsulamiento.** Los detalles internos de una clase se quedan dentro; solo se expone lo que otros necesitan. En Python se hace con atributos privados (doble guion bajo) y propiedades con `@property`, `@setter` y `@deleter` (Summerfield, 2010).
- **Herencia.** Una clase puede heredar atributos y métodos de otra. Python admite herencia simple y múltiple, lo que permite reutilizar código sin duplicar (Deitel & Deitel, 2019).
- **Polimorfismo.** Un mismo método se comporta distinto según el objeto que lo ejecute. En Python, se logra sobreescribiendo métodos en las subclases (Summerfield, 2010).
- **Abstracción.** Modelar la realidad sin llevarse todos los detalles: una clase `Producto` no necesita saber cómo se imprime una factura, solo sus propios datos y operaciones (Joyanes, 2018).

En el proyecto, estos cuatro pilares se traducen en clases como `Producto`, `Proveedor`, `Movimiento` y `Pedido`, cada una con lo suyo y sin pisar el terreno de las otras (Deitel & Deitel, 2019).

### 5.2. Estructura de Datos: Lista Circular

Una lista circular es una cadena de nodos donde cada uno apunta al siguiente y el último vuelve al primero: un ciclo cerrado (Cormen et al., 2009). No hay cabeza ni cola fijas, y se puede recorrer sin parar hasta encontrar lo que se busca (Weiss, 2013).

En el sistema, la lista circular representa la rotación de los productos en bodega. Cada nodo es un producto. Cada vez que entra mercancía nueva, el producto se agrega a la lista. Cuando hay que despachar o revisar el estado del inventario, la lista se recorre en círculo para ver cuál lleva más tiempo sin movimiento. Es útil justo en escenarios donde se espera que todos los productos roten antes de recibir reposición.

Las operaciones típicas —insertar al final, eliminar un nodo, buscar por código y recorrer la lista completa— se implementan con referencias directas al último nodo, lo que mantiene la inserción en O(1) (Cormen et al., 2009).

### 5.3. Estructura de Datos: Cola (Queue)

FIFO: el primero que entra es el primero que sale (Deitel & Deitel, 2019). Como la fila del supermercado. En ciencias de la computación, la cola es la estructura que modela cualquier escenario donde el orden de llegada importa.

En el proyecto, la cola almacena los pedidos pendientes de despacho. Cuando un cliente pide algo, el pedido se encola al final. El sistema toma el que está al frente, lo procesa y lo saca. Las cuatro operaciones básicas —`enqueue`, `dequeue`, `peek` e `is_empty` (Weiss, 2013)— alcanzan para gestionar todo el flujo.

Aunque Python trae `collections.deque`, aquí se implementa la cola manualmente con nodos enlazados. La razón es académica: entender cómo funciona por dentro la estructura (Summerfield, 2010).

### 5.4. Estructura de Datos: Pila (Stack)

LIFO: el último que entra es el primero que sale. Como una pila de platos (Joyanes, 2018; Weiss, 2013). Solo se puede acceder al elemento de arriba.

En el sistema, cada movimiento de inventario (entrada o salida) se apila como un objeto `Movimiento`. Si el usuario se equivoca, la opción de deshacer saca ese movimiento de la pila y revierte lo que hizo (Deitel & Deitel, 2019). Las operaciones son `push`, `pop`, `peek` e `is_empty`. Simple, eficiente y suficiente.

### 5.5. Análisis de Complejidad Big-O

Big-O mide cómo crece el tiempo de ejecución de un algoritmo según crece la entrada (Cormen et al., 2009). No dice cuánto tarda exactamente, sino cómo se comporta cuando los datos se multiplican.

En las estructuras del proyecto:

- **Lista circular.** Insertar al final cuesta O(1) si se guarda una referencia al último nodo. Buscar un producto por código cuesta O(n), porque hay que recorrer (Weiss, 2013).
- **Cola.** `enqueue` y `dequeue` son O(1) con nodos enlazados (Cormen et al., 2009).
- **Pila.** `push` y `pop` también son O(1) (Deitel & Deitel, 2019).

Estos costos justifican por qué se eligen estas estructuras y no otras: ninguna operación crítica del sistema se vuelve lenta cuando crece el inventario.

### 5.6. Gestión de Inventarios

Gestionar inventarios es, en esencia, decidir cuánto tener guardado para no quedarse sin producto ni ahogarse en costo de almacenamiento (Mauleón, 2018). Hay tres números que importan: el stock mínimo (lo más bajo que se deja antes de alarmarse), el stock máximo (lo que no conviene pasar) y el punto de reorden (la cantidad que dispara una nueva compra).

El sistema permite configurar estos valores por producto y lanza alertas cuando el stock se acerca al piso (Mauleón, 2018).

---

## 6. Diseño Preliminar del Sistema

### 6.1. Diagrama de Clases UML

El modelo de clases sigue la estructura que describe Weiss (2013) para sistemas orientados a objetos. Estas son las clases previstas:

**Clase `Producto`:**
Atributos: `codigo`, `nombre`, `descripcion`, `categoria`, `precio`, `stock_actual`, `stock_minimo`, `stock_maximo`. Métodos: `actualizar_stock(cantidad)`, `mostrar_info()`.

**Clase `Proveedor`:**
Atributos: `ruc`, `nombre`, `telefono`, `email`, `direccion`. Métodos: `mostrar_info()`.

**Clase `Movimiento`:**
Atributos: `tipo` (entrada/salida), `producto`, `cantidad`, `fecha`. Métodos: `aplicar()`, `revertir()`.

**Clase `Pedido`:**
Atributos: `id_pedido`, `cliente`, `productos`, `estado`, `fecha`. Métodos: `agregar_producto(producto, cantidad)`, `calcular_total()`.

**Clase `Nodo`:**
Atributos: `dato`, `siguiente`.

**Clase `ListaCircular`:**
Atributos: `ultimo`. Métodos: `insertar(dato)`, `eliminar(codigo)`, `buscar(codigo)`, `recorrer()`.

**Clase `Cola`:**
Atributos: `frente`, `final`. Métodos: `enqueue(dato)`, `dequeue()`, `peek()`, `is_empty()`.

**Clase `Pila`:**
Atributos: `tope`. Métodos: `push(dato)`, `pop()`, `peek()`, `is_empty()`.

**Clase `Inventario`:**
Atributos: `lista_circular` (ListaCircular de Producto), `cola_pedidos` (Cola de Pedido), `pila_movimientos` (Pila de Movimiento), `proveedores`. Métodos: `registrar_producto()`, `registrar_proveedor()`, `entrada_mercancia()`, `salida_mercancia()`, `procesar_pedido()`, `deshacer_movimiento()`, `reporte_bajo_stock()`.

### 6.2. Modelo Entidad-Relación (MER)

El modelo de datos preliminar usa cuatro entidades principales (Mauleón, 2018):

- **Producto:** codigo (PK), nombre, descripcion, categoria, precio, stock_actual, stock_minimo, stock_maximo.
- **Proveedor:** ruc (PK), nombre, telefono, email, direccion.
- **Movimiento:** id_movimiento (PK), tipo (entrada o salida), codigo_producto (FK), cantidad, fecha.
- **Pedido:** id_pedido (PK), cliente, estado, fecha.

Las relaciones son las que cabría esperar: un producto tiene varios movimientos asociados (1:N), un proveedor puede surtir varios productos (1:N), y los pedidos se relacionan con los productos a través de una tabla intermedia `DetallePedido` que resuelve la relación N:M.

---

## 7. Metodología

El proyecto se manejó con un enfoque incremental, que en la práctica significó lo siguiente: cada funcionalidad se codificó aparte, se probó sola y recién cuando funcionaba se pegaba al sistema principal. ¿El resultado? Los errores aparecían chiquitos, se arreglaban rápido y nadie tenía que rehacer nada de lo que ya andaba bien. El enfoque en cascada no habría dejado ese margen.

### 7.1. Herramientas y tecnologías

| Herramienta | Por qué se usó |
|---|---|
| **Python 3.14** | Lo usa el curso, su sintaxis es limpia y hay bibliotecas para todo lo que necesitaba el proyecto |
| **Tkinter** | Viene con Python, no instala nada extra y alcanza de sobra para una GUI que no es de producción |
| **SQLite + DB Browser** | Sin servidor, el archivo viaja con el proyecto, y las necesidades de persistencia del sistema no piden más que eso |
| **VS Code** | El depurador integrado de Python ahorró bastante tiempo |
| **Git + GitHub** | Control de cambios local y respaldo en la nube para la entrega final |

### 7.2. Proceso de trabajo

El desarrollo se organizó en cuatro iteraciones que no fueron secuenciales del todo —a veces una volvía a tocarse porque la siguiente revelaba algo que no encajaba:

1. **Diseño de clases y estructuras.** Las clases del dominio (Producto, Proveedor, Movimiento, Pedido) y las estructuras de datos (ListaCircular, Cola, Pila) se definieron primero en papel y después pasaron a módulos separados. Sonó más rápido de lo que fue: encontrar el punto justo entre lo que cada clase necesitaba y lo que podía compartir llevó varios ajustes.
2. **Conexión a base de datos.** El esquema relacional se armó en DB Browser for SQLite y la clase `ConexionDB` se escribió para manejar las operaciones desde Python. Acá el aprendizaje fue que modelar en SQLite es barato —crear y borrar tablas toma segundos— y eso anima a probar variantes hasta dar con una que calce.
3. **Interfaz gráfica.** La ventana principal con Tkinter y sus botones conectados a las funciones del sistema. Lo más tedioso fue alinear los controles en la cuadrícula; lo más útil, descubrir que `scrolledtext` resuelve el área de salida sin esfuerzo.
4. **Integración y pruebas.** Unificar los módulos a través de la clase `Inventario` y probar el flujo completo: registrar productos, hacer movimientos, deshacer, procesar pedidos. Justo acá saltaron la mayoría de los bugs —cosas que funcionaban solas y se rompían al juntarse.

Al cierre de la semana 13 el sistema andaba en un 60 % más o menos. Las clases del dominio, las estructuras de datos y la interfaz gráfica estaban operativas; la conexión a la base de datos corría en código pero sin amarrarse aún a los formularios de la interfaz; los algoritmos de ordenamiento y búsqueda, documentados en el papel, no habían entrado al código.

---

## 8. Implementación

El código fuente vive en `02-Programa/`, organizado como paquetes de Python. La idea fue que cada módulo hiciera una sola cosa y se comunicara con los demás a través de `Inventario`, que funciona como fachada: ni las clases del dominio saben que existe una base de datos, ni la interfaz gráfica necesita entender cómo funciona una lista circular para mostrar productos. Eso costó un par de iteraciones lograrlo —al principio todo estaba más enredado— pero una vez que quedó, agregar funcionalidad nueva se volvió más limpio.

### 8.1. Módulo de clases del dominio (`clases/`)

Define las entidades del problema y las relaciones entre ellas:

- **`registrable.py`** — Clase abstracta `Registrable` con el método `mostrar_info()`. Todas las clases que necesiten mostrarse en pantalla la implementan.
- **`producto.py`** — Clase base `Producto` con atributos encapsulados (código, nombre, categoría, precio, stock) y dos subclases: `ProductoPerecedero` (agrega días de caducidad) y `ProductoNoPerecedero` (agrega garantía en meses). La herencia permite tratar productos distintos con una misma interfaz. El polimorfismo se aplica en el método `tipo()`, que cada subclase implementa de forma distinta.
- **`proveedor.py`** — Clase `Proveedor` con RUC como identificador único, nombre, teléfono, email y dirección.
- **`movimiento.py`** — Clase abstracta `MovimientoInventario` y dos implementaciones concretas: `Entrada` y `Salida`. Cada una sabe cómo procesarse y cómo deshacerse, lo que permite la funcionalidad de *deshacer* mediante una pila.
- **`pedido.py`** — Clase `Pedido` que mantiene un diccionario de productos con cantidades y calcula el total de la orden.
- **`inventario.py`** — Clase coordinadora que integra la lista circular de productos, la cola de pedidos y la pila de movimientos. Expone métodos como `registrar_producto()`, `entrada_mercancia()`, `salida_mercancia()`, `deshacer_movimiento()`, `agregar_pedido()` y `reporte_bajo_stock()`.

### 8.2. Módulo de estructuras de datos (`estructuras/`)

Tres estructuras implementadas desde cero con nodos enlazados:

- **`lista_circular.py`** — Lista circular doblemente enlazada. Cada nodo apunta al siguiente y al anterior; el último nodo apunta al primero, formando un ciclo. Se usa para representar la rotación de productos en bodega. Inserción al final en O(1), búsqueda por código en O(n). Incluye un método `rotar()` que mueve la referencia al siguiente producto.
- **`cola.py`** — Cola FIFO con nodos enlazados. Se usa para gestionar los pedidos pendientes de despacho en orden de llegada. Operaciones `enqueue()` y `dequeue()` en O(1).
- **`pila.py`** — Pila LIFO con nodos enlazados. Cada movimiento de entrada o salida se apila al realizarse; la función de deshacer hace `pop()` y revierte la operación. `push()` y `pop()` en O(1).

### 8.3. Módulo de base de datos (`base_datos/`)

- **`conexion.py`** — Clase `ConexionDB` que maneja la conexión a SQLite, crea las tablas (proveedores, productos, movimientos) y expone métodos genéricos `ejecutar()` y `obtener()` para operaciones CRUD.
- **`esquema.sql`** — Script SQL para crear la base de datos desde DB Browser for SQLite.

La conexión a la base de datos está implementada y funcional a nivel de módulo. Queda pendiente la integración completa con la interfaz gráfica para que los datos se persistan automáticamente en cada operación.

### 8.4. Módulo de interfaz gráfica (`interfaz/`)

- **`ventana_principal.py`** — Ventana construida con Tkinter que contiene nueve botones de funcionalidad y un área de texto con scroll para la salida. Los botones permiten registrar productos y proveedores, listar y buscar productos, registrar movimientos de entrada/salida, deshacer el último movimiento, crear y procesar pedidos, y consultar el reporte de bajo stock. Cada botón abre cuadros de diálogo para ingresar datos y muestra los resultados en el área de texto.

### 8.5. Módulo principal (`main.py`)

Punto de entrada del programa. Crea una instancia de `Inventario`, la pasa a `VentanaPrincipal` e inicia el bucle de eventos de Tkinter.

### 8.6. Estado actual del sistema

| Componente | Estado |
|---|---|
| Clases del dominio (POO) | Completas: encapsulamiento, herencia, polimorfismo, abstracción |
| Estructuras de datos | Lista circular, cola y pila implementadas e integradas |
| Base de datos | Esquema creado, clase de conexión implementada, integración con GUI pendiente |
| Interfaz gráfica | Funcional para todas las operaciones del alcance |
| Algoritmos de ordenamiento | Pendientes de implementar |
| Algoritmos de búsqueda | Búsqueda lineal implementada en lista circular; búsqueda binaria pendiente |

---

## 9. Pruebas Realizadas

Antes de integrar, cada módulo se probó por su cuenta. Fue el tipo de prueba que se hace con la terminal abierta y datos inventados: crear un producto, ver si aparece, cambiarle el precio, borrarlo. Nada automatizado, pero sirvió para encontrar varias cosas que en el papel se veían bien y en la práctica no. 

### 9.1. Pruebas sobre clases del dominio

- **Registro de productos:** se crearon productos regulares, perecederos y no perecederos. Todos se almacenaron correctamente en la lista circular y mostraron la información esperada.
- **Herencia y polimorfismo:** se verificó que `ProductoPerecedero.tipo()` devuelve "Perecedero" y `ProductoNoPerecedero.tipo()` devuelve "No perecedero", mientras que `Producto.tipo()` devuelve "Producto".
- **Encapsulamiento:** se comprobó que asignar un precio negativo no modifica el atributo, gracias al setter con validación.

### 9.2. Pruebas sobre estructuras de datos

- **Lista circular:** se insertaron cinco productos, se recorrió la lista completa, se eliminó un producto del medio y se verificó que los enlaces se mantuvieran correctos. La búsqueda por código existente y no existente funcionó en ambos casos.
- **Cola:** se encolaron tres pedidos, se desencolaron en orden y se confirmó que el orden FIFO se respetó. Al vaciar la cola, `dequeue()` devolvió `None` sin errores.
- **Pila:** se apilaron cuatro movimientos, se desapilaron dos y se verificó que el orden LIFO se cumpliera. `pop()` sobre pila vacía devolvió `None`.

### 9.3. Pruebas sobre la interfaz gráfica

- Cada botón de la ventana principal se probó individualmente. Los cuadros de diálogo capturan correctamente los datos y las operaciones se reflejan en el área de texto.
- El botón de deshacer revierte el último movimiento de entrada o salida y actualiza el stock del producto afectado.
- La lista de productos con bajo stock muestra únicamente aquellos cuyo stock actual está por debajo del mínimo configurado.

### 9.4. Resultados

Ninguna de las pruebas dejó errores que rompieran el programa. La integración entre las clases de dominio, las estructuras de datos y la interfaz gráfica se mantuvo estable incluso después de varios ciclos de uso. Las operaciones CRUD sobre la base de datos se probaron desde consola directamente contra la clase `ConexionDB` —y funcionaron—, pero todavía no están conectadas a los botones de la interfaz. Eso queda para la semana 14.

---

## 10. Análisis de Complejidad Big-O

El análisis de complejidad muestra cómo se comporta el sistema cuando crece el volumen de datos. Las tablas siguientes resumen la complejidad temporal de cada operación crítica.

### 10.1. Lista circular

| Operación | Complejidad | Explicación |
|---|---|---|
| Insertar al final | O(1) | Se mantiene una referencia al último nodo; insertar requiere reasignar punteros del nuevo nodo, el último y el primero |
| Eliminar por código | O(n) | En el peor caso hay que recorrer toda la lista hasta encontrar el nodo que coincide con el código |
| Buscar por código | O(n) | Recorrido lineal nodo por nodo hasta encontrar la coincidencia |
| Recorrer (listar todos) | O(n) | Se visita cada nodo exactamente una vez |
| Rotar | O(1) | Solo se mueve la referencia `_ultimo` al siguiente nodo |

### 10.2. Cola

| Operación | Complejidad | Explicación |
|---|---|---|
| Enqueue (encolar) | O(1) | Se agrega un nodo al final; se reasignan punteros sin recorrer |
| Dequeue (desencolar) | O(1) | Se elimina el nodo del frente sin necesidad de recorrido |
| Peek (consultar frente) | O(1) | Acceso directo al nodo `_frente` |

### 10.3. Pila

| Operación | Complejidad | Explicación |
|---|---|---|
| Push (apilar) | O(1) | Se inserta un nodo en el tope sin recorrer |
| Pop (desapilar) | O(1) | Se elimina el nodo del tope; acceso directo |
| Peek (consultar tope) | O(1) | Acceso directo al nodo `_tope` |

### 10.4. Observaciones

Ninguna operación crítica del sistema supera la complejidad lineal O(n). Las operaciones más frecuentes (insertar producto, procesar pedido, deshacer movimiento) son de tiempo constante O(1). Eso significa que el sistema responde igual de rápido aunque el inventario tenga diez productos o diez mil. La búsqueda por código en la lista circular es lo más costoso (O(n)), pero en la semana 14 se agregará búsqueda binaria sobre una copia ordenada de los productos para reducir ese tiempo.

---

## 11. Conclusiones

Dos semanas de trabajo y el sistema de inventario y bodega quedó armado. No está terminado, pero lo que hay funciona y lo que falta tiene claro por dónde agarrarlo. Los conceptos de POO, estructuras de datos lineales y bases de datos relacionales —que hasta la semana 11 eran temas separados en el sílabo— terminaron conviviendo en un solo programa que hace cosas. ¿Qué se logró exactamente?

- Las clases del dominio (Producto, Proveedor, Movimiento, Pedido) se implementaron con encapsulamiento, herencia, polimorfismo y abstracción. El código quedó ordenado y, si alguien quiere agregar un tipo nuevo de producto, solo tiene que escribir una subclase más.
- La lista circular, la cola y la pila se escribieron a mano con nodos enlazados, sin tocar `collections.deque` ni nada prefabricado. El punto no era complicarse la vida: era poder explicar, cuando pregunten en la defensa, qué pasa realmente cuando se hace un `push` o un `dequeue`.
- La interfaz cubre las operaciones del alcance. Se usó Tkinter porque viene con Python, y cualquiera puede abrir el programa y empezar a registrar productos sin tocar una línea de código.
- La base de datos SQLite está creada, las tablas existen y la capa de conexión desde Python responde. Lo que no está es la integración con los formularios —hoy los datos viven en memoria y se pierden al cerrar la ventana. Eso se amarra en la semana 14.

Dicho corto: con las herramientas que se vieron en clase se armó algo que una bodega chica podría usar. Falta rematar ordenamiento, búsqueda binaria y el guardado automático, pero la estructura está.

---

## 12. Recomendaciones

Lo que toca ahora es cerrar lo que falta y dejar el sistema listo para la entrega final. En orden de prioridad:

Implementar los algoritmos de ordenamiento (burbuja y merge sort) y los de búsqueda (lineal y binaria) es lo más urgente, porque son requisito de la rúbrica. Sin eso, el proyecto queda incompleto aunque todo lo demás funcione. Después viene conectar la base de datos con la interfaz gráfica: los datos deberían guardarse solos al hacer cada operación y el sistema tendría que recordar el estado al reiniciarse —hoy todo se pierde al cerrar la ventana, y eso no sirve para un uso real.

Con eso andando, valdría la pena poner botones en la interfaz que ordenen los productos por precio, nombre o stock, y agregar búsqueda binaria sobre la lista ordenada para que las consultas no se vuelvan lentas cuando el inventario crezca. También hay que afinar los mensajes de la interfaz y validar los datos antes de aceptarlos —un precio negativo no debería llegar ni al modelo. Y de paso, hacer el manual de usuario con capturas de pantalla que muestren paso a paso cómo se usa cada funcionalidad. Eso también puntúa.

---

## 13. Referencias Bibliográficas

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

Deitel, P., & Deitel, H. (2019). *Python for Programmers*. Pearson Education.

Joyanes, L. (2018). *Programación en Python*. McGraw-Hill Interamericana de España.

Mauleón, M. (2018). *Logística y gestión de inventarios*. Ediciones Paraninfo.

Python Software Foundation. (2024). *The Python Language Reference*. https://docs.python.org/3/reference/

Summerfield, M. (2010). *Programming in Python 3: A Complete Introduction to the Python Language* (2nd ed.). Addison-Wesley Professional.

Weiss, M. A. (2013). *Data Structures and Algorithm Analysis in C++* (4th ed.). Pearson. [Principios aplicables a cualquier lenguaje de programación]

---

## 14. Anexos

### 14.1. Captura de pantalla: ventana principal del sistema

*[Insertar aquí la captura de pantalla de la ventana principal con los botones de funcionalidad y el área de texto]*

### 14.2. Captura de pantalla: registro de producto

*[Insertar aquí la captura del cuadro de diálogo de registro de producto y el mensaje de confirmación en el área de texto]*

### 14.3. Captura de pantalla: listado de productos

*[Insertar aquí la captura del listado de productos mostrado en el área de texto]*

### 14.4. Captura de pantalla: movimiento de entrada/salida

*[Insertar aquí la captura del cuadro de diálogo de movimiento y el resultado con el stock actualizado]*

### 14.5. Captura de pantalla: reporte de bajo stock

*[Insertar aquí la captura del reporte de productos con stock por debajo del mínimo]*

### 14.6. Enlace al repositorio del proyecto

*[Insertar aquí la URL del repositorio GitHub del proyecto, si aplica]*
