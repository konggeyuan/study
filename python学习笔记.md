###主要含义：所有的函数可以方便的加上一段和该类函数有关但不用每次都添加的方法

```
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
```

<pre><code>


$categories_query = "select * from ". TABLE_PRODUCTS;

$categories = $db->Execute($categories_query);

$categories->RecordCount(); //查看记录数

while(!$categories->EOF) {
    var_dump($categories->fields['products_id']);
    $categories->MoveNext();
}

</code></pre>
