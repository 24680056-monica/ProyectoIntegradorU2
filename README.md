# ProyectoIntegradorU2

# TiendaPerfumesFlet

Para este proyecto se desarrolló una pequeña tienda de perfumes utilizando Python y el framework Flet que nos permite crear nuestra interfaz.

La aplicación muestra un catálogo de perfumes en forma de tarjetas, donde cada producto tiene:

- Imagen
- Nombre
- Descripción
- Precio
- Botón para agregar al carrito
- Botón de favorito

Cada perfume se presenta en una tarjeta visual para simular el diseño de una tienda en línea.

## Configuración del entorno

Primero se importa Flet, que es el framework que permite crear la interfaz gráfica.

import flet as ft

Flet funciona creando controles visuales como textos, botones, filas, columnas, imágenes que ayudan para crear nuestro catalogo.

## Modelo de datos
En esta sección se crea la lista de productos, donde cada producto contendra su informacion respectiva.
``` python
productos = [
    {"id": 1, "nombre": "Perfume Ariana Grande", "descripcion": "fragancia femenina que encapsula la personalidad dulce y coqueta de la artista.", "precio": 2000, "ruta_imagen": "1.jpg"},
    {"id": 2, "nombre": "Miss Dior", "descripcion": "Una fragancia concentrada con colores intensos, que incluye un sensual corazón de jazmín sambac combinado con un acorde de mora y flor de saúco.", "precio": 4460, "ruta_imagen": "2.webp"},
    {"id": 3, "nombre": "CHANEL MODELO 126460", "descripcion": "Una fragancia floral en un frasco de líneas redondeadas. Imprevisible, siempre en movimiento.", "precio": 3289, "ruta_imagen": "3.webp"},
    {"id": 4, "nombre": "Coco Noir", "descripcion": "Una ambarino moderno de notas luminosas. Una creación radical.", "precio": 3300, "ruta_imagen": "coconoir.png"},
    {"id": 5, "nombre": "Ariana Grande Thank U Next", "descripcion": "Es una fragancia dulce y juvenil que refleja la personalidad divertida y empoderada de la cantante.", "precio": 2500, "ruta_imagen": "5.webp"},
    {"id": 6, "nombre": "Valentino Donna", "descripcion": "es una fragancia de la familia olfativa Ámbar Floral para Mujeres, es una mezcla moderna de flores blancas (jazmín), vainilla ahumada y notas amaderadas.", "precio": 3500, "ruta_imagen": "6.webp"},
    {"id": 7, "nombre": "PERFUME ÁRABE DAMA-YARA LATTAFA ", "descripcion": "Esta fragancia destaca por su elegancia, intensidad y duración prolongada, lo que la convierte en una opción popular.", "precio": 1000, "ruta_imagen": "7.webp"},
]
``` 
- Cada producto contiene:
- id : identificador del producto
- nombre : nombre del perfume
- descripcion : descripción breve del producto
- precio : precio del perfume
- ruta_imagen : imagen que se mostrará en la tarjeta
Siendo necesario para mostrarse en las tarjetas

## Creación de un componente reutilizable

Después se crea una clase llamada `ProductoCard`, la cual representa una tarjeta visual para cada producto.
``` python
class ProductoCard(ft.Container):
```

Se usa `Container` porque permite contener varios controles dentro y aplicar estilos como tamaño, color o bordes.

Dentro del constructor`__init__` se recibe el producto que se quiere mostrar:
``` python
def __init__(self, producto):
```
Esto permite reutilizar el mismo componente para todos los productos del catálogo.

## Configuración de la tarjeta
Aquí se definen las propiedades visuales de la tarjeta.
``` python
self.width = 250
self.height = 360
self.padding = 10
self.border_radius = 15
self.bgcolor = ft.Colors.WHITE
```
Estas propiedades definen:
- width : ancho de la tarjeta
- height : altura de la tarjeta
- padding : espacio interno
- border_radius : bordes redondeados
- bgcolor : color de fondo

## Organización del contenido

El contenido de la tarjeta se organiza utilizando una Column, que permite acomodar los elementos de arriba hacia abajo.
``` python
self.content = ft.Column(
    expand=True,
    spacing=8,
)
``` 
Aquí se agregan los diferentes elementos que tendrá la tarjeta.

### Imagen y boton
Se crea inicialmente la funcion de `ft.Stack`:
``` python
                ft.Stack(
                    width=230,
                    height=150,
                    controls=[
```
Se coloca dentro la funcion de la imagen y del boton para poder suponer el boton de corazon en la imagen del producto.

### Imagen del producto
Para mostrar la imagen se utiliza el control Image.
``` python
ft.Image(
    src=f"./{producto['ruta_imagen']}",
    width=230,
    height=150,
    fit="cover"
)
``` 
- `src` :  indica la ruta de la imagen.
- `fit="cover"` : hace que la imagen se adapte al tamaño sin deformarse.

### Botón de favorito
En la esquina de la imagen se agrega un botón de corazón usando IconButton.
``` python
ft.IconButton(
    icon=ft.Icons.FAVORITE_BORDER,
    icon_color=ft.Colors.RED_400,
)
```
Este botón simula marcar el producto como favorito.

### Nombre del producto
Después se muestra el nombre del perfume.
``` python
ft.Text(
    producto["nombre"],
    size=18,
    weight="bold",
)
``` 
Se utiliza `Text` para mostrar el nombre del producto con un tamaño mayor y en negrita.

### Descripción del perfume
Se coloca otro `Text`, para colocar el texto largo de la descripcion.
``` python
ft.Text(
    producto["descripcion"],
    size=12
)
```
Este texto es más pequeño para no ocupar demasiado espacio dentro de la tarjeta.
### Barra inferior
En esta parte del código se construye la zona inferior de la tarjeta del producto, donde se muestran el precio del perfume y el botón para agregarlo al carrito.

``` python
                # Barra de acciones
                ft.Container(expand=True),
```
Este `Container` tiene la propiedad `expand=True`, lo que significa que ocupará todo el espacio disponible dentro de la columna.
Su función es empujar la barra inferior hacia la parte baja de la tarjeta, manteniendo siempre el precio y el botón alineados abajo, sin importar cuánto texto tenga la descripción.
``` python
                # Barra inferior
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
```
Aquí se utiliza un Row porque los elementos se quieren organizar horizontalmente.

La propiedad:
``` python
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN
```
significa que los elementos se colocarán uno a cada extremo de la fila:
- El precio quedará a la izquierda.
- El botón quedará a la derecha.
### Precio
``` python
                # Precio
                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    weight="bold",
                    color=ft.Colors.RED_100
                ),
```
Se utiliza una f-string para mostrar el precio con el símbolo de dinero y se le da un valor de color rojo para que resalte.
### Boton de compra
``` python
                ft.ElevatedButton(
                    "Agregar",
                    icon=ft.Icons.SHOPPING_CART
                        )
                    ]
                )
            ]
        )
```
Este botón utiliza el control `ElevatedButton`, para hacerlo más visible ademas que se agrega un icono de carrito de compras.

## Interfaz principal
Después se crea la función principal main, donde se configura la página.
``` python 
def main(page: ft.Page):
```

Dentro se configuran algunas propiedades de la ventana.
``` python
page.title = "Tienda Perfumes"
page.bgcolor = ft.Colors.PINK_50
page.scroll = "auto"
``` 
Estas propiedades indican:
- title : título de la ventana
- bgcolor : color de fondo
- scroll : permite desplazarse si el contenido es mayor que la pantalla

### Encabezado de la página

Se agrega un título para la tienda.
``` python
header = ft.Text(
    "Perfuma",
    size=30,
    weight="bold",
    italic=True
)
``` 
Este texto muestra el nombre de la tienda, se da su tamaño y la letra.

## Creación del catálogo

Después se generan las tarjetas automáticamente usando un ciclo.
``` python
tarjetas = []

for producto in productos:
    tarjetas.append(ProductoCard(producto))
``` 
Aquí se recorre la lista de productos, tomando los valores que se dieron al inicio en el array y se crea una tarjeta para cada uno.

## Organización del catálogo

Las tarjetas se colocan dentro de una Row.
``` python
catalogo = ft.Row(
    controls=tarjetas,
    wrap=True,
    spacing=20
)
```
Esto permitiendo que:
- Las tarjetas se acomoden horizontalmente
- Se ajusten automáticamente cuando no haya espacio
- Se mantenga una separación entre ellas

## Mostrar la interfaz

Finalmente se agregan los elementos a la página.
``` python
page.add(
    header,
    catalogo
)
```
Esto hace que se muestre el título y el catálogo de productos.

## Ejecución de la aplicación

Para iniciar la aplicación se utiliza:
``` python
ft.app(
    target=main,
    assets_dir="assets"
)
``` 
Donde:
- target=main indica la función principal de la aplicación
- assets_dir="imagenes" especifica la carpeta donde se encuentran las imágenes de los productos.

# Ejecución
Se muestra una captura de como se ve al ejecutarse:
<img width="1571" height="1002" alt="image" src="https://github.com/user-attachments/assets/6ec65f1c-4e85-4842-a7b8-1f9ad06d0131" />

# Código completo
``` python
import flet as ft

# -----------------------------
# MODELO DE DATOS
# -----------------------------

productos = [
    {"id": 1, "nombre": "Perfume Ariana Grande", "descripcion": "fragancia femenina que encapsula la personalidad dulce y coqueta de la artista.", "precio": 2000, "ruta_imagen": "1.jpg"},
    {"id": 2, "nombre": "Miss Dior", "descripcion": "Una fragancia concentrada con colores intensos, que incluye un sensual corazón de jazmín sambac combinado con un acorde de mora y flor de saúco.", "precio": 4460, "ruta_imagen": "2.webp"},
    {"id": 3, "nombre": "CHANEL MODELO 126460", "descripcion": "Una fragancia floral en un frasco de líneas redondeadas. Imprevisible, siempre en movimiento.", "precio": 3289, "ruta_imagen": "3.webp"},
    {"id": 4, "nombre": "Coco Noir", "descripcion": "Una ambarino moderno de notas luminosas. Una creación radical.", "precio": 3300, "ruta_imagen": "4.avif"},
    {"id": 5, "nombre": "Ariana Grande Thank U Next", "descripcion": "Es una fragancia dulce y juvenil que refleja la personalidad divertida y empoderada de la cantante.", "precio": 2500, "ruta_imagen": "5.webp"},
    {"id": 6, "nombre": "Valentino Donna", "descripcion": "es una fragancia de la familia olfativa Ámbar Floral para Mujeres, es una mezcla moderna de flores blancas (jazmín), vainilla ahumada y notas amaderadas.", "precio": 3500, "ruta_imagen": "6.webp"},
    {"id": 7, "nombre": "PERFUME ÁRABE DAMA-YARA LATTAFA ", "descripcion": "Esta fragancia destaca por su elegancia, intensidad y duración prolongada, lo que la convierte en una opción popular.", "precio": 1000, "ruta_imagen": "7.webp"},
]


# -----------------------------
# COMPONENTE REUTILIZABLE
# -----------------------------

class ProductoCard(ft.Container):

    def __init__(self, producto):

        super().__init__()

        self.width = 250
        self.height = 360
        self.padding = 10
        self.border_radius = 15
        self.bgcolor = ft.Colors.WHITE

        self.content = ft.Column(
            expand=True,
            spacing=8,
            controls=[

                ft.Stack(
                    width=230,
                    height=150,
                    controls=[

        # Imagen
                        ft.Image(
                            src=producto["ruta_imagen"],
                            width=230,
                            height=150,
                            fit="cover"
                            ),

        # Botón corazón
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.Icons.FAVORITE_BORDER,
                                icon_color=ft.Colors.RED_400,
                            ),
                            left=5,
                            top=5
                            )
                     ]
                ),
                # Nombre
                ft.Text(
                    producto["nombre"],
                    size=18,
                    weight="bold",
                    color=ft.Colors.BLACK_38,

                ),

                # Descripción
                ft.Text(
                    producto["descripcion"],
                    size=12,
                    color=ft.Colors.BLACK_54
                ),
                # Barra de acciones
                ft.Container(expand=True),

                # Barra inferior
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                # Precio
                ft.Text(
                    f"${producto['precio']}",
                    size=16,
                    weight="bold",
                    color=ft.Colors.RED_100
                ),
                ft.ElevatedButton(
                    "Agregar",
                    icon=ft.Icons.SHOPPING_CART
                        )
                    ]
                )
            ]
        )


# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------

def main(page: ft.Page):

    page.title = "Tienda Perfumes"
    page.bgcolor = ft.Colors.PINK_50
    page.scroll = "auto"

    header = ft.Text(
        "Perfuma",
        size=30,
        weight="bold",
        italic= True,
        color=ft.Colors.PINK,
    )

    tarjetas = []

    for producto in productos:
        tarjetas.append(ProductoCard(producto))

    catalogo = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=20
    )

    page.add(
        header,
        catalogo
    )


ft.app(
    target=main,
    assets_dir="assets"
)
```
# Despliegue en web
Se muestran los resultados, la documentacion se encuentra en el apartado del documento llamado "Despliegue"

-Link: https://24680056-monica.github.io/perfumesweb/
<img width="1697" height="974" alt="image" src="https://github.com/user-attachments/assets/3387a5bf-558b-4d64-a2b1-828742286c15" />

