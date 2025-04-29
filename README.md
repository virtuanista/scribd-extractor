# scribd-extractor

Este proyecto permite extraer enlaces de documentos de Scribd y transformarlos en enlaces de tipo embed para su posterior uso.

## Estructura del proyecto

- `get_links.py`: Script para extraer enlaces de documentos de Scribd a partir de una búsqueda.
- `get_embed_links.py`: Script para transformar los enlaces extraídos en enlaces embed.
- `descargas/`: Carpeta donde se guardan los enlaces extraídos por página.
- `content/`: Carpeta donde se guardan los enlaces transformados a formato embed.

## Uso

### 1. Extraer enlaces de Scribd

Ejecuta primero `get_links.py`. Este script abrirá un navegador, te pedirá la URL de búsqueda de Scribd y la carpeta de destino (por ejemplo, `descargas`).

```bash
python get_links.py
```

- El script recorrerá las páginas de resultados y guardará los enlaces de los documentos en archivos de texto dentro de la carpeta indicada.

### 2. Transformar enlaces a formato embed

**Importante:** No ejecutes este paso sin haber ejecutado antes `get_links.py` y tener los archivos de enlaces en la carpeta de destino (por defecto, `descargas`).

Ejecuta `get_embed_links.py`:

```bash
python get_embed_links.py
```

- El script leerá todos los archivos `.txt` de la carpeta `descargas`, transformará los enlaces a formato embed y los guardará en la carpeta `content`.

## Notas

- Es necesario tener instalado Python 3 y las dependencias indicadas en los scripts (por ejemplo, Selenium y ChromeDriver para `get_links.py`).
- El script `get_embed_links.py` no funcionará si no se han generado previamente los archivos de enlaces con `get_links.py`.

## Licencia

Uso personal y educativo.

<p align="center">
	Repositorio generado por <a href="https://github.com/virtuanista" target="_blank">virtu 🎣</a>
</p>

<p align="center">
	<img src="https://open.soniditos.com/cat_footer.svg" />
</p>

<p align="center">
	Copyright © 2025
</p>

<p align="center">
	<a href="/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
