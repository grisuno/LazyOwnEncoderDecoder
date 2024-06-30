# LazyOwnEncoderDecoder

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

```sh
██╗      █████╗ ███████╗██╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔═══██╗██║    ██║████╗  ██║
██║     ███████║  ███╔╝  ╚████╔╝ ██║   ██║██║ █╗ ██║██╔██╗ ██║
██║     ██╔══██║ ███╔╝    ╚██╔╝  ██║   ██║██║███╗██║██║╚██╗██║
███████╗██║  ██║███████╗   ██║   ╚██████╔╝╚███╔███╔╝██║ ╚████║
╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
  ___          __     _ ____    
 | __|_ _  __ /  \ __| |__ /_ _ 
 | _|| ' \/ _| () / _` ||_ \ '_|
 |___|_||_\__|\__/\__,_|___/_|  
 |   \ ___ __ /  \ __| |__ /_ _ 
 | |) / -_) _| () / _` ||_ \ '_|
 |___/\___\__|\__/\__,_|___/_|  
                                
```
Visita una demo del proyecto corriendo en:

https://lazyownencoderdecoder.onrender.com/

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Y8Y2Z73AV)

LazyOwnEncoderDecoder es una aplicación web construida con Flask que permite codificar y decodificar mensajes utilizando un cifrado César combinado con una sustitución de claves y codificación Base64. La aplicación ofrece una interfaz de usuario moderna con una estética de terminal, y es responsive gracias a Bootstrap.

## Características

- Codificación y decodificación de mensajes.
- Cifrado César.
- Sustitución de claves.
- Codificación Base64.
- Interfaz de usuario responsive con Bootstrap.
- Validación de entrada y protección contra CSRF.

## Requisitos

- Python 3.x
- Flask
- Flask-WTF
- Flask-Bootstrap

## Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/grisuno/LazyOwnEncoderDecoder.git
   cd LazyOwnEncoderDecoder
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):

  ```bash   
  python -m venv venv
  source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
  ```
3. Instala las dependencias:
   ```bash   
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación Flask:

   ```bash   
   python app.py
   ```
5. Abre tu navegador y ve a http://127.0.0.1:5000.

6. Ingresa el mensaje que deseas codificar o decodificar, el valor de desplazamiento (shift value) y la clave de sustitución (substitution key).

7. Haz clic en "Encode" para codificar el mensaje o en "Decode" para decodificarlo. El resultado se mostrará en la página.

## Seguridad
La aplicación incluye las siguientes medidas de seguridad:

- Validación de entrada con WTForms.
- Protección contra CSRF con Flask-WTF.
- Uso de HTTPS recomendado en despliegue para proteger los datos en tránsito.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue los pasos a continuación para contribuir:

  Haz un fork del repositorio.
  Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
  Realiza tus cambios y haz commit (git commit -am 'Agrega nueva característica').
  Sube los cambios a tu rama (git push origin feature/nueva-caracteristica).
  Abre un Pull Request.
## Licencia
Este proyecto está licenciado bajo la Licencia GPL v3.0. Consulta el archivo LICENSE para obtener más información.
