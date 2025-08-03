# LoginChallenge2025
Mini CTF challenge for the September 2025 Activity Fair - A modified version of [LoginChallenge2022](https://github.com/ShefESH/LoginChallenge2022)

> Note - This was written and tested on Windows 10, as such I cannot ensure that it will function correctly on other OS
## Install + Setup

### Using venv

In the root directory run
``` sh
python -m venv venv
```
> Or python3 depending on your OS

Then activate the virtual environment

Windows:
``` sh
.\venv\Scripts\activate  
```

MacOS / Linux:
``` sh
source .\venv\bin\activate
```

### Install required packages
After initialising your venv, your terminal window should now have ```(venv)``` at the start of each command (if not, see above)
Now run this command from the root of the project
``` sh
pip install -r .\requirements.txt
```

### Starting the webserver
Once all the packages are installed run:
``` sh
python .\web\app.py
```

You should then see a message like this in the terminal:
```sh
(venv) PS C:\Projects\LoginChallenge2025> python .\web\app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:2346
 * Running on http://<Network IP>:2346
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 140-122-765
```
> It is up to you as to whether you want to run the server on the local network or not, if not remove the 'host' from app.run() in app.py