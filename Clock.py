import time

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        name  = func.__name__
        args_lst = []
        if args:
            args_lst.append(', '.join([repr(arg) for arg in args]))
        if kwargs:
            args_lst.append(['%s=%s' % (key, value) for key, value in sorted(kwargs.items())])
        args_str = ', '.join(args_lst)
        print('<%s(%s) Performance time : %0.8f>' %(name, args_str, time.perf_counter() -t0))
        return result
    return clocked