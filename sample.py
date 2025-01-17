import sqlite3


def main():
    # 连接到 SQLite 数据库，如果数据库文件不存在，会创建一个新的
    conn = sqlite3.connect('example.db')
    # 创建一个游标对象
    cursor = conn.cursor()

    # 创建表的 SQL 语句
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    '''
    # 执行创建表的 SQL 语句
    cursor.execute(create_table_sql)

    # 插入数据的 SQL 语句
    insert_data_sql = '''
    INSERT INTO students (name, age, grade) VALUES (?,?,?)
    '''
    # 要插入的数据
    data = [
        ('Alice', 20, 'A'),
        ('Bob', 22, 'B'),
        ('Charlie', 21, 'C')
    ]
    # 执行插入数据的操作
    cursor.executemany(insert_data_sql, data)

    # 提交事务
    conn.commit()

    # 查询数据的 SQL 语句
    select_data_sql = '''
    SELECT * FROM students
    '''
    # 执行查询操作
    cursor.execute(select_data_sql)
    # 获取查询结果
    results = cursor.fetchall()
    print("查询结果:")
    for row in results:
        print(row)

    # 更新数据的 SQL 语句
    update_data_sql = '''
    UPDATE students SET grade = 'A+' WHERE name = 'Alice'
    '''
    # 执行更新操作
    cursor.execute(update_data_sql)
    # 提交事务
    conn.commit()

    # 再次查询数据
    cursor.execute(select_data_sql)
    results = cursor.fetchall()
    print("更新后的查询结果:")
    for row in results:
        print(row)

    # 删除数据的 SQL 语句
    delete_data_sql = '''
    DELETE FROM students WHERE name = 'Charlie'
    '''
    # 执行删除操作
    cursor.execute(delete_data_sql)
    # 提交事务
    conn.commit()

    # 再次查询数据
    cursor.execute(select_data_sql)
    results = cursor.fetchall()
    print("删除后的查询结果:")
    for row in results:
        print(row)

    # 关闭游标和连接
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()