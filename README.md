# DocLib

DocLib is a healthcare application designed to help users find medical specialists nearby while also suggesting home remedies for common health issues. The app allows users to input their symptoms, select the intensity of their symptoms, and find local specialists based on their location.

## Features

- **Symptom Input**: Users can enter multiple symptoms such as cough, body ache, and stomach ache.
- **Symptom Intensity Selection**: Users can choose the severity of their symptoms (e.g., Mild, Moderate, Severe).
- **Location-Based Specialist Search**: Users can input their city to find healthcare specialists near them.
- **Home Remedies Suggestions**: The app provides home remedies based on the entered symptoms.
- **User-Friendly Interface**: Simple and intuitive design for easy navigation.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (for storing specialist information)
- **APIs**: Google Maps API (for location-based search)

## Installation

To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/tushar2704/doclib.git
   ```

2. Navigate to the project directory:
   ```bash
   cd doclib
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run Home.py
   ```

5. Open your browser and go to `http://localhost:5000`.

## Usage

1. Enter your symptoms in the input field (e.g., "cough, body ache").
2. Select the intensity of your symptoms from the dropdown menu.
3. Enter your city to find local specialists.
4. Click on "Get Health Advice and Find Specialists" to receive home remedy suggestions and a list of nearby specialists.

## Troubleshooting

If you encounter an error such as `local variable 'inputs' referenced before assignment`, ensure that all required variables are properly initialized before use in the backend code.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
