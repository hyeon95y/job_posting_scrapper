import urllib.request
from notifier._config_whatsapp import PHONE_NUMBER, API_KEY

class WhatsAppNotifier:
    def __init__(self) :
        self._PHONE_NUMBER = PHONE_NUMBER
        self._API_KEY = API_KEY

    def send_message(self, message:str) -> bool : 
        """Send message to whatsapp messenger

        Args:
            message (str): message to send

        Returns:
            bool: result
        """
        message = message.replace(' ', '+')

        url = f'https://api.callmebot.com/whatsapp.php?phone={self._PHONE_NUMBER}&text={message}&apikey={self._API_KEY}'

        try : 
            with urllib.request.urlopen(url) :
                success = True
        except : 
            success= False

        # TODO : Determine how to handle the given error
        assert success 

        return success

