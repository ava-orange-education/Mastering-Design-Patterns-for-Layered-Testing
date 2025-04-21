class TestUserAuthentication:
    
    def test_login_with_valid_credentials_returns_true(self):
        # Arrange
        user = User("john_doe", "password123")
        database = MockDatabase()
        database.add_user(user)
        
        # Act
        result = database.authenticate_user("john_doe", "password123")
        
        # Assert
        assert result == True
    
    def test_login_with_invalid_credentials_returns_false(self):
        # Arrange
        user = User("john_doe", "password123")
        database = MockDatabase()
        database.add_user(user)
        
        # Act
        result = database.authenticate_user("john_doe", "wrong_password")
        
        # Assert
        assert result == False