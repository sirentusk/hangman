def display_image():
    img_url = 'https://python-hangman.pages.dev/images/hangman1.png'
    img_tag = f'<img src="{img_url}">'
    pyscript.write('image-container', img_tag)

# Call the function to display the image
display_image()