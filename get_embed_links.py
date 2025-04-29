import os
import re

carpeta_entrada = 'descargas'
carpeta_salida = 'content'
os.makedirs(carpeta_salida, exist_ok=True)

def transformar_url(url):
    match = re.search(r'https://es\.scribd\.com/document/(\d+)', url)
    if match:
        doc_id = match.group(1)
        return f'https://es.scribd.com/embeds/{doc_id}/content'
    return ''

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith('.txt'):
        ruta_entrada = os.path.join(carpeta_entrada, archivo)
        ruta_salida = os.path.join(carpeta_salida, archivo)
        with open(ruta_entrada, encoding='utf-8') as fin, open(ruta_salida, 'w', encoding='utf-8') as fout:
            for linea in fin:
                url = linea.strip()
                nueva_url = transformar_url(url)
                if nueva_url:
                    fout.write(nueva_url + '\n')
print('Transformación completada. Archivos generados en la carpeta content.')
