def debug(function):
    def _debug(**args, **kwargs):
        result = function(**args, **kwargs)
        print(function, __name__, )