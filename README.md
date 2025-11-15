# Sistema de E-commerce "Adidas" (Proyecto Escolar)

Proyecto final para la materia de Bases de Datos II. Es una aplicación de escritorio completa desarrollada en **Python** que simula el backend y la interfaz de cliente de un sistema de e-commerce, utilizando **MongoDB** como base de datos NoSQL.

La aplicación está construida en un solo archivo `main.py` usando **Tkinter** para la interfaz gráfica y **PyMongo** para la conexión con la base de datos.

## Características Principales

El sistema se divide en dos módulos principales (Admin y Cliente) con un sistema de autenticación basado en roles.

### Autenticación y Generales
* **Login de Usuario:** Verifica las credenciales contra la colección `A_usuarios`.
* **Registro de Clientes:** Permite a nuevos usuarios crear una cuenta, que se guarda en `A_usuarios` con `rol: "cliente"` y `estado: "activo"`.
* **Sistema de Roles:** La aplicación muestra un panel diferente si el usuario es `admin` o `cliente`.
* **Navegación por Frames:** La aplicación usa una sola ventana raíz (`Tk`) y cambia entre "páginas" (`Frame`) para el login y registro.
* **Paneles Modales:** Los paneles de Admin y Cliente se abren como nuevas ventanas (`Toplevel`) que, al cerrarse, devuelven al usuario al login.

### Panel de Administrador (CRUD Completo)
Es un panel de 4 pestañas (`ttk.Notebook`) para gestionar toda la tienda:

1.  **Gestionar Productos (`A_productos`):**
    * **[Read]** Muestra todos los productos en una tabla (`Treeview`).
    * **[Create]** Permite crear nuevos productos con todos sus campos.
    * **[Update]** Al seleccionar un producto, el formulario se rellena para editarlo (usando `$set`).
    * **[Delete]** Permite eliminar un producto de la base de datos.
    * **(Req 6.3)** Muestra la imagen del producto seleccionado desde una URL.
    * **(Req 6.5)** Incluye botones para modificar el arreglo `tags_busqueda` usando **`$push`** (añadir tag) y **`$pop`** (quitar último tag).

2.  **Gestionar Inventario (`A_inventario`):**
    * **[Read]** Muestra todas las variantes de stock, usando **`$lookup`** para mostrar el *nombre* del producto en lugar de su `_id`.
    * **[Create]** Permite crear nuevas variantes (tallas/colores) usando un menú desplegable (`Combobox`) que se carga desde la colección de productos.
    * **[Update]** Permite editar el SKU, color, talla o cantidad de stock de una variante.
    * **[Delete]** Permite eliminar una variante de inventario.

3.  **Ver Usuarios (`A_usuarios`):**
    * **[Read]** Muestra una lista de todos los usuarios (clientes y admins).
    * **[Update]** Permite a un admin **Activar** o **Desactivar** una cuenta de cliente (usando `$set` en el campo `estado`). El login principal valida este campo.

4.  **Ver Órdenes (`A_ordenes`):**
    * **[Read]** Muestra un historial de todas las órdenes, usando **`$lookup`** para mostrar el *email* del cliente. Formatea la fecha (`strftime`) y el total (`:,.2f`).

### Panel de Cliente (Simulación de E-commerce)
Es un panel de 3 pestañas para la experiencia de compra:

1.  **Ver Productos (Tienda):**
    * Muestra el catálogo de productos (leído de `A_productos`).
    * Al seleccionar un producto, muestra su imagen, descripción y las tallas disponibles.
    * La lista de tallas se genera dinámicamente buscando en `A_inventario` variantes que tengan `cantidad_stock > 0`.
    * Permite "Añadir al Carrito".

2.  **Carrito:**
    * Muestra los productos añadidos a una lista temporal de Python.
    * Calcula el subtotal y el total del pedido.
    * Permite quitar items del carrito (modificando la lista).
    * **Botón "Finalizar Compra":**
        * Valida que el cliente tenga al menos una dirección guardada.
        * Crea un nuevo documento en `A_ordenes` con el arreglo `items_comprados`.
        * Actualiza el stock en `A_inventario` usando **`$inc: -1`** por cada producto comprado.
        * Limpia el carrito.

3.  **Mi Cuenta:**
    * Permite al cliente actualizar su contraseña (validando la contraseña actual).
    * **Gestión de Direcciones (Arreglo):**
        * **(Req 6.5 - Bonus $push$)** Permite al cliente añadir nuevas direcciones a su arreglo `direcciones` usando **`$push`**.
        * **(Req 6.5 - Bonus $pull$)** Muestra sus direcciones guardadas en una tabla y permite eliminarlas usando **`$pull`**.

## Tecnologías Utilizadas

* **Base de Datos:** MongoDB
* **Lenguaje:** Python 3
* **Interfaz Gráfica (GUI):** `tkinter` (con `ttk` para widgets modernos)
* **Conector Python-MongoDB:** `pymongo`
* **Manejo de Imágenes:** `Pillow` (PIL)
* **Descarga de Imágenes:** `requests`

## Instalación y Ejecución

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/emrog24/Sistema-de-E-commerce-Adidas-Proyecto-Escolar-
    cd [NOMBRE_DE_TU_CARPETA]
    ```

2.  **Instalar Dependencias (Comandos):**
    Asegúrate de tener Python 3 instalado. La aplicación requiere las siguientes bibliotecas. Ejecuta estos comandos en tu terminal:
    ```bash
    pip install pymongo
    ```
    ```bash
    pip install pillow
    ```
    ```bash
    pip install requests
    ```
    O en una sola línea:
    ```bash
    pip install pymongo pillow requests
    ```

3.  **Configurar la Base de Datos:**
    * Asegúrate de que tu servicio de MongoDB esté corriendo (usualmente en `mongodb://localhost:27017/`).
    * **Crear y poblar la base de datos:** Abre MongoDB Compass o `mongosh`, carga el archivo `Adidas_Colecciones.mongodb.js` y ejecútalo. Esto creará la base de datos `Adidas` y las 4 colecciones (`A_productos`, `A_inventario`, `A_usuarios`, `A_ordenes`) con todos los datos de prueba necesarios.

4.  **Ejecutar la Aplicación:**
    Una vez que la base de datos esté lista, ejecuta el archivo principal:
    ```bash
    python main.py
    ```

5.  **Credenciales de Prueba:**
    * **Panel de Administrador:**
        * **Usuario:** `jesusedr@adidas.mx`
        * **Contraseña:** `DIAZ1234`
    * **Panel de Cliente:**
        * Puedes registrar un nuevo cliente usando el botón **"Regístrate aquí"** en la pantalla de login.
