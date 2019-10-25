
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling base class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling left class")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling right class")
        self.num_right_calls += 1


class Subclass(RightSubclass, LeftSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling sub class")
        self.num_sub_calls += 1

        
if __name__ == "__main__":

    s = Subclass()
    s.call_me()