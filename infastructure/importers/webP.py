import os
import io
import uuid
import zipfile
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from PIL import Image

#Go will call this to get concurent downloads!

def download_chapter_to_cbz(url: str, output_path: str):

    print(f"Initializing engine for: {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 1920}
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="networkidle", timeout=45000)

            for _ in range(8):
                page.evaluate("window.scrollBy(0, window.innerHeight * 1.5);")
                page.wait_for_timeout(500)


            if "mangaplus" in url.lower() or "shonenjumpplus" in url.lower():
                print(" Manga Plus canvas engine detected. Extracting visual buffers...")
                image_buffers = extract_manga_plus_canvases(page)

            else:
                print("Standard image layout detected (Comix/Yaoiscan style).")
                image_buffers = extract_standard_images(page, url)

            if image_buffers:
                save_buffers_to_cbz(image_buffers, output_path)
                print(f"Successfully created: {output_path} ({len(image_buffers)} pages)")
                return True
            else:
                print("No readable chapter frames were extracted.")
                return False

        except Exception as e:
            print(f"Failed processing page frame: {e}")
            return False
        finally:
            browser.close()


def extract_standard_images(page, base_url: str) -> list:
    urls = page.evaluate("""
        () => {
            const list = [];
            document.querySelectorAll('img').forEach(img => {
                const w = img.naturalWidth || img.clientWidth;
                const h = img.naturalHeight || img.clientHeight;
                // Skips avatars, ads, UI icons
                if (w > 400 && h > 500) {
                    const src = img.src || img.getAttribute('src');
                    if (src && !src.startsWith('data:')) list.push(src);
                }
            });
            return list;
        }
    """)

    buffers = []
    for idx, src in enumerate([urljoin(base_url, u) for u in urls if u]):
        try:
            img_response = page.context.request.get(src, headers={"Referer": base_url})
            if img_response.status == 200:
                buffers.append(img_response.body())
        except Exception:
            continue
    return buffers


def extract_manga_plus_canvases(page) -> list:

    base64_strings = page.evaluate("""
        () => {
            const frames = [];
            document.querySelectorAll('canvas').forEach(canvas => {
                // Ignore small interface sliders or loading wheels
                if (canvas.width > 500) {
                    frames.push(canvas.toDataURL('image/jpeg', 0.9));
                }
            });
            return frames;
        }
    """)

    import base64
    buffers = []
    for data_str in base64_strings:
        if "," in data_str:
            header, encoded = data_str.split(",", 1)
            buffers.append(base64.b64decode(encoded))
    return buffers


def save_buffers_to_cbz(buffers: list, output_path: str):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as cbz:
        for idx, buf in enumerate(buffers):
            try:
                img = Image.open(io.BytesIO(buf))
                ext = img.format.lower() if img.format else "jpeg"
                filename = f"{idx + 1:03d}.{ext}"
                cbz.writestr(filename, buf)
            except Exception:
                cbz.writestr(f"{idx + 1:03d}.jpg", buf)
