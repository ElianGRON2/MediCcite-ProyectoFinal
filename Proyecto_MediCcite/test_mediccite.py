import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MediCciteTests(unittest.TestCase):

    def setUp(self):
        # Configuración inicial del driver (Simulación para Chrome)
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/Proyecto_MediCcite/index.html")

    def test_cp01_login_exitoso(self):
        """
        CP-01: Prueba de Inicio de Sesión (Referencia Pág 9 de tu PDF)
        Verifica que el usuario pueda ingresar con credenciales.
        """
        driver = self.driver
        
        # Localizar elementos (Según tu documento de QA)
        usuario = driver.find_element(By.TAG_NAME, "input") # Campo usuario
        clave = driver.find_element(By.CSS_SELECTOR, "input[type='password']") # Campo password
        boton = driver.find_element(By.TAG_NAME, "button")

        # Acciones
        usuario.send_keys("admin")
        clave.send_keys("1234")
        boton.click()
        
        # Espera implícita
        time.sleep(2)

        # Validación (Assert)
        # Verificamos que redirige o muestra el Dashboard
        assert "Dashboard" in driver.title
        print("✅ CP-01: Login Exitoso - PASÓ")

    def test_hu03_agendar_cita(self):
        """
        HU-03: Agendar Cita
        Verifica que se pueda llenar el formulario de citas.
        """
        driver = self.driver
        # Navegar a citas
        driver.get("http://localhost/Proyecto_MediCcite/citas.html")
        
        campo_paciente = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nombre del Paciente']")
        campo_paciente.send_keys("Juan Perez")
        
        boton_guardar = driver.find_element(By.XPATH, "//button[contains(text(),'Guardar')]")
        boton_guardar.click()
        
        print("✅ HU-03: Agendar Cita - PASÓ")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()