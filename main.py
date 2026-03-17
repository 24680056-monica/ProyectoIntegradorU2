import flet as ft
# -----------------------------
# MODELO DE DATOS
# -----------------------------

productos = [
    {"id": 1, "nombre": "Perfume Ariana Grande", "descripcion": "fragancia femenina que encapsula la personalidad dulce y coqueta de la artista.", "precio": 2000, "ruta_imagen": "1.jpg"},
    {"id": 2, "nombre": "Miss Dior", "descripcion": "Una fragancia concentrada con colores intensos, que incluye un sensual corazón de jazmín sambac combinado con un acorde de mora y flor de saúco.", "precio": 4460, "ruta_imagen": "2.webp"},
    {"id": 3, "nombre": "CHANEL MODELO 126460", "descripcion": "Una fragancia floral en un frasco de líneas redondeadas. Imprevisible, siempre en movimiento.", "precio": 3289, "ruta_imagen": "3.webp"},
    {"id": 4, "nombre": "Coco Noir", "descripcion": "Una ambarino moderno de notas luminosas. Una creación radical.", "precio": 3300, "ruta_imagen": "coconoir.png"},
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
                            src=f"./{producto['ruta_imagen']}",
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