from urllib import request
import json

url = (
    "http://localhost:3000"
    "/Curso_de_Python/16-JSON/retornararticulos.php"
)

with request.urlopen(url, timeout=10) as pagina:
    datos = pagina.read().decode("utf-8")

print("JSON recibido como texto")
print(datos)

lista = json.loads(datos)
print("Lista de Python")
print(lista)

print(f"{'Código':>6} {'Descripción':35} {'Precio':>10}")
for articulo in lista:
    print(
        f"{articulo['codigo']:>6} "
        f"{articulo['descripcion']:35} "
        f"{articulo['precio']:>10}"
    )