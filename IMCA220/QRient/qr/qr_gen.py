import qrcode

# Customize this with your actual base URL
base_url = "https://ylliez.github.io/CUt/IMCA220/QRient/steps/step"

# Loop to generate QR codes
for i in range(1, 9):
    # qr_url = f"{base_url}{i}.html"
    qr_url = "{}{}.html".format(base_url, i)
    qr_img = qrcode.make(qr_url)
    # qr_img.save(f"qr{i}.png")
    qr_img.save("qr{}.png".format(i))
    # print(f"Generated qr{i}.png -> {qr_url}")
    print("Generated qr{}.png -> {}".format(i, qr_url))

