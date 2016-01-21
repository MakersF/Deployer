#Deployer
Deployer is a minimal flask app to the allow to execute commands when POST requests are received.
It was developed to allow to be notified with web hooks from the GitHub o BitBucket (or any hosting service which supports them).

###Setup
Open a shell and type
```
mkdir /path/to/deployer
cd /path/to/deployer
git clone https://Makers_F@bitbucket.org/Makers_F/deployer.git
mkvirtualenv deployer
workon deployer
pip install -r requirements.txt
deactivate
```
 
Then create `/etc/init/deployer.conf`

```
description "Deployer (web hook server)"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid user
setgid www-data

env ADDRESS = "0.0.0.0"
env PORT = 8000
env PUSH_COMMAND = "argument to be passed to /bin/bash. Either a script location or -c 'your bash command'"
script
    cd /path/to/deployer
    . myprojectenv/bin/activate
    gunicorn -w 1 --bind $ADDRESS:$PORT wsgi:app
end script
```

Then type in the shell `start deployer`

###Web hooks

Go to your Hosting Service website and set a git hook to `$ADDRESS:$PORT/on-push`.
`PUSH_COMMAND` will be executed every time a push is issued to your repository
