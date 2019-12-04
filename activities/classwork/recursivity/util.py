import functools
import time

def caching(func):
    CACHE = {}
    @functools.wraps(func)
    def wrapper(self, **kwargs):
        key = hash(frozenset(kwargs.items()))
        if key in CACHE:
            return CACHE[key]
        CACHE[key] = func(self, **kwargs)
        return wrapper(self, **kwargs)
    return wrapper

def _corner_case_decorator(func):
    def wrapper(self,i,j,*args,**kwargs):
        if j>=i or j==0:
            return 1
        return func(self, i=i, j=j, *args, **kwargs)
    return wrapper

#Metadecoradores
def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            start = time.time()
            output = func(self, *args, **kwargs)
            end = time.time()
            logger.info("Start time %s End time %s" % (start, end))
            logger.info("Execution time %s" % (end - start))
            return output
        return wrapper
    return decorator


#Un decorador te permite modificar el comportamiento de una función
#Funciones de alto orden, recibe una función y saca otra
def _corner_case_decorator(func):
    def wrapper(self,i,j, *args, **kwargs):
        if j>=i or j ==0:
            return 1
        return func(self,i=i, j=j, *args, **kwargs)
    return wrapper

class TriangleBuilder(object):
    CACHE = {}

    def save(self, i, j, value):
        self.CACHE[(i,j)] = lambda: value
        return value

    @_corner_case_decorator
    def get(self, i, j, default=lambda:None):
        return self.CACHE.get((i,j),default)() #Para que lo saque como resultado en el método get y no en el lambda y lo evalúe,
    #y como la función no está en el lambda, no hay argumentos, plt ()

    @_corner_case_decorator
    def create(self, i, j):
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1,j=j)
        return self.save(i=i, j=j, value=upper_left+upper_center)


    def get_or_create(self, i, j):
        return self.get(i,j, default=lambda: self.create(i=i, j=j))

    def get_row(self, index):
        return [str(self.get_or_create(index,j)) for j in range(index+1)]
