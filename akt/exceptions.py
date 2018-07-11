
class AKTError(Exception):
    pass

class InvalidArgumentError(AKTError):
    """Raised when an argument is invalid.
    """
    def __init__(self, message):
        self.message = message
