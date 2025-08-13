from crewai_tools import SeleniumScrapingTool
from src.tools.scraper import selenium_scraper

# scraper = SeleniumScrapingTool(
#     website_url="https://terraria.wiki.gg/wiki/Weapons",
#     css_element="body"  # the part of the page you want
# )

# res = scraper._run()

# print(res)

res = selenium_scraper._run()

print(res)