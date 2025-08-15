from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from crewai.tools import tool
from collections import defaultdict

@tool
def selenium_scraper(website_url: str, css_element: str = ".mw-parser-output"):
    """Scrapes using Selenium"""

    # Headless Chrome (no UI)
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(website_url)

    # Wait for JS content to load
    driver.implicitly_wait(3)

    # Grab the main content
    content = driver.find_element(By.CSS_SELECTOR, "body").text
    driver.quit()

    return content

def analyze_classes(url: str, headless: bool = True):
    options = Options()
    options.headless = headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    # Wait for JS content to load
    driver.implicitly_wait(2)

    all_elements = driver.find_elements(By.TAG_NAME, '*')

    # Extract the tag names
    all_tags = [element.tag_name for element in all_elements]

    # Get a list of unique tags
    unique_tags = set(all_tags)

    # Print the unique tags
    print("Unique tags found on the webpage:")
    print(sorted(list(unique_tags)))

    # Finding unique classes
    all_classes = []

    for element in all_elements:
        found_class = element.get_attribute("class")
        if found_class:
            all_classes.append(found_class)
    
    unique_classes = set(all_classes)
    # Print the unique classes
    print("Unique classes found on the webpage:")
    print(sorted(list(unique_classes)))


    # Close the browser
    driver.quit()
    
    