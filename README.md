# ManipuIMG

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Description

ManipuIMG is a small image manipulation tool that allows hiding text in images, converting text to images, creating histograms, and more!

## Features

- Steganography
- Histograms
- Text as an Image

## Installation

Install via `pip install manipuimg` on Windows, `pip3 install manipuimg` on MacOS/Linux, or `!pip install manipuimg` on Jupyter Notebook.

## Usage

```py
import manipuimg

# Example usage of ImageStore
store = manipuimg.ImageStore('base')
store.text_to_image('Hello, world!')
print(store.image_to_text())  # Should print 'Hello, world!'

# Example usage of ImageHistogram
histogram = manipuimg.ImageHistogram('path/to/image.png')
histogram.calculate_histogram()
histogram.save_histogram('histogram.png')

# Example usage of ImageSteganography
steganography = manipuimg.ImageSteganography('path/to/image.png')
steganography.encode('Secret message')
print(steganography.decode())  # Should print 'Secret message'
steganography.save('stegano.png')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
