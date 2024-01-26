from appJar import gui


class SignUpApp:
    def __init__(self):
        self.app = gui("Sign Up Window", "400x200")

    def run(self):
        self.app.addLabel("title", "Sign Up")
        self.app.setLabelBg("title", "blue")
        self.app.setLabelFg("title", "white")

        self.app.addLabelEntry("Username")
        self.app.addLabelSecretEntry("Password")

        self.app.addButton("Submit", self.submitCredentials)
        self.app.go()

    def submitCredentials(self):
        username = self.app.getEntry("Username")
        password = self.app.getEntry("Password")


app = SignUpApp()
app.run()
