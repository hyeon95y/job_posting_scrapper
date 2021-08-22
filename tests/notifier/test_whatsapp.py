from notifier.whatsapp import WhatsAppNotifier
import pytest
from datetime import datetime

@pytest.fixture(scope='function')
def whatsapp_notifier():
    return WhatsAppNotifier()

def test_send_message(whatsapp_notifier):
    result = whatsapp_notifier.send_message(f'test message via pytest at {datetime.now()}')
    assert result