from contextlib import closing
import psycopg2

class Articulos:
    def abrir(self):
        return psycopg2.connect(
            host="127.0.0.1", port=5433, dbname="md1",
            user="usuario", password="clave",
        )
        
    def alta(self, datos):
        sql = """INSERT INTO public.articulos (codigo, descripcion, precio)
            VALUES (%s, %s, %s)"""
        with closing(self.abrir()) as conexion:
            with conexion, conexion.cursor() as cursor:
                cursor.execute(sql, datos)
 
    def consulta(self, datos):
        sql = """SELECT descripcion, precio FROM public.articulos
            WHERE codigo = %s"""
        with closing(self.abrir()) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql, datos)
                return cursor.fetchall()
            
    def recuperar_todos(self):
        sql = """SELECT codigo, descripcion, precio
            FROM public.articulos ORDER BY codigo"""
        with closing(self.abrir()) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
 
    def baja(self, datos):
        sql = "DELETE FROM public.articulos WHERE codigo = %s"
        with closing(self.abrir()) as conexion:
            with conexion, conexion.cursor() as cursor:
                cursor.execute(sql, datos)
                return cursor.rowcount
 
    def modificacion(self, datos):
        sql = """UPDATE public.articulos SET descripcion = %s, precio = %s
            WHERE codigo = %s"""
        with closing(self.abrir()) as conexion:
            with conexion, conexion.cursor() as cursor:
                cursor.execute(sql, datos)
                return cursor.rowcount