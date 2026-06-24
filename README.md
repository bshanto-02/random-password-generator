# Random Password Generator

A simple Flask web application that generates secure random passwords based on user-defined criteria.

## Features

- Generate strong and secure passwords
- Custom password length selection
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special characters
- User-friendly web interface
- Built with Flask and Python

## Technologies Used

- Python 3
- Flask
- HTML
- CSS
- Bootstrap (optional)

## Project Structure

```
random-password-generator/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bshanto-02/random-password-generator.git
cd random-password-generator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Usage

1. Enter the desired password length.
2. Select the character types:
   - Uppercase Letters
   - Lowercase Letters
   - Numbers
   - Special Characters
3. Click **Generate Password**.
4. Copy and use the generated password.

## Example Generated Password

```text
T#9mK$2pX!7qL@4
```

## Security Notes

- Passwords are generated using Python's secure random functions.
- No generated passwords are stored on the server.
- Password generation happens dynamically for each request.

## Future Improvements

- Password strength meter
- Copy-to-clipboard button
- Password history
- Dark mode
- API endpoint for password generation

## Author

**Shanto**
GitHub: https://github.com/bshanto-02

## License

This project is licensed under the MIT License.
