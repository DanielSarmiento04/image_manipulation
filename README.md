# Image Manipulation Web App

## Overview

This project provides a web-based tool for manipulating images using OpenCV algorithms. It allows users to modify various image properties, add text, draw on the image, recognize objects, and resize or upscale images. The app is built with a focus on ease of use and offers a range of powerful editing and processing features.

## Features

- **Image Property Adjustments**:
  - Modify brightness, contrast, saturation, and more.
  
- **Change Image Extension**:
  - Convert images between popular formats (JPEG, PNG, BMP, etc.).
  
- **Add Text and Draw**:
  - Overlay custom text onto the image.
  - Draw freehand on the image using a built-in drawing tool.
  
- **Object Recognition**:
  - Automatically detect and label objects in images using pre-trained models integrated with OpenCV.

- **Resolution Upscaling/Downscaling**:
  - Seamlessly resize images or upscale them using algorithms such as bilinear interpolation, bicubic interpolation, or advanced methods like Lanczos.

## Built With

- **Frontend**: 
  - HTML5, CSS3, JavaScript (React/Vanilla)
  - Image rendering and manipulation through HTML Canvas

- **Backend**:
  - Python (Flask/Django/FastAPI)
  - Image processing with OpenCV

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- OpenCV (Python)
- A modern web browser (Chrome, Firefox, Safari)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/image-manipulation-webapp.git
    cd image-manipulation-webapp
    ```

2. **Backend setup**:
    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Frontend setup**:
    ```bash
    cd ../frontend
    npm install
    npm run build
    ```

4. **Running the application**:
    - Run the backend server:
      ```bash
      python app.py
      ```
    - Serve the frontend:
      ```bash
      npm start
      ```

5. Open your browser and go to `http://localhost:3000` to access the web app.

## Usage

- Upload an image from your local machine.
- Select from the available tools to edit the image:
  - **Change properties**: Adjust brightness, contrast, etc.
  - **Convert extension**: Export the image in the desired format.
  - **Add text/draw**: Annotate the image.
  - **Object recognition**: Automatically detect objects.
  - **Upscale/Downscale resolution**: Modify image resolution.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**.
2. Create a new branch:
    ```bash
    git checkout -b feature/new-feature
    ```
3. Make your changes and test thoroughly.
4. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
5. Push to your branch:
    ```bash
    git push origin feature/new-feature
    ```
6. Open a pull request and provide a detailed description of your changes.

### Code of Conduct

Please ensure that your contributions adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- OpenCV for the powerful image processing library.
- Contributions from the open-source community.

---

Feel free to reach out with any questions or feedback. Happy coding!
