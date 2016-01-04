from flask import Flask
import subprocess as sp
import os
app = Flask(__name__)

@app.route("/on-push", methods=['POST'])
def on_push():
    command = os.environ.get('PUSH_COMMAND', False)
    if command:
        try:
            sp.Popen(command, shell=True, executable='/bin/bash')
            return ''
        except:
            return ('An exception occurred while handling the request', 503)
    return ('', 204)

if __name__ == "__main__":
    app.run()
