class DisasterNotFound(Exception):

    def __init__(
        self,
        message="Disaster not found"
    ):

        self.message = message