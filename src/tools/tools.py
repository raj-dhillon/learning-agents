from crewai.tools import tool
from tools.scraper import selenium_scraper
import os, uuid


# Agent tools
@tool
def raj_info():
    """Tool to provide information about Raj's physical capabilities."""
    return "Raj can do 10 pullups, 15 pistol squats, and 30 pushups."

@tool
def scraper_tool_chunk(url: str, chunk_size: int = 2000, overlap: int = 200) -> list:
    """Splits scraped text into overlapping chunks to preserve context and stores
    as individual text files."""

    full_text = selenium_scraper(website_url=url)
    words = full_text.split()

    # make uuid
    unique_id = str(uuid.uuid4())
    os.makedirs("scraped_chunks", exist_ok=True)

    chunk_files = []
    start = 0
    chunk_num = 0
    while start < len(words):
        end = min(len(words), start + chunk_size)
        chunk = " ".join(words[start:end])
        file_name = f"scraped_chunks/{unique_id}_{chunk_num}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(chunk)

        chunk_files.append(file_name)
        start += chunk_size - overlap
        chunk_num += 1
    
    return {
        "uuid": unique_id,
        "num_chunks": chunk_num,
        "chunk_files": chunk_files
    }

@tool
def read_chunk_file(filename: str) -> str:
    """
    Reads the content of a chunk file and returns it as a string.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as err:
        return f"Failed to read file: {err}"
    
@tool
def read_all_chunk_files(filename_list: list) -> str:
    """
    Reads the contents of a list of chunk files and returns it as a string.
    """
    try:
        full_text = []
        for file in filename_list:
            with open(file, "r", encoding="utf-8") as f:
                full_text.append(f.read())
    except Exception as err:
        return f"Failed to read file: {err}"

    return full_text