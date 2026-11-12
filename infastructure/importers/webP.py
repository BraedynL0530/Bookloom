from core.classes.Book import Book
from bs4 import BeautifulSoup as BS
import os
import requests
from urllib.parse import urlparse, urljoin
import zipfile

#TODO: transfer to go in future
def download_concurrent(url, concurrency=3):
    id = 0
    done = False
    Book = None
    for i in range(concurrency):
        id += 1
        if Book:
            download_chapter(url, id,Book)
        else:
            Book = download_chapter(url, id)






def download_chapter(url, book,id=0):
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    Headers = {
        "User-Agent": agent,
        "referer": url
    }
    title = "temp"  # fetch from url/something else
    index = id
    output_path = f"{title}chapter {index}.cbz"
    soup = BS(requests.get(url, headers=Headers).content, "html.parser")
    imgs = find_manhwa_images_heuristically(soup, url)
    valid_exts = ['.jpg', '.jpeg', '.png', '.webp']
    if not imgs:
        return

    if book.chapters:
        book.chapters.append(output_path) #needs to be changed
    else:
        newBook = Book(title, output_path)
        return newBook



def clean_url(url, base_url: str):
    if not url:
        return None
    url = url.strip()
    if url.startswith('//'):
        return 'https:' + url
    return urljoin(base_url, url)


def find_manhwa_images_heuristically(soup, base_url: str) -> list:
    candidate_blocks = []

    for element in soup.find_all(['div', 'section', 'article', 'main']):
        imgs = element.find_all('img', recursive=False)
        if len(imgs) < 3:
            imgs = element.find_all('img')
            if len(imgs) < 3:
                continue

        score = 0
        valid_urls = []
        domains = {}

        for img in imgs:
            src = img.get('data-src') or img.get('src') or img.get('data-lazy-src') or img.get('origin-src')
            src = clean_url(src, base_url)

            if not src:
                continue

            low_val_keywords = ['logo', 'banner', 'icon', 'avatar', 'loader', 'widget', 'ad', 'button']
            if any(key in src.lower() for key in low_val_keywords):
                score -= 10
                continue

            if any(ext in src.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
                valid_urls.append(src)

                domain = urlparse(src).netloc
                domains[domain] = domains.get(domain, 0) + 1

        if len(valid_urls) < 3:
            continue

        score += len(valid_urls) * 5

        if domains:
            primary_domain_count = max(domains.values())
            if primary_domain_count / len(valid_urls) > 0.85:
                score += 100

        text_length = len(element.get_text(strip=True))
        if text_length > 0:
            text_to_img_ratio = text_length / len(valid_urls)
            if text_to_img_ratio > 50:
                score -= 50

        attrs_string = " ".join([str(v) for v in element.attrs.values()]).lower()
        if any(k in attrs_string for k in ['reader', 'chapter', 'vung-doc', 'images-go', 'comic-wrap']):
            score += 40

        candidate_blocks.append({
            'element': element,
            'urls': valid_urls,
            'score': score
        })

    if not candidate_blocks:
        return []

    candidate_blocks.sort(key=lambda x: x['score'], reverse=True)
    best_candidate = candidate_blocks[0]

    print(f"Selected target block with footprint score: {best_candidate['score']}")
    return best_candidate['urls']

# plugin file saving,