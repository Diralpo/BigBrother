# 数据库课设实验报告----简易学生信息系统

本项目已托管到远端git仓库：https://github.com/Diralpo/BigBrother.git

### 一、使用说明

运行server.py即可启动后端服务器，打开WebPage文件夹下的index.html即可使用

注意：您需要的config文件夹下的const.py中根据自己的情况来对一些数据库配置进行修改。

### 二、开发环境与技术说明

#### 1、Web服务器

本系统采用前后端分离的方式进行开发。后端Web服务器采用了基于Python3的Flask框架提供支持。

前端网页采用html，应用了bootstrap3作为页面的基础框架。

前后端的通信方面采用了JQuery的Ajax方法进行实现，消息以json方式进行传递。

后端服务器开启的端口为8080，如果您的机器的8080端口被占用，请在程序内进行更改。

#### 2、开发语言

前端：Html   JavaScript

后端：Python 3.6

#### 3、数据库管理系统

按要求使用MySQL

### 三、数据库表的定义

定义语句如下


     CREATE TABLE `student` (
       `id` int(11) NOT NULL,
       `name` varchar(18) NOT NULL,
       `sex` enum('man','woman') NOT NULL,
       `contact` varchar(30) DEFAULT NULL,
       PRIMARY KEY (`id`)
     ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


| 键      | 说明                                         |
| ------- | -------------------------------------------- |
| id      | 学号，11位整型，作为主键，不可重复，不可为空 |
| name    | 姓名，18位字符类型，不可为空                 |
| sex     | 性别，枚举类型，值为man或woman               |
| contact | 联系方式，30位字符类型，不可为空             |


### 四、数据库的连接 ###

#### 1、数据库的连接方式 ####

使用Python的PyMySQL库与mysql数据库进行交互
相应的语句如下


	def login_db(user, pwd, db_name):
		try:
	        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, 
					passwd=pwd, db=db_name, charset="utf8", 
					cursorclass = pymysql.cursors.DictCursor)
	        cursor = db.cursor()
	        return db, cursor
	    except pymysql.err.InternalError:
	        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, 
					passwd=pwd, db='mysql', charset="utf8")
	        cursor = db.cursor()
	        create_database(cursor, db_name)
	
	        db = pymysql.connect(host=const.DB_HOST, port=const.DB_PORT, user=user, 
					passwd=pwd, db=db_name, charset="utf8", 
					cursorclass = pymysql.cursors.DictCursor)
	        cursor = db.cursor()
	        return db, cursor


#### 2、实现增、删、改、查功能的语句 ####

实现增功能的语句

	def insert_stu(db, cursor, user_data):
	    try:
	        stu_id = user_data['id']
	        name = user_data['name']
	        sex = user_data['sex']
	        try:
	            contact = user_data['contact']
	            sql_insert = '''insert into student(id, name, sex, contact) values 
					({}, "{}", "{}", "{}")'''.format(stu_id, name, sex, contact)
	        except KeyError:
	            sql_insert = '''insert into student(id, name, sex) values (
					{}, "{}",  "{}")'''.format(stu_id, name, sex)
	    except KeyError:
	        return -1
	    try:
	        cursor.execute(sql_insert)
	        db.commit()
	        return 0
	    except :
	        db.rollback()
	    return -1

实现删功能的语句

	def del_stu(db, cursor, user_data):
	    try:
	        stu_id = user_data['id']
	        sql = "delete from student where id={}".format(stu_id)
	        cursor.execute(sql)
	        db.commit()
	        return 0
	    except KeyError:
	        return -1
	    except:
	        return -2

实现改功能的语句

	def tran_stu(db, cursor, user_data):
	    try:
	        stu_id = user_data['id']
	        name = user_data['name']
	        sex = user_data['sex']
	        try:
	            contact = user_data['contact']
	            sql_insert = '''update student set name='{}',sex = '{}',contact ='{}' 
					where id={}'''.format(name, sex, contact, stu_id)
	        except KeyError:
	            sql_insert = '''update student set name='{}',sex = '{}' where id={}'''.format(
	                name, sex, stu_id)
	    except KeyError:
	        return -1
	    except:
	        return -2
	    try:
	        cursor.execute(sql_insert)
	        db.commit()
	        return 0
	    except :
	        db.rollback()
	    return -1

实现查功能的语句

	def query_stu(db, cursor, user_data):
	    try:
	        stu_id = user_data['id']
	        if stu_id is "":
	            sql = "select * from student where id={}".format(stu_id)
	            cursor.execute(sql)
	            res = cursor.fetchall()
	        else:
	            stu_name = user_data['name']
	            sql = "select * from student where name like '{}'".format(stu_name)
	            cursor.execute(sql)
	            res = cursor.fetchall()
	        return res
	    except:
	        return None

### 五、展现各种功能的截图 ###

#### 主页如下所示 ####

![](/img/zy.png)

#### 实现新增功能的截图如下 ####

![](/img/xz1.png)
![](/img/xg2.png)

#### 实现查询功能的截图如下 ####

![](/img/cx1.png)
![](/img/cx2.png)

#### 注：要查询到后才能删除和修改

#### 实现修改功能的截图如下 ####

![](/img/xg1.png)
![](/img/xg2.png)

#### 实现删除功能的截图如下 ####

![](/img/sc1.png)
![](/img/sc2.png)