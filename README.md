# Zivia Quiz App 🧠

Zivia is a simple desktop quiz application built with Python and Tkinter. It fetches true/false questions from the Open Trivia Database API and challenges you to test your knowledge. The application provides instant feedback and keeps track of your score as you play.

## Screenshot



***
## Features ✨

* **Interactive GUI**: Clean and simple user interface built with Tkinter.
* **Live Trivia Questions**: Fetches fresh questions directly from the Open Trivia DB API.
* **Instant Feedback**: The screen turns green for correct answers and red for incorrect ones.
* **Score Tracking**: Keeps a running total of your score.
* **Cross-Platform**: Can be run directly on any OS with Python or as a Docker container.

***
## Requirements

To run this application, you will need the following installed:

* Python 3.11+
* Docker Desktop (for containerized usage)
* Git

***
## Local Installation (Without Docker)

To run the app directly on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Zivia.git](https://github.com/YOUR_USERNAME/Zivia.git)
    cd Zivia
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python src/zivia/main.py
    ```

***
## Usage with Docker 🐳

This is the recommended way to run the application for a consistent and isolated environment.

1.  **Build the Docker image:**
    From the root of the project directory, run:
    ```bash
    docker build -t zivia-quiz-app .
    ```

2.  **Run the Docker container:**
    The command differs based on your operating system.

    * **On Windows (using PowerShell, CMD, or Git Bash):**
        *You must have an X Server like **VcXsrv** installed and running with "Disable access control" enabled.*
        ```bash
        docker run -it --rm -e DISPLAY=host.docker.internal:0.0 zivia-quiz-app
        ```

    * **On macOS (with XQuartz) or Linux:**
        ```bash
        docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X-unix:/tmp/.X-unix zivia-quiz-app
        ```

***
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
