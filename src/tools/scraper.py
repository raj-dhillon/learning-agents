from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import hashlib

def selenium_scraper(website_url: str, css_element: str = ".mw-parser-output", css_selectors: list = None):
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
    css_selectors = ["body"]
    if css_selectors is None or len(css_selectors) == 0:
        css_selectors = [css_element]

    all_text = set()

    selector_string = ", ".join(css_selectors)
    elements = driver.find_elements(By.CSS_SELECTOR, selector_string)
    
    seen_fingerprints = set()

    for el in elements:
        try:
            fingerprint = hashlib.md5(el.text.strip().encode()).hexdigest()
            
            if not fingerprint or fingerprint in seen_fingerprints:
                continue
            
            seen_fingerprints.add(fingerprint)
            text = el.text
            if text:
                all_text.add(text)
        except Exception:
            continue # skip stale elements
    content = "\n\n".join(all_text)

    driver.quit()
    return content

def analyze_classes(url: str, headless: bool = True):
    options = Options()
    options.headless = headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_page_load_timeout(300)  # increase page load timeout to 5 minutes
    
    driver.get(url)
    # Wait for JS content to load
    driver.implicitly_wait(5)

    all_elements = driver.find_elements(By.TAG_NAME, '*')

    unique_tags = set()
    unique_classes = set()

    # Get tags and classes
    for element in all_elements:
        try:
            # Get a set of unique tags
            tag = element.tag_name
            unique_tags.add(tag)

            # Finding unique classes
            clas = element.get_attribute("class")
            if clas:
                for c in clas.split():
                    if c:
                        unique_classes.add(c.strip())

        except StaleElementReferenceException:
            # skip stale elements
            continue

    # Print the unique tags
    print("Unique tags found on the webpage:")
    print(sorted(list(unique_tags)))

    # Print the unique classes
    print("Unique classes found on the webpage:")
    print(sorted(list(unique_classes)))


    # Close the browser
    driver.quit()
    
    