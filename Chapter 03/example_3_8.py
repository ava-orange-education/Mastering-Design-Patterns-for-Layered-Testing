class DatabaseStub:
    def get_data(self):
        return {"id": 1, "name": "Test Item"}

def process_data():
    db = DatabaseStub()
    data = db.get_data()
    return f"Processed {data['name']}"
    
def test_process_data():
    result = process_data()
    assert result == "Processed Test Item"

from unittest.mock import Mock

def notify_user(email_system, user_email):
    message = "You have a new notification"
    email_system.send_email(user_email, message)

def test_notify_user():
    email_system_mock = Mock()
    
    notify_user(email_system_mock, "user@example.com")
    
    email_system_mock.send_email.assert_called_once_with("user@example.com", "You have a new notification")

