# -*- coding: utf-8 -*-
"""Genera diagramas .drawio editables en diagrams.net"""

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def crear_drawio(celdas, nombre_archivo):
    root = ET.Element("mxGraphModel")
    root.set("dx", "1200")
    root.set("dy", "900")
    root.set("grid", "1")
    root.set("gridSize", "10")
    root.set("guides", "1")
    root.set("tooltips", "1")
    root.set("connect", "1")
    root.set("arrows", "1")
    root.set("fold", "1")
    root.set("page", "0")
    root.set("pageScale", "1")
    root.set("pageWidth", "1200")
    root.set("pageHeight", "900")

    root.set("math", "0")
    root.set("shadow", "0")

    diagram = ET.SubElement(root, "root")
    # Celda 0 y 1 son obligatorias en draw.io
    mx0 = ET.SubElement(diagram, "mxCell")
    mx0.set("id", "0")
    mx1 = ET.SubElement(diagram, "mxCell")
    mx1.set("id", "1")
    mx1.set("parent", "0")

    for celda in celdas:
        mx = ET.SubElement(diagram, "mxCell")
        mx.set("id", str(celda["id"]))
        mx.set("value", celda.get("value", ""))
        mx.set("style", celda.get("style", ""))
        mx.set("vertex", celda.get("vertex", "0"))
        mx.set("parent", celda.get("parent", "1"))
        if "geometry" in celda:
            g = ET.SubElement(mx, "mxGeometry")
            g.set("x", str(celda["geometry"]["x"]))
            g.set("y", str(celda["geometry"]["y"]))
            g.set("width", str(celda["geometry"]["w"]))
            g.set("height", str(celda["geometry"]["h"]))
            g.set("as", "geometry")

    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(xml_str)
    print(f"Generado: {nombre_archivo}")


def generar_uml():
    celdas = []
    cid = 2

    style_clase = "rounded=1;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#333;"
    style_header = "rounded=1;whiteSpace=wrap;html=1;fillColor=#2d6a4f;strokeColor=#2d6a4f;fontColor=#ffffff;fontStyle=1;"
    style_attrib = "text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;overflow=hidden;fillColor=none;strokeColor=none;"
    style_method = "text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;overflow=hidden;fillColor=none;strokeColor=none;fontColor=#555;"

    def add_clase(x, y, w, h, nombre, atributos, metodos, color):
        nonlocal cid
        parent = cid
        cid += 1
        celdas.append({"id": parent, "value": "", "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor=#f8f9fa;strokeColor=#333;", "vertex": "1", "geometry": {"x": x, "y": y, "w": w, "h": h}})

        # Header
        celdas.append({"id": cid, "value": f"<b>{nombre}</b>", "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor={color};strokeColor={color};fontColor=#ffffff;fontStyle=1;", "vertex": "1", "parent": str(parent), "geometry": {"x": 0, "y": 0, "w": w, "h": 28}})
        cid += 1

        # Atributos
        attr_text = "<br>".join(atributos)
        celdas.append({"id": cid, "value": attr_text, "style": "text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;overflow=hidden;fillColor=none;strokeColor=none;fontColor=#333;", "vertex": "1", "parent": str(parent), "geometry": {"x": 0, "y": 30, "w": w, "h": len(atributos) * 16 + 6}})
        cid += 1

        # Métodos
        if metodos:
            met_text = "<hr>" + "<br>".join(metodos)
            celdas.append({"id": cid, "value": met_text, "style": "text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;overflow=hidden;fillColor=none;strokeColor=none;fontColor=#555;fontStyle=0;", "vertex": "1", "parent": str(parent), "geometry": {"x": 0, "y": 30 + len(atributos) * 16 + 6, "w": w, "h": len(metodos) * 16 + 10}})
            cid += 1

    # Nodo
    add_clase(500, 55, 160, 90, "Nodo",
              ["- dato: object", "- siguiente: Nodo"],
              [], "#2d6a4f")

    # ListaCircular
    add_clase(100, 175, 190, 140, "ListaCircular",
              ["- ultimo: Nodo"],
              ["+ insertar(dato)", "+ eliminar(codigo)", "+ buscar(codigo)", "+ recorrer()"], "#1b4332")

    # Cola
    add_clase(480, 175, 170, 120, "Cola",
              ["- frente: Nodo", "- final: Nodo"],
              ["+ enqueue(dato)", "+ dequeue()", "+ peek()", "+ is_empty()"], "#1b4332")

    # Pila
    add_clase(840, 175, 170, 120, "Pila",
              ["- tope: Nodo"],
              ["+ push(dato)", "+ pop()", "+ peek()", "+ is_empty()"], "#1b4332")

    # Producto
    add_clase(50, 370, 190, 130, "Producto",
              ["- codigo: str", "- nombre: str", "- descripcion: str", "- categoria: str",
               "- precio: float", "- stock_actual: int", "- stock_minimo: int", "- stock_maximo: int"],
              ["+ actualizar_stock(cant)", "+ mostrar_info()"], "#0f3460")

    # Proveedor
    add_clase(290, 370, 185, 100, "Proveedor",
              ["- ruc: str", "- nombre: str", "- telefono: str", "- email: str", "- direccion: str"],
              ["+ mostrar_info()"], "#0f3460")

    # Movimiento
    add_clase(530, 370, 180, 115, "Movimiento",
              ["- tipo: str", "- producto: Producto", "- cantidad: int", "- fecha: str"],
              ["+ aplicar()", "+ revertir()"], "#0f3460")

    # Pedido
    add_clase(760, 370, 185, 115, "Pedido",
              ["- id_pedido: int", "- cliente: str", "- estado: str", "- fecha: str"],
              ["+ agregar_producto(prod, cant)", "+ calcular_total()"], "#0f3460")

    # Inventario
    add_clase(290, 570, 420, 150, "Inventario",
              ["- lista_circular: ListaCircular", "- cola_pedidos: Cola",
               "- pila_movimientos: Pila", "- proveedores: list[Proveedor]"],
              ["+ registrar_producto(p)", "+ registrar_proveedor(p)",
               "+ entrada_mercancia(cod, cant)", "+ salida_mercancia(cod, cant)",
               "+ encolar_pedido(pedido)", "+ procesar_pedido()",
               "+ deshacer_movimiento()", "+ reporte_bajo_stock()"], "#e63946")

    crear_drawio(celdas, "C:/Users/Eli/Desktop/NUEVO PROYECTO PROGRAMACION/01-Documentacion/diagrama_uml.drawio")


def generar_mer():
    celdas = []
    cid = 2

    def add_entidad(x, y, w, h, nombre, atributos, color):
        nonlocal cid
        parent = cid
        cid += 1
        celdas.append({"id": parent, "value": "", "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor=#f0f4ff;strokeColor={color};", "vertex": "1", "geometry": {"x": x, "y": y, "w": w, "h": h}})

        # Header
        celdas.append({"id": cid, "value": f"<b>{nombre}</b>", "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor={color};strokeColor={color};fontColor=#ffffff;fontStyle=1;", "vertex": "1", "parent": str(parent), "geometry": {"x": 0, "y": 0, "w": w, "h": 36}})
        cid += 1

        # Atributos
        attr_text = "<br>".join(f"• {a}" for a in atributos)
        celdas.append({"id": cid, "value": attr_text, "style": "text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;overflow=hidden;fillColor=none;strokeColor=none;fontColor=#333;", "vertex": "1", "parent": str(parent), "geometry": {"x": 0, "y": 38, "w": w, "h": len(atributos) * 17 + 6}})
        cid += 1

    add_entidad(180, 100, 200, 140, "PROVEEDOR",
                ["RUC (PK)", "nombre", "teléfono", "email", "dirección"], "#0f3460")

    add_entidad(550, 100, 200, 170, "PRODUCTO",
                ["código (PK)", "nombre", "descripción", "categoría",
                 "precio", "stock_actual", "stock_min", "stock_max"], "#0f3460")

    add_entidad(180, 370, 200, 130, "MOVIMIENTO",
                ["id_movimiento (PK)", "tipo (E/S)", "cantidad", "fecha", "cod_producto (FK)"], "#1b4332")

    add_entidad(550, 370, 200, 130, "PEDIDO",
                ["id_pedido (PK)", "cliente", "estado", "fecha"], "#1b4332")

    add_entidad(880, 370, 200, 130, "DETALLE PEDIDO",
                ["id_detalle (PK)", "id_pedido (FK)", "cod_producto (FK)", "cantidad"], "#e63946")

    crear_drawio(celdas, "C:/Users/Eli/Desktop/NUEVO PROYECTO PROGRAMACION/01-Documentacion/diagrama_mer.drawio")


if __name__ == "__main__":
    generar_uml()
    generar_mer()
