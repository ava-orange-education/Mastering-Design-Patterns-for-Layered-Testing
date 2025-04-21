# Arrange
user = User("john_doe", "password123")
database = MockDatabase()
database.add_user(user)

# Act
result = database.authenticate_user("john_doe", "password123")

# Assert
assert result == True