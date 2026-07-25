# -*- coding: utf-8 -*-
"""Genera diagrama UML de clases y diagrama MER como SVG."""

def generar_uml_svg(ruta):
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">')
    svg.append('<rect width="1200" height="900" fill="#ffffff"/>')

    titulo = 'Diagrama de Clases UML — Sistema de Gestión de Inventario y Bodega'
    svg.append(f'<text x="600" y="30" text-anchor="middle" font-family="Arial" font-size="18" font-weight="bold" fill="#1a1a2e">{titulo}</text>')

    # Definición de clases: (x, y, ancho, alto, nombre, [atributos], [metodos], color_encabezado)
    # Organizadas en posiciones estratégicas
    clases = [
        # Fila 0: Nodo (arriba, centro)
        (500, 55, 160, 90, 'Nodo',
         ['- dato: object', '- siguiente: Nodo'],
         [],
         '#2d6a4f'),

        # Fila 1: Estructuras de datos
        (100, 175, 190, 140, 'ListaCircular',
         ['- ultimo: Nodo'],
         ['+ insertar(dato)', '+ eliminar(codigo)',
          '+ buscar(codigo)', '+ recorrer()'],
         '#1b4332'),

        (480, 175, 170, 120, 'Cola',
         ['- frente: Nodo', '- final: Nodo'],
         ['+ enqueue(dato)', '+ dequeue()',
          '+ peek()', '+ is_empty()'],
         '#1b4332'),

        (840, 175, 170, 120, 'Pila',
         ['- tope: Nodo'],
         ['+ push(dato)', '+ pop()',
          '+ peek()', '+ is_empty()'],
         '#1b4332'),

        # Fila 2: Clases del dominio
        (50, 370, 190, 130, 'Producto',
         ['- codigo: str', '- nombre: str', '- descripcion: str',
          '- categoria: str', '- precio: float', '- stock_actual: int',
          '- stock_minimo: int', '- stock_maximo: int'],
         ['+ actualizar_stock(cant)', '+ mostrar_info()'],
         '#0f3460'),

        (290, 370, 185, 100, 'Proveedor',
         ['- ruc: str', '- nombre: str', '- telefono: str',
          '- email: str', '- direccion: str'],
         ['+ mostrar_info()'],
         '#0f3460'),

        (530, 370, 180, 115, 'Movimiento',
         ['- tipo: str', '- producto: Producto',
          '- cantidad: int', '- fecha: str'],
         ['+ aplicar()', '+ revertir()'],
         '#0f3460'),

        (760, 370, 185, 115, 'Pedido',
         ['- id_pedido: int', '- cliente: str',
          '- estado: str', '- fecha: str'],
         ['+ agregar_producto(prod, cant)', '+ calcular_total()'],
         '#0f3460'),

        # Fila 3: Inventario (clase principal)
        (290, 570, 420, 150, 'Inventario',
         ['- lista_circular: ListaCircular', '- cola_pedidos: Cola',
          '- pila_movimientos: Pila', '- proveedores: list[Proveedor]'],
         ['+ registrar_producto(p)', '+ registrar_proveedor(p)',
          '+ entrada_mercancia(cod, cant)', '+ salida_mercancia(cod, cant)',
          '+ encolar_pedido(pedido)', '+ procesar_pedido()',
          '+ deshacer_movimiento()', '+ reporte_bajo_stock()'],
         '#e63946'),
    ]

    # Dibujar clases
    for x, y, w, h, nombre, atributos, metodos, color in clases:
        # Sombra
        svg.append(f'<rect x="{x+3}" y="{y+3}" width="{w}" height="{h}" rx="4" fill="#d0d0d0"/>')
        # Cuerpo
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#f8f9fa" stroke="#333" stroke-width="1.5"/>')
        # Encabezado
        alt_header = 28
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{alt_header}" rx="4" fill="{color}"/>')
        svg.append(f'<rect x="{x}" y="{y+alt_header-4}" width="{w}" height="4" fill="{color}"/>')
        # Nombre clase
        svg.append(f'<text x="{x+w/2}" y="{y+18}" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#ffffff">{nombre}</text>')

        # Atributos
        ay = y + alt_header + 4
        for attr in atributos:
            svg.append(f'<text x="{x+8}" y="{ay+14}" font-family="Consolas" font-size="10" fill="#333">{attr}</text>')
            ay += 16

        # Separador atributos-métodos
        if metodos:
            sep_y = ay + 2
            svg.append(f'<line x1="{x+4}" y1="{sep_y}" x2="{x+w-4}" y2="{sep_y}" stroke="#999" stroke-width="0.8" stroke-dasharray="3,3"/>')
            ay = sep_y + 6

        # Métodos
        for met in metodos:
            svg.append(f'<text x="{x+8}" y="{ay+14}" font-family="Consolas" font-size="10" fill="#555">{met}</text>')
            ay += 16

    # Flechas de relación

    # 1. Inventario usa ListaCircular, Cola, Pila
    def flecha_uso(x1, y1, x2, y2, etiqueta=""):
        # line
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#555" stroke-width="1.2" stroke-dasharray="5,3"/>')
        # diamond at end
        dx, dy = x2 - x1, y2 - y1
        dist = (dx*dx + dy*dy) ** 0.5
        if dist > 0:
            ux, uy = dx/dist, dy/dist
            # small diamond
            sz = 6
            svg.append(f'<polygon points="{x2},{y2} {x2-sz*ux+sz*0.5*uy},{y2-sz*uy-sz*0.5*ux} {x2-2*sz*ux},{y2-2*sz*uy} {x2-sz*ux-sz*0.5*uy},{y2-sz*uy+sz*0.5*ux}" fill="#555" stroke="#555" stroke-width="1"/>')
        if etiqueta:
            mx, my = (x1+x2)/2, (y1+y2)/2
            svg.append(f'<text x="{mx-30}" y="{my-8}" font-family="Arial" font-size="10" fill="#555">{etiqueta}</text>')

    # Inventario (500, 645) centro base -> ListaCircular (195, 175) centro tope
    flecha_uso(500, 570, 195, 315, "usa")
    # Inventario -> Cola
    flecha_uso(500, 570, 565, 295, "usa")
    # Inventario -> Pila
    flecha_uso(500, 570, 925, 295, "usa")

    # 2. Nodo -> ListaCircular, Cola, Pila (composición: Nodo es parte de)
    def flecha_composicion(x1, y1, x2, y2):
        svg.append(f'<line x1="{x1+80}" y1="{y1+90}" x2="{x2}" y2="{y2}" stroke="#555" stroke-width="1.5"/>')
        # filled diamond on owner side
        sz = 7
        svg.append(f'<polygon points="{x1+80},{y1+90} {x1+80+sz},{y1+90+sz} {x1+80},{y1+90+2*sz} {x1+80-sz},{y1+90+sz}" fill="#333" stroke="#333" stroke-width="1"/>')

    flecha_composicion(500, 55, 150, 175)
    flecha_composicion(500, 55, 550, 175)
    flecha_composicion(500, 55, 910, 175)

    # 3. Asociación Inventario <-> Producto, Proveedor, Movimiento, Pedido
    def flecha_asociacion(x1, y1, x2, y2, etiqueta=""):
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#555" stroke-width="1.2"/>')
        # arrow at x2,y2
        dx, dy = x2 - x1, y2 - y1
        dist = (dx*dx + dy*dy) ** 0.5
        if dist > 0:
            ux, uy = dx/dist, dy/dist
            sz = 8
            svg.append(f'<polygon points="{x2},{y2} {x2-sz*ux+sz*0.4*uy},{y2-sz*uy-sz*0.4*ux} {x2-sz*ux-sz*0.4*uy},{y2-sz*uy+sz*0.4*ux}" fill="#555" stroke="#555" stroke-width="1"/>')
        if etiqueta:
            mx, my = (x1+x2)/2, (y1+y2)/2
            svg.append(f'<text x="{mx+5}" y="{my-5}" font-family="Arial" font-size="9" fill="#666">{etiqueta}</text>')

    flecha_asociacion(290, 570, 145, 500, "gestiona")
    flecha_asociacion(500, 570, 382, 485, "registra")
    flecha_asociacion(500, 570, 620, 485, "genera")
    flecha_asociacion(710, 570, 852, 485, "procesa")

    svg.append('</svg>')

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f"UML generado: {ruta}")


def generar_mer_svg(ruta):
    svg = []
    svg.append('<?xml version="1.0" encoding="UTF-8"?>')
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650">')
    svg.append('<rect width="1100" height="650" fill="#ffffff"/>')

    titulo = 'Modelo Entidad-Relación (MER) — Sistema de Gestión de Inventario y Bodega'
    svg.append(f'<text x="550" y="30" text-anchor="middle" font-family="Arial" font-size="18" font-weight="bold" fill="#1a1a2e">{titulo}</text>')

    # Entidades: (cx, cy, ancho, alto, nombre, [atributos], color_rect)
    entidades = [
        (180, 100, 200, 140, 'PROVEEDOR',
         ['RUC (PK)', 'nombre', 'teléfono', 'email', 'dirección'],
         '#0f3460'),

        (550, 100, 200, 170, 'PRODUCTO',
         ['código (PK)', 'nombre', 'descripción', 'categoría',
          'precio', 'stock_actual', 'stock_min', 'stock_max'],
         '#0f3460'),

        (180, 370, 200, 130, 'MOVIMIENTO',
         ['id_movimiento (PK)', 'tipo (E/S)', 'cantidad',
          'fecha', 'cod_producto (FK)'],
         '#1b4332'),

        (550, 370, 200, 130, 'PEDIDO',
         ['id_pedido (PK)', 'cliente', 'estado', 'fecha'],
         '#1b4332'),

        (880, 370, 200, 100, 'DETALLE\nPEDIDO',
         ['id_detalle (PK)', 'id_pedido (FK)', 'cod_producto (FK)', 'cantidad'],
         '#e63946'),
    ]

    for cx, cy, w, h, nombre, atributos, color in entidades:
        # Sombra
        svg.append(f'<rect x="{cx+2}" y="{cy+2}" width="{w}" height="{h}" rx="4" fill="#d0d0d0"/>')
        # Rectángulo entidad
        svg.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="{h}" rx="4" fill="#f0f4ff" stroke="{color}" stroke-width="2"/>')
        # Encabezado
        if '\n' in nombre:
            lines = nombre.split('\n')
            alt_h = 18 + 16 * len(lines)
        else:
            alt_h = 36
        svg.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="{alt_h}" rx="4" fill="{color}"/>')
        svg.append(f'<rect x="{cx}" y="{cy+alt_h-4}" width="{w}" height="4" fill="{color}"/>')

        if '\n' in nombre:
            lines = nombre.split('\n')
            for li, ln in enumerate(lines):
                svg.append(f'<text x="{cx+w/2}" y="{cy+14+16*li}" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#ffffff">{ln}</text>')
        else:
            svg.append(f'<text x="{cx+w/2}" y="{cy+23}" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#ffffff">{nombre}</text>')

        # Atributos
        ay = cy + alt_h + 6
        for attr in atributos:
            svg.append(f'<text x="{cx+12}" y="{ay+14}" font-family="Consolas" font-size="10" fill="#333">• {attr}</text>')
            ay += 17

    # Relaciones
    # Proveedor 1 --- N Producto
    x1, y1 = 280, 170
    x2, y2 = 550, 200
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="2"/>')
    svg.append(f'<text x="390" y="160" font-family="Arial" font-size="12" font-weight="bold" fill="#333">1</text>')
    svg.append(f'<text x="480" y="175" font-family="Arial" font-size="12" font-weight="bold" fill="#333">N</text>')
    svg.append(f'<text x="390" y="200" font-family="Arial" font-size="10" fill="#666">suministra</text>')

    # Producto 1 --- N Movimiento
    svg.append(f'<line x1="550" y1="300" x2="280" y2="370" stroke="#333" stroke-width="2"/>')
    svg.append(f'<text x="500" y="315" font-family="Arial" font-size="12" font-weight="bold" fill="#333">1</text>')
    svg.append(f'<text x="370" y="355" font-family="Arial" font-size="12" font-weight="bold" fill="#333">N</text>')
    svg.append(f'<text x="400" y="325" font-family="Arial" font-size="10" fill="#666">genera</text>')

    # Pedido 1 --- N DetallePedido
    svg.append(f'<line x1="650" y1="450" x2="880" y2="420" stroke="#333" stroke-width="2"/>')
    svg.append(f'<text x="710" y="460" font-family="Arial" font-size="12" font-weight="bold" fill="#333">1</text>')
    svg.append(f'<text x="810" y="435" font-family="Arial" font-size="12" font-weight="bold" fill="#333">N</text>')
    svg.append(f'<text x="750" y="448" font-family="Arial" font-size="10" fill="#666">contiene</text>')

    # Producto 1 --- N DetallePedido
    svg.append(f'<line x1="750" y1="270" x2="980" y2="370" stroke="#333" stroke-width="2"/>')
    svg.append(f'<text x="790" y="295" font-family="Arial" font-size="12" font-weight="bold" fill="#333">1</text>')
    svg.append(f'<text x="930" y="350" font-family="Arial" font-size="12" font-weight="bold" fill="#333">N</text>')
    svg.append(f'<text x="850" y="320" font-family="Arial" font-size="10" fill="#666">aparece en</text>')

    # Leyenda
    svg.append(f'<rect x="30" y="550" width="220" height="80" rx="4" fill="#f8f9fa" stroke="#ccc" stroke-width="1"/>')
    svg.append(f'<text x="140" y="568" text-anchor="middle" font-family="Arial" font-size="11" font-weight="bold" fill="#333">Convenciones</text>')
    svg.append(f'<rect x="40" y="578" width="12" height="12" fill="#0f3460"/>')
    svg.append(f'<text x="58" y="589" font-family="Arial" font-size="10" fill="#333">Entidad fuerte</text>')
    svg.append(f'<rect x="40" y="598" width="12" height="12" fill="#1b4332"/>')
    svg.append(f'<text x="58" y="609" font-family="Arial" font-size="10" fill="#333">Entidad débil / dependiente</text>')

    svg.append('</svg>')

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f"MER generado: {ruta}")


if __name__ == '__main__':
    import sys
    base = sys.argv[1] if len(sys.argv) > 1 else '.'
    generar_uml_svg(f'{base}/diagrama_uml.svg')
    generar_mer_svg(f'{base}/diagrama_mer.svg')
