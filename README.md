# Python Auto Mailer

## Overview

This Python script sends personalized emails with attachments using Gmail's SMTP server. It loads recipient information from a csv and email configuration allowing customization of email content, recipients, and attachment files.

## Prerequisites

Before running the script, ensure you have:

- Python 3.x installed ([Download Python](https://www.python.org/downloads/)). I'm using 3.9
- A Gmail account with [2-Step Verification](https://myaccount.google.com/security-checkup) enabled and an [App Password](https://support.google.com/accounts/answer/185833) generated

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vaibhava17/auto-mailer.git
    cd auto-mailer
    ```

2. **Install dependencies**:
    ```bash
    pip install requirements.txt
    ```

3. **Create a `.env` file**:
    Create a file named `.env` in the root directory with your Gmail account credentials:
    ```
    EMAIL_USER=your_email@gmail.com
    EMAIL_PASSWORD=your_generated_app_password
    EMAIL_SUBJECT=your_subject
    EMAIL_FROM=your_from_email
    EMAIL_ATTACHMENT=your_attachment_file_path
    CSV_FILE=your_data_file_path
    ```

4. **Prepare `content.json`**:
    Create a `content.json` file in the root directory with the following structure:
    ```json
    {
        "body": "Hi, \n\nThis is My content here."
    }
    ```

## Usage

Run the script `main.py` to send personalized emails:
```bash
python main.py
```

## Additional Notes

- Ensure that `python-dotenv` is installed (`pip install python-dotenv`) to load environment variables from `.env`.
- Customize `content.json` to adjust email content as per your requirements.
- Make sure your Gmail account allows access to less secure apps or has 2-Step Verification enabled with the app password.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.