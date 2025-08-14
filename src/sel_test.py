from crewai_tools import SeleniumScrapingTool
from src.tools.scraper import selenium_scraper, analyze_classes

# res = selenium_scraper._run(website_url="https://terraria.wiki.gg/wiki/Muramasa", css_element="body")
# print(res)

analyze_classes("https://terraria.wiki.gg/wiki/Muramasa")