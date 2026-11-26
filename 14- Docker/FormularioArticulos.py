import tkinter as tk
from tkinter import ttk, messagebox as mb
from decimal import Decimal, InvalidOperation
from psycopg2 import Error
from psycopg2.errors import UniqueViolation
from articulos import Articulos
class FormularioArticulos:
    
    def __init__(self, ventana):
        self.articulos = Articulos()
        self.ventana = ventana
        ventana.title("Mantenimiento de artículos")
        self.cuaderno = ttk.Notebook(ventana)
        self.cuaderno.pack(padx=10, pady=10, fill="both", expand=True)
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
 
    def pagina(self, titulo):
        marco = ttk.Frame(self.cuaderno, padding=10)
        self.cuaderno.add(marco, text=titulo)
        return marco
    
    def campo(self, marco, texto, fila, solo_lectura=False):
        variable = tk.StringVar(master=marco)
        ttk.Label(marco, text=texto).grid(row=fila, column=0, sticky="e")
        estado = "readonly" if solo_lectura else "normal"
        entrada = ttk.Entry(marco, textvariable=variable, state=estado)
        entrada.grid(row=fila, column=1, padx=6, pady=4)
        return variable
    
    def boton(self, marco, texto, fila, accion):
        ttk.Button(marco, text=texto, command=accion).grid(
            row=fila, column=1, padx=6, pady=5, sticky="w"
    )
        
    def leer_codigo(self, campo_codigo):
        try:
            codigo = int(campo_codigo.get())
        except ValueError:
            raise ValueError("Introduce un código entero.") from None
        if not -2147483648 <= codigo <= 2147483647:
            raise ValueError("El código está fuera del rango de INTEGER.")
        return codigo
    
    def leer_datos(self, campo_descripcion, campo_precio):
        descripcion = campo_descripcion.get().strip()
        if not descripcion or len(descripcion) > 100:
            raise ValueError("Escribe entre 1 y 100 caracteres.")
        try:
            precio = Decimal(campo_precio.get().strip().replace(",", "."))
        except InvalidOperation:
            raise ValueError("Introduce un precio como 9,95.") from None
        if not precio.is_finite() or abs(precio) > Decimal("999999.99"):
            raise ValueError("El precio está fuera del rango permitido.")
        if precio != precio.quantize(Decimal("0.01")):
            raise ValueError("Usa como máximo dos decimales.")
        return descripcion, precio
    
    def carga_articulos(self):
        marco = self.pagina("Alta")
        self.codigocarga = self.campo(marco, "Código", 0)
        self.descripcioncarga = self.campo(marco, "Descripción", 1)
        self.preciocarga = self.campo(marco, "Precio", 2)
        self.boton(marco, "Guardar", 3, self.agregar)
 
    def agregar(self):
        try:
            codigo = self.leer_codigo(self.codigocarga)
            descripcion, precio = self.leer_datos(
                self.descripcioncarga, self.preciocarga
            )
            self.articulos.alta((codigo, descripcion, precio))
        except UniqueViolation:
            mb.showwarning("Código repetido", "Ese código ya existe.")
            return
        except (ValueError, Error) as error:
            mb.showerror("No se guardó el artículo", str(error))
            return
        mb.showinfo("Alta", "Artículo guardado.")
        self.codigocarga.set("")
        self.descripcioncarga.set("")
        self.preciocarga.set("")
 
    def consulta_por_codigo(self):
        marco = self.pagina("Consulta")
        self.codigo = self.campo(marco, "Código", 0)
        self.descripcion = self.campo(marco, "Descripción", 1, True)
        self.precio = self.campo(marco, "Precio", 2, True)
        self.boton(marco, "Consultar", 3, self.consultar)
 
    def consultar(self):
        self.cargar_por_codigo(self.codigo, self.descripcion, self.precio)
 
    def cargar_por_codigo(self, campo_codigo, descripcion, precio):
        descripcion.set("")
        precio.set("")
        try:
            codigo = self.leer_codigo(campo_codigo)
            filas = self.articulos.consulta((codigo,))
        except (ValueError, Error) as error:
            mb.showerror("Error en la consulta", str(error))
            return
        if filas:
            texto, importe = filas[0]
            descripcion.set(texto)
            precio.set(str(importe))
        else:
            mb.showinfo("Consulta", "Ese código no existe.")
 
    def listado_completo(self):
        marco = self.pagina("Listado")
        self.boton(marco, "Actualizar listado", 0, self.listar)
        self.tabla = ttk.Treeview(
            marco, columns=("codigo", "descripcion", "precio"),
            show="headings", height=9,
        )
        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("precio", text="Precio")
        self.tabla.column("codigo", width=75)
        self.tabla.column("descripcion", width=220)
        self.tabla.column("precio", width=85)
        self.tabla.grid(row=1, column=0, columnspan=2, pady=6)
 
    def listar(self):
        try:
            filas = self.articulos.recuperar_todos()
        except Error as error:
            mb.showerror("Error en el listado", str(error))
            return
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)
        for fila in filas:
            self.tabla.insert("", "end", values=fila)
 
    def borrado(self):
        marco = self.pagina("Borrado")
        self.codigoborra = self.campo(marco, "Código", 0)
        self.boton(marco, "Borrar", 1, self.borrar)
    
    def borrar(self):
        try:
            codigo = self.leer_codigo(self.codigoborra)
            if not mb.askyesno("Borrado", f"¿Borrar el código {codigo}?"):
                return
            cantidad = self.articulos.baja((codigo,))
        except (ValueError, Error) as error:
            mb.showerror("Error en el borrado", str(error))
            return
        mensaje = "Artículo borrado." if cantidad else "Ese código no existe."
        mb.showinfo("Borrado", mensaje)
 
    def modificar(self):
        marco = self.pagina("Modificación")
        self.codigomod = self.campo(marco, "Código", 0)
        self.descripcionmod = self.campo(marco, "Descripción", 1)
        self.preciomod = self.campo(marco, "Precio", 2)
        self.boton(marco, "Consultar", 3, self.consultar_mod)
        self.boton(marco, "Modificar", 4, self.modifica)
 
    def consultar_mod(self):
        self.cargar_por_codigo(
        self.codigomod, self.descripcionmod, self.preciomod
    )
 
    def modifica(self):
        try:
            codigo = self.leer_codigo(self.codigomod)
            descripcion, precio = self.leer_datos(
                self.descripcionmod, self.preciomod
            )
            cantidad = self.articulos.modificacion(
                (descripcion, precio, codigo)
            )
        except (ValueError, Error) as error:
            mb.showerror("Error en la modificación", str(error))
            return
        mensaje = "Artículo modificado." if cantidad else "Código inexistente."
        mb.showinfo("Modificación", mensaje)

if __name__ == "__main__":
 ventana = tk.Tk()
 FormularioArticulos(ventana)
 ventana.mainloop()