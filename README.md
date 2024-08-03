# Moodalyze

Moodalyze is an application designed to track and analyze sentiments of topics across Twitter. By leveraging Twikit for scraping tweets and a HuggingFace Language Model (LLM) for sentiment analysis, Moodalyze provides insights into the public mood on various topics.

## Features

- **Tweet Scraping**: Uses Twikit to scrape tweets based on specified keywords or hashtags.
- **Sentiment Analysis**: Utilizes HuggingFace's state-of-the-art LLM to analyze the sentiments of scraped tweets.
- **Interactive Frontend**: Built with React and Vite for a smooth and responsive user experience.
- **Robust Backend**: Powered by Flask, handling tweet processing and sentiment analysis with Python.

## Tech Stack

- **Frontend**: React, Vite
- **Backend**: Flask, Python
- **Sentiment Analysis**: HuggingFace LLM
- **Tweet Scraping**: Twikit

## Installation

### Prerequisites

- Node.js and npm (for frontend)
- Python 3.x (for backend)
- Pip (Python package installer)

### Backend Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/moodalyze.git
    cd moodalyze/backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Start the Flask server:
    ```sh
    flask run
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```sh
    cd ../frontend
    ```

2. Install the required npm packages:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm run dev
    ```

## Usage

1. Open your browser and navigate to `http://localhost:3000` to access the Moodalyze frontend.
2. Enter the desired keyword or hashtag to scrape tweets.
3. View the sentiment analysis results presented in a user-friendly interface.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact

For questions or suggestions, feel free to open an issue or contact the project maintainers at devangsharma@ucla.edu

---

Happy Moodalyzing!
