import sqlite3

# Create database and table
connection = sqlite3.connect("lists.db")
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS list (
    task text
)
""")
connection.commit()


# Takes mode
mode = input("Do you want to make a new task (1) or finish a task (2) or view your tasks (3): ")
if mode == "1":
    mode = input("Enter the task: ")
    c.execute("INSERT INTO list VALUES ('{}')".format(mode))
    connection.commit()

    c.execute("SELECT rowid, * FROM list WHERE task='{}'".format(mode))
    lst = c.fetchall()
    connection.commit()
    print("Task is added. The number for your task is: {}.\nNote: The number value has changed for each task".format(lst[0][0]))
elif mode == "2":
    mode = input("Please choose a way to delete. Through number(1) or through the task(2): ")
    if mode == "1":
        mode = input("Enter the number of the task: ")
        c.execute("DELETE FROM list WHERE rowid={}".format(int(mode)))
        connection.commit()

        print("Phew! The task is over!")
    else:
        mode = input("Enter the task: ")
        c.execute("DELETE FROM list WHERE task='{}'".format(mode))
        connection.commit()

        print("Phew! The task is over!")
else:
    c.execute("SELECT rowid, * FROM list")
    lst = c.fetchall()
    connection.commit()

    for i in lst:
        print("Number: {}    Task: {}".format(i[0], i[1]))



connection.close()