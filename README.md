# Website Status Checker

## Purpose
This program checks the status of multiple websites and sends an email with the results. It helps website owners or administrators monitor the uptime of their websites and quickly address any issues that may arise.

## Use Case
Are you running multiple websites and want to ensure that they are all functioning properly? Do you want to be alerted immediately if any of your websites go down? Our website status checker can help! With our program, you can easily check the status of all your websites and receive an email notification with the results.

Here's an example of how the website status checker might work in practice:

### Example 1: Checking the status of multiple websites
Suppose the user wants to check the status of the following websites:

- http://www.example.com
- https://www.example.org
- https://www.example.net

When the user runs the website status checker, the program will check the status of each website and send an email with the results.

If all websites are up and running, the user will receive an email like this:

SUCCESS: http://www.example.com is up and running!
SUCCESS: https://www.example.org is up and running!
SUCCESS: https://www.example.net is up and running!

If any of the websites are down, the user will receive an email like this:

SUCCESS: http://www.example.com is up and running!
WARNING: https://www.example.org returned a status code of 404
SUCCESS: https://www.example.net is up and running!


## Installation
The program is written in Python and requires the following packages:

- requests
- smtplib

You can install these packages using pip:
-pip install requests
-pip install secure-smtplib


## Configuration
The program can be configured by modifying the `config.yml` file. The file contains the following parameters:

- `sender_email`: The email address of the sender.
- `recipient_email`: The email address of the recipient.
- `password`: The password for the sender's email account.
- `urls`: A list of URLs to check.

If the `config.yml` file doesn't exist, the program will prompt you to enter the email parameters and URLs to check.

## Usage
To use the program, follow these steps:

1. Clone the repository to your local machine using the following command:
    ```
    git clone https://github.com/<your-username>/website-status-checker.git
    ```
2. Navigate to the directory where the script is located.
3. Run the script using the following command:
    ```
    python checkstatus.py
    ```
4. The program will check the status of each URL and send an email with the results.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue or create a pull request.

## Contact
If you have any questions or comments about this project, you can contact me at <your-email-address>.

