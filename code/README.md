TicketBuddy is a ticket booking web app that is designed for booking tickets. It allows users to book tickets for various movies across different venues. There are two roles: user and admin. Regular users can sign up, log in, search for movies and book tickets, while the admin has additional privileges such as managing venues and movies.

Steps to run:
1. Create a virtual environment
2. pip install -r requirements.txt
3. Activate virtual environment inside the folder where it has downloaded
4. Execute backend from the app folder in a ubuntu WSL terminal-
    source setup.sh
    python main.py
5. To install node_modules do "npm install" inside the terminal of the frontend folder
6. Execute npm run serve, to run the frontend inside the frontend folder
7. Run mailhog in ubuntu terminal outside VS code to show that the mails are being sent, execute Mailhog
8. Have Redis-Celery ready
9. Have the virtual environment ready for celery
10. In a wsl terminal activate the virtual environment for celery, then activate celery:
    source setup.sh
    bash worker.sh
11. Comment lines 30 and 35, and uncomment lines 31 and 36 in task.py to show that messages are actually being sent
12. See the mails being sent in chrome, open = localhost:8025
