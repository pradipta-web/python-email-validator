# Python Email Validator

A lightweight Python-based email validator that checks email address formats using regular expressions through an interactive command-line interface.

## Features

- Validate email address formats.
- Check email structure.
- Detect missing @ symbols.
- Validate domain extensions.
- Detect consecutive dots.
- Display VALID or INVALID results.
- Support multiple email checks.
- Interactive command-line interface.

## Technologies Used

- Python
- Regular Expressions (re)
- Colorama

## Project Structure

```text
python-email-validator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-email-validator.git
```

2. Navigate to the project directory:

```bash
cd python-email-validator
```

3. Create a virtual environment:

```bash
py -m venv venv
```

4. Install dependencies:

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
.\venv\Scripts\python.exe app.py
```

Enter an email address to check its format.

Type `exit` to close the application.

## Example

```text
Enter email (or type 'exit' to quit):
> user@gmail.com

Status: VALID
Message: Email format is valid.
```

## Author

**Kinervaaa**

GitHub: https://github.com/pradipta-web