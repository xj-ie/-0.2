

# -0.2

美多商城后台



#### 1、项目环境的配置

​	![image-20200826085703466](image/image-20200826085703466.png)



```mermaid
graph LR
all_projects[美多后台]-->login((登录))-->login_portl(接口分析)
login_portl-->login_1[请求方式]-->logins_1(POST)
login_portl-->login_2[请求参数]-->logins_2("username,password{josn}")
login_portl-->login_3[请求地址]-->logins_3(meiduo_adim/authorizations/)
login_portl-->login_4[返回结果]-->logins_4(Username,token,id)
login-->login_str(业务逻辑)
all_projects-->linst(商品管理)-->image_table[图片表管理 ModelViewSet]-->add_data((增加))-->add_port[接口分析]-->add_show(显示选择接口)
add_show-->as_1[请求方式]-->al1(GET)
add_show-->as_2[请求参数]-->al2(token身分证明)
add_show-->as_3[请求地址]-->al3(/meiduo_admin/skus/simplie/)
add_show-->as_4[返回结果]-->al4(SKU_id,SKU)
add_port-->add_commit(增加接口)
add_commit-->ad_1[请求方式]-->a1(POST)
add_commit-->ad_2[请求参数]-->a2(token身分证明,sku,image)
add_commit-->ad_3[请求地址]-->a3(/meiduo_admin/skus/images/)
add_commit-->ad_4[返回结果]-->a4(id,image,sku)
image_table-->change_data((修改))-->change_port(接口分析)
image_table-->delere_data((删除))
image_table-->show_data((展显))-->show_port(接口分析)
change_port-->cs_1[请求方式]-->c1(PUT)
change_port-->cs_2[请求参数]-->c2(token身分证明,id,image)
change_port-->cs_3[请求地址]-->c3(/meiduo_admin/skus/simplie/)
change_port-->cs_4[返回结果]-->c4(id,name,image_url)
show_port-->ss_1[请求方式]-->s1(GET)
show_port-->ss_2[请求参数]-->s2(token身分证明)
show_port-->ss_3[请求地址]-->s3(/meiduo_admin/skus/simplie/)
show_port-->ss_4[返回结果]-->s4(count,id,lilens,page,pages,pagesize)
```



### 1、业务说明

​	验证用户名和密码成功后，为用户签发JWT,前端将签发JWT保存下来。

### 2、后端接口设计 

```mermaid
graph LR
login_portl(接口分析)
login_portl-->login_1[请求方式]-->logins_1(POST)
login_portl-->login_2[请求参数]-->logins_2("username,password{josn}")
login_portl-->login_3[请求地址]-->logins_3(meiduo_adim/authorizations/)
login_portl-->login_4[返回结果]-->logins_4(Username,token,id)
```



​	**请求方式**：POST  meiduo_admin/authorizations/

​	**请求参数**：JSON 或者 表单

|  参数名  | 类型 | 是否必须 |  说明  |
| :------: | :--: | :------: | :----: |
| useranme | str  |    是    | 用户名 |
| password | str  |    是    |  密码  |

**返回**：JSON

​	{

​		"useranme":"##",

​		"user_id": ##,

​		"token":"##"

​	}

|  返回值  | 类型 | 是否必须 |    说明    |
| :------: | :--: | :------: | :--------: |
| useranme | str  |    是    |   用户名   |
|    id    | int  |    是    |   用户id   |
|  token   | str  |    是    | 身份证凭证 |



![image-20200827194456131](image/image-20200827194456131.png)



### 1、业务说明

​	通过rest_frame中的GenteAPIView视图类完成

```

```

统计功能 

### 2、后端接口设计



​	**请求方式**：GET

​	**请求参数**：JSON

| 参数名 | 是否必传 | 类型 |   说明   |
| :----: | :------: | :--: | :------: |
| token  |    是    | str  | 身份凭证 |



​	**返回参数**

{

"user_count": count,

"datetime":time

}

|  返回参数  |   类型   | 是否必传 |   说明    |
| :--------: | :------: | :------: | :-------: |
| user_count |   int    |    是    | 统计个数  |
|  datatime  | datatime |    是    | 统计 时间 |

![image-20200827215021925](image/image-20200827215021925.png)

## 日增用户接口定义

### 1、接口分析

​	**请求方式**：GET /meiduo_admin/statistical/day_increment/

​	**请求参数**： 请求传递token(身份验证参数)

​	**返回参数**：JSON

{

'date'：new_user_date,

"count": day_create_count

}

|  返回参数  |   类型   | 是否必传 |       说明       |
| :--------: | :------: | :------: | :--------------: |
|    date    | datetime |    是    |     今日时间     |
| user_count |   int    |    是    | 今日用户创建个数 |

## 日活用户接口定义

### 1、后端接口设计

​		**请求方式**：GET /meiduo_admin/statistical/day_activate

​		**请求参数**：JWT token（头部传递）

| 请求参数 | 类型 | 是否必传 | 携带部位 |   说明   |
| :------: | :--: | :------: | :------: | :------: |
|  token   | str  |    是    | 请求头部 | 身体验证 |

**返回参数：**

{

"conut"：day_activate_count,

"date": date_day

}

| 返回参数 | 类型 | 是否必需 |      说明      |
| :------: | :--: | :------: | :------------: |
|  count   | int  |    是    | 日活用户总个数 |
|   date   | date |    是    |    当天日期    |

## 下单用户接口

![image-20200828093010828](image/image-20200828093010828.png)

### 1、接口分析

​	**请求方式**：GET

​	**请求参数**：JWT token



| 请求参数 | 类型 | 是否必传 | 携带部位 |   说明   |
| :------: | :--: | :------: | :------: | :------: |
|  token   | str  |    是    | 请求头部 | 身体验证 |

**返回参数：**

{

"conut"：day_activate_count,

"date": date_day

}

| 返回参数 | 类型 | 是否必需 |      说明      |
| :------: | :--: | :------: | :------------: |
|  count   | int  |    是    | 下单用户的个数 |
|   date   | date |    是    |  当天日期下单  |

------



## 月增用户接口

![image-20200828103012608](image/image-20200828103012608.png)

### 1、接口设计

​	**请求方式**：get /meiduo_admin/statistical/month_increment/

​	**请求参数**：JWT token

| 请求参数 | 类型 | 是否必传 | 携带部位 |   说明   |
| :------: | :--: | :------: | :------: | :------: |
|  token   | str  |    是    | 请求头部 | 身体验证 |

​	**返回结果**：JSON

[

{"count": day_createuser，“date”：day_date},

{"count": day_createuser，“date”：day_date},

......（共三十天）

]

| 返回值 | 类型 | 是否必传 |    说明    |
| :----: | :--: | :------: | :--------: |
| count  | int  |    是    | 日增用户数 |
|  date  | date |    是    |  当天时间  |

## 日分类访问类

![image-20200828152617543](image/image-20200828152617543.png)

### 接口分析

​	**请求方式**：GET /meiduo_admin/statistical/goods_day_views/

​	**请求参数**：token

| 请求参数 | 类型 | 是否必传 | 携带部位 |   说明   |
| :------: | :--: | :------: | :------: | :------: |
|  token   | str  |    是    | 请求头部 | 身体验证 |

​	 **返回参数**：JSON

```json
 [
        {
            "category": "分类名称",
            "count": "访问量"
        },
        {
            "category": "分类名称",
            "count": "访问量"
        },
        ...
    ]
```

| 返回参数 | 类型 | 是否必需 |   说明   |
| :------: | :--: | :------: | :------: |
| category | str  |    是    |  分类名  |
|  count   | int  |    是    | 日访问量 |

## 用户管理

### ![image-20200828170020363](image/image-20200828170020363.png)

### 用户查询分析

​	**请求方式**：GET /meiduo_admin/users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>

​	**请求参数**：JWF token，Keywork，page，pagesize

|   参数   | 类型 | 是否必传 | 携带部位 |    说明    |
| :------: | :--: | :------: | :------: | :--------: |
|  token   | srt  |    是    |  请求头  |  身份验证  |
| Keywork  | srt  |    否    |  请求行  |   关键词   |
|   page   | int  |    否    |  请求行  |   第几页   |
| pagesize | int  |    否    |  请求和  | 每页最大数 |

​	**返回参数**：JOSN

```JSON
{
    "count": username.count().
    "lines":[
        {
        "id":user.id,
        "username":user.name,
        "phone":user.phone,
        "email":user.email,
        },
        {
        "id":user.id,
        "username":user.name,
        "phone":user.phone,
        "email":user.email,
        }
        .....
    ],
	"page":page,
	"pages":page.count(),
	"pagesize":pagesize,
}
```

| 返回参数 | 类型 | 是否必需 |    说明    |
| :------: | :--: | :------: | :--------: |
|  count   | int  |    是    | 用户总个数 |
|  lines   | list |    是    |  用户说明  |
|   page   | int  |    是    |    行页    |
|  pages   | int  |    是    |  最大行页  |
| pagesize | int  |    是    |   页容量   |

### 业务分析

​	**1**、**获取传入数据**

​		通过keywork是否存在，判断单一用户查询还是多个用户查询。

​	**2、单一用户查询**

​		通过keywork来查询数据，并构建JSON返回结果。

​	**3、多个用户查询**

​		未有keywork传入，直接查询所以数据 ，并构建JSON返回结果。

### 新增用户接口分析

![image-20200829072023614](image/image-20200829072023614.png)

**请求方式**：POST  /meiduo_admin/users/

**请求参数**：username，password，email, mobile, token

|   参数   | 类型 | 是否必传 |     携带部位      |   说明   |
| :------: | :--: | :------: | :---------------: | :------: |
| username | str  |    是    |  请求体（body）   |  用户名  |
| password | str  |    是    |  请求体（body）   |  密码em  |
|  email   | str  |    是    |  请求体（body）   |   邮箱   |
|  mobile  | str  |    是    |  请求体（body）   |  手机号  |
|  token   | str  |    是    | 请求头（headres） | 身份验证 |

**返回数据**：JSON

```json
{
id:"userid"
username:"username",
email:"email",
mobile:"mobile",
}
```

| 返回参数 | 类型 | 是否必需 |  说明  |
| :------: | :--: | :------: | :----: |
| username | str  |    是    | 用户名 |
|    id    | int  |    是    | 用户id |
|  email   | str  |    是    |  邮箱  |
|  mobile  | str  |    是    | 手机号 |

### 业务分析

​	**1、获取前端数据 **

​	**2、验证数据**

​		定义序列化器来验证

​	**3、保存数据**

​		通过序列器来保存

​	**4、返回数据** 

​		通过序列化器返回

## 商品管理

### 规格表管理

#### 	增加商品接口分析

![image-20200829173207299](image/image-20200829173207299.png)

**请求方式：**POST /meiduo_admin/goods/specs/

**请求参数**： name、spu_id、jwt token

|  参数  | 类型 | 是否必传 |     携带部位      |   说明    |
| :----: | :--: | :------: | :---------------: | :-------: |
|  name  | str  |    是    |  body（请求体）   |  规范名   |
| spu_id | int  |    是    |  body（请求体）   | SPU商品id |
| token  | str  |    是    | headres（请求头） | 身份验证  |

**返回参数**：

```json
{
        "id": "规格id",
        "name": "规格名称",
        "spu": "SPU商品名称",
        "spu_id": "SPU商品id"
    }
```

| 参数   | 类型 | 是否必须 | 说明        |
| ------ | ---- | -------- | ----------- |
| id     | Int  | 是       | 规格id      |
| name   | Str  | 是       | 规格名称    |
| spu    | str  | 是       | SPU商品名称 |
| spu_id | Int  | 是       | spu商品id   |

#### 	修改商品接口分析

#### 	修改商品接口分析 

#### 	**查询商品接口分析**

​		![image-20200829164339469](image/image-20200829164339469.png)

​		**请求方式**：GET /meiduo_admin/goods/specs/

​		**请求参数**： token

| 参数  | 类型 | 是否必传 | 携带部位 |   说明   |
| :---: | :--: | :------: | :------: | :------: |
| token | str  |    是    |  请求头  | 身份验证 |

​	  **返回参数**

​		

```JSON
{
    "pages": 2,
    "count": 8,
    "page": 1,
    "lines": [
        {
            "id": 2,
            "spu": "Apple MacBook Pro 笔记本222222222222",
            "spu_id": 1,
            "create_time": "2018-04-11T17:21:57.862419Z",
            "update_time": "2018-04-11T17:21:57.862464Z",
            "name": "颜色"
        },
        {
            "id": 3,
            "spu": "Apple MacBook Pro 笔记本222222222222",
            "spu_id": 1,
            "create_time": "2018-04-11T17:22:04.687913Z",
            "update_time": "2018-04-11T17:22:04.687956Z",
            "name": "版本"
        },
    ],
    "pagesize": 10
}
```

| 返回参数 | 类型 | 是否必需 |    说明    |
| :------: | :--: | :------: | :--------: |
|  count   | int  |    是    |   总个数   |
|  lines   | list |    是    | 规格表数据 |
|  pages   | int  |    是    |   总页数   |
|   page   | int  |    是    |    页码    |
| pagesize | int  |    是    |   页容量   |

------



### 图片表管理





```mermaid

graph LR
image_table[图片表管理 ModelViewSet]-->add_data((增加))-->add_port[接口分析]-->add_show(显示选择接口)
add_show-->as_1[请求方式]-->al1(GET)
add_show-->as_2[请求参数]-->al2(token身分证明)
add_show-->as_3[请求地址]-->al3(/meiduo_admin/skus/simplie/)
add_show-->as_4[返回结果]-->al4(SKU_id,SKU)
add_port-->add_commit(增加接口)
add_commit-->ad_1[请求方式]-->a1(POST)
add_commit-->ad_2[请求参数]-->a2(token身分证明,sku,image)
add_commit-->ad_3[请求地址]-->a3(/meiduo_admin/skus/images/)
add_commit-->ad_4[返回结果]-->a4(id,image,sku)
image_table-->change_data((修改))-->change_port(接口分析)
image_table-->delere_data((删除))
image_table-->show_data((展显))-->show_port(接口分析)
change_port-->cs_1[请求方式]-->c1(PUT)
change_port-->cs_2[请求参数]-->c2(token身分证明,id,image)
change_port-->cs_3[请求地址]-->c3(/meiduo_admin/skus/simplie/)
change_port-->cs_4[返回结果]-->c4(id,name,image_url)
show_port-->ss_1[请求方式]-->s1(GET)
show_port-->ss_2[请求参数]-->s2(token身分证明)
show_port-->ss_3[请求地址]-->s3(/meiduo_admin/skus/simplie/)
show_port-->ss_4[返回结果]-->s4(count,id,lilens,page,pages,pagesize)


```

### 查询-接口分析

```mermaid

graph LR
show_port(接口分析)
show_port-->ss_1[请求方式]-->GET
show_port-->ss_2[请求参数]-->token身分证明
show_port-->ss_3[请求地址]-->/meiduo_admin/skus/simplie/
show_port-->ss_4[返回结果]-->count,id,lilens,page,pages,pagesize



```

**请求方式**：GET  /meiduo_admin/skus/simplie/

**请求参数**：token

**返回参数**：JSON

```
{
count：图片个数，
lilens：[data]，
page：页码，
pages：总页数，
pagesize：页容量，
}
```

| 返回参数 | 类型 | 是否必需 |  说明  |
| :------: | :--: | :------: | :----: |
|  count   | int  |    是    |  个数  |
|  lilens  | 数组 |    是    |  数据  |
|   page   | int  |    是    |  页码  |
| pagesize | int  |    是    | 页容量 |
|  pages   | int  |    是    |  页数  |



### 增加-接口分析 

```mermaid

graph LR
add_port[接口分析]-->add_show(显示选择接口)
add_show-->as_1[请求方式]-->GET
add_show-->as_2[请求参数]-->token身分证明
add_show-->as_3[请求地址]-->/meiduo_admin/skus/simplie/
add_show-->as_4[返回结果]-->SKU_id,SKU
add_port[接口分析]-->add_commit(增加接口)
add_commit-->ad_1[请求方式]-->POST
add_commit-->ad_2[请求参数]-->token身分证明,sku,image
add_commit-->ad_3[请求地址]-->/meiduo_admin/skus/images/
add_commit-->ad_4[返回结果]-->id,image,sku

```

#### 显示选择接口

​	**请求方式**：GET

​	**请求参数**：token

| 参数  | 类型 |   携带地址   | 是否必传 |   说明   |
| :---: | :--: | :----------: | :------: | :------: |
| token | str  | body(请求体) |    是    | 身份验证 |

​	**返回数据**： 

```JSon
[
{sku_id:'',sku_name:''},
{sku_id:'',sku_name:''}
....
]
```

| 返回参数 | 类型 | 是否必需 |    说明     |
| :------: | :--: | :------: | :---------: |
|    id    | int  |    是    |  sku商品id  |
|   name   | str  |    是    | sku商品名称 |

#### 增加图片数据接口

​	**请求方式：**POST /meiduo_admin/skus/images/

​	**请求参数：**token， id，name

| 参数  | 类型 |    携带地址     | 是否必传 |   说明    |
| :---: | :--: | :-------------: | :------: | :-------: |
| token | str  | headres(请求行) |    是    | 身份验证  |
|  id   | int  |  body(请求体)   |    是    | sku商品id |
| name  | str  |  body(请求体)   |    是    | sku商品id |

​	**返回数据：**JSON

```JSON
{
id:""
sku_id:"",
image_url:"",
}
```

| 返回参数  | 类型 | 是否必传 |   说明   |
| :-------: | :--: | :------: | :------: |
|    id     | int  |    是    |  图片id  |
|  sku_id   | int  |    是    |  商品id  |
| image_url | str  |    是    | 图片地址 |

## 业务分析

```mermaid

graph LR
add_port[新增图片接口]--查询所有商品信息-->add_show(显示选择接口)
add_show--商品信息-->add_commit
add_port--图片-->add_commit(增加接口)-->chage(是否保存成功)--成功-->0(保存图片信息)
chage--失败-->1(返回错误信息)

```

### 更新-接口分析

```mermaid
graph LR
change_port(接口分析)
change_port-->cs_1[请求方式]-->PUT
change_port-->cs_2[请求参数]-->token身分证明,id,image
change_port-->cs_3[请求地址]-->/meiduo_admin/skus/simplie/
change_port-->cs_4[返回结果]-->id,name,image_url
```

**请求方式**：PUT  /meiduo_admin/skus/simplie/

**请求参数**：token,id,image

| 参数  | 类型  | 是否必传 |      携带部位       |   说明   |
| :---: | :---: | :------: | :-----------------: | :------: |
| token |  str  |    是    |  headers（请求头）  | 身份验证 |
|  id   |  int  |    是    |   body（请求体）    |  商品id  |
| image | bytes |    是    | body（请求体files） | 上传图片 |

​	**返回参数**：

​	{

id：图片id，

image_url:图片地址，

sku_id:商品id，

}

| 返回参数 | 类型 | 是否必需 |   说明   |
| :------: | :--: | :------: | :------: |
|    id    | int  |    是    |  图片id  |
|  image   | str  |    是    | 图片地址 |
|  sku_id  | int  |    是    |  商品id  |

### sku表管理

```mermaid
graph LR
linst(商品表管理)

skus(sku表管理)-->sku_add((增加))
skus(sku表管理)-->sku_show((展示))-->skus_port(接口分析)
skus(sku表管理)-->sku_delere((删除))
skus(sku表管理)-->sku_svae((保存))


skus_port-->skuscs_1[请求方式]-->GET
skus_port-->skuscs_2[请求参数]-->token身分证明
skus_port-->skuscs_3[请求地址]-->/meiduo_admin/skus/
skus_port-->skuscs_4[返回结果]-->id,name,image_url
```

#### sku展示接口

​	多个展示接口

```mermaid
graph LR
skus_port(接口分析)
skus_port-->skuscs_1[请求方式]-->GET
skus_port-->skuscs_2[请求参数]-->token身分证明
skus_port-->skuscs_3[请求地址]-->/meiduo_admin/skus/
skus_port-->skuscs_4[返回结果]-->id,name,image_url
```

**请求方式**：GET  /meiduo_admin/skus/

**请求参数**：token

| 参数  | 类型 | 是否必传 |   说明   |
| :---: | :--: | :------: | :------: |
| token | str  |    是    | 身份验证 |

**返回参数**：

```json
{
        "counts": "商品SPU总数量",
        "lists": [
            {
                "id": "商品SKU ID",
                "name": "商品SKU名称",
                "spu": "商品SPU名称",
                "spu_id": "商品SPU ID",
                "caption": "商品副标题",
                "category_id": "三级分类id",
                "category": "三级分类名称",
                "price": "价格",
                "cost_price": "进价",
                "market_price": "市场价格",
                "stock": "库存",
                "sales": "销量",
                "is_launched": "上下架",
                "specs": [
                    {
                        "spec_id": "规格id",
                        "option_id": "选项id"
                    },
                    ...
                ]
            },
            ...
          ],
            "page": "页码",
            "pages": "总页数",
            "pagesize": "页容量"
      }
```

|  返回值  | 类型 | 是否必须 |    说明    |
| :------: | :--: | :------: | :--------: |
|  count   | int  |    是    | SKUs商总量 |
|  lists   | 数组 |    是    |  SKU信息   |
|   page   | int  |    是    |    页码    |
|  pages   | int  |    是    |   总页数   |
| pagesize | int  |    是    |   页容量   |

后面由于个人，已经略过了





### 订单接口

```mermaid
graph LR
订单接口-->展示内容-->订单展示-->show_port(接口分析)
展示内容-->订单详情展示-->detail_port(接口分析)
订单接口-->订单修改-->状态修改-->change_port(接口分析)
show_port-->order_s1(请求方式)-->order_s1_get(GET)
show_port-->order_s2(请求地址)-->order_s1_url( /meduie_main/order/)
show_port-->order_s4(请求方式)-->order_s1_request(token)
show_port-->order_s3(返回参数)-->order_s1_return("{count：订单个数，
lists：[{订单对象}，{订单对象}，。。。]，
page：页码，
pages：总页数，
pagesize：页容量，
}")
detail_port-->order_detail_s1(请求方式)-->order_s2_get(GET)
detail_port-->order_detail_s2(请求地址)-->order_s2_url("/meduie_main/(?P<pk>\d)/order/")
detail_port-->order_detail_s4(请求方式)-->order_s2_request(token)
detail_port-->order_detail_s3(返回参数)-->order_s2_return("{
order：订单对象，
sku_id:商品id，
defaultimage：商品图片
count：商品数量 ，
price：商品阶格，
}")


```

#### 订单展示 

```mermaid
graph LR
show_port(接口分析)
show_port-->order_s1(请求方式)-->order_s1_get(GET)
show_port-->order_s2(请求地址)-->order_s1_url( /meduie_main/order/)
show_port-->order_s4(请求方式)-->order_s1_request(token)
show_port-->order_s3(返回参数)-->order_s1_return("{count：订单个数，
lists：[{订单对象}，{订单对象}，。。。]，
page：页码，
pages：总页数，
pagesize：页容量，
}")




```

​	**请求方式**:GET /meduie_main/order/

​	**请求参数**：token

| 参数  | 类型 | 是否必传 |     携带部位      |   说明   |
| :---: | :--: | :------: | :---------------: | :------: |
| token | str  |    是    | 请求头（headres） | 身份验证 |

​	**返回结果**：JSON

```json
{

count：订单个数，
lists：[{订单对象}，{订单对象}，。。。]，
page：页码，
pages：总页数，
pagesize：页容量，

}
```

| 返回参数 | 类型 | 是否必需 |   说明   |
| :------: | :--: | :------: | :------: |
|  count   | int  |    是    | 订单个数 |
|  lists   | list |    是    | 数据内容 |
|  pages   | int  |    是    |  总页数  |
|   page   | int  |    是    |   页码   |
| pagesize | int  |    是    |  页容量  |

#### 订单详细接口

```mermaid
graph LR
detail_port(接口分析)
detail_port-->order_detail_s1(请求方式)-->order_s2_get(GET)
detail_port-->order_detail_s2(请求地址)-->order_s2_url("/meduie_main/(?P<pk>\d)/order/")
detail_port-->order_detail_s4(请求方式)-->order_s2_request("token，pk")
detail_port-->order_detail_s3(返回参数)-->order_s2_return("{
order：订单对象，
sku_id:商品id，
defaultimage：商品图片
count：商品数量 ，
price：商品价格，
}")

```

**请求方式**：GET

**请求参数**：pk， token

| 参数  | 类型 | 是否必传 |    携带部位     |   说明   |
| :---: | :--: | :------: | :-------------: | :------: |
|  pk   | int  |    是    | 请求行（lines） |  订单id  |
| token | str  |    是    | 请求头（heads） | 身份验证 |

**返回结果**：JSON

```
{
order：订单对象，
count：商品个数，
sku_id:商品id，
default：商品图片，
price：商品价格，
}
```

| 返回参数 |   类型    | 是否必需 |   说明   |
| :------: | :-------: | :------: | :------: |
|  order   | <objects> |    是    | 订单对象 |
|  count   |    int    |    是    | 商品个数 |
|  sku_id  |    int    |    是    |  商品id  |
|  price   |    int    |    是    | 商品价格 |
| default  |    str    |    是    | 图片地址 |

#### 订单状态修改

```mermaid
graph LR
change_port(接口分析)
change_port-->order_change_s1(请求方式)-->order_change_get(PUT)
change_port-->order_change_s2(请求地址)-->order_change_url("/meiduo_admin/orders/(?P<order_id>\d+)/status/")
change_port-->order_change_s4(请求方式)-->order_change_request("token，pk，status")
change_port-->order_change_s3(返回参数)-->order_change_return(" {
        order_id: 20181126102807000000004,
        status: 1
    }")
```

**请求方式**:PUT /meiduo_admin/orders/(?P<order_id>\d+)/status/

**请求参数**：token，pk，status

|  参数  | 类型 | 是否必传 |     携带部位      |   说明   |
| :----: | :--: | :------: | :---------------: | :------: |
| token  | str  |    是    | 请求头（headers） | 身份验证 |
|   pk   | str  |    是    |  请求体（body）   |  订单id  |
| status | int  |    是    |  请求体（body）   | 订单状态 |

**返回参数**：JSON

```json
{order_id:订单id，
status：订单状态}
```

| 返回参数 | 类型 | 是否必需 |   说明   |
| :------: | :--: | :------: | :------: |
| order_id | str  |    是    |  订单id  |
|  status  | int  |    是    | 订单状态 |

