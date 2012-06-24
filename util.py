import objc
import inspect

# Replacement wrapper lambdas depending on the number of parameters required.  Support up to 8
# parameters, including self.  This is necessary to suppress a PyObjC DeprecationWarning about
# Not all Objective-C arguments being present in the Python argument list (collapsed as *args).
__swizzleIMPMap = {0: lambda f: lambda: f(),
                   1: lambda f: lambda self: f(self),
                   2: lambda f: lambda self, a: f(self, a),
                   3: lambda f: lambda self, a, b: f(self, a, b),
                   4: lambda f: lambda self, a, b, c: f(self, a, b, c),
                   5: lambda f: lambda self, a, b, c, d: f(self, a, b, c, d),
                   6: lambda f: lambda self, a, b, c, d, e: f(self, a, b, c, d, e),
                   7: lambda f: lambda self, a, b, c, d, e, g: f(self, a, b, c, d, e, g),
                   8: lambda f: lambda self, a, b, c, d, e, g, h: f(self, a, b, c, d, e, g, h),
                  }
                  
def swizzle(old):
    def swizzleWithNewMethod_(f):
        cls = old.definingClass
        oldSelectorName = old.__name__.replace("_", ":")
        oldIMP = cls.instanceMethodForSelector_(oldSelectorName)
        newSelectorName = f.__name__.replace("_", ":")
        
        argc = len(inspect.getargspec(f)[0])
        newSEL = objc.selector(f, selector=newSelectorName, signature=old.signature)
        oldSEL = objc.selector(__swizzleIMPMap[argc](oldIMP), selector=newSelectorName, signature=old.signature)
    
        # Swap the two methods
        objc.classAddMethod(cls, newSelectorName, oldSEL)
        objc.classAddMethod(cls, oldSelectorName, newSEL)
        
        return f
    
    return swizzleWithNewMethod_
