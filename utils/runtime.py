from time import perf_counter


def get_runtime(method):
    def inner_runtime(*args, **kwargs):
        start = perf_counter()
        result = method(*args, **kwargs)

        print(f'"{method.__name__}" took {perf_counter() - start:2.5f} seconds')

        return result

    return inner_runtime
