from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -bn1 | head -20")

    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time: {server_time}
    
    Top Output:
    {top_output}
    </pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
