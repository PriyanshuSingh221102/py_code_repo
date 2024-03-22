# so i commited the code using git -> learning git using this.
import segno
from urllib.request import urlopen
import os  # Import the os module to handle file paths

# Create the QR code with the URL
slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")

# Get the GIF from the URL
nirvana_url = urlopen("https://media1.tenor.com/m/27LpDvNbEXQAAAAC/puzzle-scramble.gif")

# Get the current working directory (where the Python file is located)
script_path = os.path.dirname(__file__)  # Use __file__ to get the script's path

# Construct the full path for saving the GIF
gif_path = os.path.join(script_path, "app2.gif")  # Define gif_path outside the code block

# Create the animated QR code with the GIF background and save it to the specified path
slts_qrcode.to_artistic(
    background=nirvana_url,
    target=gif_path,
    scale=5,
)
