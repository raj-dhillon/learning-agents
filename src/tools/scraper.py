from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from crewai.tools import tool

@tool
def selenium_scraper():
    """Scrapes using Selenium"""

    # Headless Chrome (no UI)
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://terraria.wiki.gg/wiki/Weapons")

    # Wait for JS content to load
    driver.implicitly_wait(3)

    # Grab the main content
    content = driver.find_element(By.CSS_SELECTOR, ".mw-parser-output").text
    driver.quit()
    
    return content

