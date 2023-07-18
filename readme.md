# Words counter

This project is a web application that counts words and characters in text.

## Features

The application counts words and characters:
- in text entered in a text field
- on a picture from file or url

## Technologies Used

- Python
- Flask
- OpenCV
- HTML/CSS

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lilmarcin/words-counter.git

2. Navigate to the project directory:

    ```bash
    cd words-counter

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

    Install separately if necessary:
    -`pip install torch torchvision torchaudio`
    -`pip install easyocr`

## Usage

1. Run the Flask application:

    ```bash
    python app.py

2. Open a web browser and go to http://localhost:5000.
3. On the home page, select the option you are interested in (write text or upload image with text).
![GIF](images/home_page.gif)
3. In the `write text` option, type the text in the box and click `count`. See example results:
![Screenshot](images/write1.png)
![Screenshot](images/result_write1.png)
4. In the `upload image` option, type the image url or upload from file and click `upload`. See example results:
![Screenshot](images/upload.png)
![Screenshot](images/result_image_url.png)
![Screenshot](images/result_image_file.png)
![Screenshot](images/result_image_file1.png)



## License
This project is licensed under the MIT License.