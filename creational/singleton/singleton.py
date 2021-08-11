import random as random


class Database:
    _instance = None

    def __init__(self):
        '''
        Despite the instance being created only once,
        the init method is called twice.
        The initializers still get called twice.
        This is not what we want
        '''
        print(f'id = {random.randint(1, 101)}')

    @classmethod
    def __new__(cls, *args, **kwargs):
        '''
        This method ensures that if the
        cls._instance already exists then just return it.
        This means no duplication.
        '''
        if not cls._instance:
            cls._instance = super(
                Database, cls
            ).__new__(*args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
