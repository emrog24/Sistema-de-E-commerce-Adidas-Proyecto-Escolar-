import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from PIL import Image, ImageTk 
import requests
from io import BytesIO
from datetime import datetime
from bson.objectid import ObjectId 

print("--- Iniciando main.py ---")

#  CONEXIÓN GLOBAL A MONGODB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Adidas"]
    col_usuarios = db["A_usuarios"]
    col_productos = db["A_productos"]
    col_inventario = db["A_inventario"]
    col_ordenes = db["A_ordenes"]
    print("Conexión a todas las colecciones (usuarios, productos, inventario, ordenes) exitosa.")
except Exception as e:
    print(f"ERROR AL CONECTAR A LA BASE DE DATOS: {e}")
    exit()

# FUNCIÓN DE NAVEGACIÓN 
def show_frame(frame_deseado):
    """
    Esta función toma un frame (una página) y la pone al frente.
    """
    login_frame.pack_forget()
    register_frame.pack_forget()
    
    frame_deseado.pack(fill="both", expand=True)
    print("Mostrando un nuevo frame...")

#  LÓGICA DE BACKEND (Verificar y Registrar) 

def verificar_login():
    """
    Verifica el email y contraseña contra la BBDD.
    """
    email = entry_email_login.get()
    password = entry_password_login.get()

    if not email or not password:
        messagebox.showwarning("Error", "Por favor, ingresa email y contraseña.")
        return

    try:
        usuario = col_usuarios.find_one({
            "email": email,
            "password": password
        })

        if usuario:
            # ¡Usuario encontrado!
            if usuario.get("estado") == "inactivo":
                messagebox.showerror("Cuenta Inactiva", "Esta cuenta ha sido desactivada por un administrador.")
                return #Si no esta activa, no deja entrar

            rol = usuario.get("rol", "cliente")
            nombre = usuario.get("nombre_completo", "Usuario")
            
            messagebox.showinfo("¡Éxito!", f"¡Bienvenido, {nombre}!")
            
            # Ocultamos la ventana principal
            root.withdraw() 
            
            if rol == "admin":
                iniciar_panel_admin(nombre) 
            else:
                iniciar_panel_cliente(nombre)
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos.")
            
    except Exception as e:
        messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos: {e}")


def registrar_usuario():
    """
    Toma los datos de los campos de registro, valida y registra al usuario.
    """
    nombre = entries_reg["Nombre"].get()
    email = entries_reg["Email"].get()
    password = entries_reg["Pass"].get()
    password_confirm = entries_reg["PassConfirm"].get()
    fecha_nac_str = entries_reg["FechaNac"].get()
    
    if not all([nombre, email, password, password_confirm, fecha_nac_str]):
        messagebox.showwarning("Campos vacíos", "Por favor, rellena todos los campos.")
        return

    if password != password_confirm:
        messagebox.showwarning("Contraseñas no coinciden", "Las contraseñas no son iguales.")
        return
        
    try:
        fecha_nac_obj = datetime.strptime(fecha_nac_str, '%Y-%m-%d')
    except ValueError:
        messagebox.showwarning("Formato incorrecto", "Usa el formato AAAA-MM-DD para la fecha.")
        return

    try:
        if col_usuarios.find_one({"email": email}):
            messagebox.showwarning("Email en uso", "Ese correo electrónico ya está registrado.")
            return
    except Exception as e:
        messagebox.showerror("Error de DB", f"No se pudo consultar la base de datos: {e}")
        return

    nuevo_cliente = {
        "nombre_completo": nombre,
        "email": email,
        "password": password, 
        "rol": "cliente",
        "fecha_nacimiento": fecha_nac_obj,
        "direcciones": [],
        "estado": "activo"
    }

    try:
        col_usuarios.insert_one(nuevo_cliente)
        messagebox.showinfo("¡Éxito!", "¡Usuario registrado! Ahora puedes iniciar sesión.")
        
        for entry in entries_reg.values():
            entry.delete(0, 'end')
        
        show_frame(login_frame)
        
    except Exception as e:
        messagebox.showerror("Error de Registro", f"No se pudo registrar el usuario: {e}")

#  CREACIÓN DE LA VENTANA PRINCIPAL 
root = tk.Tk()
root.title("Adidas - App")

# ESTILO PARA BOTONES TIPO "LINK"
style = ttk.Style()
style.configure("Link.TButton", 
                foreground="blue", 
                borderwidth=0,
                font=('Arial', 10, 'underline'))
style.map("Link.TButton", foreground=[('active', 'red')])

# DEFINICIÓN DE LAS "PÁGINAS" (Frames) 

# PÁGINA DE LOGIN 
login_frame = ttk.Frame(root, padding="20 20 20 20")

try:
    url_logo = "https://logodownload.org/wp-content/uploads/2014/07/adidas-logo-0.png"
    response = requests.get(url_logo)
    img_data = BytesIO(response.content)
    img_pil = Image.open(img_data)
    img_pil = img_pil.resize((150, 100), Image.LANCZOS) 
    logo_tk = ImageTk.PhotoImage(img_pil) # Guardamos el logo principal aquí
    panel_logo = ttk.Label(login_frame, image=logo_tk)
    panel_logo.pack(pady=10) 
except Exception as e:
    print(f"No se pudo cargar el logo desde la URL: {e}")
    logo_tk = None 
    panel_logo = ttk.Label(login_frame, text="[Logo de Adidas]")
    panel_logo.pack(pady=10)

frame_form_login = ttk.Frame(login_frame)
frame_form_login.pack(padx=30, pady=20) 

label_email_login = ttk.Label(frame_form_login, text="Email:")
label_email_login.pack(anchor="w") 
entry_email_login = ttk.Entry(frame_form_login, font=("Arial", 12), width=30)
entry_email_login.pack(pady=5) 

label_pass_login = ttk.Label(frame_form_login, text="Contraseña:")
label_pass_login.pack(anchor="w")
entry_password_login = ttk.Entry(frame_form_login, show="*", font=("Arial", 12), width=30)
entry_password_login.pack(pady=5)

btn_login = ttk.Button(login_frame, text="Iniciar Sesión", command=verificar_login)
btn_login.pack(pady=20, ipadx=20, ipady=5) 

separator = ttk.Separator(login_frame, orient='horizontal')
separator.pack(padx=30, ipadx=100) 

label_registro = ttk.Label(login_frame, text="¿No tienes una cuenta?")
label_registro.pack(pady=(15, 5))

btn_ir_a_registro = ttk.Button(login_frame, 
                             text="Regístrate aquí", 
                             command=lambda: show_frame(register_frame), 
                             style="Link.TButton", 
                             cursor="hand2") 
btn_ir_a_registro.pack()


# PÁGINA DE REGISTRO 
register_frame = ttk.Frame(root, padding="20 20 20 20")

label_titulo_reg = ttk.Label(register_frame, text="Crear Cuenta de Cliente", font=("Arial", 16, "bold"))
label_titulo_reg.pack(pady=20)

frame_form_reg = ttk.Frame(register_frame, padding="10 0 10 0")
frame_form_reg.pack()

campos_reg = ["Nombre", "Email", "Pass", "PassConfirm", "FechaNac"]
labels_reg = ["Nombre Completo:", "Email:", "Contraseña:", "Confirmar Contraseña:", "Fecha Nacimiento (AAAA-MM-DD):"]
entries_reg = {} 

for i, campo in enumerate(campos_reg):
    label = ttk.Label(frame_form_reg, text=labels_reg[i])
    label.grid(row=i, column=0, sticky="w", pady=5, padx=5)
    
    if "Pass" in campo:
        entry = ttk.Entry(frame_form_reg, show="*", font=("Arial", 11), width=35)
    else:
        entry = ttk.Entry(frame_form_reg, font=("Arial", 11), width=35)
    
    entry.grid(row=i, column=1, pady=5, padx=5)
    entries_reg[campo] = entry 

btn_registrar = ttk.Button(register_frame, text="Registrarme", command=registrar_usuario)
btn_registrar.pack(pady=20, ipadx=20, ipady=5)

btn_ir_a_login = ttk.Button(register_frame, 
                          text="Ya tengo cuenta (Volver a Login)", 
                          command=lambda: show_frame(login_frame),
                          style="Link.TButton", 
                          cursor="hand2")
btn_ir_a_login.pack()

# PÁGINA DEL PANEL DE ADMINISTRADOR
def iniciar_panel_admin(nombre_admin):
    """
    Crea y muestra la ventana principal del panel de administrador.
    """
    print(f"Iniciando panel de admin para {nombre_admin}...")
    
    admin_window = tk.Toplevel(root)
    admin_window.title(f"Panel de Administrador - Bienvenido {nombre_admin}")
    admin_window.geometry("1000x700")

    logo_tk_admin = None
    mapa_productos = {} 

    # FUNCIÓN DE CERRAR SESIÓN 
    def cerrar_sesion():
        print("Cerrando sesión de admin...")
        admin_window.destroy() 
        root.deiconify()       
    
    #Frame superior para bienvenida y botón 
    frame_superior = ttk.Frame(admin_window)
    frame_superior.pack(fill="x", padx=10, pady=5)

    try:
        url_logo = "https://logodownload.org/wp-content/uploads/2014/07/adidas-logo-0.png"
        response = requests.get(url_logo)
        img_data = BytesIO(response.content)
        img_pil = Image.open(img_data)
        img_pil = img_pil.resize((60, 40), Image.LANCZOS) 
        logo_tk_admin = ImageTk.PhotoImage(img_pil)
        panel_logo_admin = ttk.Label(frame_superior, image=logo_tk_admin)
        panel_logo_admin.image = logo_tk_admin 
        panel_logo_admin.pack(side="left", padx=10) 
    except Exception as e:
        print(f"No se pudo cargar el logo de admin: {e}")

    label_bienvenida = ttk.Label(frame_superior, text=f"Usuario: {nombre_admin}", font=("Arial", 12))
    label_bienvenida.pack(side="left", padx=10) 

    btn_cerrar_sesion = ttk.Button(frame_superior, text="Cerrar Sesión", command=cerrar_sesion)
    btn_cerrar_sesion.pack(side="right", padx=10)

    notebook = ttk.Notebook(admin_window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # PESTAÑA 1: GESTIONAR PRODUCTOS 
    productos_tab = ttk.Frame(notebook, padding="10")
    notebook.add(productos_tab, text="Gestionar Productos")
    producto_id_actual = tk.StringVar(value="")
    
    def cargar_productos():
        for item in tabla_productos.get_children():
            tabla_productos.delete(item)
        mapa_productos.clear()
        lista_nombres_productos = []
        try:
            for producto in col_productos.find():
                mapa_productos[producto.get("nombre_producto")] = str(producto.get("_id"))
                lista_nombres_productos.append(producto.get("nombre_producto"))
                tabla_productos.insert("", "end", values=(
                    str(producto.get("_id", "")), 
                    producto.get("nombre_producto", "N/A"),
                    producto.get("categoria", "N/A"),
                    producto.get("precio_mxn", 0.0),
                    producto.get("tags_busqueda", [])
                ))
            if 'combo_producto_inv' in locals() or 'combo_producto_inv' in globals():
                combo_producto_inv['values'] = sorted(lista_nombres_productos)
            print("Productos cargados en la tabla y mapa actualizado.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar los productos: {e}", parent=admin_window)
    def eliminar_producto():
        selected_item = tabla_productos.focus()
        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona un producto.", parent=admin_window)
            return
        confirmar = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que quieres eliminar este producto?")
        if confirmar:
            try:
                item_data = tabla_productos.item(selected_item)
                producto_id_str = item_data['values'][0]
                col_productos.delete_one({"_id": ObjectId(producto_id_str)})
                messagebox.showinfo("Éxito", "Producto eliminado.", parent=admin_window)
                cargar_productos()
                limpiar_formulario() 
            except Exception as e:
                messagebox.showerror("Error al Eliminar", f"No se pudo eliminar: {e}", parent=admin_window)
    def seleccionar_producto(event):
        selected_item = tabla_productos.focus()
        if not selected_item:
            return
        item_data = tabla_productos.item(selected_item)
        producto_id_str = item_data['values'][0]
        try:
            producto = col_productos.find_one({"_id": ObjectId(producto_id_str)})
            if not producto:
                messagebox.showerror("Error", "No se encontró el producto.", parent=admin_window)
                return
            limpiar_formulario(silencioso=True)
            producto_id_actual.set(producto_id_str)
            entry_nombre.insert(0, producto.get("nombre_producto", ""))
            entry_precio.insert(0, producto.get("precio_mxn", 0.0))
            entry_categoria.insert(0, producto.get("categoria", ""))
            entry_imagen_url.insert(0, producto.get("url_imagen_principal", ""))
            entry_desc.insert("1.0", producto.get("descripcion", ""))
            tags = ", ".join(producto.get("tags_busqueda", []))
            entry_tags.insert(0, tags)
            url_imagen = producto.get("url_imagen_principal", "")
            if url_imagen:
                try:
                    response = requests.get(url_imagen)
                    img_data = BytesIO(response.content)
                    img_pil = Image.open(img_data)
                    img_pil = img_pil.resize((150, 100), Image.LANCZOS)
                    img_tk_producto = ImageTk.PhotoImage(img_pil)
                    panel_imagen_producto.configure(image=img_tk_producto)
                    panel_imagen_producto.image = img_tk_producto 
                except Exception as e:
                    print(f"Error al cargar imagen del producto: {e}")
                    panel_imagen_producto.configure(image=logo_tk_admin)
                    panel_imagen_producto.image = logo_tk_admin
            print(f"Mostrando datos para editar: {producto_id_str}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el producto: {e}", parent=admin_window)
    def limpiar_formulario(silencioso=False):
        producto_id_actual.set("") 
        entry_nombre.delete(0, "end")
        entry_precio.delete(0, "end")
        entry_categoria.delete(0, "end")
        entry_imagen_url.delete(0, "end")
        entry_tags.delete(0, "end")
        entry_desc.delete("1.0", "end")
        entry_nuevo_tag.delete(0, "end")
        panel_imagen_producto.configure(image=logo_tk_admin)
        panel_imagen_producto.image = logo_tk_admin
        if not silencioso:
            print("Formulario limpiado.")
    def crear_producto():
        try:
            if producto_id_actual.get():
                messagebox.showwarning("Modo Edición", "Ya hay un producto cargado. Limpia el formulario.", parent=admin_window)
                return
            nuevo_producto = {
                "nombre_producto": entry_nombre.get(),
                "descripcion": entry_desc.get("1.0", "end-1c"), 
                "precio_mxn": float(entry_precio.get()),
                "categoria": entry_categoria.get(),
                "url_imagen_principal": entry_imagen_url.get(),
                "tags_busqueda": [tag.strip() for tag in entry_tags.get().split(",")] 
            }
            col_productos.insert_one(nuevo_producto)
            messagebox.showinfo("Éxito", "Producto creado.", parent=admin_window)
            cargar_productos()
            limpiar_formulario()
        except ValueError:
            messagebox.showerror("Error de Tipo", "El precio debe ser un número.", parent=admin_window)
        except Exception as e:
            messagebox.showerror("Error al Crear", f"No se pudo crear: {e}", parent=admin_window)
    def actualizar_producto():
        try:
            producto_id = producto_id_actual.get()
            if not producto_id:
                messagebox.showwarning("Modo Creación", "No hay ningún producto seleccionado.", parent=admin_window)
                return
            datos_actualizados = {
                "nombre_producto": entry_nombre.get(),
                "descripcion": entry_desc.get("1.0", "end-1c"),
                "precio_mxn": float(entry_precio.get()),
                "categoria": entry_categoria.get(),
                "url_imagen_principal": entry_imagen_url.get(),
                "tags_busqueda": [tag.strip() for tag in entry_tags.get().split(",")]
            }
            col_productos.update_one({"_id": ObjectId(producto_id)}, {"$set": datos_actualizados})
            messagebox.showinfo("Éxito", "Producto actualizado.", parent=admin_window)
            cargar_productos()
            limpiar_formulario()
        except ValueError:
            messagebox.showerror("Error de Tipo", "El precio debe ser un número.", parent=admin_window)
        except Exception as e:
            messagebox.showerror("Error al Actualizar", f"No se pudo actualizar: {e}", parent=admin_window)
    def anadir_tag_push():
        producto_id = producto_id_actual.get()
        nuevo_tag = entry_nuevo_tag.get()
        if not producto_id:
            messagebox.showwarning("Sin producto", "Primero selecciona un producto.", parent=admin_window)
            return
        if not nuevo_tag:
            messagebox.showwarning("Sin tag", "Escribe el tag que deseas añadir.", parent=admin_window)
            return
        try:
            col_productos.update_one(
                {"_id": ObjectId(producto_id)},
                {"$push": {"tags_busqueda": nuevo_tag.strip()}}
            )
            messagebox.showinfo("Éxito", f"Tag '{nuevo_tag}' añadido.", parent=admin_window)
            cargar_productos()
            limpiar_formulario() 
        except Exception as e:
            messagebox.showerror("Error de $push", f"No se pudo añadir el tag: {e}", parent=admin_window)
    def quitar_tag_pop():
        producto_id = producto_id_actual.get()
        if not producto_id:
            messagebox.showwarning("Sin producto", "Primero selecciona un producto.", parent=admin_window)
            return
        confirmar = messagebox.askyesno("Confirmar $pop", "¿Seguro que quieres eliminar el ÚLTIMO tag?")
        if not confirmar:
            return
        try:
            col_productos.update_one({"_id": ObjectId(producto_id)}, {"$pop": {"tags_busqueda": 1}})
            messagebox.showinfo("Éxito", "Último tag eliminado.", parent=admin_window)
            cargar_productos()
            limpiar_formulario() 
        except Exception as e:
            messagebox.showerror("Error de $pop", f"No se pudo quitar el tag: {e}", parent=admin_window)
    paned_window = ttk.PanedWindow(productos_tab, orient="horizontal")
    paned_window.pack(fill="both", expand=True)
    frame_lista = ttk.Frame(paned_window)
    paned_window.add(frame_lista, weight=2) 
    frame_formulario = ttk.Frame(paned_window)
    paned_window.add(frame_formulario, weight=1) 
    label_titulo_lista = ttk.Label(frame_lista, text="Lista de Productos", font=("Arial", 14, "bold"))
    label_titulo_lista.pack(pady=10)
    columnas = ("id", "nombre", "categoria", "precio", "tags")
    tabla_productos = ttk.Treeview(frame_lista, columns=columnas, show="headings")
    tabla_productos.heading("id", text="ID (MongoDB)")
    tabla_productos.heading("nombre", text="Nombre Producto")
    tabla_productos.heading("categoria", text="Categoría")
    tabla_productos.heading("precio", text="Precio (MXN)")
    tabla_productos.heading("tags", text="Tags")
    tabla_productos.column("id", width=150)
    tabla_productos.column("nombre", width=250)
    tabla_productos.column("categoria", width=100)
    tabla_productos.column("precio", width=80)
    tabla_productos.column("tags", width=200)
    tabla_productos.pack(fill="both", expand=True)
    tabla_productos.bind("<<TreeviewSelect>>", seleccionar_producto)
    frame_botones_lista = ttk.Frame(frame_lista)
    frame_botones_lista.pack(pady=10)
    btn_recargar = ttk.Button(frame_botones_lista, text="Recargar Lista", command=cargar_productos)
    btn_recargar.pack(side="left", padx=5)
    btn_eliminar = ttk.Button(frame_botones_lista, text="Eliminar Seleccionado", command=eliminar_producto)
    btn_eliminar.pack(side="left", padx=5)
    label_titulo_form = ttk.Label(frame_formulario, text="Crear / Editar Producto", font=("Arial", 14, "bold"))
    label_titulo_form.pack(pady=10)
    panel_imagen_producto = ttk.Label(frame_formulario, image=logo_tk_admin)
    panel_imagen_producto.pack(pady=10)
    panel_imagen_producto.image = logo_tk_admin 
    form_grid = ttk.Frame(frame_formulario)
    form_grid.pack(fill="x", padx=10)
    ttk.Label(form_grid, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
    entry_nombre = ttk.Entry(form_grid, width=40)
    entry_nombre.grid(row=0, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid, text="Descripción:").grid(row=1, column=0, sticky="w", pady=5)
    entry_desc = tk.Text(form_grid, height=5, width=40)
    entry_desc.grid(row=1, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid, text="Precio (MXN):").grid(row=2, column=0, sticky="w", pady=5)
    entry_precio = ttk.Entry(form_grid, width=40)
    entry_precio.grid(row=2, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid, text="Categoría:").grid(row=3, column=0, sticky="w", pady=5)
    entry_categoria = ttk.Entry(form_grid, width=40)
    entry_categoria.grid(row=3, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid, text="URL Imagen:").grid(row=4, column=0, sticky="w", pady=5)
    entry_imagen_url = ttk.Entry(form_grid, width=40)
    entry_imagen_url.grid(row=4, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid, text="Tags (separar con ,):").grid(row=5, column=0, sticky="w", pady=5)
    entry_tags = ttk.Entry(form_grid, width=40)
    entry_tags.grid(row=5, column=1, sticky="ew", pady=5)
    form_grid.grid_columnconfigure(1, weight=1)
    frame_botones_form = ttk.Frame(frame_formulario)
    frame_botones_form.pack(pady=10)
    btn_crear = ttk.Button(frame_botones_form, text="Crear Producto Nuevo", command=crear_producto)
    btn_crear.pack(side="left", padx=5)
    btn_actualizar = ttk.Button(frame_botones_form, text="Guardar Cambios (Editar)", command=actualizar_producto)
    btn_actualizar.pack(side="left", padx=5)
    btn_limpiar = ttk.Button(frame_botones_form, text="Limpiar Formulario", command=limpiar_formulario)
    btn_limpiar.pack(side="left", padx=5)
    ttk.Separator(frame_formulario, orient="horizontal").pack(fill="x", padx=10, pady=15)
    label_titulo_pushpop = ttk.Label(frame_formulario, text="Gestión de Tags ($push/$pop)", font=("Arial", 12, "bold"))
    label_titulo_pushpop.pack(pady=5)
    frame_pushpop = ttk.Frame(frame_formulario)
    frame_pushpop.pack(fill="x", padx=10)
    ttk.Label(frame_pushpop, text="Nuevo Tag:").grid(row=0, column=0, sticky="w", padx=5)
    entry_nuevo_tag = ttk.Entry(frame_pushpop, width=20)
    entry_nuevo_tag.grid(row=0, column=1, sticky="ew", padx=5)
    btn_push = ttk.Button(frame_pushpop, text="Añadir Tag ($push)", command=anadir_tag_push)
    btn_push.grid(row=0, column=2, padx=5)
    btn_pop = ttk.Button(frame_pushpop, text="Quitar Último ($pop)", command=quitar_tag_pop)
    btn_pop.grid(row=1, column=0, columnspan=3, pady=10)
    frame_pushpop.grid_columnconfigure(1, weight=1)
    
    # PESTAÑA 2: GESTIONAR INVENTARIO 
    inventario_tab = ttk.Frame(notebook, padding="10")
    notebook.add(inventario_tab, text="Gestionar Inventario")
    inventario_id_actual = tk.StringVar(value="")
    
    def cargar_inventario():
        for item in tabla_inventario.get_children():
            tabla_inventario.delete(item)
        try:
            pipeline = [
                {"$lookup": {"from": "A_productos", "localField": "producto_id", "foreignField": "_id", "as": "producto_info"}},
                {"$unwind": {"path": "$producto_info", "preserveNullAndEmptyArrays": True}}
            ]
            for item in col_inventario.aggregate(pipeline):
                tabla_inventario.insert("", "end", values=(
                    str(item.get("_id", "")),
                    item.get("producto_info", {}).get("nombre_producto", "N/A"),
                    item.get("sku", "N/A"),
                    item.get("talla_us", "N/A"),
                    item.get("color", "N/A"),
                    item.get("cantidad_stock", 0)
                ))
            print("Inventario cargado en la tabla.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudo cargar el inventario: {e}", parent=admin_window)
    def limpiar_formulario_inv(silencioso=False):
        inventario_id_actual.set("")
        combo_producto_inv.set("")
        entry_sku_inv.delete(0, "end")
        entry_talla_inv.delete(0, "end")
        entry_color_inv.delete(0, "end")
        entry_stock_inv.delete(0, "end")
        if not silencioso:
            print("Formulario de inventario limpiado.")
    def seleccionar_variante(event):
        selected_item = tabla_inventario.focus()
        if not selected_item:
            return
        item_data = tabla_inventario.item(selected_item)
        variante_id_str = item_data['values'][0]
        try:
            variante = col_inventario.find_one({"_id": ObjectId(variante_id_str)})
            if not variante:
                messagebox.showerror("Error", "No se encontró la variante.", parent=admin_window)
                return
            limpiar_formulario_inv(silencioso=True)
            inventario_id_actual.set(variante_id_str)
            producto_nombre = "N/A"
            for nombre, id_prod in mapa_productos.items():
                if id_prod == str(variante.get("producto_id")):
                    producto_nombre = nombre
                    break
            combo_producto_inv.set(producto_nombre)
            entry_sku_inv.insert(0, variante.get("sku", ""))
            entry_talla_inv.insert(0, variante.get("talla_us", ""))
            entry_color_inv.insert(0, variante.get("color", ""))
            entry_stock_inv.insert(0, variante.get("cantidad_stock", 0))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la variante: {e}", parent=admin_window)
    def crear_variante():
        try:
            if inventario_id_actual.get():
                messagebox.showwarning("Modo Edición", "Ya hay una variante cargada. Limpia el formulario.", parent=admin_window)
                return
            nombre_prod_sel = combo_producto_inv.get()
            if not nombre_prod_sel:
                messagebox.showwarning("Sin producto", "Debes seleccionar un producto.", parent=admin_window)
                return
            producto_id_obj = ObjectId(mapa_productos[nombre_prod_sel])
            nueva_variante = {
                "producto_id": producto_id_obj,
                "sku": entry_sku_inv.get(),
                "talla_us": entry_talla_inv.get(),
                "color": entry_color_inv.get(),
                "cantidad_stock": int(entry_stock_inv.get())
            }
            col_inventario.insert_one(nueva_variante)
            messagebox.showinfo("Éxito", "Nueva variante de inventario creada.", parent=admin_window)
            cargar_inventario()
            limpiar_formulario_inv()
        except ValueError:
            messagebox.showerror("Error de Tipo", "El stock debe ser un número entero (ej. 50)", parent=admin_window)
        except Exception as e:
            messagebox.showerror("Error al Crear", f"No se pudo crear la variante: {e}", parent=admin_window)
    def actualizar_variante():
        try:
            variante_id = inventario_id_actual.get()
            if not variante_id:
                messagebox.showwarning("Modo Creación", "No hay ninguna variante seleccionada.", parent=admin_window)
                return
            nombre_prod_sel = combo_producto_inv.get()
            if not nombre_prod_sel:
                messagebox.showwarning("Sin producto", "Debes seleccionar un producto.", parent=admin_window)
                return
            producto_id_obj = ObjectId(mapa_productos[nombre_prod_sel])
            datos_actualizados = {
                "producto_id": producto_id_obj,
                "sku": entry_sku_inv.get(),
                "talla_us": entry_talla_inv.get(),
                "color": entry_color_inv.get(),
                "cantidad_stock": int(entry_stock_inv.get())
            }
            col_inventario.update_one({"_id": ObjectId(variante_id)}, {"$set": datos_actualizados})
            messagebox.showinfo("Éxito", "Inventario actualizado.", parent=admin_window)
            cargar_inventario()
            limpiar_formulario_inv()
        except ValueError:
            messagebox.showerror("Error de Tipo", "El stock debe ser un número entero.", parent=admin_window)
        except Exception as e:
            messagebox.showerror("Error al Actualizar", f"No se pudo actualizar: {e}", parent=admin_window)
    def eliminar_variante():
        selected_item = tabla_inventario.focus()
        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona una variante para eliminar.", parent=admin_window)
            return
        confirmar = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que quieres eliminar esta variante de inventario?")
        if confirmar:
            try:
                item_data = tabla_inventario.item(selected_item)
                variante_id_str = item_data['values'][0]
                col_inventario.delete_one({"_id": ObjectId(variante_id_str)})
                messagebox.showinfo("Éxito", "Variante eliminada.", parent=admin_window)
                cargar_inventario()
                limpiar_formulario_inv()
            except Exception as e:
                messagebox.showerror("Error al Eliminar", f"No se pudo eliminar: {e}", parent=admin_window)
    paned_window_inv = ttk.PanedWindow(inventario_tab, orient="horizontal")
    paned_window_inv.pack(fill="both", expand=True)
    frame_lista_inv = ttk.Frame(paned_window_inv)
    paned_window_inv.add(frame_lista_inv, weight=2) 
    frame_formulario_inv = ttk.Frame(paned_window_inv)
    paned_window_inv.add(frame_formulario_inv, weight=1) 
    label_titulo_lista_inv = ttk.Label(frame_lista_inv, text="Inventario de Variantes (Stock)", font=("Arial", 14, "bold"))
    label_titulo_lista_inv.pack(pady=10)
    columnas_inv = ("id", "producto", "sku", "talla", "color", "stock")
    tabla_inventario = ttk.Treeview(frame_lista_inv, columns=columnas_inv, show="headings")
    tabla_inventario.heading("id", text="ID Variante")
    tabla_inventario.heading("producto", text="Producto")
    tabla_inventario.heading("sku", text="SKU")
    tabla_inventario.heading("talla", text="Talla")
    tabla_inventario.heading("color", text="Color")
    tabla_inventario.heading("stock", text="Stock")
    tabla_inventario.column("id", width=120)
    tabla_inventario.column("producto", width=200)
    tabla_inventario.column("sku", width=100)
    tabla_inventario.column("talla", width=50)
    tabla_inventario.column("color", width=150)
    tabla_inventario.column("stock", width=50)
    tabla_inventario.pack(fill="both", expand=True)
    tabla_inventario.bind("<<TreeviewSelect>>", seleccionar_variante)
    frame_botones_inv = ttk.Frame(frame_lista_inv)
    frame_botones_inv.pack(pady=10)
    btn_recargar_inv = ttk.Button(frame_botones_inv, text="Recargar Inventario", command=cargar_inventario)
    btn_recargar_inv.pack(side="left", padx=5)
    btn_eliminar_inv = ttk.Button(frame_botones_inv, text="Eliminar Variante", command=eliminar_variante)
    btn_eliminar_inv.pack(side="left", padx=5)
    label_titulo_form_inv = ttk.Label(frame_formulario_inv, text="Crear / Editar Variante", font=("Arial", 14, "bold"))
    label_titulo_form_inv.pack(pady=10)
    panel_imagen_inv = ttk.Label(frame_formulario_inv, image=logo_tk_admin)
    panel_imagen_inv.pack(pady=10)
    panel_imagen_inv.image = logo_tk_admin 
    form_grid_inv = ttk.Frame(frame_formulario_inv)
    form_grid_inv.pack(fill="x", padx=10)
    ttk.Label(form_grid_inv, text="Producto:").grid(row=0, column=0, sticky="w", pady=5)
    combo_producto_inv = ttk.Combobox(form_grid_inv, state="readonly")
    combo_producto_inv.grid(row=0, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid_inv, text="SKU:").grid(row=1, column=0, sticky="w", pady=5)
    entry_sku_inv = ttk.Entry(form_grid_inv)
    entry_sku_inv.grid(row=1, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid_inv, text="Talla (US):").grid(row=2, column=0, sticky="w", pady=5)
    entry_talla_inv = ttk.Entry(form_grid_inv)
    entry_talla_inv.grid(row=2, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid_inv, text="Color:").grid(row=3, column=0, sticky="w", pady=5)
    entry_color_inv = ttk.Entry(form_grid_inv)
    entry_color_inv.grid(row=3, column=1, sticky="ew", pady=5)
    ttk.Label(form_grid_inv, text="Cantidad Stock:").grid(row=4, column=0, sticky="w", pady=5)
    entry_stock_inv = ttk.Entry(form_grid_inv)
    entry_stock_inv.grid(row=4, column=1, sticky="ew", pady=5)
    form_grid_inv.grid_columnconfigure(1, weight=1)
    frame_botones_form_inv = ttk.Frame(frame_formulario_inv)
    frame_botones_form_inv.pack(pady=20)
    btn_crear_inv = ttk.Button(frame_botones_form_inv, text="Crear Variante", command=crear_variante)
    btn_crear_inv.pack(side="left", padx=5)
    btn_actualizar_inv = ttk.Button(frame_botones_form_inv, text="Guardar Cambios", command=actualizar_variante)
    btn_actualizar_inv.pack(side="left", padx=5)
    btn_limpiar_inv = ttk.Button(frame_botones_form_inv, text="Limpiar Formulario", command=limpiar_formulario_inv)
    btn_limpiar_inv.pack(side="left", padx=5)

    # PESTAÑA 3: VER USUARIOS
    usuarios_tab = ttk.Frame(notebook, padding="10")
    notebook.add(usuarios_tab, text="Ver Usuarios")

    def cargar_usuarios():
        for item in tabla_usuarios.get_children():
            tabla_usuarios.delete(item)
        try:
            for usuario in col_usuarios.find():
                tabla_usuarios.insert("", "end", values=(
                    str(usuario.get("_id", "")),
                    usuario.get("nombre_completo", "N/A"),
                    usuario.get("email", "N/A"),
                    usuario.get("rol", "N/A"),
                    usuario.get("estado", "N/A")
                ))
            print("Usuarios cargados en la tabla.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar los usuarios: {e}", parent=admin_window)
    def toggle_estado_usuario():
        selected_item = tabla_usuarios.focus()
        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona un usuario de la lista.", parent=admin_window)
            return
        try:
            item_data = tabla_usuarios.item(selected_item)
            usuario_id_str = item_data['values'][0]
            usuario_email = item_data['values'][2] 
            estado_actual = item_data['values'][4]
            admin_logueado = col_usuarios.find_one({"nombre_completo": nombre_admin})
            email_admin_logueado = admin_logueado.get("email") if admin_logueado else ""
            if usuario_email == email_admin_logueado:
                messagebox.showerror("Acción Inválida", "No puedes desactivarte a ti mismo.", parent=admin_window)
                return
            nuevo_estado = "inactivo" if estado_actual == "activo" else "activo"
            confirmar = messagebox.askyesno("Confirmar Acción", f"¿Estás seguro de que quieres cambiar el estado de '{usuario_email}' a '{nuevo_estado}'?")
            if confirmar:
                col_usuarios.update_one(
                    {"_id": ObjectId(usuario_id_str)},
                    {"$set": {"estado": nuevo_estado}}
                )
                messagebox.showinfo("Éxito", f"Usuario '{usuario_email}' ahora está '{nuevo_estado}'.", parent=admin_window)
                cargar_usuarios()
        except Exception as e:
            messagebox.showerror("Error al Actualizar", f"No se pudo cambiar el estado: {e}", parent=admin_window)
    frame_lista_usuarios = ttk.Frame(usuarios_tab)
    frame_lista_usuarios.pack(fill="both", expand=True, padx=10, pady=10)
    label_titulo_usuarios = ttk.Label(frame_lista_usuarios, text="Lista de Usuarios (Clientes y Admins)", font=("Arial", 14, "bold"))
    label_titulo_usuarios.pack(pady=10)
    panel_imagen_usr = ttk.Label(frame_lista_usuarios, image=logo_tk_admin)
    panel_imagen_usr.pack(pady=10)
    panel_imagen_usr.image = logo_tk_admin 
    frame_botones_usuarios = ttk.Frame(frame_lista_usuarios)
    frame_botones_usuarios.pack(pady=10)
    btn_recargar_usuarios = ttk.Button(frame_botones_usuarios, text="Recargar Lista", command=cargar_usuarios)
    btn_recargar_usuarios.pack(side="left", padx=5)
    btn_toggle_estado = ttk.Button(frame_botones_usuarios, text="Activar / Desactivar Usuario", command=toggle_estado_usuario)
    btn_toggle_estado.pack(side="left", padx=5)
    columnas_usr = ("id", "nombre", "email", "rol", "estado")
    tabla_usuarios = ttk.Treeview(frame_lista_usuarios, columns=columnas_usr, show="headings")
    tabla_usuarios.heading("id", text="ID Usuario")
    tabla_usuarios.heading("nombre", text="Nombre Completo")
    tabla_usuarios.heading("email", text="Email")
    tabla_usuarios.heading("rol", text="Rol")
    tabla_usuarios.heading("estado", text="Estado")
    tabla_usuarios.column("id", width=150)
    tabla_usuarios.column("nombre", width=250)
    tabla_usuarios.column("email", width=250)
    tabla_usuarios.column("rol", width=80)
    tabla_usuarios.column("estado", width=80)
    tabla_usuarios.pack(fill="both", expand=True)

    # PESTAÑA 4: VER ÓRDENES 
    ordenes_tab = ttk.Frame(notebook, padding="10")
    notebook.add(ordenes_tab, text="Ver Órdenes")
    
    # Lógica de la Pestaña Órdenes 
    def cargar_ordenes():
        for item in tabla_ordenes.get_children():
            tabla_ordenes.delete(item)
        try:
            # $lookup para buscar el email del usuario
            pipeline = [
                {
                    "$lookup": {
                        "from": "A_usuarios", 
                        "localField": "usuario_id",
                        "foreignField": "_id",
                        "as": "usuario_info"
                    }
                },
                {
                    "$unwind": {
                        "path": "$usuario_info",
                        "preserveNullAndEmptyArrays": True
                    }
                }
            ]
            for orden in col_ordenes.aggregate(pipeline):
                
                fecha = orden.get("fecha_pedido")
                # Verificamos si 'fecha' es un objeto datetime real
                if isinstance(fecha, datetime):
                    fecha_str = fecha.strftime("%Y-%m-%d %H:%M")
                else:
                    # Si no es fecha (es None, un string, o falta), mostramos N/A
                    fecha_str = "N/A (Fecha Inválida)" 
                items = orden.get("items_comprados", [])
                if len(items) == 1:
                    items_str = f"1 item ({items[0].get('nombre_producto')})"
                else:
                    items_str = f"{len(items)} items"

                tabla_ordenes.insert("", "end", values=(
                    str(orden.get("_id", "")),
                    fecha_str, 
                    orden.get("usuario_info", {}).get("email", "N/A (Usuario Borrado)"),
                    orden.get("estado", "N/A"),
                    items_str, 
                    f"${orden.get('total_pedido', 0.0):,.2f}"
                ))
            print("Órdenes cargadas en la tabla.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar las órdenes: {e}", parent=admin_window)
    frame_lista_ordenes = ttk.Frame(ordenes_tab)
    frame_lista_ordenes.pack(fill="both", expand=True, padx=10, pady=10)
    label_titulo_ordenes = ttk.Label(frame_lista_ordenes, text="Historial de Órdenes", font=("Arial", 14, "bold"))
    label_titulo_ordenes.pack(pady=10)
    panel_imagen_ord = ttk.Label(frame_lista_ordenes, image=logo_tk_admin)
    panel_imagen_ord.pack(pady=10)
    panel_imagen_ord.image = logo_tk_admin 
    btn_recargar_ordenes = ttk.Button(frame_lista_ordenes, text="Recargar Lista de Órdenes", command=cargar_ordenes)
    btn_recargar_ordenes.pack(pady=10)
    columnas_ord = ("id", "fecha", "email_cliente", "estado", "items", "total")
    tabla_ordenes = ttk.Treeview(frame_lista_ordenes, columns=columnas_ord, show="headings")
    tabla_ordenes.heading("id", text="ID Orden")
    tabla_ordenes.heading("fecha", text="Fecha Pedido")
    tabla_ordenes.heading("email_cliente", text="Email Cliente")
    tabla_ordenes.heading("estado", text="Estado")
    tabla_ordenes.heading("items", text="Items")
    tabla_ordenes.heading("total", text="Total Pedido")
    tabla_ordenes.column("id", width=150)
    tabla_ordenes.column("fecha", width=130)
    tabla_ordenes.column("email_cliente", width=200)
    tabla_ordenes.column("estado", width=80)
    tabla_ordenes.column("items", width=200)
    tabla_ordenes.column("total", width=100)
    tabla_ordenes.pack(fill="both", expand=True)

    cargar_productos()
    cargar_inventario()
    cargar_usuarios()
    cargar_ordenes()
    
    admin_window.protocol("WM_DELETE_WINDOW", cerrar_sesion)

# PÁGINA DEL PANEL DE CLIENTE 
def iniciar_panel_cliente(nombre_cliente):
    """
    Crea y muestra la ventana principal del panel de cliente.
    """
    print(f"Iniciando panel de cliente para {nombre_cliente}...")
    
    cliente_window = tk.Toplevel(root)
    cliente_window.title(f"Tienda Adidas - Bienvenido {nombre_cliente}")
    cliente_window.geometry("1000x700")

    # Variables Globales del Cliente 
    carrito_actual = []
    producto_seleccionado_id = tk.StringVar(value="")
    variante_seleccionada_id = tk.StringVar(value="")
    img_tk_producto_cliente = None
    usuario_id_cliente = tk.StringVar(value="")

    # Función de cerrar sesión 
    def cerrar_sesion():
        print("Cerrando sesión de cliente...")
        cliente_window.destroy() 
        root.deiconify()         
    
    # Frame superior 
    frame_superior = ttk.Frame(cliente_window)
    frame_superior.pack(fill="x", padx=10, pady=5)
    
    label_logo_cliente = ttk.Label(frame_superior, image=logo_tk)
    label_logo_cliente.pack(side="left", padx=10)

    label_bienvenida = ttk.Label(frame_superior, text=f"Cliente: {nombre_cliente}", font=("Arial", 12))
    label_bienvenida.pack(side="left", padx=10)

    btn_cerrar_sesion = ttk.Button(frame_superior, text="Cerrar Sesión", command=cerrar_sesion)
    btn_cerrar_sesion.pack(side="right", padx=10)
    
    # Creación del Notebook (Pestañas)
    notebook = ttk.Notebook(cliente_window)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # PESTAÑA 1: VER PRODUCTOS 
    productos_tab_cli = ttk.Frame(notebook, padding="10")
    notebook.add(productos_tab_cli, text="Ver Productos (Tienda)")

    def cargar_productos_tienda():
        for item in tabla_productos_cli.get_children():
            tabla_productos_cli.delete(item)
        try:
            for producto in col_productos.find({}, {"nombre_producto": 1, "categoria": 1, "precio_mxn": 1}):
                tabla_productos_cli.insert("", "end", values=(
                    str(producto.get("_id", "")), 
                    producto.get("nombre_producto", "N/A"),
                    producto.get("categoria", "N/A"),
                    f"${producto.get('precio_mxn', 0.0):,.2f}"
                ))
            print("Tienda cargada con productos.")
        except Exception as e:
            messagebox.showerror("Error de Carga", f"No se pudieron cargar los productos: {e}", parent=cliente_window)
    def seleccionar_producto_tienda(event):
        nonlocal img_tk_producto_cliente
        selected_item = tabla_productos_cli.focus()
        if not selected_item:
            return
        item_data = tabla_productos_cli.item(selected_item)
        producto_id_str = item_data['values'][0]
        producto_seleccionado_id.set(producto_id_str)
        try:
            producto = col_productos.find_one({"_id": ObjectId(producto_id_str)})
            if not producto:
                return
            label_detalle_nombre.config(text=producto.get("nombre_producto"))
            label_detalle_precio.config(text=f"${producto.get('precio_mxn', 0.0):,.2f}")
            text_detalle_desc.config(state="normal")
            text_detalle_desc.delete("1.0", "end")
            text_detalle_desc.insert("1.0", producto.get("descripcion", ""))
            text_detalle_desc.config(state="disabled")
            url_imagen = producto.get("url_imagen_principal", "")
            if url_imagen:
                try:
                    response = requests.get(url_imagen)
                    img_data = BytesIO(response.content)
                    img_pil = Image.open(img_data)
                    img_pil = img_pil.resize((200, 150), Image.LANCZOS)
                    img_tk_producto_cliente = ImageTk.PhotoImage(img_pil)
                    panel_imagen_cli.configure(image=img_tk_producto_cliente)
                    panel_imagen_cli.image = img_tk_producto_cliente
                except Exception as e:
                    print(f"Error al cargar imagen del cliente: {e}")
                    panel_imagen_cli.configure(image=logo_tk)
                    panel_imagen_cli.image = logo_tk
            tallas_disponibles = []
            cursor_tallas = col_inventario.find({
                "producto_id": ObjectId(producto_id_str),
                "cantidad_stock": {"$gt": 0} 
            })
            for variante in cursor_tallas:
                tallas_disponibles.append(variante.get("talla_us"))
            if tallas_disponibles:
                combo_tallas_cli['values'] = sorted(tallas_disponibles)
                combo_tallas_cli.set("Selecciona una talla")
                btn_anadir_carrito.config(state="normal")
            else:
                combo_tallas_cli['values'] = []
                combo_tallas_cli.set("Sin stock")
                btn_anadir_carrito.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el producto: {e}", parent=cliente_window)
    def anadir_al_carrito():
        prod_id = producto_seleccionado_id.get()
        talla_sel = combo_tallas_cli.get()
        if not prod_id or talla_sel == "Selecciona una talla" or talla_sel == "Sin stock":
            messagebox.showwarning("Datos incompletos", "Por favor, selecciona un producto Y una talla.", parent=cliente_window)
            return
        try:
            variante = col_inventario.find_one({
                "producto_id": ObjectId(prod_id),
                "talla_us": talla_sel
            })
            producto = col_productos.find_one({"_id": ObjectId(prod_id)})
            if not variante or not producto:
                messagebox.showerror("Error", "No se encontró la variante seleccionada.", parent=cliente_window)
                return
            item_carrito = {
                "inventario_id": variante.get("_id"),
                "sku": variante.get("sku"),
                "nombre_producto": producto.get("nombre_producto"),
                "talla": talla_sel,
                "precio_unitario": producto.get("precio_mxn")
            }
            carrito_actual.append(item_carrito)
            print(f"Item añadido al carrito: {item_carrito['nombre_producto']}")
            messagebox.showinfo("¡Éxito!", f"{item_carrito['nombre_producto']} (Talla {talla_sel}) fue añadido a tu carrito.", parent=cliente_window)
            actualizar_tabla_carrito()
            notebook.select(carrito_tab)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo añadir al carrito: {e}", parent=cliente_window)
    paned_window_cli = ttk.PanedWindow(productos_tab_cli, orient="horizontal")
    paned_window_cli.pack(fill="both", expand=True)
    frame_lista_cli = ttk.Frame(paned_window_cli)
    paned_window_cli.add(frame_lista_cli, weight=1) 
    frame_detalle_cli = ttk.Frame(paned_window_cli)
    paned_window_cli.add(frame_detalle_cli, weight=1)
    label_tienda = ttk.Label(frame_lista_cli, text="Tienda de Productos", font=("Arial", 14, "bold"))
    label_tienda.pack(pady=10)
    columnas_cli = ("id", "nombre", "categoria", "precio")
    tabla_productos_cli = ttk.Treeview(frame_lista_cli, columns=columnas_cli, show="headings")
    tabla_productos_cli.heading("id", text="ID")
    tabla_productos_cli.heading("nombre", text="Nombre Producto")
    tabla_productos_cli.heading("categoria", text="Categoría")
    tabla_productos_cli.heading("precio", text="Precio")
    tabla_productos_cli.column("id", width=0, stretch=tk.NO)
    tabla_productos_cli.column("nombre", width=250)
    tabla_productos_cli.column("categoria", width=100)
    tabla_productos_cli.column("precio", width=80)
    tabla_productos_cli.pack(fill="both", expand=True, padx=5, pady=5)
    tabla_productos_cli.bind("<<TreeviewSelect>>", seleccionar_producto_tienda)
    btn_recargar_cli = ttk.Button(frame_lista_cli, text="Recargar Tienda", command=cargar_productos_tienda)
    btn_recargar_cli.pack(pady=10)
    label_detalle = ttk.Label(frame_detalle_cli, text="Detalles del Producto", font=("Arial", 14, "bold"))
    label_detalle.pack(pady=10)
    panel_imagen_cli = ttk.Label(frame_detalle_cli, image=logo_tk)
    panel_imagen_cli.pack(pady=10)
    panel_imagen_cli.image = logo_tk 
    label_detalle_nombre = ttk.Label(frame_detalle_cli, text="Selecciona un producto", font=("Arial", 12, "bold"))
    label_detalle_nombre.pack(pady=5)
    label_detalle_precio = ttk.Label(frame_detalle_cli, text="$0.00", font=("Arial", 12))
    label_detalle_precio.pack(pady=5)
    text_detalle_desc = tk.Text(frame_detalle_cli, height=8, width=50, wrap="word", state="disabled")
    text_detalle_desc.pack(pady=10, padx=10)
    frame_comprar = ttk.Frame(frame_detalle_cli)
    frame_comprar.pack(pady=10)
    ttk.Label(frame_comprar, text="Talla disponible:").pack(side="left", padx=5)
    combo_tallas_cli = ttk.Combobox(frame_comprar, state="readonly", width=15)
    combo_tallas_cli.pack(side="left", padx=5)
    btn_anadir_carrito = ttk.Button(frame_comprar, text="Añadir al Carrito", command=anadir_al_carrito, state="disabled")
    btn_anadir_carrito.pack(side="left", padx=10)

    # PESTAÑA 2: CARRITO DE COMPRAS
    carrito_tab = ttk.Frame(notebook, padding="10")
    notebook.add(carrito_tab, text="Carrito")
    
    def actualizar_tabla_carrito():
        for item in tabla_carrito.get_children():
            tabla_carrito.delete(item)
        total_carrito = 0.0
        for i, item in enumerate(carrito_actual):
            precio = item.get("precio_unitario", 0.0)
            tabla_carrito.insert("", "end", iid=i, values=( 
                item.get("nombre_producto"),
                item.get("talla"),
                f"${precio:,.2f}"
            ))
            total_carrito += precio
        label_total_carrito.config(text=f"Total: ${total_carrito:,.2f}")
        label_items_carrito.config(text=f"Items en el carrito: {len(carrito_actual)}")
    def quitar_del_carrito():
        selected_item = tabla_carrito.focus() 
        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Selecciona un item del carrito para quitar.", parent=cliente_window)
            return
        try:
            indice_a_borrar = int(selected_item)
            item_borrado = carrito_actual.pop(indice_a_borrar)
            print(f"Item quitado del carrito: {item_borrado['nombre_producto']}")
            actualizar_tabla_carrito() 
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo quitar el item: {e}", parent=cliente_window)
    def finalizar_compra():
        if not carrito_actual:
            messagebox.showwarning("Carrito vacío", "Tu carrito está vacío.", parent=cliente_window)
            return
        try:
            usuario = col_usuarios.find_one({"nombre_completo": nombre_cliente})
            if not usuario:
                messagebox.showerror("Error Fatal", "No se encontró tu usuario.", parent=cliente_window)
                return
            lista_direcciones = usuario.get("direcciones", [])
            if not lista_direcciones:
                messagebox.showwarning("¡Falta tu dirección!", 
                                       "No tienes una dirección de envío guardada. Por favor, ve a la pestaña 'Mi Cuenta' y añade una dirección para continuar.",
                                       parent=cliente_window)
                notebook.select(cuenta_tab)
                return 
            direccion_envio_final = lista_direcciones[0]
            confirmar = messagebox.askyesno("Confirmar Compra", f"Estás a punto de comprar {len(carrito_actual)} item(s) por un total de {label_total_carrito.cget('text')}. ¿Continuar?")
            if not confirmar:
                return
            total_pedido = 0.0
            items_para_db = []
            for item in carrito_actual:
                items_para_db.append({
                    "inventario_id": item["inventario_id"],
                    "sku": item["sku"],
                    "nombre_producto": item["nombre_producto"],
                    "cantidad": 1,
                    "precio_unitario": item["precio_unitario"]
                })
                total_pedido += item["precio_unitario"]
            nueva_orden = {
                "usuario_id": usuario.get("_id"),
                "fecha_pedido": datetime.now(),
                "estado": "Pagado",
                "items_comprados": items_para_db,
                "total_pedido": total_pedido,
                "direccion_envio": direccion_envio_final
            }
            col_ordenes.insert_one(nueva_orden)
            for item in carrito_actual:
                col_inventario.update_one(
                    {"_id": item["inventario_id"]},
                    {"$inc": {"cantidad_stock": -1}}
                )
            carrito_actual.clear()
            actualizar_tabla_carrito()
            cargar_productos_tienda()
            messagebox.showinfo("¡Gracias por tu compra!", "Tu pedido ha sido procesado exitosamente.")
            notebook.select(productos_tab_cli)
        except Exception as e:
            messagebox.showerror("Error en la Compra", f"No se pudo procesar tu orden: {e}", parent=cliente_window)
    label_titulo_carrito = ttk.Label(carrito_tab, text="Mi Carrito de Compras", font=("Arial", 16, "bold"))
    label_titulo_carrito.pack(pady=10)
    frame_central_carrito = ttk.Frame(carrito_tab)
    frame_central_carrito.pack(fill="both", expand=True, padx=10, pady=10)
    panel_imagen_carr = ttk.Label(frame_central_carrito, image=logo_tk)
    panel_imagen_carr.pack(pady=10)
    panel_imagen_carr.image = logo_tk
    columnas_carr = ("nombre", "talla", "precio")
    tabla_carrito = ttk.Treeview(frame_central_carrito, columns=columnas_carr, show="headings")
    tabla_carrito.heading("nombre", text="Producto")
    tabla_carrito.heading("talla", text="Talla")
    tabla_carrito.heading("precio", text="Precio")
    tabla_carrito.column("nombre", width=300)
    tabla_carrito.column("talla", width=100)
    tabla_carrito.column("precio", width=100)
    tabla_carrito.pack(fill="both", expand=True, pady=10)
    btn_quitar_item = ttk.Button(frame_central_carrito, text="Quitar Item Seleccionado", command=quitar_del_carrito)
    btn_quitar_item.pack(pady=5)
    frame_final_carrito = ttk.Frame(carrito_tab)
    frame_final_carrito.pack(fill="x", padx=10, pady=10)
    label_items_carrito = ttk.Label(frame_final_carrito, text="Items en el carrito: 0", font=("Arial", 12))
    label_items_carrito.pack(side="left", padx=10)
    label_total_carrito = ttk.Label(frame_final_carrito, text="Total: $0.00", font=("Arial", 14, "bold"))
    label_total_carrito.pack(side="left", padx=20)
    btn_finalizar = ttk.Button(frame_final_carrito, text="Finalizar Compra", command=finalizar_compra)
    btn_finalizar.pack(side="right", padx=10, ipadx=20, ipady=10)

    # PESTAÑA 3: MI CUENTA 
    cuenta_tab = ttk.Frame(notebook, padding="10")
    notebook.add(cuenta_tab, text="Mi Cuenta")

    # Lógica de la Pestaña Mi Cuenta 
    def cargar_datos_cuenta():
        #Carga los datos del cliente logueado en los formularios.
        try:
            usuario = col_usuarios.find_one({"nombre_completo": nombre_cliente})
            if not usuario:
                messagebox.showerror("Error", "No se pudieron cargar tus datos.", parent=cliente_window)
                return
            
            usuario_id_cliente.set(str(usuario.get("_id")))
            
            entry_cuenta_nombre.config(state="normal")
            entry_cuenta_email.config(state="normal")
            entry_cuenta_nombre.delete(0, "end")
            entry_cuenta_email.delete(0, "end")
            entry_cuenta_nombre.insert(0, usuario.get("nombre_completo", ""))
            entry_cuenta_email.insert(0, usuario.get("email", ""))
            entry_cuenta_nombre.config(state="disabled") 
            entry_cuenta_email.config(state="disabled")
            
            for item in tabla_direcciones.get_children():
                tabla_direcciones.delete(item)
                
            direcciones = usuario.get("direcciones", [])
            if not direcciones:
                tabla_direcciones.insert("", "end", values=("Aún no tienes direcciones", "", "", ""))
            else:
                for dir in direcciones:
                    tabla_direcciones.insert("", "end", values=(
                        dir.get("alias", "N/A"),
                        dir.get("calle", "N/A"),
                        dir.get("ciudad", "N/A"),
                        dir.get("codigo_postal", "N/A")
                    ))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar tus datos: {e}", parent=cliente_window)

    def cambiar_password():
        pass_actual = entry_pass_actual.get()
        pass_nueva = entry_pass_nueva.get()
        pass_confirmar = entry_pass_confirmar.get()
        
        if not pass_actual or not pass_nueva or not pass_confirmar:
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos de contraseña.", parent=cliente_window)
            return
        if pass_nueva != pass_confirmar:
            messagebox.showwarning("Error", "La nueva contraseña y la confirmación no coinciden.", parent=cliente_window)
            return
            
        try:
            usuario = col_usuarios.find_one({
                "_id": ObjectId(usuario_id_cliente.get()),
                "password": pass_actual
            })
            
            if not usuario:
                messagebox.showerror("Error", "Tu contraseña actual es incorrecta.", parent=cliente_window)
                return
                
            col_usuarios.update_one(
                {"_id": ObjectId(usuario_id_cliente.get())},
                {"$set": {"password": pass_nueva}}
            )
            
            messagebox.showinfo("Éxito", "¡Contraseña actualizada! Por seguridad, serás desconectado.")
            cerrar_sesion()
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la contraseña: {e}", parent=cliente_window)

    def anadir_direccion():
        alias = entry_dir_alias.get()
        calle = entry_dir_calle.get()
        ciudad = entry_dir_ciudad.get()
        cp = entry_dir_cp.get()
        
        if not alias or not calle or not ciudad or not cp:
            messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos de la dirección.", parent=cliente_window)
            return
            
        nueva_direccion = {
            "alias": alias,
            "calle": calle,
            "ciudad": ciudad,
            "codigo_postal": cp
        }
        
        try:
            # Usamos $push para añadir la dirección al arreglo
            col_usuarios.update_one(
                {"_id": ObjectId(usuario_id_cliente.get())},
                {"$push": {"direcciones": nueva_direccion}}
            )
            messagebox.showinfo("Éxito", "¡Dirección añadida!", parent=cliente_window)
            cargar_datos_cuenta() 
            
            entry_dir_alias.delete(0, "end")
            entry_dir_calle.delete(0, "end")
            entry_dir_ciudad.delete(0, "end")
            entry_dir_cp.delete(0, "end")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo añadir la dirección: {e}", parent=cliente_window)

    def quitar_direccion():
        selected_item = tabla_direcciones.focus()
        if not selected_item:
            messagebox.showwarning("Nada seleccionado", "Selecciona una dirección de la tabla para quitar.", parent=cliente_window)
            return
            
        item_data = tabla_direcciones.item(selected_item)
        alias_a_borrar = item_data['values'][0]
        
        if alias_a_borrar == "Aún no tienes direcciones":
            return
            
        confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que quieres borrar la dirección '{alias_a_borrar}'?")
        if not confirmar:
            return
            
        try:
            # Usamos $pull para quitar un sub-documento del arreglo
            col_usuarios.update_one(
                {"_id": ObjectId(usuario_id_cliente.get())},
                {"$pull": {"direcciones": {"alias": alias_a_borrar}}}
            )
            messagebox.showinfo("Éxito", "¡Dirección eliminada!", parent=cliente_window)
            cargar_datos_cuenta()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo quitar la dirección: {e}", parent=cliente_window)

    # Layout de la Pestaña Mi Cuenta 
    paned_window_cuenta = ttk.PanedWindow(cuenta_tab, orient="horizontal")
    paned_window_cuenta.pack(fill="both", expand=True)

    frame_datos_personales = ttk.Frame(paned_window_cuenta)
    paned_window_cuenta.add(frame_datos_personales, weight=1)
    
    label_datos = ttk.Label(frame_datos_personales, text="Mis Datos", font=("Arial", 14, "bold"))
    label_datos.pack(pady=10, padx=10)
    
    form_grid_cuenta = ttk.Frame(frame_datos_personales, padding="10")
    form_grid_cuenta.pack(fill="x")
    
    ttk.Label(form_grid_cuenta, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
    entry_cuenta_nombre = ttk.Entry(form_grid_cuenta, state="disabled", width=40)
    entry_cuenta_nombre.grid(row=0, column=1, sticky="ew", pady=5)
    
    ttk.Label(form_grid_cuenta, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
    entry_cuenta_email = ttk.Entry(form_grid_cuenta, state="disabled", width=40)
    entry_cuenta_email.grid(row=1, column=1, sticky="ew", pady=5)
    
    form_grid_cuenta.grid_columnconfigure(1, weight=1)
    
    label_pass = ttk.Label(frame_datos_personales, text="Cambiar Contraseña", font=("Arial", 14, "bold"))
    label_pass.pack(pady=(20, 10), padx=10)
    
    form_grid_pass = ttk.Frame(frame_datos_personales, padding="10")
    form_grid_pass.pack(fill="x")
    
    ttk.Label(form_grid_pass, text="Pass Actual:").grid(row=0, column=0, sticky="w", pady=5)
    entry_pass_actual = ttk.Entry(form_grid_pass, show="*", width=30)
    entry_pass_actual.grid(row=0, column=1, sticky="ew", pady=5)
    
    ttk.Label(form_grid_pass, text="Pass Nueva:").grid(row=1, column=0, sticky="w", pady=5)
    entry_pass_nueva = ttk.Entry(form_grid_pass, show="*", width=30)
    entry_pass_nueva.grid(row=1, column=1, sticky="ew", pady=5)
    
    ttk.Label(form_grid_pass, text="Confirmar Nueva:").grid(row=2, column=0, sticky="w", pady=5)
    entry_pass_confirmar = ttk.Entry(form_grid_pass, show="*", width=30)
    entry_pass_confirmar.grid(row=2, column=1, sticky="ew", pady=5)
    
    form_grid_pass.grid_columnconfigure(1, weight=1)
    
    btn_cambiar_pass = ttk.Button(frame_datos_personales, text="Actualizar Contraseña", command=cambiar_password)
    btn_cambiar_pass.pack(pady=10)

    # Frame Derecho (Direcciones)
    frame_direcciones = ttk.Frame(paned_window_cuenta)
    paned_window_cuenta.add(frame_direcciones, weight=2)
    
    label_dir = ttk.Label(frame_direcciones, text="Mis Direcciones de Envío", font=("Arial", 14, "bold"))
    label_dir.pack(pady=10, padx=10)

    form_grid_dir = ttk.Frame(frame_direcciones, padding="10")
    form_grid_dir.pack(fill="x")
    
    ttk.Label(form_grid_dir, text="Alias (ej. Casa):").grid(row=0, column=0, sticky="w", pady=5)
    entry_dir_alias = ttk.Entry(form_grid_dir)
    entry_dir_alias.grid(row=0, column=1, sticky="ew", pady=5, padx=5)
    
    ttk.Label(form_grid_dir, text="Calle y Número:").grid(row=1, column=0, sticky="w", pady=5)
    entry_dir_calle = ttk.Entry(form_grid_dir)
    entry_dir_calle.grid(row=1, column=1, sticky="ew", pady=5, padx=5)
    
    ttk.Label(form_grid_dir, text="Ciudad:").grid(row=2, column=0, sticky="w", pady=5)
    entry_dir_ciudad = ttk.Entry(form_grid_dir)
    entry_dir_ciudad.grid(row=2, column=1, sticky="ew", pady=5, padx=5)
    
    ttk.Label(form_grid_dir, text="Código Postal:").grid(row=3, column=0, sticky="w", pady=5)
    entry_dir_cp = ttk.Entry(form_grid_dir)
    entry_dir_cp.grid(row=3, column=1, sticky="ew", pady=5, padx=5)
    
    form_grid_dir.grid_columnconfigure(1, weight=1)
    
    btn_anadir_dir = ttk.Button(frame_direcciones, text="Añadir Nueva Dirección", command=anadir_direccion)
    btn_anadir_dir.pack(pady=10)
    
    ttk.Separator(frame_direcciones, orient="horizontal").pack(fill="x", padx=10, pady=15)
    
    label_dir_lista = ttk.Label(frame_direcciones, text="Direcciones Guardadas", font=("Arial", 12, "bold"))
    label_dir_lista.pack(pady=5, padx=10)
    
    columnas_dir = ("alias", "calle", "ciudad", "cp")
    tabla_direcciones = ttk.Treeview(frame_direcciones, columns=columnas_dir, show="headings", height=5)
    tabla_direcciones.heading("alias", text="Alias")
    tabla_direcciones.heading("calle", text="Calle")
    tabla_direcciones.heading("ciudad", text="Ciudad")
    tabla_direcciones.heading("cp", text="C.P.")
    tabla_direcciones.column("alias", width=100)
    tabla_direcciones.column("calle", width=200)
    tabla_direcciones.column("ciudad", width=100)
    tabla_direcciones.column("cp", width=50)
    tabla_direcciones.pack(fill="x", expand=True, padx=10)
    
    btn_quitar_dir = ttk.Button(frame_direcciones, text="Quitar Dirección Seleccionada ($pull)", command=quitar_direccion)
    btn_quitar_dir.pack(pady=10)

    cargar_productos_tienda()
    cargar_datos_cuenta()

    cliente_window.protocol("WM_DELETE_WINDOW", cerrar_sesion)

# INICIAR LA APLICACIÓN
login_frame.pack_forget()
register_frame.pack_forget()

show_frame(login_frame)

print("Lanzando la aplicación...")
root.mainloop()

print("--- Programa finalizado ---")