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
> It is up to you as to whether you want to run the server on the local network or not, if not remove the 'host' argument from app.run() in app.py<br>
> Same applies for the 'debug' option, having it on allows for verbose error handling, and live reloading but does not directly affect the site itself, it is your choice as to whether or not to include it

# Hints + Solutions
## Challenge 1
The first challenge is simple <strong>parameter tampling</strong> (Same as LoginChallenge2022). When the user attempts to login, if the login is unsuccessful, the parameter ```loginSuccessful=False``` is set in the url.<br>
Modifying this to 'True' (case insensitive) allows the user to move onto the next stage of the challenge.<br>
Hints:

- Observe the URL after a failed login attempt — what changes?
- Pay close attention to how parameters in the URL are used by the server.
- URL parameters can often be manipulated directly in the browser's address bar — try experimenting there.
- Not all applications verify the integrity of client-side parameters. Sometimes, trust is assumed.

> Note: should there is only one correct login on the server side - the admin - whose details are <br>
Username: admin<br>
Password: admin<br>
> If the user correctly guesses these credentials on their first try, they will <i>technically</i> bypass the next two challenges but this is a good reminder of how weak/default credentials can compromise an entire application, regardless of other security mechanisms in place.

## Challenge 2
Upon successful login, the user will be redirect to a random users profile page.
> Note: in Challenge 1 there is an extra parameter ```userId``` which is set to 1 by default. If the user modifies this (which they do not and are not expected to do) they will be redirect to this profile instead upon successful login.

The data on each page is randomly generated at page load time, but stays consistent based on ```userId```.<br>
The challenge here is to realise that this site has <strong>broken access control</strong> (Note the 'logout' button on every page), and the user should navigate to /users/0 to find the admin page.<br>

Hints:

- The url has an id after /users/ - could this indicate how the site displays profiles?
- What happens if you try changing id
- Isn't it strange that you have a 'logout' button on each page, even if you didn't originally log-in as them?
- If a site has an admin account, where do you think it would appear in an incrementing ID system?

## Challenge 3
Once the user successfully 'accesses' the admin account, they should see a big blue button labelled 'Admin Console'. Upon clicking this button, they will be taken to the Admin Console page, but an error message about missing permission will be displayed (because they have not actually logged in as admin and thus are missing the permission).<br>
The users goal is to realise that there is a cookie set in the browser `is_admin` which is set to `false` by default. Modifying this to `true` and then refreshing the page, will display the protected user data of the site, as well as a congratulations message!<br>
> Note: If the user successfully logged in as the admin in Challenge 1, they will have the `is_admin` flag set to `true`, and thus will immediately see the congratulations message

Hints:

- You need to find a way to change your permissions - how could the site be doing this?
- Browsers store cookies for each site - perhaps you could have a look?
- What happens if you modify the is_admin cookie?
- After changing a cookie, make sure to refresh the page so the new value takes effect
