###主要含义：所有的函数可以方便的加上一段和该类函数有关但不用每次都添加的方法

<pre><code>

def test(level):
    def log(func):
        def wrapper(*args):
            print 'cccc'
            return func(*args)
        return wrapper
    return log 

@test(level='yyy')
def aa(ee=2222):
    print 1111
aa()
</code></pre>


