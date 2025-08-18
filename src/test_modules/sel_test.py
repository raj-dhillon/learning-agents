from crewai_tools import SeleniumScrapingTool
from src.tools.scraper import selenium_scraper, analyze_classes
from tools.tools import scraper_tool_chunk, read_chunk_file

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

CONTENT_CLASSES = [
  "articlePage",
  "mw-parser-output",
  "toc",
  "thumb",
  "thumbcaption",
  "reference",
  "page__main",
  "page-content",
  "pi-data",
  "pi-title",
  "pi-image",
  "pi-data-label",
  "pi-data-value",
  "mw-headline",
  "mw-redirect",
  "mw-selflink"
]
CONTENT_CLASSES = ["body ." + c for c in CONTENT_CLASSES]

# res = selenium_scraper._run(website_url="https://godofwar.fandom.com/wiki/Kratos", css_element="body", css_selectors=CONTENT_CLASSES)
# res = selenium_scraper(website_url="https://godofwar.fandom.com/wiki/Kratos", css_element="body", css_selectors=CONTENT_CLASSES)
# res = selenium_bs_scraper(website_url="https://godofwar.fandom.com/wiki/Kratos", css_element="body", css_selectors=CONTENT_CLASSES)
# print(res)
# with open('kratos_final.txt', 'w') as f:
#     f.write(res)

# analyze_classes("https://godofwar.fandom.com/wiki/Kratos")

# data = scraper_tool_chunk._run("https://themagicians.fandom.com/wiki/Quentin_Coldwater")
# print(data)

print(read_chunk_file._run("scraped_chunks/6acca429-82ff-4df2-92f9-0b07b2016074_0.txt"))