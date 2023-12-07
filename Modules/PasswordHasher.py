from argon2 import PasswordHasher # pip install argon2-cffi

class HashingDemo(object):
    def __init__(self, password, comparer):
        self.password = password
        self.comparer = comparer
        self.hasher = PasswordHasher()
        self.hashed_password = self.hasher.hash(password)
    
    def hash_password(self, password):
        return self.hasher.hash(password)
    
    def verify_password(self, hashed_pass, password):
        try:
            if self.hasher.verify(hashed_pass, password):
                return True
        except:
            return False
        
    def __repr__(self):
        return str(self.verify_password(self.hashed_password, self.comparer))

if __name__ == "__main__":
    pass_0 = "P4ssw0rd"
    pass_1 = "12345678"
    check_against = "P4ssw0rd"
    true_ins = HashingDemo(pass_0, check_against)
    false_ins = HashingDemo(pass_1, check_against)
    true_hash = true_ins.hashed_password.split(',p=')[-1]
    false_hash = false_ins.hashed_password.split(',p=')[-1]
    print(f"Instance_0: Password = {pass_0} | Hash = {true_hash} | {pass_0} = {check_against} == {true_ins}")
    print(f"Instance_1: Password = {pass_1} | Hash = {false_hash} | {pass_1} = {check_against} == {false_ins}")
    

