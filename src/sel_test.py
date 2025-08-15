from crewai_tools import SeleniumScrapingTool
from src.tools.scraper import selenium_scraper, analyze_classes

# res = selenium_scraper._run(website_url="https://terraria.wiki.gg/wiki/Muramasa", css_element="body")
# print(res)

# analyze_classes("https://terraria.wiki.gg/wiki/Muramasa")

relevant_classes = [
    'infobox', 'infobox-inline', 'ingredients', 'item', 'rarity', 
    'recipes', 'stack', 'stackdigits', 'knockback', 'stat', 
    'station', 'statistics', 'text', 'title', 'small-bold', 
    'thumbcaption', 'thumbimage', 'thumbinner', 
    'mw-body-content', 'mw-parser-output', 'content-body', 'content-wrapper'
]

relevant_classes = [f".{c}" for c in relevant_classes]

# res = selenium_scraper._run(website_url="https://terraria.wiki.gg/wiki/Muramasa", css_element="body", css_selectors=relevant_classes)

res = selenium_scraper._run(website_url="https://godofwar.fandom.com/wiki/Kratos", css_element="body")
print(res)

# analyze_classes("https://godofwar.fandom.com/wiki/Kratos")