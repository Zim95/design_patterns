import random as random


'''
One way of solving the issue of initializers getting called twice,
is to create a singleton decorator.
'''
def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    '''
    By creating the decorator we no longer need the new method.
    '''

    _instance = None

    def __init__(self):
        '''
        Despite the instance being created only once,
        the init method is called twice.
        The initializers still get called twice.
        This is not what we want
        '''
        print(f'id = {random.randint(1, 101)}')


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
