import random
import string
import os
import codecs
import qrcode

# ====== CONFIG =======
BASE_URL = "https://ylliez.github.io/CUt/IMCA220/QRient/steps/"  # Change this!
OUTPUT_DIR = "./steps"  # Where HTML and QR codes will be saved
SLICE_IMAGE_PATH = "../slices/slice_{}.png"  # path to slice images in HTML

NUM_SLICES = 8

# ====== Helpers =======

def random_token(length=6):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def make_html(filename, slice_num):
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Piece Unlocked!</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 2rem;
    }}
    img {{
      max-width: 90vw;
      height: auto;
      margin-top: 1rem;
      border: 2px solid #333;
    }}
  </style>
</head>
<body>
  <h1>You&apos;ve unlocked piece #{slice_num}!</h1>
  <img src="{slice_image_path}" alt="Unlocked slice {slice_num}" />
  <script>
    localStorage.setItem("slice{slice_num}", "true");
    setTimeout(function () {{
      window.location.href = "../index.html";
    }}, 5000);
  </script>
</body>
</html>"""

    slice_image_path = SLICE_IMAGE_PATH.format(slice_num)
    return html_template.format(slice_num=slice_num, slice_image_path=slice_image_path)

def save_file(path, content):
    with codecs.open(path, "w", "utf-8") as f:
        f.write(content)

def generate_qr_code(url, path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)

# ====== MAIN =======

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filenames = []
    for i in range(1, NUM_SLICES + 1):
        token = random_token()
        filename = "step_{}.html".format(token)
        filenames.append(filename)

        # Create HTML file
        html_content = make_html(filename, i)
        save_file(os.path.join(OUTPUT_DIR, filename), html_content)

        # Generate QR code pointing to URL
        url = BASE_URL + filename
        qr_path = os.path.join(OUTPUT_DIR, "qr_slice{}.png".format(i))
        generate_qr_code(url, qr_path)

        print "Created slice #{}: {}".format(i, filename)
        print " -> URL: {}".format(url)
        print " -> QR code saved at: {}\n".format(qr_path)

    print "All done! You can print the QR code images in the 'output' folder."

if __name__ == "__main__":
    main()
