import pymysql
from pymysql import Error


def Connect_and_read(query):
    data = []
    connection = pymysql.connect(
        # host='123.60.21.190',  # 例如 'localhost'
        host='localhost',  # 例如 'localhost'
        database='block_chain',  # 数据库名称
        user='root',  # 用户名
        password='qweasd'  # 密码
    )

    try:
        # 创建游标对象
        with connection.cursor() as cursor:
            cursor.execute(query)
            # 获取字段属性
            field_names = [i[0] for i in cursor.description]

            # 处理每一行数据
            for row in cursor.fetchall():
                # 将行数据转换为字典
                row_data = dict(zip(field_names, row))
                data.append(row_data)
            # 获取查询结果
            results = cursor.fetchall()
            for row in results:
                row_data = dict(zip(field_names, row))
                data.append(row_data)
    except Error as e:
        print("连接到 MySQL 时出错", e)
    finally:
        connection.close()
        print("MySQL 连接已关闭")

    return data


# query = "SELECT * FROM emulator_copy1"
# 调用函数并打印结果
# data = Connect_and_read(query)
# print("数据列表:")
# for row in data:
#     print(row)
