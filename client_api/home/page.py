from assertions import HomeAssertions
from home_labels import HomeLabels

class HomePage:
    
    def __init__(self):
        self.home_assertions = HomeAssertions()
        self.home_labels = HomeLabels()

    def go_to_home(self):
        pass

    def enter_username(self, username):
        pass

    def enter_password(self, pwd):
        pass
