# Django Recruitment Tasks

Two Django applications created as recruitment tasks.

## Task 1: Text Processor

Upload a text file and scramble letters within words (keeping first and last letters in place).

**Features:**
- File upload with validation
- Scrambles middle letters of words
- Preserves formatting and punctuation

## Task 2: PESEL Validator

Validate Polish PESEL identification numbers.

**Features:**
- Format and checksum validation
- Extracts birth date and gender
- Accepts PESEL with spaces or hyphens

## Requirements

- Python 3.13
- Django 5.2.6

## Installation

1. Clone repository and navigate to project directory

2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start server:
   ```bash
   python manage.py runserver
   ```

## Usage

- **Text Processor**: http://127.0.0.1:8000/
- **PESEL Validator**: http://127.0.0.1:8000/pesel/

### Example PESEL numbers for testing:
- Valid: `44051401458`
- Valid with spaces: `440 514 014 58`
- Invalid checksum: `12345678901`
- Invalid date: `00000000000`
