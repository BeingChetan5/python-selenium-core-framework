from core_api.api_helper import CoreApi


class HomeAssertions:

    def __init__(self):
        self.core_api = CoreApi()
    
    def verify_home_screen(self):
        text = self.core_api.get_element_by_id(id)
