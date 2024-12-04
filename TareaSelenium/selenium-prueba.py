import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración global del navegador
@pytest.fixture
def browser():
    browser = webdriver.Chrome()  # Asegúrate de tener el chromedriver configurado
    base_url = "http://127.0.0.1:5500/index.html"  # Cambia la ruta según tu sistema de archivos
    browser.get(base_url)
    yield browser
    browser.quit()

# Función para pausar la ejecución
def espera(tiempo):
    time.sleep(tiempo)

# Historia de Usuario: Navegar y regresar usando "Volver al Inicio"
def test_navegar_y_volver(browser):
    # Navegar a una sección, en este caso "Ver Galería"
    tarjeta = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Ver Galeria"))
    )
    tarjeta.click()
    espera(3)
    
    # Verificar que se abrió la página correcta
    assert "Pagina.html" in browser.current_url, "No se abrió la página correcta"
    browser.save_screenshot("Undertaleg.png")
    
    # Usar el botón "Volver al Inicio" para regresar
    volver = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    volver.click()
    espera(5)
    
    # Verificar que se regresó al índice
    assert "index.html" in browser.current_url, "No se volvió a la página principal"

    # Historia de Usuario: Navegar y regresar usando "Volver al Inicio"
def test_navegar_y_volver2(browser):
    # Navegar a una sección, en este caso "Ver Galería"
    tarjeta = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Ver Galeria1"))
    )
    tarjeta.click()
    espera(5)
    
    # Verificar que se abrió la página correcta
    assert "Pagina2.html" in browser.current_url, "No se abrió la página correcta"
    browser.save_screenshot("Zelda.png")
    
    # Usar el botón "Volver al Inicio" para regresar
    volver = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-primary.me-4"))
    )
    volver.click()
    
    # Verificar que se regresó al índice
    assert "index.html" in browser.current_url, "No se volvió a la página principal"