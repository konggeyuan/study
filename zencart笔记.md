# zencart笔记
<!-- create time: 2014-05-19 02:41:11  -->

-----------
###首页模板调用书序
-----
1. common =>主要模板目录

2. tpl_main_page.php 主模板页面

3. tp_main_page => $body_code => 调用 includes/modules/pages/index/main_template_vars.php 

4. 调用首页产品显示模板

5. 显示模板/templates/tpl_index_product_list.php

###zencart节奏

1. Application_top.php文件中将进行许多常量的定义, 加载配置文件等工作

2. 定义了一个变量$language_page_directory

3. 加载includes/templates/common/html_header.php     //当前页面顶部头文件

4. 如果无$_GET['main_page']参数,则加载includes/templates/template_print/common/main_template_vars.php

------------
###数据库操作
-------------

* 循环读取数据库数据
<pre><code>


$categories_query = "select * from ". TABLE_PRODUCTS;

$categories = $db->Execute($categories_query);

$categories->RecordCount(); //查看记录数

while(!$categories->EOF) {
    var_dump($categories->fields['products_id']);
    $categories->MoveNext();
}

</code></pre>

* 防sql注入
<pre><code>
$sql = "select products_model from " . TABLE_PRODUCTS . " where products_id = :productID:";
$sql = $db->bindVars($sql, ':productID:', $theProductId, 'integer');
</code></pre>

* 数据库数据插入

<pre><code>
global $db; //全局变量
$sql = "insert into " . TABLE_SOMETHING . " (fieldname1, fieldname2) values (:value1:, :value2:)";
$sql = $db->bindVars($sql, ':value1:', $valueOne, 'integer');
$sql = $db->bindVars($sql, ':value2:', $valueTwo, 'string');
$result = $db->Execute($sql);
$newRecordId = $db->Insert_ID();  
echo 'The new record added was number: ' . $newRecordId;

</code></pre>
