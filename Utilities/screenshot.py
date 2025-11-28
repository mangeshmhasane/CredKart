from datetime import datetime
@staticmethod
def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")