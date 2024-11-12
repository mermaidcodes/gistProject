1. Setup
Manual Setup
1. Clone this repository

2. Local setup dependencies
Google Chrome Driver 80+

PIP
Python 3

python --version
If the result of following command contains Python 2.X.X, please remove Python2 beforehand and install Python 3.
3. Install Robot and its dependencies locally
pip install -r requirements.txt
pip install --upgrade robotframework
4. Install the Google Chrome Driver locally

5. Fill .env.local file
Check if .env.local exists there.
This file contains tokens and credentials.

 Run tests
 robot -v CONFIG_FILE:"/path/to/gistProject/resources/configs/gistvariables.robot" ./tests/getGist.robot
