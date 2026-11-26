<?php
header('Content-Type: application/json; charset=utf-8');

$server = "127.0.0.1";
$usuario = "root";
$clave = "";
$base = "articulos";
$puerto = 3306;

$conexion = mysqli_connect($server, $usuario, $clave, $base, $puerto);
mysqli_set_charset($conexion, 'utf8mb4');

$sql = "SELECT codigo, descripcion, precio
        FROM articulos ORDER BY codigo";
$datos = mysqli_query($conexion, $sql);
$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);

echo json_encode($resultado, JSON_UNESCAPED_UNICODE);
mysqli_close($conexion);