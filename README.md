# Galería en MongoDB con Django - Python

Aplicación Web Galería utilizando base de datos NoSQL - MongoDB con **Python - Django**

## **Nota**

Para utilizar la aplicación Web, debe tener intalado [**MongoDB**](https://www.mongodb.com/try/download/community), [**Python**](https://www.mongodb.com/try/download/community).

## **Instalación**

### **Paso 1**

**Forma 1:** Dar clic en **Code**, luego **Download Zip** y descomprimir el archivo en tu ordenador.

**Forma 2:** Abrir una terminal en tu ordenador y ejecutar el siguiente comando:

    git clone https://github.com/HenryGP14/GaleriaMongoDB.git

### **Paso 2**

Instalar todos los paquedes que se encuentran en el archivo **requirements.txt**, lo puedes hacer uno por uno o ejecutar el siguiente comando en tu consola:

    pip install -r requirements.txt

### **Paso 3**

Instalar el motor de base de datos [**MongoDB**](https://www.mongodb.com/try/download/community)

### **Paso 4**

Configurar el archivo **.env**, este archivo es aquel que contendrá todas las configuraciones necesarias para que el aplicativo funcione.

-   **Primero:** Cambiar el nombre del archivo "**.env.example**"a "**.env**"

-   **Segundo:** Generar una Secret Key.

    **Forma 1:** Generar la Secret Key por python consola [**Click aquí para más información.**](https://pypi.org/project/secret-key-generator/)

    **Forma 2:** Generar la Secret Key por Online visitar la página de [**Djecrety.**](https://djecrety.ir/)

-   **Tercero:** Configurar el acceso del motor de base de datos de MongoDB, para más información [**click aquí.**](https://www.mongodb.com/compatibility/mongodb-and-django)

-   **Cuarto:** Colocar la Secret Key en <font color=red>**SECRET_KEY**</font> en el archivo **.env**

### **Paso 5**

Construir la base de datos, ejecutando el siguiete comando en tu consola:

    python manage.py migrate

### **Paso 6**

Ejecutar la aplicación con el siguiete comando en consola:

    python manage.py runserver

# **Errores**

Si con anterioridad has trabajado con **Django** y conectado a motores de base de datos relacionales como: **PostgreSQL**, **MySQL**, **etc**, vas a precentar un error al instalar el paquede **djongo** (es el controlador para comunicarme con el motor de base de datos **MongoDB**), y debes desinstalar el siguiete paquete:

    pip uninstall sqlparse

---

**Nota:** Si aun tienes problemas con la instalación de **djongo** puedes dar [**click aquí**](https://www.mongodb.com/compatibility/mongodb-and-django).

---
