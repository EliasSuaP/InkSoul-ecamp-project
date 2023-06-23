# InkSoul-ecamp-project
## Proyecto libre hecho principalmente con Django. Aplicación web de un estudio de tatuajes.

### Herramientas utilizadas

- Django 4.2
- Boostrap 5
- Html 5
- Css 3
- JavaScript Vanilla

Este proyecto de app web conta de las siguentes secciones:

- Home
- Reservar:
  ##### Funcionalidades: Contiene un formulario que permite el ingreso de 4 campos: Nombre, apellido, fecha y hora. Permite reservar una hora con los tatuadores. Al enviar los formularios mediante la views.py se utiliza el método get() para estraer el nombre y apellido de quién envia el form y se crea un mensaje de agradecimiento personalizado al redirigirlo al template 'gracias.html'
- Venta de kits:
  ##### Se muestran diferentes kits de productos obteniendo la url desde [una nube pública ](https://imgfz.com/es/) con la descripción de cada uno, precio y mediante un ciclo for en el template con sintaxis jinja 2 se logra mostrar cada una de las url que está guardada en un models.py. Adicionalmente en la parte inferior de cada carta de producto se muestra un mensaje que indica "Debe estar registrado para poder comprar este producto", lo que se convierte en un botón de comprar al iniciar sesión.
- Tatuadores:
  
- Galerías:
  ##### Funcionalidades: Dropdown que muestra 3 galerías distintas que traen imágenes desde [una nube pública ](https://imgfz.com/es/) mediante una url que es guardada en los models.py a la cuál se accede mediante un ciclo for (jinja2) para iterar y mostrar cada una de las imágenes.

- Botón Inicio de sesión:
  ##### Funcionalidades: Al iniciar sesión nos redirige al template de Home y muestra un mensaje de bienvenida personalizado (Funcionalidad hecha con sintaxis jinja2), además se quitan los botones de **iniciar sesión** y **registrarse** sustituyendolos por uno de **cerrar sesión** y **shopping** que conecta con la venta de kits. Adicionalmente se habilita un botón que permite comprar los kits.
- Botón Registrarse (Sin funcionalidad de momento)
