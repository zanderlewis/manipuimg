from PIL import Image
import math
import glob
import os


class ImageStore:
    def __init__(self, base_filename):
        self.base_filename = base_filename

    def text_to_image(self, text, size=(500, 500)):
        colors = [
            (ord(c) % 256, (ord(c) // 256) % 256, (ord(c) // 256 // 256) % 256)
            for c in text
        ]
        grid_size = math.isqrt(len(colors))
        if grid_size * grid_size < len(colors):
            grid_size += 1
        img = Image.new("RGB", (grid_size, grid_size), color="white")
        img.putdata(colors + [(255, 255, 255)] * (grid_size * grid_size - len(colors)))
        img = img.resize(size, resample=Image.NEAREST)
        img.save(f"{self.base_filename}_{grid_size}x{grid_size}.png")

    def image_to_text(self):
        filename = self.get_latest_file()
        original_size = int(filename.split("_")[-1].split("x")[0])
        img = Image.open(filename)
        img = img.resize((original_size, original_size), Image.NEAREST)
        colors = list(img.getdata())
        text = "".join(
            chr(r + g * 256 + b * 256 * 256)
            for r, g, b in colors
            if (r, g, b) != (255, 255, 255)
        )
        return text

    def get_latest_file(self):
        return max(glob.glob(f"{self.base_filename}_*.png"), key=os.path.getctime)


import matplotlib.pyplot as plt


class ImageHistogram:
    def __init__(self, filename):
        self.image = Image.open(filename)

    def calculate_histogram(self):
        self.histogram = self.image.histogram()

    def save_histogram(self, filename):
        plt.figure(figsize=(10, 6))
        plt.bar(range(256), self.histogram[:256], color="red", alpha=0.7)
        plt.bar(range(256), self.histogram[256:512], color="green", alpha=0.7)
        plt.bar(range(256), self.histogram[512:], color="blue", alpha=0.7)
        plt.savefig(filename)


import binascii


class ImageSteganography:
    def __init__(self, filename):
        self.image = Image.open(filename)

    def encode(self, message):
        binary_message = bin(int(binascii.hexlify(message.encode("utf-8")), 16))[2:]
        binary_message = binary_message.zfill(8 * ((len(binary_message) + 7) // 8))

        # Store the length of the message in the first 32 pixels
        binary_length = bin(len(binary_message))[2:].zfill(32)
        data = list(self.image.getdata())
        new_data = []
        for i in range(32):
            pixel = ((data[i][0] & ~1) | int(binary_length[i]),) + data[i][1:]
            new_data.append(pixel)

        for i in range(len(binary_message)):
            pixel = ((data[i + 32][0] & ~1) | int(binary_message[i]),) + data[i + 32][
                1:
            ]
            new_data.append(pixel)

        new_data += data[len(binary_message) + 32 :]
        self.image.putdata(new_data)

    def decode(self):
        data = list(self.image.getdata())
        binary_length = "".join([str(data[i][0] & 1) for i in range(32)])
        message_length = int(binary_length, 2)

        binary_message = "".join(
            [str(data[i + 32][0] & 1) for i in range(message_length)]
        )
        hex_message = hex(int(binary_message, 2))[2:]
        try:
            return binascii.unhexlify(hex_message).decode("utf-8")
        except UnicodeDecodeError:
            return "Could not decode message: Not valid UTF-8 encoded text"

    def save(self, filename):
        self.image.save(filename)


