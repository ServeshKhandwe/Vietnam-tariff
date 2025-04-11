# Vietnam-Germany HS Code Finder

A Streamlit-based web application that helps users find Harmonized System (HS) codes for trade between Vietnam and Germany. The application uses AI models to analyze trade-related queries and provide accurate HS code classifications.

## Features

- Interactive web interface built with Streamlit
- AI-powered HS code classification using OpenAI's GPT model
- Support for Vietnamese and German trade classifications
- User-friendly interface with custom styling
- CSV data integration for HS code database

## Prerequisites

- Python 3.8 or higher
- Conda package manager
- Git

## Installation

<!-- 1. Clone the repository:
```bash
git clone <your-repository-url>
cd vt-zip
``` -->

1. Create a new Conda environment:
```bash
conda create -n vietnam-tariff python=3.11
conda activate vietnam-tariff
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup

1. Export your OpenAI API key in your terminal:
```bash
export OPENAI_API_KEY='your_api_key_here'
```

Note: You'll need to export this key every time you open a new terminal session. To make it permanent, you can add the export command to your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`).

2. Place your CSV file containing HS code data in the root directory and name it `input2.csv`
3. Add any trade-related image you want to display in the app and name it `VN-German-trade.jpg`

## Usage

1. Activate the Conda environment:
```bash
conda activate vt-zip
```

2. Run the Streamlit app:
```bash
streamlit run main.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

4. Enter your trade-related query in the text area and click the "Find HS Code" button to get the classification

## Project Structure

- `main.py`: Main application file containing the Streamlit app
- `requirements.txt`: List of Python dependencies
- `input2.csv`: HS code database (to be added by user)
- `VN-German-trade.jpg`: Trade-related image (to be added by user)

## Dependencies

The project uses several key Python packages:
- Streamlit for the web interface
- Pandas for data handling
- OpenAI for AI-powered classification
- Other supporting packages listed in requirements.txt

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository. 