from flask import Flask

privKeyPath = "private.pem"  # Private Key
publicKeyPath = "public.pem"  # Public Key

app = Flask(__name__)


@app.route("/")
def running():
    return "<p>Server is running</p>"

####################################
#       INSERT YOUR CODE HERE      #
####################################


if __name__ == "__main__":
    # DO NOT CHANGE BELOW
    app.run(host='0.0.0.0', port=5000, debug=True)
