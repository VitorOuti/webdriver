from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def create_driver(download_directory=None):
    print('Inicializando Webdriver do Chrome')
    chrome_options = Options()
    
    # Configurações adicionais para estabilidade
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    
    # Definir pasta para downloads, se especificada
    if download_directory:
        prefs = {"download.default_directory": download_directory}
        chrome_options.add_experimental_option("prefs", prefs)
    
    # Instancia o ChromeDriver com o WebDriver Manager
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), 
        options=chrome_options
    )
    
    return driver
