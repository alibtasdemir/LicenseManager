class Client():
    def __init__(self, username, serialNumber, mac):
        self.serverUrl = "http://localhost:5000"
        self.publickeyPath = "public.pem"
        self.licensePath = "license.txt"
        self.username = username
        self.serialNumber = serialNumber
        self.MAC = mac
        self.signature = self.create_signature()

    def create_signature(self):
        return "{}${}${}".format(self.username, self.serialNumber, self.MAC)

    ####################################
    #       INSERT YOUR CODE HERE      #
    ####################################


if __name__ == "__main__":
    username = # _____
    serialNumber = # _____
    MAC = get_mac_address()
    client = Client(username, serialNumber, MAC)
    client.run()
