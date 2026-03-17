# Despliegue a una pagina web

## Crear build web
Se ejecuta la terminal git bash en nuestra carpeta donde esta nuestro main yse activa el entorno virtual
``` bash
$ source .venv/Scripts/activate
```
Ahora se ejecuta el siguiente comando para crear la carpeta del build web
``` bash
 flet publish main.py --base-url /perfumesweb/
```
## Despliegue de pagina
Se crea un repositorio en github con el nombre de "perfumesweb"

Ahora se agregaran los archivos a este reposito de la siguiente manera:
``` bash
git init
```
Esto para inicializar. Para agregar se ejecuta lo siguiente:
``` bash
git add .
```
Este agregara los documentos de esta carpeta a mi repositorio. Y se debe hacer un commit.
``` bash
git commit -m "deploy files"
```
Posteriormente, se agrega un branch main.
``` bash
$ git branch -M main
```
Y se marcan al repositorio que se dirigiran:
``` bash
$ git remote add origin https://github.com/24680056-monica/perfumesweb.git
```
O en el caso que marque error, quiere decir que ya tiene marcado o reconoce su direccion. Simplemente se hace un push.
``` bash
git push -u origin main
```
## Crear page en GitHub
Una vez que aparecen los documentos o archivos en nuestro repositorio se debe ir al apartado de settings y se ahi al apartado de `pages`.
Se modifica en el branch y cambiandolo al main y en el icono de carpetas, nuestra carpeta creada con el comando que creo nuestra web.
Ejemplo:
<img width="797" height="454" alt="image" src="https://github.com/user-attachments/assets/554ead69-557d-4cd6-9fdb-b7fdcde0288f" />

Y se da save, despues se espera a que se despliegue la pagina, dandonos al final un link.

# Resultado Final
Nuestra pagina se observara como: 
<img width="1683" height="955" alt="image" src="https://github.com/user-attachments/assets/5175c067-c8b1-43ad-8caa-e89bebe3afec" />

El link de la pagina es el siguiente:
https://24680056-monica.github.io/perfumesweb/

