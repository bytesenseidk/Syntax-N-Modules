from argon2 import PasswordHasher

class HashingDemo(object):
    def __init__(self):
        self.hasher = PasswordHasher()
        self.hashed_password_0 = self.hasher.hash("password") # Both passwords are the same
        self.hashed_password_1 = self.hasher.hash("password") # Yet hashed to different values
        self.match_0 = self.hasher.verify(self.hashed_password_0, "password")
        try:
            # This will raise an exception instead of returning False
            self.match_1 = self.hasher.verify(self.hashed_password_1, "wrong")
        except:
            self.match_1 = False
        
    def __str__(self):
        results = ''
        results += f"1'st Hashed Password: {self.hashed_password_0}\n"
        results += f"2'nd Hashed Password: {self.hashed_password_1}\n"
        results += f"Does 'password' Match {self.hashed_password_0}: {self.match_0}\n"
        results += f"Does 'wrong' Match {self.hashed_password_1}: {self.match_1}"
        return results

if __name__ == "__main__":
    print(HashingDemo())
    
