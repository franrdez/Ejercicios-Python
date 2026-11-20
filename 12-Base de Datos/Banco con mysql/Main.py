import tkinter as tk
from tkinter import messagebox
from Cajero import cajero

class main:

    def __init__(self):

        self.cajero = cajero()
        self.cliente = None

        self.ventana = tk.Tk()
        self.ventana.title("Cajero Poligonero")
        self.ventana.geometry("400x350")

        self.menu_principal()
        self.ventana.mainloop()

    def salir(self):
        self.cajero.cerrar_conexion()
        self.ventana.destroy()

    def menu_principal(self):

        for widget in self.ventana.winfo_children():
            widget.destroy()

        tk.Label(self.ventana, text="Bienvenido al Cajero Poligonero",
                 font=("Arial", 16)).pack(pady=20)

        tk.Label(self.ventana, text="Elija una opción").pack(pady=10)

        tk.Button(self.ventana, text="1 - Elegir cliente",
                  command=self.seleccionar_cliente).pack(pady=10)

        tk.Button(self.ventana, text="2 - Salir",
                  command=self.salir).pack(pady=10)

    def seleccionar_cliente(self):

        for widget in self.ventana.winfo_children():
            widget.destroy()

        tk.Label(self.ventana, text="Seleccione un cliente",
                 font=("Arial", 16)).pack(pady=20)

        for cliente in self.cajero.clientes:

            tk.Button(self.ventana, text=cliente.nombre,
                      command=lambda c=cliente: self.operaciones(c)).pack(pady=5)

        tk.Button(self.ventana, text="Volver",
                  command=self.menu_principal).pack(pady=15)

    def operaciones(self, cliente):

        self.cliente = cliente

        for widget in self.ventana.winfo_children():
            widget.destroy()

        tk.Label(self.ventana, text="Hola " + cliente.nombre,
                 font=("Arial", 16)).pack(pady=10)

        tk.Label(self.ventana,
                 text="Efectivo disponible: " + str(self.cajero.efectivo) + " €").pack(pady=5)

        tk.Button(self.ventana, text="1 - Ingresar dinero",
                  command=self.ingresar_dinero).pack(pady=5)

        tk.Button(self.ventana, text="2 - Extraer dinero",
                  command=self.extraer_dinero).pack(pady=5)

        tk.Button(self.ventana, text="3 - Consultar saldo",
                  command=self.consultar_saldo).pack(pady=5)

        tk.Button(self.ventana, text="4 - Volver",
                  command=self.seleccionar_cliente).pack(pady=15)

    def ingresar_dinero(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ingresar dinero")
        ventana.geometry("250x150")

        tk.Label(ventana, text="Cantidad a ingresar:").pack(pady=10)

        entrada = tk.Entry(ventana)
        entrada.pack()

        def ingresar():

            try:
                cantidad = float(entrada.get())
                resultado = self.cajero.ingresar_dinero(self.cliente, cantidad)
                messagebox.showinfo("Cajero", resultado)
                ventana.destroy()
                self.operaciones(self.cliente)

            except ValueError:
                messagebox.showerror("Error", "Introduce una cantidad válida")

        tk.Button(ventana, text="Ingresar", command=ingresar).pack(pady=10)

    def extraer_dinero(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Extraer dinero")
        ventana.geometry("250x150")

        tk.Label(ventana, text="Cantidad a extraer:").pack(pady=10)

        entrada = tk.Entry(ventana)
        entrada.pack()

        def extraer():

            try:
                cantidad = float(entrada.get())

                resultado = self.cajero.extraer_dinero(self.cliente, cantidad)

                messagebox.showinfo("Cajero", resultado)

                ventana.destroy()
                self.operaciones(self.cliente)

            except ValueError:
                messagebox.showerror("Error", "Introduce una cantidad válida")

        tk.Button(ventana, text="Extraer", command=extraer).pack(pady=10)

    def consultar_saldo(self):

        saldo = self.cliente.devolver_saldo()

        messagebox.showinfo("Consulta de saldo",
                            "El saldo de " + self.cliente.nombre +
                            " es de " + str(saldo) + " €")


main()