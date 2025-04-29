import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re

# Configuración inicial
search_url = input('Introduce la URL de búsqueda de Scribd: ')
dest_folder = input('Introduce la carpeta de destino para los enlaces extraídos: ')

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Configuración de Selenium
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Ejecutar en modo headless (sin ventana)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080')

# Cambia el path al chromedriver si es necesario
driver = webdriver.Chrome(options=chrome_options)

def limpiar_blur(driver):
    # Ejecuta el JS para eliminar el blur
    js = '''
        (function() {
            if (typeof window.jQuery === 'undefined') {
                let script = document.createElement('script');
                script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
                script.onload = init;
                document.head.appendChild(script);
            } else {
                init();
            }
            function init() {
                const $ = window.jQuery;
                const limpiarScribd = () => {
                    $('._1qNr2d').remove();
                    $('#scribd_blur_incontent_display--1').remove();
                    $('[data-blur-type]').css({'filter': 'none','pointer-events': 'auto'});
                    $('.absimg').css('opacity', '1.0');
                    $('.text_layer').css({'color': '#000','text-shadow': '0 0 0 #000'});
                    $('button:contains("Omitir anuncio")').parent().parent().remove();
                };
                limpiarScribd();
            }
        })();
    '''
    driver.execute_script(js)

def extraer_enlaces_documentos(driver):
    enlaces = set()
    # Buscar todos los <a> con la clase específica
    docs = driver.find_elements(By.CSS_SELECTOR, 'a.ListItem-module_linkOverlay__H60l3')
    for doc in docs:
        href = doc.get_attribute('href')
        if href and href.startswith('https://es.scribd.com/document/'):
            enlaces.add(href)
    return enlaces

def guardar_enlaces(enlaces, dest_folder, page):
    with open(os.path.join(dest_folder, f'enlaces_pagina_{page}.txt'), 'w', encoding='utf-8') as f:
        for enlace in enlaces:
            f.write(enlace + '\n')

def aceptar_cookies(driver):
    try:
        # Espera breve para que el banner cargue
        time.sleep(2)
        btn = driver.find_element(By.CSS_SELECTOR, 'button.osano-cm-accept-all')
        if btn.is_displayed():
            btn.click()
            print('Cookies aceptadas.')
            time.sleep(1)
    except Exception:
        pass

# Proceso principal
driver.get(search_url)
time.sleep(3)
aceptar_cookies(driver)
limpiar_blur(driver)

pagina = 1
enlaces_totales = set()
while True:
    print(f'Extrayendo página {pagina}...')
    time.sleep(2)
    limpiar_blur(driver)
    enlaces = extraer_enlaces_documentos(driver)
    guardar_enlaces(enlaces, dest_folder, pagina)
    enlaces_totales.update(enlaces)
    # Intentar ir a la siguiente página por URL
    pagina += 1
    next_url = f"{search_url}&page={pagina}" if 'page=' not in search_url else re.sub(r'page=\d+', f'page={pagina}', search_url)
    driver.get(next_url)
    time.sleep(2)
    aceptar_cookies(driver)
    # Si no hay resultados nuevos, terminamos
    if not driver.find_elements(By.CSS_SELECTOR, 'a.ListItem-module_linkOverlay__H60l3'):
        break

driver.quit()
print(f'Enlaces extraídos: {len(enlaces_totales)}')
print(f'Guardados en la carpeta: {dest_folder}')
