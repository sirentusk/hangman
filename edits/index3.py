import asyncio
import micropip
import http.client
from io import BytesIO

async def install_pillow():
    await micropip.install("pillow")

async def load_and_display_image(img_url):
    conn = http.client.HTTPSConnection("python-hangman.pages.dev")
    conn.request("GET", "/images/hangman2.png")
    response = conn.getresponse()
    img_data = BytesIO(response.read())
    from PIL import Image  # Import Pillow here after ensuring it's installed
    img = Image.open(img_data)
    img.show()  # This will open the image in a new window if a GUI is available

# Define a main coroutine to manage the execution
async def main():
    await install_pillow()  # Await the installation of Pillow here
    await load_and_display_image('https://python-hangman.pages.dev/images/hangman2.png')

# Schedule the main coroutine to run
asyncio.ensure_future(main())
